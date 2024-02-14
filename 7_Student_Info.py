# student info prectice program
Students = []

def add_student():
    name = input("Enter the student name: ").title().lstrip().rstrip()
    id = int(input("Enter the id of student: "))
    list_of_student = {
        'name' : name, 
        'id': id
    }
    
    Students.append(list_of_student)
    print(f"The {name} will be successfully added with id number is {list_of_student.get('id')}")
    
def remove_student():
    id = int(input("Enter the ID number of the student you want to delete: "))
    for i in Students:
        if id == i['id']:
            Students.remove(i)
    print(f"the {id} Student is successfully removed!!")
    
def display_student():
    id = int(input("Enter the id number of student you want to display them: "))
    for student in Students:
        if student['id'] == id:
            print(f"the student name is {student['name']} with the id number is {student['id']}.")

            
def display_all_student():
    for student in Students:
        print(f"student information:\n name: {student['name']} id: {student['id']}")
        
while True:
    print("1.Add Student")
    print("2.Remove Student")
    print("3.Display student")
    print("4.Print_all_students")
    print("5.Exit")

    Choice = int(input("Enter your choice: "))
    if Choice == 1:
        add_student()
    elif Choice == 2:
        remove_student()
    elif Choice == 3:
        display_student()
    elif Choice == 4:
        display_all_student()
    elif Choice == 5:
        print("Thanks")
        break
    else:
        print("Enter the valid choice!!")
    