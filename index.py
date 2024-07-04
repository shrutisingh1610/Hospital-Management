from Read_Data import * 
from Write_Data import *
from utility import *


print("********************************************************************")
print("*                                                                  *")
print("*             Welcome to Hospital Management System                *")
print("*                                                                  *")
print("********************************************************************")
	
tries = 0
tries_flag = ""
while tries_flag != "Close the program":

	Patients_DataBase = Read_Patients_DataBase()
	Doctors_DataBase  = Read_Doctors_DataBase()
			
	print("-----------------------------------------")
	print("|Enter 1 for Admin mode			|\n|Enter 2 for User mode			|\n|Enter 3 for Exit			|")
	print("-----------------------------------------")
	choice_admin_or_user = input("Enter your mode: ") 
	
	if choice_admin_or_user == "1":																			#Admin mode
		print("*****************************************\n|         Welcome to admin mode         |\n*****************************************")
		Password = input("Please enter your password: ")
		while True:
			if Password == "1234":
				print("-----------------------------------------")
				print("|To manage patients press 1 		|\n|To manage doctors press 2	 	|\n|To manage appointments press 3 	|\n|To go back press E			|")
				print("-----------------------------------------")
				AdminOptions = input ("Enter your choice: ")
				AdminOptions = AdminOptions.upper()
				
				if AdminOptions == "1":															#Admin mode --> Pateints Management
					Print_Admin_Patients_Options()
					Admin_choice = input ("Enter your choice: ")
					Admin_choice = Admin_choice.upper()
					
					if Admin_choice == "1": 										#Admin mode --> Pateints Management --> Enter new patient data
						try:		#To avoid non integer input
							patient_ID = int(input("Enter patient ID: "))
							while patient_ID in Patients_DataBase:		#if Admin entered used ID
								patient_ID = int(input("This ID is unavailable, please try another ID: "))
							Patients_DataBase[patient_ID]=Get_Patient_Data()
						except:
							print("Patient ID should be an integer number")
								
					elif Admin_choice == "2":										#Admin mode --> Pateints Management --> Display patient data
						Print_Patient_Details(Patients_DataBase)
					
					elif Admin_choice == "3":										#Admin mode --> Pateints Management --> Delete patient data
						try:		#To avoid non integer input
							patient_ID = int(input("Enter patient ID: "))
							while patient_ID not in Patients_DataBase:
								patient_ID = int(input("Incorrect ID, Please Enter patient ID: "))
							Patients_DataBase.pop(patient_ID)
							print("----------------------Patient data deleted successfully----------------------")
						except:
							print("Patient ID should be an integer number")
							
					elif Admin_choice == "4":						 				#Admin mode --> Pateints Management --> Edit patient data
						Patients_DataBase = Edit_Patient_Details(Patients_DataBase)
      
					elif Admin_choice == "E":										#Admin mode --> Pateints Management --> Back
						continue

					else:
						print("Please enter a correct choice\n")
								
				elif AdminOptions == "2":															#Admin mode --> Doctors Management
					Print_Admin_Doctors_Options()
					Admin_choice = input ("Enter your choice: ")
					Admin_choice = Admin_choice.upper()
					
					if Admin_choice == "1": 											#Admin mode --> Doctors Management --> Enter new doctor data
						try:		#To avoid non integer input
							Doctor_ID = int(input("Enter doctor ID: "))
							while Doctor_ID in Doctors_DataBase:			#if Admin entered used ID
								Doctor_ID = int(input("This ID is unavailable, please try another ID: "))
							Doctors_DataBase[Doctor_ID]=Get_Doctor_Data()
							print("----------------------Doctor added successfully----------------------")
						except:
							print("Doctor ID should be an integer number")
						
					elif Admin_choice == "2": 											#Admin mode --> Doctors Management --> Display doctor data
						Print_Doctor_Details(Doctors_DataBase)
					
					elif Admin_choice == "3":											#Admin mode --> Doctors Management --> Delete doctor data
						try:		#To avoid non integer input
							Doctor_ID = int(input("Enter doctor ID: "))
							while Doctor_ID not in Doctors_DataBase:
								Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID: "))
							Doctors_DataBase.pop(Doctor_ID)
							print("/----------------------Doctor data deleted successfully----------------------/")
						except:
							print("Doctor ID should be an integer number")

					elif Admin_choice == "4":											#Admin mode --> Doctors Management --> Edit Doctor data
						Doctors_DataBase = Edit_Doctor_Details(Doctors_DataBase)
									
					elif Admin_choice == "E":											#Back
						continue
							
					else:
						print("\nPlease enter a correct choice\n")
									
				elif AdminOptions == "3":															#Admin mode --> Appointment Management
					Print_Admin_Appointment_Options()
					Admin_choice = input ("Enter your choice: ")
					Admin_choice = Admin_choice.upper()
					if Admin_choice == "1":												#Admin mode --> Appointment Management --> Book an appointment							
						try:		#To avoid non integer input
							Doctor_ID = int(input("Enter the ID of doctor: "))
							while Doctor_ID not in Doctors_DataBase:
								Doctor_ID = int(input("Doctor ID incorrect, Please enter a correct doctor ID: "))
							print("---------------------------------------------------------")
							print("|To book an appointment for an exist patient Enter 1   |\n|To book an appointment for a new patient Enter 2      |\n|To go Back Enter E                                     |")
							print("---------------------------------------------------------")
							Admin_choice = input ("Enter your choice: ")
							Admin_choice = Admin_choice.upper()
							if Admin_choice == "1":
								patient_ID = int(input("Enter patient ID: "))
								while patient_ID not in Patients_DataBase:		#if Admin entered incorrect ID
									patient_ID = int(input("Incorrect ID, please Enter a correct patient ID: "))	
							
							elif Admin_choice == "2":
								patient_ID = int(input("Enter patient ID: "))
								while patient_ID in Patients_DataBase:		#if Admin entered used ID
									patient_ID = int(input("This ID is unavailable, please try another ID: "))					
								Patients_DataBase[patient_ID]=Get_Patient_Data()
							
							elif Admin_choice == "E":
								break
								
							Doctors_DataBase = Book_Appointment(Doctors_DataBase, Doctor_ID, patient_ID)						
							print("/----------------------Appointment booked successfully----------------------/")
						except:
								print("Doctor ID should be an integer number")
			
					elif Admin_choice == "2":												#Admin mode --> Appointment Management --> Edit an appointment
						try: Doctors_DataBase = Edit_Appointment(Doctors_DataBase, Patients_DataBase, Doctor_ID)
						except:
							Doctor_ID = int(input("Enter doctor ID: "))
							while Doctor_ID not in Doctors_DataBase:
								Doctor_ID = int(input("Doctor ID incorrect, Please enter a correct doctor ID: "))
							Doctors_DataBase = Edit_Appointment(Doctors_DataBase, Patients_DataBase, Doctor_ID)
				
					elif Admin_choice == "3":												#Admin mode --> Appointment Management --> Cancel an appointment
						try:		#To avoid non integer input
							patient_ID = int(input("Enter patient ID: "))
							while patient_ID not in Patients_DataBase:
								patient_ID = int(input("Invorrect ID, Enter patient ID: "))
							try:
									AppointmentIndex,PairKey = AppointmentIndexInDoctorsDataBase(Doctors_DataBase, patient_ID)						
									Doctors_DataBase[PairKey].pop(AppointmentIndex)
									print("/----------------------appointment canceled successfully----------------------/")
							except:
									print("No Appointment for this patient")
						except:	 #To avoid no return function
							print("Patient ID should be an integer number")
					
					elif Admin_choice == "E":												#Back
						continue
					
					else:
						print("please enter a correct choice")
				
				elif AdminOptions == "E":															#Back
					break
				
				else:
					print("Please enter a correct option")
			
			elif Password != "1234":
				if tries < 2:
					Password = input("Password incorrect, please try again: ")
					tries += 1
				else:
					print("Incorrect password, no more tries")
					tries_flag = "Close the program"
					break
		
			Write_Patients_DataBase(Patients_DataBase)
			Write_Doctors_DataBase(Doctors_DataBase)
								
	elif choice_admin_or_user == "2":																		#User mode
		print("****************************************\n|         Welcome to user mode         |\n****************************************")
		while True:
			print("\n-----------------------------------------")
			print("|To view hospital's departments Enter 1 |")
			print("|To view hospital's doctors Enter 2     |")
			print("|To view patients' residents Enter 3    |")
			print("|To view patient's details Enter 4      |")
			print("|To view doctor's appointments Enter 5  |")
			print("|To go Back Enter E                     |")
			print("-----------------------------------------")
			UserOptions = input("Enter your choice: ")
			UserOptions = UserOptions.upper()
			
			if   UserOptions == "1":											#User mode --> view hospital's departments
						print("Hospital's departments:")
						for i in Doctors_DataBase:
							print("	"+Doctors_DataBase[i][0][0])
				
			elif UserOptions == "2":											#User mode --> view hospital's Doctors
						print("Hospital's doctors:")
						for i in Doctors_DataBase:
							print("	"+Doctors_DataBase[i][0][1]+" in "+Doctors_DataBase[i][0][0]+" department, from "+Doctors_DataBase[i][0][2])
							
			elif UserOptions == "3":											#User mode --> view patients' residents
				for i in Patients_DataBase:
					print("	Patient: "+Patients_DataBase[i][2]+" in "+Patients_DataBase[i][0]+" department and followed by "+Patients_DataBase[i][1]+", age: "+Patients_DataBase[i][3]+", from: "+Patients_DataBase[i][5]+", RoomNumber: "+Patients_DataBase[i][6])
			
			elif UserOptions == "4":											#User mode --> view patient's details
				try:				#To avoid non integer input
					patient_ID = int(input("Enter patient's ID: "))
					while patient_ID not in Patients_DataBase:
						patient_ID = int(input("Incorrect Id, Please enter patient ID: "))
					print("	patient name: ",Patients_DataBase[patient_ID][2])
					print("	patient age: ",Patients_DataBase[patient_ID][3])
					print("	patient gender: ",Patients_DataBase[patient_ID][4])
					print("	patient address: ",Patients_DataBase[patient_ID][5])
					print("	patient room number: ",Patients_DataBase[patient_ID][6])
					print("	patient is in "+Patients_DataBase[patient_ID][0]+" department")
					print("	patient is followed by doctor: "+Patients_DataBase[patient_ID][1])
				except:
					print("Patient ID should be an integer number")
						
			elif UserOptions == "5":											#User mode --> view doctor's appointments
				try:				#To avoid non integer input
					Doctor_ID = int(input("Enter doctor's ID: "))
					while Doctor_ID not in Doctors_DataBase:
						Doctor_ID = int(input("Incorrect Id, Please enter doctor ID: "))
					print(Doctors_DataBase[Doctor_ID][0][1]+" has appointments:")
					for i in Doctors_DataBase[Doctor_ID]:
						if type(i[0])==str:
							continue
						else:
							print("	from: "+i[1]+"    to: "+i[2])
				except:
					print("Doctor ID should be an integer number")
				
			elif UserOptions == "E":											#Back
				break
				
			else:
				print("Please Enter a correct choice")
				
	elif choice_admin_or_user == "3":
		break			
	else:
		print("Invalid choice")