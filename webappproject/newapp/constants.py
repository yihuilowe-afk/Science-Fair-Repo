from django.urls import reverse
data= {
    "lotion":{
        "Category":"Paper",
        "Status":"Recyclable"
    },
    "#1 Plastic": {
        "Category":"<p>PETE/PET plastic (Polyethylene terephthalate)</p>",
        "Status":"<p>Recyclable</p>",
        "Examples":"<ul><li>Single-use drink bottles</li><li>Condiment containers</li><li>Produce containers</li></ul>"
    },
    "#2 Plastic": {
        "Category":"<p>HDPE/PE-HD plastic (High density polyethylene)</p>",
        "Status":"<p>Recyclable</p>",
        "Examples":"<ul><li>Milk jugs</li><li>Shampoo/conditioner bottles</li><li>Some cereal/grocery bags <ul><li>Note: no plastic bags are accepted for municipal recycling</li></ul></li></ul>"
    },
    "#3 Plastic": {
        "Category":"PVC/V plastic (Polyvinyl chloride)",
        "Status":"Not Reyclable",
        "Examples":"<ul><li>Piping</li><li>Children's/pet's toys</li><li>Medical Equipment</li></ul>"
    },
    "#4 Plastic": {
        "Category": "LDPE/LD-PE plastic (Low density Polyethylene)",
        "Status": "Not Recyclable",
        "Examples":"<ul><li>Shrink wrap</li><li>Bubble wrap</li><li>Shopping/bread bags</li></ul>"
    },
    "#5 Plastic": {
        "Category": "PP plastic (Polypropylene)",
        "Status": "Recyclable",
        "Examples":"<ul><li>Yogurt containers</li><li>Medicine/syrup bottles</li><li>Straws</li></ul>"
    },
    "#6 Plastic": {
        "Category": "PS plastic (Polystyrene)",
        "Status": "Not Recyclable",
        "Examples":"<ul><li>Egg cartons</li><li>Disposable cups/plates</li><li>Takeout containers</li></ul>"
    },
    "#7 Plastic": {
        "Category": 'Other/"O" plastics',
        "Status": "Not Recyclable",
        "Examples":"<ul><li>Car parts</li><li>Medical/electronic equipment</li><li>Sunglasses</li></ul>"
    },
}

