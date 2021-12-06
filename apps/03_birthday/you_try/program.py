import datetime
from datetime import date


def print_header():
    print("---------------------------")
    print("      BIRTHDAY APP")
    print("---------------------------")


def get_bday_info():
    year = int(input("In which year where you born [YYYY]?"))
    month = int(input("In which month where you born [MM]?"))
    day = int(input("In which day where you born [DD]?"))
    return datetime.date(year, month, day)


def compute_days(birthday: datetime.date, today: datetime.date) -> datetime.timedelta:
    modifiedBirthday: date = datetime.date(today.year, birthday.month, birthday.day)
    return modifiedBirthday - today


def print_bday_message(delta: datetime.timedelta):
    if delta.days < 0:
        print("Your birthday was {} days ago".format(-delta.days))
    elif delta.days > 0:
        print("Your birthday will be in {} days ".format(delta.days))
    else:
        print("Happy birthday!")
    pass


def main():
    print_header()
    bday = get_bday_info()
    delta = compute_days(bday, datetime.date.today())
    print_bday_message(delta)


main()
