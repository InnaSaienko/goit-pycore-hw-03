import json
from datetime import datetime, date, timedelta


def adjust_for_weekend(num_day):
    if num_day == 5:
        return 2
    elif num_day == 6:
        return 1
    return 0


def get_upcoming_birthdays(users_file):
    with open(users_file, 'r') as file:
        users = json.load(file)

    today = date.today()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")
        congratulation_date = birthday.date().replace(year=today.year)

        if congratulation_date < today:
            congratulation_date = congratulation_date.replace(year=congratulation_date.year + 1)

        diff_days = (congratulation_date - today).days

        if 0 <= diff_days <= 7:
            weekday = congratulation_date.weekday()
            congratulation_date += timedelta(adjust_for_weekend(weekday))

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


birthdays = get_upcoming_birthdays('users_data.json')
print("List of greetings on this week:", birthdays)