def html_head(Item):
    home_url = reverse('home')
    if Item[0].lower() == "a" or Item[0].lower() == "i" or Item[0].lower() == "o" or Item[0].lower() == "e" or Item[0].lower() == "u":
        article= "This is likely an: "
    else:
        article= "This is likely a: "
    return ("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <title>RecycLabel Chicago</title>
    <style>
        header {
        background-color: #6c757d;}

        .margined{
        margin-left: 20px;
        margin-right: 20px;
        margin-top: 10px;
        margin-bottom: 10px;}
        
        .accordion{
        width:600px;}

        .accordion .listitem{
        list-style:none;
        width:90vw;
        margin-bottom: 20px;
        padding: 10px;
        border-radius: 8px;
        background: #8c9299;
        box-shadow:6px 6px 10px -1px rgba(0, 0, 0, 0.15),
                    -6px -6px 10px -1px rgba(255, 255, 255, 0.7)}

        .accordion li label{
        display: flex;
        align-items: center;
        padding: 10px;
        font-size: 18px;
        font-weight: 500;
        cursor: pointer;}

        label::before{
        content: '+';
        margin-right: 10px;
        margin-bottom: 5px;
        font-size: 24px;
        font-weight: 600px;}

        input[type="radio"]{
        display:none;}

        .accordion .content{
        padding:0 10px;
        line-height: 26 px;
        max-height:0;
        overflow: hidden;
        transition: max-height 0.5s, padding 0.5s;}

        .accordion input[type="radio"]:checked + label + .content{
        max-height: 400px;
        padding: 10px 10px 20px;}

        .accordion input[type="radio"]:checked + label::before{
        content: "-";}
    </style>
</head>
<body>
    <header>
        <br>
        <div class="margined">
            <h1>
                Get Identifying - Photo Recognition
            </h1>
        </div>
    </header>
    <br>
    <a href="""+f'"{home_url}"'+""" role="button" class="btn btn-outline-secondary margined">Home</a>
    <br>
    <hr>
    <div class="margined">
        <h2>
""" + f"{article}<strong>{Item}</strong>" + """
        </h2>
    </div>
    <hr>
    <br>
    <ul class="accordion">
        <li class="listitem">
            <input type="radio" name="accordion" id="first">
            <label for="first">Item Category</label>
            <div class="content">
                <p>""" + data[Item]["Category"].lower() + """</p>
            </div>
        </li>
        <li class="listitem">
            <input type="radio" name="accordion" id="second">
            <label for="second">Recyclable?</label>
            <div class="content">
                <p>you bet it is!</p>
            </div>
        </li>
        <li class="listitem">
            <input type="radio" name="accordion" id="third">
            <label for="third">Recyclable?</label>
            <div class="content">
                <p>you bet it is!</p>
            </div>
        </li>
        <li class="listitem">
            <input type="radio" name="accordion" id="fourth">
            <label for="fourth">Recyclable?</label>
            <div class="content">
                <p>you bet it is!</p>
            </div>
        </li>
    </ul>
</body>
""")


def numbers_head(Item):
    home_url = reverse('home')
    return ("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <title>RecycLabel Chicago</title>
    <style>
        header {
        background-color: #6c757d;}

        .margined{
        margin-left: 20px;
        margin-right: 20px;
        margin-top: 10px;
        margin-bottom: 10px;}

        .accordion{
        width:600px;}

        .accordion .listitem{
        list-style:none;
        width:90vw;
        margin-bottom: 20px;
        padding: 10px;
        border-radius: 8px;
        background: #8c9299;
        box-shadow:6px 6px 10px -1px rgba(0, 0, 0, 0.15),
                    -6px -6px 10px -1px rgba(255, 255, 255, 0.7)}

        .accordion li label{
        display: flex;
        align-items: center;
        padding: 10px;
        font-size: 18px;
        font-weight: 500;
        cursor: pointer;}

        label::before{
        content: '+';
        margin-right: 10px;
        margin-bottom: 5px;
        font-size: 24px;
        font-weight: 600px;}

        input[type="radio"]{
        display:none;}

        .accordion .content{
        padding:0 10px;
        line-height: 26 px;
        max-height:0;
        overflow: hidden;
        transition: max-height 0.5s, padding 0.5s;}

        .accordion input[type="radio"]:checked + label + .content{
        max-height: 400px;
        padding: 10px 10px 20px;}

        .accordion input[type="radio"]:checked + label::before{
        content: "-";}
    </style>
</head>
<body>
    <header>
        <br>
        <div class="margined">
            <h1>
                Get Identifying - Photo Recognition
            </h1>
        </div>
    </header>
    <br>
    <a href="""+f'"{home_url}"'+""" role="button" class="btn btn-outline-secondary margined">Home</a>
    <br>
    <hr>
    <div class="margined">
        <h2>
""" + f"<strong>{Item}</strong>" + """
        </h2>
    </div>
    <hr>
    <br>
    <ul class="accordion">
        <li class="listitem">
            <input type="radio" name="accordion" id="first">
            <label for="first">Item Category</label>
            <div class="content">
                <p>""" + data[Item]["Category"] + """</p>
            </div>
        </li>
        <li class="listitem">
            <input type="radio" name="accordion" id="second">
            <label for="second">Examples</label>
            <div class="content">
                <p>"""+ data[Item]["Examples"] +"""</p>
            </div>
        </li>
        <li class="listitem">
            <input type="radio" name="accordion" id="third">
            <label for="third">Recyclable?</label>
            <div class="content">
                <p>"""+ data[Item]["Status"] +"""</p>
            </div>
        </li>
        <li class="listitem">
            <input type="radio" name="accordion" id="fourth">
            <label for="fourth">Recyclable?</label>
            <div class="content">
                <p>you bet it is!</p>
            </div>
        </li>
    </ul>
</body>
""")

