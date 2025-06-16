from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо дату народження зі строки у об'єкт datetime.date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Отримуємо день народження в поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув у цьому році — переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи попадає день народження в наступні 7 днів
        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            # Якщо день народження припадає на суботу або неділю — переносимо на понеділок
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            # Додаємо у фінальний список словник з ім'ям та датою привітання
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Приклад тесту:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Ivan Petrov", "birthday": "1992.01.22"},
    {"name": "Olga Shevchenko", "birthday": "1980.01.20"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)