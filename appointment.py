class Appointment:
    def __init__(self, app_id, patient_id, doctor_id, date, time):
        self.app_id = app_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
    
    def __str__(self):
        return f"Appointment ID: {self.app_id}, Patient: {self.patient_id}, Doctor: {self.doctor_id}, Date: {self.date}, Time: {self.time}"

