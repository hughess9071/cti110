def is_leap_year(year):
    if year % 4 == 0:  # Check if the year is divisible by 4
        if year % 100 == 0:  # Check if the year is a century year
            if year % 400 == 0:  # Check if the century year is divisible by 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Read the year from the user
ly = int(input())

# Check if the year is a leap year
if is_leap_year(ly):
    print(ly, "- leap year")
else:
    print(ly, "- not a leap year")