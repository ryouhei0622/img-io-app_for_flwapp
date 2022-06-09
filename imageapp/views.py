from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
#from .forms import *
from .models import ImageModel
from django.views.generic import CreateView
from django.conf import settings

import os, cv2, sys, re, math, Levenshtein, pickle, shutil, math
import numpy as np
import pandas as pd

from infer.infer import *

# Create your views here.
class image_upload(CreateView):
    #テンプレートファイルの連携
    template_name = 'image_upload.html'
    #テーブルの連携
    model = ImageModel
    #入力項目の定義
    fields = ('name', 'author', 'img')
    #リダイレクト先を指定
    success_url = reverse_lazy('display')
    pass

def success(request):
    return render(request,'success.html')

def display_img(request):


    if request.method == 'GET':
        # getting all the objects of hotel.
        # imgs = img.objects.all()
        # return render(request, 'display_img.html', {'imgs' : imgs})
        last_img = ImageModel.objects.order_by("id").last() 
        #img_gray = cv2.cvtColor(last_img, cv2.COLOR_BGR2GRAY)'
        bb, contour4mask, df_n, ARR = infer_arr(str(settings.BASE_DIR) + last_img.img.url)
        # gray(last_img.img.url)
        result(last_img.img.url)
        last_img.gray = "gray.jpg"
        last_img.save()
        print(last_img.img.url)
        return render(request, 'display_image.html', {'last_img' : last_img})



def home(request):
    return render(request, 'home.html')

def gray(url):
    print(url)
    path = str(settings.BASE_DIR) + url
    print(path)
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output = str(settings.BASE_DIR) + "/media/gray.jpg"

    cv2.imwrite(output, img_gray)

def result(url):
    print(1, url)
    path = str(settings.BASE_DIR) + '/data/img_lr.png'
    print(2, path)
    img = cv2.imread(path)
    result_img = img
    output = str(settings.BASE_DIR) + "/media/gray.jpg"

    cv2.imwrite(output, result_img)
   