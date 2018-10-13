from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from django.views.generic import TemplateView
from .models import Image
from keras.models import load_model
from .models import TextFiles
import random
import numpy as np
from keras.preprocessing import image
from keras import backend as k

def home(request):
    template_name = 'index.html'
    form=ImageForm()
    return render(request,template_name,{'form':form})

class Model:
    def __init__(self):
        self.model=load_model('building_model.h5')

    def predict(self,sample_image):
        image1 = image.load_img(sample_image, target_size=(64, 64))
        image1 = image.img_to_array(image1)
        img1 = np.expand_dims(image1, 0)
        result = self.model.predict(img1)
        if (int(result) == 0):
            predict='No crack'
        else:
            predict='Crack'
        k.clear_session()
        return predict
class DeepAgri(TemplateView):
    template_name = 'DeepAgri.html'
    def post(self,request):
        if request.method=='POST':
            form=ImageForm(request.POST,request.FILES)
            if form.is_valid():
                num=random.randint(0,1000)
                model=Image(image=request.FILES['image'], name=str(num))
                model.save()
                obj=Image.objects.all()
                for img in obj:
                    if img.name==str(num):
                        pic_image=img.image
                        pic=img.image
                str_image=str(pic_image)
                list=str_image.split("/")
                img=list[1]
                model = Model()
                prediction=model.predict('media\\images\\' + img)
                return render(request, self.template_name,{'image': image,'pic':pic, 'predict': prediction})
        else:
            form=ImageForm()
        return render(request,'index.html',{'form':form})