import calendar
result = [y for y in range(2023, 2063) if calendar.isleap(y)]
print(result[::-1])