from django.shortcuts import render
from datetime import datetime

def current_datetime(request):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'current_datetime.html', {'current_datetime': current_datetime})