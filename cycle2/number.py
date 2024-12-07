integers =input("Enter numbers (comma seperated): ")
int_list = [ number.strip() for number in integers.split(",") ]
new_list = []
for number in int_list:
    if int(number) > 100:
        number = number.replace(number, "score")
    new_list.append(number)
print(new_list)
