from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

now = datetime.now()

def time (request):
    return HttpResponse(f"This is {now.strftime('%H:%M:%S')}")
