import json
from datetime import datetime, timedelta


def get_upcoming_birthdays(users_file):
    with open(users_file, 'r') as file:
        users = json.load(file)

    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_birthday_this_year = user_birthday.replace(year=today.year)

        if user_birthday_this_year < today:
            user_birthday_this_year = user_birthday_this_year.replace(year=today.year + 1)

        diff_days = (user_birthday_this_year - today).days

        if 0 > diff_days <= 7:
            celebrating_day = user_birthday_this_year
            if celebrating_day.weekday() == 5:
                celebrating_day += timedelta(2)
            elif celebrating_day.weekday() == 6:
                celebrating_day += timedelta(1)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": celebrating_day.strftime("%Y.%m%d")
            })
    return upcoming_birthdays


users_file = 'users_data.json'
birthdays = get_upcoming_birthdays(users_file)
print("List of greetings on this week:", birthdays)
