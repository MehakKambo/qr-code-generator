from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from qrcode import *
import time
from io import BytesIO

# Create your views here.

def qr_gen(request):
    if request.method == "POST":
        data = request.POST['data']
        img = make(data)
        response = HttpResponse(content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="output.png"'
        img.save(response,"PNG")
        return response
    return render(request, 'index.html')