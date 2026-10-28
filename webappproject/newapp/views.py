from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
from tensorflow.keras.utils import load_img, image_dataset_from_directory
from keras.utils import img_to_array
from tensorflow import data, math
from tensorflow.keras.models import load_model
from tensorflow.keras.applications import resnet50
from tensorflow.keras import layers, models, optimizers
import tempfile
from pathlib import Path
from . import constants as c
from .models import ImageSubmit, NumberInput, FileSubmit

Item = ""
Item2 = ""
Item3 = ""
Item4 = ""
Number=""
inputType = ""
predictions=""
# Create your views here.
def home(request):
    form = NumberInput()
    return render(request, 'newapp/home.html',{'form': form})

def photo(request):
    inputType = "camera"
    form = ImageSubmit()
    disclaimer= "*note: Camera only works on mobile devices"
    return render(request,
                  'newapp/photoinput.html',
                  {'form': form, 'disclaimer': disclaimer})

def file(request):
    inputType = "file"
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
    return HttpResponse("Successfully trained!", content_type="text/html")

def number(request):
    global Number
    if request.method == "POST":
        form = NumberInput(request.POST)
        if form.is_valid():
            Number = form.cleaned_data["plastic_number"]
            if 'e' in str(Number) or int(Number) > 7:
                form = NumberInput()
                return render(request,
                              'newapp/home.html',
                              {'form': form})
            Number = int(form.cleaned_data["plastic_number"])
            Item = f"#{Number} Plastic"
            return render(request,
                      'newapp/info.html',
                      {'article': '', 'Item': Item, 'Category': c.data[Item]['Category'],
                       'Status': c.data[Item]['Status'], 'WhyORexamples': c.data[Item]['Examples'], 'li3':"Examples", 'more':''})
        else:
            print("Form Errors:", form.errors.as_data())
            print("Raw POST data was:", request.POST)
            form = NumberInput()
            return render(request,
                          'newapp/home.html',
                          {'form': form})
    else:
        Item = f"#{Number} Plastic"
        return render(request,
                      'newapp/info.html',
                      {'article': '', 'Item': Item, 'Category': c.data[Item]['Category'],
                       'Status': c.data[Item]['Status'], 'WhyORexamples': c.data[Item]['Examples'], 'li3':"Examples", 'more':''})

def analyze(request):
    global Item
    global Item2
    global Item3
    global Item4
    global predictions
    this_directory = Path(__file__).resolve().parent
    if request.method == "POST":
        if inputType == "camera":
            form = ImageSubmit(request.POST, request.FILES)
        else:
            form = FileSubmit(request.POST, request.FILES)
        if form.is_valid():
            originalfile = form.cleaned_data["input_file"]
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
            class_names = ["Bottle Cap", "Cereal Bag", "Milk Jug", "PET Bottle", "Plastic Bag", "Plastic Utensil",
                           "Plastic Wrapper", "Single-use Cup", "Soap Bottle", "Spray Bottle", "Takeout Container",
                           "Water Jug",
                           "Yogurt Container"]
            model.summary()
            raw_predictions = model.predict(img)
            predictions = np.argsort(raw_predictions[0])[-4:][::-1]
            print("Raw model predictions:", raw_predictions)
            predicted_label = class_names[np.argmax(raw_predictions[0])]
            confidence_score = round(float(raw_predictions[0][predictions[0]] * 100), 2)
            print(f"{predicted_label} + {confidence_score}")
            Item = predicted_label
            Item2 = class_names[predictions[1]]
            Item3 = class_names[predictions[2]]
            Item4 = class_names[predictions[3]]
            if file_path.exists():
                file_path.unlink()
            if Item[0].lower() == "a" or Item[0].lower() == "i" or Item[0].lower() == "o" or Item[0].lower() == "e" or \
                    Item[0].lower() == "u":
                article = "Looks like this is an: "
            else:
                article = "Looks like this is a: "
            more = f"""<li class="listitem"><input type="radio" name="accordion" id="fourth"><label for="fourth">Doesn't Look Right?</label><div class="content"><p>This result was only {confidence_score}% confident, so here are some other possibilities:</p><br><a href="{reverse('possibility-2')}" role="button" class="btn btn-outline-dark">{Item2} - {round(float(raw_predictions[0][predictions[1]] * 100), 2)}%</a><br><a href="{reverse('possibility-3')}" role="button" class="btn btn-outline-dark">{Item3} - {round(float(raw_predictions[0][predictions[2]] * 100), 2)}%</a><br><a href="{reverse('possibility-4')}"  role="button" class="btn btn-outline-dark">{Item4} - {round(float(raw_predictions[0][predictions[3]] * 100), 2)}%</a></div></li>"""
            return render(request,
                          'newapp/info.html',
                          {'article': article, 'Item':Item, 'Category': c.data[Item]['Category'],
                           'Status': c.data[Item]['Status'], 'WhyORexamples': c.data[Item]['Why'], 'li3':"Why?", 'more':more})
        else:
            print("Form Errors:", form.errors.as_data())
            print("Raw POST data was:", request.POST)
            form = ImageSubmit()
            return render(request,
                          'newapp/photoinput.html',
                          {'form': form})
    else:
        if Item[0].lower() == "a" or Item[0].lower() == "i" or Item[0].lower() == "o" or Item[0].lower() == "e" or \
                Item[0].lower() == "u":
            article = "Looks like this is an: "
        else:
            article = "Looks like this is a: "
        return render(request,
                      'newapp/info.html',
                      {'article': article, 'Item': Item, 'Category': c.data[Item]['Category'],
                       'Status': c.data[Item]['Status'], 'WhyORexamples': c.data[Item]['Why'], 'li3':"Why?", 'more':''})


