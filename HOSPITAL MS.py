class hospital():
    def __init__(self):
        self.file="hospital.txt"
    def add_patient(self):
        patient_id=input("Enter patient id:")
        patient_name=input("enter patient name:")
        disease=input("enter disease:")
        doctor_name=input("enter doctor name:")
        try:
            with open(self.file,"r") as f:
                patients= f.readlines()
        except:
            patients=[]
        for patient in patients:
            if patient.strip()=="":
                continue
            i,n,d,o=patient.strip().split(",")
            if i==patient_id:
                print("ALREADY ADDED")
                return
        with open(self.file,"a") as f:
            f.write(str(patient_id)+","+patient_name+","+disease+","+doctor_name+"\n")
        print("PATIENT ADDED")
    def view_patient(self):
        with open(self.file,"r") as f:
            patients=f.readlines()
        found=False
        if not patients:
            print("NO PATIENTS DETAILS TO VIEW")
            return
        print("PATIENT DETAILS")    
        for patient in patients:
            if patient.strip()=="":
                continue
            i,n,d,o=patient.strip().split(",")
            print("\nPatient id:",i,
                  "\nPatient name:",n,
                  "\nDisease :",d,
                  "\nDoctor name:",o,"\n")
            found=True
        
    def search_patient(self):
        patient_id=input("Enter patient id:")
        with open (self.file,"r") as f:
            patients=f.readlines()
        found=False
        for patient in patients:
            if patient.strip()=="":
                continue
            i,n,d,o=patient.strip().split(",")
            if i==patient_id:
                print("\nPatient id:",i,
                  "\nPatient name:",n,
                  "\nDisease :",d,
                  "\nDoctor name:",o,"\n")
                found=True
        if not found:
            print("INVALID PATIENT ID")
    def update_patient(self):
        patient_id=input("Enter patient id:")
        patients_name=input("enter patient name:")
        diseases=input("enter disease:")
        doctor_names=input("enter doctor name:")
        with open(self.file,"r") as f:
            patients=f.readlines()
        update=[]
        found=False
        for patient in patients:
            if patient.strip()=="":
                continue
            i,n,d,o=patient.strip().split(",")
            if i==patient_id:
                update.append(str(i)+","+patients_name+","+diseases+","+doctor_names+"\n")
                found=True

            else:
                update.append(patient)
        with open(self.file,"w") as f:
            f.writelines(update)
            
        if found:
            print("UPDATED PATIENT DETAILS")
        else:
            print("INVALID PATIENT ID")
    def delete_patient(self):
        patient_id=input("Enter patient id:")
        with open(self.file,"r") as f:
            patients=f.readlines()
        delete=[]
        found=False
        for patient in patients:
            if patient.strip()=="":
                continue
            i,n,d,o=patient.strip().split(",")
            if i==patient_id:
                found=True
            else:
                delete.append(patient)
        with open(self.file,"w") as f:
            f.writelines(delete)
        if found:
            print("PATIENT DELETED")
        else:
            print("INVALID PATIENT ID")
system=hospital()
while True:
    print("\n HOSPITAL MANAGEMENT SYSTEM")
    print("1.add patient")
    print("2.view patient")
    print("3.search patient")
    print("4.update patient")
    print("5.delete patient")
    print("6.EXIT")
    choice=input("enter your choice:")
    if choice=="1":
        system.add_patient()
    elif choice=="2":
        system.view_patient()
    elif choice=="3":
        system.search_patient()
    elif choice=="4":
        system.update_patient()
    elif choice=="5":
        system.delete_patient()
    
    elif choice=="6":
        print("------------EXITING HOSPITAAL MANAGEMENT SYSTEM------------------")
        break
    else :
        print("invalid choice :(")
            
        
                
                





                
                
        
            
                
            
            
        
                  

        
        
         
             
