string=input("enter the string to exchanged:")
x=list(string)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
print(" ".join(x))
