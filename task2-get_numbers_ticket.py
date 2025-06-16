import random

def get_numbers_ticket(min, max, quantity):
    if not 1 <= quantity <= (max - min + 1):
        return[]
    if not min < max:
        return[]
    if not (1 <= min <= 1000 and 1 <= max <= 1000):
        return[]
    lottery_numbers = random.sample(range(min, max + 1), quantity)
    return lottery_numbers

lottery_numbers = get_numbers_ticket(10, 20, 3)
print("Ваші лотерейні числа:", lottery_numbers)