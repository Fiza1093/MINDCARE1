

# Health Care Management System - Version 1.1
# Features: Patient registration, appointment booking, consultation fee calculation

def register_patient(patient_id, patient_name):
    print("Patient", patient_name, "registered with ID", patient_id)

def book_appointment(patient_id, doctor_name):
    print("Appointment booked for patient", patient_id, "with Dr.", doctor_name)

def calculate_fee(consultation_days, rate=500):
    fee = consultation_days * rate
    print("Consultation Fee = Rs.", fee)
    return fee


# Example usage
register_patient(101, "Rahul")
book_appointment(101, "Sharma")
calculate_fee(1)
