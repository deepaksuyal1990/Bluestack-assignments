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
        if args[0] not in range(1, 32):
            raise ValueError("Date should be in range 1 to 31")
        elif args[1] not in range(1, 13):
            raise ValueError("Month should be in range 1 to 12")
        elif args[2] not in range(1800, 2101):
            raise ValueError("year should be in range 1800 to 2100")

    @staticmethod
    def get_next_date(inp):
        """
        Calculate next date for a given date

        :returns Next calculated date in format DD/MM/YYY and error message for ValueError
        """
        try:
            date = inp.split("/")
            day, month, year = int(date[0]), int(date[1]), int(date[2])
            Nextdate.date_validator(day, month, year)
            date_format = '%d/%m/%Y'
            input_date = datetime.strptime(inp, date_format)
            # Add 1 day to input date
            value = input_date + timedelta(days=1)
            return value.strftime("%d/%m/%Y")
        except ValueError as exc:
            return exc
