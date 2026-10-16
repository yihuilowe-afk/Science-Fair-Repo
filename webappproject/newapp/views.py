
from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
from tensorflow.keras.utils import load_img, image_dataset_from_directory
from keras.utils import img_to_array
from tensorflow import data
from tensorflow.keras.models import load_model
from tensorflow.keras.applications import resnet50
from tensorflow.keras import layers, models, optimizers
import tempfile
from pathlib import Path
from . import constants as c
from .models import ImageSubmit, NumberInput, FileSubmit

Item = ""
Number=""
# Create your views here.
def home(request):
    form = NumberInput()
    return render(request, 'newapp/home.html',{'form': form})

def photo(request):
    form = ImageSubmit()
    disclaimer= "*note: Camera only works on mobile devices"
    return render(request,
                  'newapp/photoinput.html',
                  {'form': form, 'disclaimer': disclaimer})

def file(request):
    form = FileSubmit()
    disclaimer = ""
    return render (request,
                   'newapp/photoinput.html',
                   {'form':form, 'disclaimer':disclaimer})

def train_model(request):
    this_directory = Path(__file__).resolve().parent
    dataset = this_directory / "dataset"
    train_dataset = image_dataset_from_directory(
        dataset,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(224, 224),
        batch_size=32,
        label_mode="categorical"
    )
    val_dataset = image_dataset_from_directory(
        dataset,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(224, 224),
        batch_size=32,
        label_mode="categorical"
    )
    class_names = train_dataset.class_names
    print("Discovered classes:", class_names)
    model = resnet50.ResNet50(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    model.trainable = False
    inputs = layers.Input(shape=(224, 224, 3))
    x = resnet50.preprocess_input(inputs)
    x = model(x, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    num_classes = len(class_names)
    outputs = layers.Dense(num_classes, activation='softmax')(x)
    model = models.Model(inputs, outputs)
    model.compile(
        optimizer=optimizers.Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    AUTOTUNE = data.AUTOTUNE
    train_dataset = train_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_dataset = val_dataset.cache().prefetch(buffer_size=AUTOTUNE)
    model.fit(
        train_dataset,
        validation_data=val_dataset,
        epochs=10
    )
    model_save_path = this_directory / "trash_data_resnet50.keras"
    model.save(str(model_save_path))

def number(request):
    global Number
    if request.method == "POST":
        form = NumberInput(request.POST)
        if form.is_valid():
            Number = int(form.cleaned_data["plastic_number"])
            if Number > 7:
                Number = 7
            return HttpResponse(f"{c.numbers_head(f"#{Number} Plastic")}", content_type= "text/html")
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
    this_directory = Path(__file__).resolve().parent
    if request.method == "POST":
        form = ImageSubmit(request.POST, request.FILES)
        if form.is_valid():
            originalfile = form.cleaned_data["image_file"]
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in originalfile.chunks():
                    temp_file.write(chunk)
                temp_file.close()
                file_path = Path(temp_file.name)
            print(file_path)
            original = load_img(file_path, target_size=(224, 224))
            np_img = img_to_array(original)
            inputimg = np.expand_dims(np_img, axis=0)
            img = resnet50.preprocess_input(inputimg.copy())
            model = load_model(str(this_directory / "trash_data_resnet50.keras"))
            class_names = ["Aluminum Can", "Baby Bottle", "Cleaning Product", "PET Bottle", "PET Bottle", "Soap Bottle", "Yogurt Container"]
            model.summary()
            predictions = model.predict(img)
            predicted_index = np.argmax(predictions[0])
            predicted_label = class_names[predicted_index]
            confidence_score = round(predictions[0][predicted_index] * 100, 2)
            print(f"{predicted_label} + {confidence_score}")
            Item = predicted_label
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


