def Print_Admin_Patients_Options():
    print("-----------------------------------------")
    print("|To add new patient press 1	  	|")
    print("|To display patient press 2	  	|")
    print("|To delete patient data press 3		|")
    print("|To edit patient data press 4    	|")
    print("|To go back press E      		|")
    print("-----------------------------------------")
    
def Get_Patient_Data():					
    Department=input("Enter patient department: ")
    DoctorName=input("Enter name of doctor following the case: ")
    Name      =input("Enter patient name: ")
    Age       =input("Enter patient age: ")
    Gender    =input("Enter patient gender: ")
    Address   =input("Enter patient address: ")
    RoomNumber=input("Enter patient room number: ")
    print("----------------------Patient added successfully----------------------")
    return [Department, DoctorName, Name, Age, Gender, Address, RoomNumber]

def Print_Patient_Details(Data):
    try:		#To avoid non integer input
        patient_ID = int(input("Enter patient ID: "))
        while patient_ID not in Data:
            patient_ID = int(input("Incorrect ID, Please Enter patient ID: "))
        print("\nPatient name:",Data[patient_ID][2])
        print("Patient age:",Data[patient_ID][3])
        print("Patient gender:",Data[patient_ID][4])
        print("Patient address:",Data[patient_ID][5])
        print("Patient room number:",Data[patient_ID][6])
        print("Patient is in "+Data[patient_ID][0]+" department")
        print("Patient is followed by doctor: "+Data[patient_ID][1])
    except:
        print("Patient ID should be an integer number")

def Edit_Patient_Details(Data):
    try:		#To avoid non integer input
        patient_ID=int(input("Enter patient ID: "))
        while patient_ID not in Data:
            patient_ID = int(input("Incorrect ID, Please Enter patient ID: "))
        while True:
            print("------------------------------------------")
            print("|To Edit patient's Department Enter 1    |")
            print("|To Edit Doctor following case Enter 2 |")
            print("|To Edit patient's Name Enter 3          |")
            print("|To Edit patient's Age Enter 4           |")
            print("|To Edit patient's Gender Enter 5        |")
            print("|To Edit patient's Address Enter 6       |")
            print("|To Edit patient's RoomNumber Enter 7    |")
            print("|To go Back Enter E                      |")
            print("-----------------------------------------")
            Admin_choice = input("Enter your choice: ")
            Admin_choice = Admin_choice.upper()
            if Admin_choice == "1":
                Data[patient_ID][0]=input("\nEnter patient department: ")
                print("----------------------Patient Department edited successfully----------------------")
                
            elif Admin_choice == "2":
                Data[patient_ID][1]=input("\nEnter Doctor follouing case: ")
                print("----------------------Doctor follouing case edited successfully----------------------")

            elif Admin_choice == "3":
                Data[patient_ID][2]=input("\nEnter patient name: ")
                print("----------------------Patient name edited successfully----------------------")
            
            elif Admin_choice == "4":
                Data[patient_ID][3]=input("\nEnter patient Age: ")
                print("----------------------Patient age edited successfully----------------------")
        
            elif Admin_choice == "5":
                Data[patient_ID][4]=input("\nEnter patient gender: ")
                print("----------------------Patient gender edited successfully----------------------")
                
            elif Admin_choice == "6":
                Data[patient_ID][5]=input("\nEnter patient address: ")
                print("----------------------Patient address edited successfully----------------------")
                
            elif Admin_choice == "7":
                Data[patient_ID][6]=input("\nEnter patient RoomNumber: ")
                print("----------------------Patient Room Number edited successfully----------------------")
        
            elif Admin_choice == "E":
                return Data
                
            else:
                print("Please Enter a correct choice")
            return Data
    except:
        print("Patient ID should be an integer number")
        return Data

def Print_Admin_Doctors_Options():
    print("-----------------------------------------")
    print("|To add new doctor Enter 1              |")
    print("|To display doctor Enter 2              |")
    print("|To delete doctor data Enter 3          |")
    print("|To edit doctor data Enter 4            |")
    print("|To go back enter E                     |")
    print("-----------------------------------------")

def Get_Doctor_Data():
    Department=input("Enter Doctor department: ")
    Name      =input("Enter Doctor name: ")
    Address   =input("Enter Doctor address: ")
    return [[Department, Name, Address]]

