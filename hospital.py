from patient import Patient
from doctor import Doctor
from appointment import Appointment
from utils import save_data, load_data

class Hospital:
    def __init__(self):
        self.patients = load_data('patients.json', [])
        self.doctors = load_data('doctors.json', [])
        self.appointments = load_data('appointments.json', [])
        self.next_patient_id = len(self.patients) + 1
        self.next_doctor_id = len(self.doctors) + 1
        self.next_app_id = len(self.appointments) + 1
    
    def add_patient(self, name, age, phone, condition):
        patient = Patient(self.next_patient_id, name, age, phone, condition)
        self.patients.append(patient.__dict__)
        save_data(self.patients, 'patients.json')
        self.next_patient_id += 1
        print(f"Patient {patient.name} added with ID {patient.patient_id}")
    
    def add_doctor(self, name, specialty, phone):
        doctor = Doctor(self.next_doctor_id, name, specialty, phone)
        self.doctors.append(doctor.__dict__)
        save_data(self.doctors, 'doctors.json')
        self.next_doctor_id += 1
        print(f"Doctor {doctor.name} added with ID {doctor.doctor_id}")
    
    def add_appointment(self, patient_id, doctor_id, date, time):
        if any(p['patient_id'] == patient_id for p in self.patients) and any(d['doctor_id'] == doctor_id for d in self.doctors):
            app = Appointment(self.next_app_id, patient_id, doctor_id, date, time)
            self.appointments.append(app.__dict__)
            save_data(self.appointments, 'appointments.json')
            # Link to doctor
            for doc in self.doctors:
                if doc['doctor_id'] == doctor_id:
                    doc['appointments'].append(app.__dict__)
            save_data(self.doctors, 'doctors.json')
            self.next_app_id += 1
            print(f"Appointment {app.app_id} scheduled.")
        else:
            print("Invalid patient or doctor ID")
    
    def view_patients(self):
        for p in self.patients:
            print(Patient(**p))
    
    def view_doctors(self):
        for d in self.doctors:
            print(Doctor(**d))
    
    def view_appointments(self):
        for a in self.appointments:
            print(Appointment(**a))
    
    def delete_patient(self, patient_id):
        self.patients = [p for p in self.patients if p['patient_id'] != patient_id]
        save_data(self.patients, 'patients.json')
        print(f"Patient {patient_id} deleted.")
    
    # Similar methods for doctor, appointment delete...

