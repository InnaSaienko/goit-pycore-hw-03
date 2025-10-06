from datetime import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        #today = datetime.strptime("2021-05-05", "%Y-%m-%d").date()
        return (today - date_obj).days
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD"


get_days_from_today("2021-10-09")
print(get_days_from_today("2021-10-09"))