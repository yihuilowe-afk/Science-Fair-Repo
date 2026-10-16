from django.urls import reverse
data= {
    "Aluminum Can":{
        "Category":"Aluminum",
        "Status":"Recyclable - If empty",
        "Why":"Liquid may make the item too heavy to be moved by airflow during sorting"
    },
    "PET Bottle":{
        "Category":"#1 Plastic - PETE/PET plastic (Polyethylene terephthalate)",
        "Status":"Recyclable - If empty",
        "Why":"Liquid may make the item too heavy to be moved by airflow during sorting"
    },
    "Cleaning Product":{
        "Category":"#1 Plastic - PETE/PET plastic (Polyethylene terephthalate)",
        "Status": "Recyclable - If empty and cleaned. Additionally, put the spray trigger/pump back on the bottle before recycling it.",
        "Why":"The spray trigger is also recyclable, but is too small to be recycled on its own"
    },
    "Yogurt Container": {
        "Category": "#5 Plastic - PP plastic (Polypropylene)",
        "Status": "Recyclable - Clean and dry the container. If its cap is plastic, you can recycle that too, but if it's foil, it's not recyclable",
        "Why":"The foil used on yogurt containers often contains a plastic film which makes it difficult to recycle"
    },
    "Soap Bottle":{
        "Category":"#1 Plastic - PETE/PET plastic (Polyethylene terephthalate)",
        "Status": "Recyclable - If empty and cleaned. Additionally, put the pump back on the bottle before recycling it.",
        "Why":"The pump is also recyclable, but is too small to be recycled on its own"
    },
    "Single-use Cups": {
        "Category": "#6 Plastic - PS plastic (Polystyrene)",
        "Status": "Not Recyclable",
        "Why": "Consists mostly of air, and is hard to clean"
    },
    "Takeout Container": {
        "Category": "#6 Plastic - PS plastic (Polystyrene)",
        "Status": "Not Recyclable",
        "Why": "Consists mostly of air, and is hard to clean food residue"
    },
    "Milk Jug": {
        "Category": "#2 Plastic - HDPE/PE-HD plastic (High density polyethylene)",
        "Status": "Recyclable - If empty",
        "Why": "Leftover liquid may make the item to heavy to move during sorting"
    },
    "Water Jug": {
        "Category": "#2 Plastic - HDPE/PE-HD plastic (High density polyethylene) <br>    -Sometimes #1 or #5",
        "Status": "Recyclable - If empty",
        "Why": "Leftover liquid may make the item to heavy to move during sorting"
    },
    "Bottle Cap": {
        "Category": "#1 Plastic - PETE/PET plastic (Polyethylene terephthalate)",
        "Status": "Recyclable - If attached to bottle",
        "Why": "Caps are often too small to be recycled on their own, attach it to a bottle to ensure it get recycled!"
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
        article= "Looks like this is an: "
    else:
        article= "Looks like this is a: "
    return ("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <title>RecycLabel Plastics</title>
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
                <strong>RecycLabel Plastics</strong>
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
                <p>""" + data[Item]["Category"] + """</p>
            </div>
        </li>
        <li class="listitem">
            <input type="radio" name="accordion" id="second">
            <label for="second">Is it Recyclable?</label>
            <div class="content">
                <p>"""+ data[Item]["Status"] +"""</p>
            </div>
        </li>
        <li class="listitem">
            <input type="radio" name="accordion" id="third">
            <label for="third">Why?</label>
            <div class="content">
                <p>"""+ data[Item]["Why"] +"""</p>
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
    <title>RecycLabel Plastics</title>
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
                <strong>RecycLabel Plastics</strong>
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
    </ul>
</body>
""")

