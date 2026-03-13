class Doctor:
    def __init__(self, doctor_id, name, specialty, phone):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.phone = phone
        self.appointments = []
    
    def add_appointment(self, appointment):
        self.appointments.append(appointment)
    
    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialty: {self.specialty}, Phone: {self.phone}"

