from datetime import datetime

def get_days_from_today(date: str):
    try:
        you_input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        days_count = (today - you_input_date).days
        return days_count
        
    except ValueError:
        print('Please, input data in YYYY-MM-DD format!')

user_date = input("Please enter the date (YYYY-MM-DD): ")
result = get_days_from_today(user_date)
print(result) 