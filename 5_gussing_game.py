# gussing game 
print("Welcome to the gussing game!")
secret_number = 4

for i in range(1,100):
    user_input = int(input("Enter the number : "))
    if user_input == secret_number:
        print("Congrats!")
        break
    elif user_input<secret_number:
        print("the number is very low compare to the correct number!")
    elif user_input>secret_number:
        print("the number is very high compare to the correct number!")
    else:
        print("Enter the valid number!")