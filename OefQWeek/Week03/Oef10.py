#oefening 10
import calendar

jaar1 = int(input("Geef een jaartal in: "))
jaar2 = int(input("Geef een ander jaartal in: "))

schrikkel= calendar.leapdays(jaar1,jaar2)
print(schrikkel)