def Print_Doctor_Details(Data):
    try:		#To avoid non integer input
        Doctor_ID = int(input("Enter doctor ID: "))
        while Doctor_ID not in Data:
            Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID: "))
        print("Doctor name: ",Data[Doctor_ID][0][1])
        print("Doctor address: ",Data[Doctor_ID][0][2])
        print("Doctor is in "+Data[Doctor_ID][0][0]+" department")
    except:
        print("Doctor ID should be an integer number")
        
def Edit_Doctor_Details(Data):
    try:		#To avoid non integer input	
        Doctor_ID=input("Enter doctor ID: ")
        while Doctor_ID not in Data:
            Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID: "))
        print("-----------------------------------------")
        print("|To Edit doctor's department Enter 1    |")
        print("|To Edit doctor's name Enter 2          |")
        print("|To Edit doctor's address Enter 3       |")
        print("|To go Back Enter E                      |")
        print("-----------------------------------------")
        Admin_choice=input("Enter your choice: ")
        Admin_choice = Admin_choice.upper()
        if Admin_choice == "1":
            Data[Doctor_ID][0][0]=input("Enter Doctor's Department: ")
            print("/----------------------Doctor's department edited successfully----------------------/")
            
        elif Admin_choice == "2":
            Data[Doctor_ID][0][1]=input("Enter Doctor's Name: ")
            print("----------------------Doctor's name edited successfully----------------------")
            
        elif Admin_choice == "3":
            Data[Doctor_ID][0][2]=input("Enter Doctor's Address: ")
            print("----------------------Doctor's address edited successfully----------------------")
        
        elif Admin_choice == "E":
            return Data
        
        else:
            print("\nPlease enter a correct choice\n")
        return Data    
    except:
        print("Doctor ID should be an integer number")
        return Data
    
def Print_Admin_Appointment_Options():
    print("-----------------------------------------")
    print("|To book an appointment Enter 1         |")
    print("|To edit an appointment Enter 2         |")
    print("|To cancel an appointment Enter 3       |")
    print("|To go back enter E                     |")
    print("-----------------------------------------")

def Book_Appointment(Data, D_ID, P_ID):
    Session_Start = input("Session starts at: ")
    while Session_Start[:2] == "11" or Session_Start[:2] == "12":
        Session_Start = input("Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours: ")
        
    for i in Data[D_ID]:
        if type(i[0])!=str:
            while Session_Start >= i[1] and Session_Start < i[2]:
                Session_Start = input("This appointment is already booked, Please Enter another time for start of session: ")
    Session_End  = input("Session ends at: ")
    
    New_Appointment=list()
    New_Appointment.append(P_ID)
    New_Appointment.append(Session_Start)
    New_Appointment.append(Session_End)
    Data[D_ID].append(New_Appointment)	
    return Data

def AppointmentIndexInDoctorsDataBase (Data, patient_ID):
	for i in Data:
		for j in Data[i]:							
			if str(patient_ID) == str(j[0]):
				Appointment_index = Data[i].index(j)
				return Appointment_index, i

def Edit_Appointment(Doc_Data, Patient_Data, ID=1):
    try:		#To avoid non integer input
        patient_ID = int(input("Enter patient ID: "))						
        while patient_ID not in Patient_Data:
            patient_ID = int(input("Incorrect Id, Please Enter correct patient ID: "))
        try:   #To avoid no return function
            AppointmentIndex, PairKey = AppointmentIndexInDoctorsDataBase(Doc_Data, patient_ID)
            Session_Start = input ("Please enter the new start time: ")
            while Session_Start[:2] == "11" or Session_Start[:2] == "12":
                Session_Start = input("Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours: ")
                
            for i in Doc_Data[ID]:
                if type(i[0])!=str:
                    while Session_Start >= i[1] and Session_Start < i[2]:
                        Session_Start = input("This appointment is already booked, Please Enter an other time for start of session: ")
            Session_End = input ("Please enter the new end time: ")
            Doc_Data[PairKey][AppointmentIndex]=[patient_ID,Session_Start,Session_End]							
            print("/----------------------appointment edited successfully----------------------/")
            return Doc_Data
        except:
            print("No Appointment for this patient")
    except:
        print("Doctor ID should be an integer number")
    return Doc_Data