from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
#from .forms import *
from .models import ImageModel
from django.views.generic import CreateView
from django.conf import settings

#遊び
import cv2
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
        gray(last_img.img.url)
        edge(last_img.img.url)
        last_img.edge = 'edge.jpg'
        last_img.gray = 'gray.jpg'
        last_img.save()
        return render(request, 'display_image.html', {'last_img' : last_img})
def display_imag_2(request):
    last_img = ImageModel.objects.order_by("id").last() 
    return render(request, 'display_image_2.html', {'last_img' : last_img})


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

def edge(url):
    print(url)
    path = str(settings.BASE_DIR) + url
    print(path)
    img = cv2.imread(path)
    img_edge = cv2.Canny(img,180,300)
    output = str(settings.BASE_DIR) + "/media/edge.jpg"

    cv2.imwrite(output, img_edge)
   