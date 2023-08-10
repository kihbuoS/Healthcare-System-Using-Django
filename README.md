# Healthcare System

Welcome to the Healthcare System, a Django-based web application with microservices for doctors, patients, and appointments. This system facilitates appointment booking, payment, and management between patients and doctors.

## Features

- **Authentication:** JWT-based authentication for secure access.
- **Patient Portal:**
  - Account creation and password change.
  - Appointment booking and cancellation.
  - Payment for consultation fees.

- **Doctor Portal:**
  - View appointments and patient details.

## Microservices

1. **Doctor Microservice:**
   - Handles doctor information and availability.
   - Provides an API for doctors to check appointments.

2. **Patient Microservice:**
   - Manages patient accounts, authentication, and profile information.
   - Enables patients to book appointments, change passwords, and manage payments.

3. **Appointment Microservice:**
   - Handles appointment scheduling and cancellation.
   - Integrates with patient and doctor microservices for a seamless experience.

Created by - Soubhik 
