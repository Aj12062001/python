from datetime import datetime
print("current date and time: ",datetime.now())
print("current year: ",datetime.now().year)
print("month of the year: ",datetime.now().strftime("%B"))
print("week no. of year: ",datetime.now().isocalendar()[1])
print("week day of year: ",datetime.now().strftime("%A"))
print("day of year: ",datetime.now().timetuple().tm_yday)
print("day of month: ",datetime.now().day)
print("day of week: ",datetime.now().weekday())


