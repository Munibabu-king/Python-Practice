from datetime import date
day,month,year=input("enter the day and month and year").split(","))
currentday=date.today().day
currentmonth=date.today().month
currentyear=date.today().year
Day=currentday - day
Month=currentmonth - month
Year=currentyear - year
print("{}-{}-{}".format(Day,Month,Year))
