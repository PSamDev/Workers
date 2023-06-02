print("Welcome to our company's portal")

identity = input("Name.....")
branch = input("Branch.....")
office = input("Office.....")

print("To confirm your identity, please fill in the lines to show the names of overseers in your branch")

first, managingdirector = input("Managing Director...Mr "), "is the Managing Director"
second, hiringmanager = input("hiring manager...Mr "), "is the hiring manager"
third, secretary = input("Secretary...Mr "), "is the secretary"
fourth, receptionst = input("receptionist...Mr "), "is the receptionist"
fifth, accountant = input("Accountant...Mr "), "is the accountant"
sixth, hardwareengineer = input("Hardware Engineer...Mr "), "is the Engineer"


elders = f"In your branch {branch} Mr {fourth,receptionst} Mr {third, secretary} Mr {second, hiringmanager} Mr {first, managingdirector} Mr {fifth, accountant} Mr {sixth, hardwareengineer}"
print("")
print(elders)
print("")

msg = "%s please wait for your inputs to be confirmed ................ This may take few seconds" %identity
print(msg)

print(".")
print(".")
print(".")
print(f"Confirmed!! please, contact your secretary Mr {third} for further information")
