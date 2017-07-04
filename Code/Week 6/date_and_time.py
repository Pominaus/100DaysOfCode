#
# This module was just a practice with the datetime library and dates. It's a simple way to convert the ISO
# date format 'yyyy-mm-dd' to letterhead format 'dd/mon/yyyy'.
#
import datetime


def month(key):
    """ Turns a given number into a 3 letter month string
    raises a ValueError if month is not valid int (1-12 inclusive)"""

    month_dict = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    try:
        output = month_dict[key]
    except KeyError:
        raise ValueError("Entered month number({}) is not valid".format(key))
    else:
        return output


def date_str(date_obj):
    """Takes a datetime object and returns a string in the format
    dd/mmm/yyyy where d,y are ints and m is a string"""

    dd, yyyy = date_obj.day, date_obj.year
    mmm = month(date_obj.month)
    return "{}/{}/{}".format(dd,mmm,yyyy)


def get_date(date=None, *args, **kwargs):
    """Returns a date in the format DD/MMM/YYYY
    If no argument is passed, returns today's date as set by the datetime module
    Accepts one optional argument 'date', a datetime object.
    If present returns formatted date of 'date' parameter."""

    date_obj = (date or datetime.date.today())
    return date_str(date_obj)


if __name__ == "__main__":
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    tomorrow = today + one_day
    yesterday = today - one_day
    yesterday_date = get_date(yesterday)
    today_date = get_date()
    tomorrow_date = get_date(tomorrow)
    print(yesterday_date, tomorrow_date, today_date)




