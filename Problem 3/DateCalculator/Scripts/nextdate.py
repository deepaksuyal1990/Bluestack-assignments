"""Nextdate class"""
from datetime import datetime, timedelta


class Nextdate:
    """Class containing methods to calculate next date from a provided date"""
    @staticmethod
    def date_validator(*args):
        """
        Validate the input

        :returns Respective validation message
        """
        value = "Pass"
        if not args[0] in range(32):
            value = "Invalid value for date"
        elif not args[1] in range(13):
            value = "Invalid value for month"
        elif not args[2] in range(1799, 2101):
            value = "year value should be between 1800 to 2100"

        return value

    @staticmethod
    def get_next_date(inp):
        """
        Calculate next date for a given date

        :returns Next calculated date in format DD/MM/YYY and error message for ValueError
        """
        try:
            date = inp.split("/")
            day, month, year = int(date[0]), int(date[1]), int(date[2])
            value = Nextdate.date_validator(day, month, year)
            if value == "Pass":
                date_format = '%d/%m/%Y'
                now = datetime.strptime(inp, date_format)
                value = (now + timedelta(days=1)).strftime("%d/%m/%Y")
            return value
        except ValueError:
            return "Only numeric values are allowed"
