class Patient:
    def __init__(self, patient_id, name, age, phone, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.phone = phone
        self.condition = condition
    
    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Phone: {self.phone}, Condition: {self.condition}"

