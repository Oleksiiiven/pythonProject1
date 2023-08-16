import calendar
current_year = calendar.datetime.datetime.now().year
leap_years = []
while len(leap_years) < 10:
    current_year += 1
    if calendar.isleap(current_year):
        leap_years.append(current_year)
print(leap_years)