def op2(request):
    if Item2[0].lower() == "a" or Item2[0].lower() == "i" or Item2[0].lower() == "o" or Item2[0].lower() == "e" or \
            Item2[0].lower() == "u":
        article = "This could also be an: "
    else:
        article = "This could also be a: "
    more = f"""<li class="listitem"><input type="radio" name="accordion" id="fourth"><label for="fourth">Doesn't Look Right?</label><div class="content"><p>Other possibilities:</p></a><br><a href="{reverse('possibility-3')}" role="button" class="btn btn-outline-dark">{Item3}</a><br><a href="{reverse('possibility-4')}"  role="button" class="btn btn-outline-dark">{Item4}</a></div></li>"""
    return render(request,
                  'newapp/info.html',
                  {'article': article, 'Item': Item2, 'Category': c.data[Item2]['Category'],
                   'Status': c.data[Item2]['Status'], 'WhyORexamples': c.data[Item2]['Why'], 'li3': "Why?", 'more': more})

def op3(request):
    if Item3[0].lower() == "a" or Item3[0].lower() == "i" or Item3[0].lower() == "o" or Item3[0].lower() == "e" or \
            Item3[0].lower() == "u":
        article = "This could also be an: "
    else:
        article = "This could also be a: "
    more = f"""<li class="listitem"><input type="radio" name="accordion" id="fourth"><label for="fourth">Doesn't Look Right?</label><div class="content"><p>Other possibilities:</p></a><br><a href="{reverse('possibility-2')}" role="button" class="btn btn-outline-dark">{Item2}</a><br><a href="{reverse('possibility-4')}"  role="button" class="btn btn-outline-dark">{Item4}</a></div></li>"""
    return render(request,
                  'newapp/info.html',
                  {'article': article, 'Item': Item3, 'Category': c.data[Item3]['Category'],
                   'Status': c.data[Item3]['Status'], 'WhyORexamples': c.data[Item3]['Why'], 'li3': "Why?",
                   'more': more})

def op4(request):
    if Item4[0].lower() == "a" or Item4[0].lower() == "i" or Item4[0].lower() == "o" or Item4[0].lower() == "e" or \
            Item4[0].lower() == "u":
        article = "This could also be an: "
    else:
        article = "This could also be a: "
    more = f"""<li class="listitem"><input type="radio" name="accordion" id="fourth"><label for="fourth">Doesn't Look Right?</label><div class="content"><p>Other possibilities:</p></a><br><a href="{reverse('possibility-2')}" role="button" class="btn btn-outline-dark">{Item2}</a><br><a href="{reverse('possibility-3')}"  role="button" class="btn btn-outline-dark">{Item3}</a></div></li>"""
    return render(request,
                  'newapp/info.html',
                  {'article': article, 'Item': Item4, 'Category': c.data[Item4]['Category'],
                   'Status': c.data[Item4]['Status'], 'WhyORexamples': c.data[Item4]['Why'], 'li3': "Why?",
                   'more': more})