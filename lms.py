
# Health Care Management System - Version 1.0
# Feature: Patient Registration and Appointment Management

def register_patient(patient_id, patient_name):
    print("Patient", patient_name, "registered with ID", patient_id)

def book_appointment(patient_id, doctor_name):
    print("Appointment booked for patient", patient_id, "with Dr.", doctor_name)


# Example usage
register_patient(101, "Rahul")
book_appointment(101, "Sharma")
