import re

def normalize_phone(phone_number):
    # Видаляємо всі символи крім цифр і плюса
    cleaned = re.sub(r'[^\d+]', '', phone_number.strip())
    
    # Очищаємо зайві плюси: залишаємо тільки перший плюс
    if cleaned.startswith('+'):
        cleaned = '+' + cleaned[1:].replace('+', '')
    else:
        cleaned = cleaned.replace('+', '')
    
    # Виділяємо тільки цифри
    digits_only = re.sub(r'\D', '', cleaned)

    # Логіка нормалізації
    if digits_only.startswith('380'):
        normalized = '+380' + digits_only[3:]
    elif digits_only.startswith('0'):
        normalized = '+38' + digits_only
    else:
        normalized = None

    # Перевіряємо, що номер нормальної довжини (12 цифр після +)
    if normalized and len(normalized) == 13:
        return normalized
    else:
        return None


# Приклад використання:
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "++380 44 123 4567", 
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = []
for num in raw_numbers:
    normalized = normalize_phone(num)
    if normalized:
        sanitized_numbers.append(normalized)

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)