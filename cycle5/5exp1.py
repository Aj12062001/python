import calendar
yrs=int(input("enter a year: "))
if calendar.isleap(yrs):
	print(f"{yrs} is a leap year.")
else:
	print(f"{yrs} is not a leap year.")
