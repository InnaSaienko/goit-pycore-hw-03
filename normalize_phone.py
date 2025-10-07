import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_num):
    formatted_phone_number = re.sub(r"[^\d+]", "", phone_num)

    if not formatted_phone_number.startswith("+"):
        if formatted_phone_number.startswith("380"):
            formatted_phone_number = "+" + formatted_phone_number
        elif formatted_phone_number.startswith("80"):
            formatted_phone_number = "+3" + formatted_phone_number
        else:
            formatted_phone_number = "+38" + formatted_phone_number

    return formatted_phone_number



data_of_formatted_numbers = [normalize_phone(phone_num) for phone_num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", data_of_formatted_numbers)


