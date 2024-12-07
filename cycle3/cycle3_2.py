num=int(input("enter the number:"))
n1,n2=0,1
if num==1:
	print("the fibonacci series of 1 is 0")
elif num<=0:
	print("enter a valid number")
else:
	print(f"the fibonacci series of number {num}; ")
	for i in  range(1,num+1):
		print(n1)
		n=n1+n2
		n1,n2=n2,n
