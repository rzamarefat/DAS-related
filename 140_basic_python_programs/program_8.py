"""
Write a Python program to display calendar.
"""

def display_calendar():
    import calendar
    year = input("Please enter the year: ")
    month = input("Please enter the month: ")

    cal = calendar.month(int(year), int(month))
    print(cal)


if __name__ == "__main__":
    display_calendar()
