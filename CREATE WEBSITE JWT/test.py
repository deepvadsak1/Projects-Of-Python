my_list = []
my_dict = {}
x = 1

while True:
    value = input("Enter a value (or 1 for 'exit'): ")
    if value == '1':
        break

    my_list.append(value)
    my_dict[x] = value
    x += 1

print("List:", my_list)
print("Dictionary:", my_dict)
