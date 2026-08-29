from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from records.models import MedicalRecord

from .services import ask_ai


@login_required
def citizen_summary(request):

    records = (
        MedicalRecord.objects
        .filter(patient=request.user)
        .select_related("doctor")
        .prefetch_related("prescriptions")[:10]
    )

    if records:

        data = []

        for record in records:

            medicines = []

            for prescription in record.prescriptions.all():

                medicines.append(
                    f"{prescription.medicine_name} "
                    f"{prescription.dosage} "
                    f"{prescription.frequency} "
                    f"for {prescription.duration}"
                )

            medicines_text = (
                ", ".join(medicines)
                if medicines
                else "No medicines recorded"
            )

            data.append(
                f"""
Date: {record.record_date}
Diagnosis: {record.diagnosis}
Symptoms: {record.symptoms or "Not recorded"}
Doctor's Notes: {record.notes or "Not recorded"}
Medicines: {medicines_text}
"""
            )

        medical_text = "\n".join(data)

        prompt = f"""
You are OneHealth AI, a healthcare information assistant.

Analyze ONLY the medical records provided below.

Create a short, clear and patient-friendly health summary.

Structure the response as:

1. Overall Summary
2. Recorded Conditions
3. Symptoms
4. Medicines/Prescriptions
5. Doctor's Notes
6. Important Information

Rules:

- Do not diagnose the patient.
- Do not invent medical information.
- Do not recommend new medicines.
- Do not change or reinterpret prescriptions.
- Do not claim that the patient has a disease unless it
  appears in the provided records.
- If information is missing, say "Not recorded".
- Explain medical terms simply when useful.
- Keep the answer concise.
- Clearly state that this is an informational summary
  and not a medical diagnosis.

Medical Records:

{medical_text}
"""

        summary = ask_ai(prompt)

    else:

        summary = (
            "No medical records are available for AI analysis yet.\n\n"
            "Once a doctor adds medical records to your "
            "OneHealth profile, you can generate an AI summary."
        )

    return render(
        request,
        "ai/citizen_summary.html",
        {
            "summary": summary,
        }
    )


@login_required
def government_summary(request):

    records = MedicalRecord.objects.all()

    disease_counts = {}

    for record in records:

        disease = record.diagnosis

        disease_counts[disease] = (
            disease_counts.get(disease, 0) + 1
        )

    data = "\n".join(
        [
            f"{disease}: {count} cases"
            for disease, count
            in disease_counts.items()
        ]
    )

    if not data:

        data = "No medical records available."

    prompt = f"""
You are OneHealth Government Health Intelligence AI.

Analyze the following aggregated medical-record counts.

Provide:

1. Most frequent conditions
2. Potentially unusual patterns
3. Conditions that may require monitoring
4. Administrative observations

Rules:

- Do not identify individual patients.
- Do not diagnose anyone.
- Do not claim an outbreak has been proven.
- Use the term "potential anomaly" for unusual patterns.
- Base your analysis only on the provided data.

Data:

{data}
"""

    summary = ask_ai(prompt)

    return render(
        request,
        "ai/government_summary.html",
        {
            "summary": summary,
            "disease_counts": disease_counts,
        }
    )


@login_required
def chatbot(request):

    answer = None

    if request.method == "POST":

        question = request.POST.get(
            "question",
            ""
        ).strip()

        if question:

            records = (
                MedicalRecord.objects
                .filter(patient=request.user)
                .prefetch_related("prescriptions")[:10]
            )

            record_data = []

            for record in records:

                medicines = []

                for prescription in record.prescriptions.all():

                    medicines.append(
                        f"{prescription.medicine_name} "
                        f"{prescription.dosage} "
                        f"{prescription.frequency} "
                        f"for {prescription.duration}"
                    )

                record_data.append(
                    f"""
Date: {record.record_date}
Diagnosis: {record.diagnosis}
Symptoms: {record.symptoms or "Not recorded"}
Notes: {record.notes or "Not recorded"}
Medicines: {", ".join(medicines) if medicines else "None recorded"}
"""
                )

            record_text = (
                "\n".join(record_data)
                if record_data
                else "No medical records available."
            )

            prompt = f"""
You are OneHealth Citizen Assistant.

You help the user understand:

- Their existing OneHealth medical records
- Their recorded prescriptions
- The OneHealth platform

Patient's existing records:

{record_text}

User question:

{question}

Rules:

- Answer only using the provided records when the
  question is about the patient's medical history.
- Do not diagnose diseases.
- Do not prescribe medicines.
- Do not recommend changing prescriptions.
- Do not invent information.
- Do not replace a doctor.
- If the records do not contain the answer,
  clearly say that the information is not available.
- Keep the answer short and easy to understand.
"""

            answer = ask_ai(prompt)

    return render(
        request,
        "ai/chatbot.html",
        {
            "answer": answer,
        }
    )