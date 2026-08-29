# OneHealth

### Digital Healthcare Management Platform with AI Assistance

OneHealth is a web-based healthcare management platform designed to bring citizens, doctors, hospitals, appointments, medical records, and AI-assisted health information into one system.

The project was developed as a hackathon MVP with a focus on solving a practical problem: keeping a citizen's healthcare information organized and making it easier for citizens and doctors to access relevant information through a centralized platform.

The current MVP is built with Django and provides separate workflows for citizens, doctors, and administrators.

---

## Overview

Healthcare information is often distributed across prescriptions, hospital visits, medical reports, and different healthcare providers. This can make it difficult for citizens to maintain a clear history of their medical information.

OneHealth provides a centralized platform where:

- Citizens can maintain their healthcare profile.
- Every citizen receives a unique OneHealth ID.
- Doctors can find patients using their OneHealth ID.
- Doctors can create and manage medical records.
- Prescriptions can be linked to medical records.
- Citizens can view their medical history.
- Citizens can book hospital appointments.
- An AI assistant can summarize existing medical records.
- A chatbot can answer questions about the user's records and the OneHealth platform.
- Government-level views can provide aggregated health information.

The current version is an MVP intended for demonstration and further development.

---

## Key Features

### Citizen Module

- Citizen registration
- Citizen profile
- Unique OneHealth ID
- Personal health information
- Medical record history
- Prescription history
- Appointment booking
- Upcoming appointment view
- AI-generated medical record summary
- OneHealth AI chatbot

### Doctor Module

- Doctor registration
- Doctor profile
- Doctor dashboard
- Patient search using OneHealth ID
- Patient medical history
- Medical record creation
- Diagnosis and symptom recording
- Doctor notes
- Prescription creation
- Appointment-related medical records

### Hospital & Appointment Module

- Hospital listing
- Hospital information
- Appointment booking
- Appointment history
- Upcoming appointments

### AI Module

The AI layer currently provides two main features:

**AI Medical Summary**

Generates a concise summary from the citizen's existing medical records.

**OneHealth AI Chatbot**

Allows citizens to ask questions related to:

- Their available medical records
- Recorded prescriptions
- The OneHealth platform

The AI is instructed not to diagnose diseases, prescribe medicines, or invent information that is not present in the provided records.

### Government Module

The government module works with aggregated medical-record information and provides a higher-level view of recorded conditions.

The current implementation is intended as a prototype for future public-health analytics rather than a production epidemiological system.

---

# Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Django Templates |
| Database | SQLite |
| ORM | Django ORM |
| Authentication | Django Authentication |
| AI Integration | AI API |
| Development Server | Django Development Server |
| Version Control | Git & GitHub |
| Operating Environment | Linux / Ubuntu |

# Project Structure

```text
OneHealth/
├── accounts/
├── ai/
├── appointments/
├── config/
├── government/
├── hospitals/
├── records/
├── static/
├── templates/
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```
---


## AI Features

OneHealth includes an AI assistance layer designed to help citizens understand their existing healthcare information and interact with the platform more easily.

### AI Medical Summary

Generates a concise, patient-friendly summary from the citizen's existing medical records.

The summary is generated only from the information available in the user's OneHealth records.

### OneHealth AI Chatbot

Answers questions about the user's available medical records and the OneHealth platform.

Uses the user's existing records as context for medical-history-related questions.

### AI Safety controls

AI is instructed not to diagnose diseases, prescribe medicines, or invent medical information.

### Government Health Insights:

 Provides analysis of aggregated medical-record data for administrative and public-health insights.

### Future Scope

Disease prediction and early-risk assessment using trained ML models.
Hospital and doctor recommendation based on location and healthcare needs.
Multilingual and regional-language AI assistance.
Voice-based health assistant.
Android/mobile application integration.
Integration with government health systems and existing hospital/healthcare platforms.
Advanced public-health analytics and trend detection.
Secure digital medical-report/document uploads.
AI-assisted preventive healthcare recommendations.




## Author

**Anand Kumar Yadav**

- GitHub: [@Andycyborg](https://github.com/Andycyborg)
- Project Repository: [OneHealth](https://github.com/Andycyborg/OneHealth.git)