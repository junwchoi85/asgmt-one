import datetime

DATE_FORMATS = [
    "%Y-%m-%d",
    "%d-%m-%Y",
    "%m/%d/%Y",
    "%d/%m/%Y",
    "%Y.%m.%d",
    "%d.%m.%Y",
    "%B %d, %Y",
    "%d %B %Y",
    "%Y%m%d",
    "%d%m%Y",
]


def parse_date(date_str: str) -> datetime:
    """
    Parse a date string to a datetime object
    """
    for date_format in DATE_FORMATS:
        try:
            return datetime.datetime.strptime(date_str, date_format)
        except ValueError:
            continue
    raise ValueError(f"Invalid date format: {date_str}")


def get_today():
    """
    Get today's date
    :return: Today's date
    """
    return datetime.date.today()


def get_one_month_from_today():
    """
    Get the date one month from today
    :return: The date one month from today
    """
    today = get_today()
    return today + datetime.timedelta(days=30)


def format_date(date):
    """
    Format a date as 'YYYY-MM-DD'
    :param date: Date to format
    :return: Formatted date
    """
    return date.strftime('%Y-%m-%d')


def get_today_formatted():
    """
    Get today's date formatted as 'YYYY-MM-DD'
    :return: Today's date formatted as 'YYYY-MM-DD'
    """
    return format_date(get_today())


def get_one_month_from_today_formatted():
    """
    Get the date one month from today formatted as 'YYYY-MM-DD'
    :return: The date one month from today formatted as 'YYYY-MM-DD'
    """
    return format_date(get_one_month_from_today())


def get_x_weeks_from_today(x):
    """
    Get the date x weeks from today
    :param x: Number of weeks
    :return: The date x weeks from today
    """
    today = get_today()
    return today + datetime.timedelta(weeks=x)


def get_x_weeks_from_today_formatted(x):
    """
    Get the date x weeks from today formatted as 'YYYY-MM-DD'
    :param x: Number of weeks
    :return: The date x weeks from today formatted as 'YYYY-MM-DD'
    """
    return format_date(get_x_weeks_from_today(x))


if __name__ == '__main__':
    print(parse_date('20210101').strftime('%Y-%m-%d'))
