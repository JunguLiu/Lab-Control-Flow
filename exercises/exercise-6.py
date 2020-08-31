# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

m = input("Enter the month of the year (Jan - Dec): ")
d = input("Enter the day of the month: ")
month = ["Jan", "Feb", 'Mar', "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
value = (month.index(m) + 1) * 100 + int(d)

if value >= 320 and value <= 620:
    print(m + " " + d + "is in Spring")
elif value >= 621 and value <= 921:
    print(m+" " +d+ "is in Summer")
elif value >= 922 and value <= 1220:
    print(m + " " + d + "is in Fall")
else:
    print(m + " " + d + "is in Winter")
