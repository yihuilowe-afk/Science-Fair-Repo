from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
from tensorflow.keras.utils import load_img
from keras.utils import img_to_array
from keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications import resnet50
import tempfile
from pathlib import Path
from django.core.files.storage import default_storage
from . import constants as c
from .models import ImageSubmit, NumberInput

Item = ""
Number=""
# Create your views here.
def home(request):
    form = NumberInput()
    return render(request, 'newapp/home.html',{'form': form})

def photo(request):
    form = ImageSubmit()
    return render(request,
                  'newapp/photoinput.html',
                  {'form': form})

def number(request):
    global Number
    if request.method == "POST":
        form = NumberInput(request.POST)
        if form.is_valid():
            Number = int(form.cleaned_data["plastic_number"])
            if Number > 7:
                Number = 7
            return HttpResponse(f"{c.numbers_head(f"#{Number} plastic")}", content_type= "text/html")
        else:
            print("Form Errors:", form.errors.as_data())
            print("Raw POST data was:", request.POST)
            form = NumberInput()
            return render(request,
                          'newapp.html',
                          {'form': form})
    else:
        return HttpResponse(f"{c.numbers_head(f"#{Number} plastic")}", content_type="text/html")

def analyze(request):
    global Item
    if request.method == "POST":
        form = ImageSubmit(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["camera_file"]
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in file.chunks():
                    temp_file.write(chunk)
                temp_file.close()
                file_path = Path(temp_file.name)
            print(file_path)
            original = load_img(file_path, target_size=(224, 224))
            np_img = img_to_array(original)
            inputimg = np.expand_dims(np_img, axis=0)
            img = resnet50.preprocess_input(inputimg.copy())
            model = resnet50.ResNet50(weights="imagenet")
            predictions = model.predict(img)
            label = decode_predictions(predictions)
            Possibilities =[]
            for i in range(5):
                percent = float(label[0][i][2] * 100)
                Possibilities.append({"Name": f"{label[0][i][1]}", "Percent": f"{round(percent, 2)}%"})
            Item = Possibilities[0]["Name"]
            if file_path.exists():
                file_path.unlink()
            return HttpResponse(f"{c.html_head(Item)}", content_type= "text/html")
        else:
            print("Form Errors:", form.errors.as_data())
            print("Raw POST data was:", request.POST)
            form = ImageSubmit()
            return render(request,
                          'newapp/photoinput.html',
                          {'form': form})
    else:
        return HttpResponse(f"{c.html_head(Item)}", content_type="text/html")


