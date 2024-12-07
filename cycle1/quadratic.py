import math
a=float(input("enter the coefficent of a:"))
b=float(input("enter the coefficent of b:"))
c=float(input("enter the coefficent of c:"))
d=(b*b)-(4*a*c)
if a==0:
        print("coefficent of a cannot be zero")
elif d==0:
	sol3=-b/(2*a)
	print(f"the solution is {sol3}")
elif d>0:
	sol1=(-b+math.sqrt(d))/(2*a)
	sol2=(-b-math.sqrt(d))/(2*a)
	print(f"this has 2 real solutions {sol1:.2f} and {sol2:.2f}")
else:
	sol4=(-b)/(2*a)
	sol5=math.sqrt(abs(d))/(2*a)
	print(f"the real part={sol4} and imaginary part={sol5} and -{sol5}")


