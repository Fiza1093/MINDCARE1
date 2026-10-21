

# MindCae Health Care Management System - Version 2.0
# Features: Patient registration, appointment booking,
# consultation fee calculation, doctor search

doctors = ["Dr. Sharma", "Dr. Patel", "Dr. Reddy"]

def register_patient(patient_id, patient_name):
    print("Patient", patient_name, "registered with ID", patient_id)

def book_appointment(patient_id, doctor_name):
    print("Appointment booked for patient", patient_id,
          "with", doctor_name)

def calculate_fee(consultation_days, rate=500):
    fee = consultation_days * rate
    print("Consultation Fee = Rs.", fee)
    return fee

def search_doctor(name):
    if name in doctors:
        print(name, "is available")
    else:
        print(name, "not found")


# Example usage
register_patient(101, "Rahul")
book_appointment(101, "Dr. Sharma")
calculate_fee(1)
search_doctor("Dr. Patel")
