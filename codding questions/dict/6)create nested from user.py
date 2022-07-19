main_d={}
NofE = int(input("enter number of element : "))
for i in range(NofE):
    s_no = int(input("enter the registration number : "))
    main_d[s_no] ={}
    name=input("enter the name : ")
    rollno=input("enter the Roll no : ")
    place = input("enter the place : ")
    main_d[s_no]["Name"] = name
    main_d[s_no]["Rollno"] = rollno
    main_d[s_no]["Place"] = place
print(main_d)
#  -----------------------------------------------------
for i in main_d:
    print(main_d[s_no]["Name"])
    print(main_d[s_no]["Rollno"])
    print(main_d[s_no]["Place"])
