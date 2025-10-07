import random

def get_numbers_ticket(min_num, max_num, quantity):
    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []

    return sorted(random.sample(range(min_num, max_num + 1), quantity))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
