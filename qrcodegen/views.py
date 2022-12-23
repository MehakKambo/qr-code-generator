from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time

# Create your views here.

def qr_gen(request):
    if request.method == "POST":
        data = request.POST('data')