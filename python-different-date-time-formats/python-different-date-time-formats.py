import time
import datetime

print('Today: ', datetime.date.today())

print("Time in seconds since the epoch: %s" %time.time())
print("Current date and time: ", datetime.datetime.now())
print("Or Current date and time: ", datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

print("Full weekday name: ", datetime.date.today().strftime("%A"))
print("Abbreviated weekday name: ", datetime.date.today().strftime("%a"))

print("Full month name: ", datetime.date.today().strftime("%B"))
print("Abbreviated month name: ", datetime.date.today().strftime("%b"))

print("Appropriate date and time: ", datetime.date.today().strftime("%c"))

print("Day of the month as a decimal number: ", datetime.date.today().strftime("%d"))

print("Microsecond as a decimal number: ", datetime.date.today().strftime("%f"))

print("Hour (24-hour clock) as a decimal number: ", datetime.date.today().strftime("%H"))
print("Hour (12-hour clock) as a decimal number: ", datetime.date.today().strftime("%I"))

print("Day of the year as a decimal number: ", datetime.date.today().strftime("%j"))

print("Month as a decimal number: ", datetime.date.today().strftime("%m"))

print("Minute as a decimal number: ", datetime.date.today().strftime("%M"))

print("Either AM or PM: ", datetime.date.today().strftime("%p"))

print("Second as a decimal number: ", datetime.date.today().strftime("%S"))

print("Week number of the year: ", datetime.date.today().strftime("%U"))

print("Weekday as a decimal number: ", datetime.date.today().strftime("%w"))

print("Week number of the year: ", datetime.date.today().strftime("%W"))

print("Appropriate date representation: ", datetime.date.today().strftime("%x"))
print("Appropriate time representation: ", datetime.date.today().strftime("%X"))

print("Year without century as a decimal number: ", datetime.date.today().strftime("%y"))
print("Year with century as a decimal number: ", datetime.date.today().strftime("%Y"))

print("UTC offset in the form ±HHMM[SS[.ffffff]]: ", datetime.date.today().strftime("%z"))
print("Time zone name (empty string if the object is naive): ", datetime.date.today().strftime("%Z"))

print("A literal '%' character: ", datetime.date.today().strftime("%%"))

print("ISO 8601 year with century: ", datetime.date.today().strftime("%G"))

print("ISO 8601 weekday as a decimal number: ", datetime.date.today().strftime("%U"))

print("ISO 8601 week as a decimal number: ", datetime.date.today().strftime("%V"))

print("Combine directives to form date and time: ", datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S%z %p"))