list1 = [int(num) for num in input("Enter 1st list numbers (space seperated):").split()]
list2 = [int(num) for num in input("Enter 1st list numbers (space seperated):").split()]
if(len(list1) == len(list2)):
    print("Length is same")
else:
    print("Length is not same")
sum1=sum(list1)
sum2=sum(list2)
if( sum1==sum2):
    print("Sum is Same")
else:
    print("Sum is different")
same1=set(list1)
same2=set(list2)
if same1==same2:
    print(f" the same values in both list are {same1}")
else:
   print("there are no same values")

