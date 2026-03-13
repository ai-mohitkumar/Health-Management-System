from hospital import Hospital

def main():
    hospital = Hospital()
    
    while True:
        print("\n=== Health Management System ===")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Add Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Delete Patient")
        print("0. Exit")
        
        choice = input("Choose option: ")
        
        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            phone = input("Phone: ")
            condition = input("Condition: ")
            hospital.add_patient(name, age, phone, condition)
        
        elif choice == '2':
            name = input("Name: ")
            specialty = input("Specialty: ")
            phone = input("Phone: ")
            hospital.add_doctor(name, specialty, phone)
        
        elif choice == '3':
            patient_id = int(input("Patient ID: "))
            doctor_id = int(input("Doctor ID: "))
            date = input("Date (YYYY-MM-DD): ")
            time = input("Time: ")
            hospital.add_appointment(patient_id, doctor_id, date, time)
        
        elif choice == '4':
            hospital.view_patients()
        
        elif choice == '5':
            hospital.view_doctors()
        
        elif choice == '6':
            hospital.view_appointments()
        
        elif choice == '7':
            patient_id = int(input("Patient ID to delete: "))
            hospital.delete_patient(patient_id)
        
        elif choice == '0':
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

