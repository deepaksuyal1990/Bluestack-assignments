from django.shortcuts import render
from Scripts.nextdate import Nextdate


def output(request):
    return render(request, 'page.html')

def calculatedate(request):
    """Calculate next date"""
    day = request.POST.get('Date')
    month = request.POST.get('Month')
    year = request.POST.get('Year')
    date = '{}/{}/{}'.format(day, month, year)
    data = Nextdate.get_next_date(date)
    return render(request, 'page.html', {"data": data})
