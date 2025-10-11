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


def normalize_phone(phone_number):
    formatted_phone_number = re.sub(r"[^\d+]", "", phone_number)

    if len(formatted_phone_number) != 0 and formatted_phone_number[0] != "+":
        prefix = ""

        if formatted_phone_number.startswith("80"):
            prefix = "3"
        elif formatted_phone_number.startswith("0"):
            prefix = "38"

        formatted_phone_number = f"+{prefix}formatted_phone_number"

    return formatted_phone_number


data_formatted_numbers = tuple(normalize_phone(phone_num) for phone_num in raw_numbers)
print("Normalized phone numbers for sending SMS: ", data_formatted_numbers)
