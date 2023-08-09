leap_years = [year for year in range(1900, 2001) if year % 4 == 0]
not_leap_years = [year for year in range(1900, 2001) if year % 4 != 0]

century_dict = {'leap': leap_years, 'not leap': not_leap_years}
print(century_dict)
