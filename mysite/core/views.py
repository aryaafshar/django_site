from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
#from django.urls import reverse_lazy
from mysite.settings import *
#from .forms import BookForm
#from .models import Book
import torch


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        
        
        

        # Images
        #imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images

        # Inference
        if (name!=None):
            
            model = torch.hub.load('ultralytics/yolov5','custom', BASE_DIR + '/best.pt')
            results = model("media"+"/"+name)
            results.save(save_dir='media/result',exist_ok=True)  # or .show()
            name='result/'+name
            context['url'] = fs.url(name)
        
        # Results
        
        
        
   
        #results.xyxy[0]  # img1 predictions (tensor)
        #results.pandas().xyxy[0]  # img1 predictions (pandas)
        context['url'] = fs.url(name)

    return render(request, 'upload.html', context)

def video(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        
        
        

        # Images
        #imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images

        # Inference
        if (name!=None):
            
            model = torch.hub.load('ultralytics/yolov5','custom', BASE_DIR + '/best.pt')
            vd="media/"+name
            model
            results=model(vd)
             
            results.save(save_dir='media/result',exist_ok=True)  # or .show()
            name='result/'+name
            context['url'] = fs.url(name)
        
        # Results
        
        
        
   
        #results.xyxy[0]  # img1 predictions (tensor)
        #results.pandas().xyxy[0]  # img1 predictions (pandas)
        context['url'] = fs.url(name)

    return render(request, 'video.html', context)
