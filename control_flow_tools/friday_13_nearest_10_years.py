import datetime

today = datetime.date.today()
end_date = today.replace(year=today.year + 10)

for d in (today + datetime.timedelta(days=n) for n in range((end_date - today).days)):
    if d.day == 13 and d.weekday() == 4:
        print(d.strftime("%Y-%m-%d"))
