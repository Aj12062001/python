n=int(input("enter the no.of people:"))
c=int(input("enter the no.of people below age 10:"))
a=int(input("enter the no.of people age between 10 to 60:"))
o=int(input("enter the no.of people  age 60 and above:"))
child=c*7
adult=a*10
old=o*5
total_fair=child+adult+old
print(f"the total fair of {n} people is {total_fair}")

