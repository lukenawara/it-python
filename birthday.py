import datetime
from banner import banner

banner("BIRTHDAY", "Mr. Baldus")

# 1. Find out when you were born
# 2. Figure out how many days until your birthday
# 3. Print information about the birthday: Days until, Days ago, or Happy B-Day

def main():
    birthday = get_birthday_info()
    today = datetime.date.today()
    num_days = compute_days_between_dates(birthday, today)
    print_birthday_info(num_days)


def get_birthday_info():
    print("When were you born?")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    current_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = current_year - target_date
    return dt.days


def print_birthday_info(number_of_days):
    if number_of_days == 0:
        print("Happy Birthday!!")
    elif number_of_days < 0:
        print(f"Your birthday was {-number_of_days} days ago. Don't you remember?")
    else:
        print(f"Your birthday is in {number_of_days} days. Can't wait!")


main()