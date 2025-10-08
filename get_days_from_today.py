from datetime import datetime


def get_days_from_today(date: str):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD"

    # today = datetime.strptime("2021-05-05", "%Y-%m-%d").date()
    today = datetime.today().date()
    return (today - date_obj).days


days_diff = get_days_from_today("2021-10-09")
print(days_diff)
