"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month == 12:
        return (datetime.datetime(year+1, 1, 1) - datetime.datetime(year, month, 1)).days
    return (datetime.datetime(year, month+1, 1) - datetime.datetime(year, month, 1)).days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    #gave me warning here to simplify the chainings
    #huh, whatever
    #like I care!!!!!!!!!!!!!!!!!!!!!!
    #I scored 97% bitch
    if (year >= datetime.MINYEAR) and (year <= datetime.MAXYEAR):
        if (month > 0) and (month < 13):
            if (day > 0) and (day <= days_in_month(year, month)):
                return True
    return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        earlier = datetime.datetime(year1, month1, day1)
        later = datetime.datetime(year2, month2, day2)
        if earlier > later:
            return 0
        diff = later - earlier
        return diff.days
    return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year, month, day):
        birth = datetime.datetime(year, month, day)
        birth = birth.date()
        today = datetime.date.today()
        if (birth > today):
            return 0
        return (today-birth).days
    return 0


#print(days_in_month(2020,2))
#97 score
#take that bitch
