from django.urls import reverse
data= {
    "Aluminum Can": {
        "Category":"Aluminum",
        "Status":"Recyclable - If empty  *note: don't crush it!",
        "Why":"Liquid may make the item too heavy to be moved by airflow during sorting, and crushing makes the can too small to be processed"
    },
    "Bottle Cap": {
        "Category": "#1 Plastic - PETE/PET plastic (Polyethylene terephthalate)",
        "Status": "Recyclable - If attached to bottle",
        "Why": "Caps are often too small to be recycled on their own, attach it to a bottle to ensure it get recycled!"
    },
    "Cardboard Tube": {
        "Category": "Paper/Cardboard",
        "Status": "Recyclable - If clean, and not too stiff(easily flattened)",
        "Why": "Grease contaminates the cardboard, and stiff tubes cannot be flattened for recycling"
    },
    "Cereal Bag": {
        "Category": "#2 Plastic - HDPE/PE-HD (High density polyethylene)",
        "Status": "Not Recyclable",
        "Why": "Soft plastics such as bags jam machinery, and can mess up the sorting process"
    },
    "Spray Bottle": {
        "Category":"#1 Plastic - PETE/PET (Polyethylene terephthalate)",
        "Status": "Recyclable - If empty and cleaned. Additionally, some types allow you to keep the spray trigger on the bottle before recycling it.",
        "Why":"The spray trigger is also recyclable, but is too small to be recycled on its own"
    },
    "Milk Jug": {
        "Category": "#2 Plastic - HDPE/PE-HD (High density polyethylene)",
        "Status": "Recyclable - If empty",
        "Why": "Leftover liquid may make the item to heavy to move during sorting"
    },
    "PET Bottle": {
        "Category":"#1 Plastic - PETE/PET (Polyethylene terephthalate)",
        "Status":"Recyclable - If empty",
        "Why":"Liquid may make the item too heavy to be moved by airflow during sorting"
    },
    "Plastic Bag": {
        "Category": "#4 Plastic - LDPE/LD-PE plastic (Low density Polyethylene)",
        "Status": "Not Recyclable",
        "Why": "Soft plastics such as bags jam machinery, and can mess up the sorting process"
    },
    "Plastic Utensil": {
        "Category": "#6 Plastic - PS (Polystyrene)",
        "Status": "Not Recyclable",
        "Why": "Too small to be properly sorted, sometimes made of different plastic types that are hard to distinguish"
    },
    "Plastic Wrapper": {
        "Category": "Various Plastics",
        "Status": "Not Recyclable",
        "Why": "Small, soft plastics don't recycle well; Wrappers rarely have identification on them"
    },
    "Single-use Cup": {
        "Category": "#6 Plastic - PS (Polystyrene)",
        "Status": "Not Recyclable",
        "Why": "Consists mostly of air, and is hard to clean; low value and hard to process"
    },
    "Soap Bottle": {
        "Category":"#1 Plastic - PETE/PET (Polyethylene terephthalate)",
        "Status": "Recyclable - If empty and cleaned. Additionally, put the pump back on the bottle before recycling it.",
        "Why":"The pump is also recyclable, but is too small to be recycled on its own"
    },
    "Takeout Container": {
        "Category": "#6 Plastic - PS (Polystyrene) or #1 Plastic - PP (Polypropylene)",
        "Status": "Not Recyclable",
        "Why": "<p>#6: Consists mostly of air, and is hard to clean food residue<br>#1: Often made of black colored plastic, which is nearly impossible to sort. If not black, it can be cleaned and recycled<p>"
    },
    "Water Jug": {
        "Category": "#2 Plastic - HDPE/PE-HD (High density polyethylene) or sometimes #1 or #5",
        "Status": "Recyclable - If empty",
        "Why": "Leftover liquid may make the item to heavy to move during sorting"
    },
    "Yogurt Container": {
        "Category": "#5 Plastic - PP (Polypropylene)",
        "Status": "Recyclable - Clean and dry the container. If its cap is plastic, you can recycle that too, but if it's foil, it's not recyclable",
        "Why":"The foil used on yogurt containers often contains a plastic film which makes it difficult to recycle"
    },
    "#1 Plastic": {
        "Category":"PETE/PET plastic (Polyethylene terephthalate)",
        "Status":"Recyclable",
        "Examples":"<ul><li>Single-use drink bottles</li><li>Condiment containers</li><li>Produce containers</li></ul>"
    },
    "#2 Plastic": {
        "Category":"HDPE/PE-HD plastic (High density polyethylene)",
        "Status":"Recyclable - excluding soft plastics such as bags",
        "Examples":"<ul><li>Milk jugs</li><li>Shampoo/conditioner bottles</li><li>Some cereal/grocery bags <ul><li>Note: no plastic bags are accepted for municipal recycling</li></ul></li></ul>"
    },
    "#3 Plastic": {
        "Category":"PVC/V plastic (Polyvinyl chloride)",
        "Status":"Not Recyclable - excluding pure PVC containers",
        "Examples":"<ul><li>Piping</li><li>Children's/pet's toys</li><li>Medical Equipment</li></ul>"
    },
    "#4 Plastic": {
        "Category": "LDPE/LD-PE plastic (Low density Polyethylene)",
        "Status": "Recyclable - excluding soft plastics or films",
        "Examples":"<ul><li>Shrink/Bubble wrap  <ul><li>Note: no plastic films are accepted for municipal recycling</li></ul></li><li>Grocery containers</li><li>Bread bags  <ul><li>Note: no plastic bags are accepted for municipal recycling</li></ul></li></ul>"
    },
    "#5 Plastic": {
        "Category": "PP plastic (Polypropylene)",
        "Status": "Recyclable",
        "Examples":"<ul><li>Yogurt containers</li><li>Medicine/syrup bottles</li><li>Straws  <ul><li>Note: small plastic straws/utensils are not accepted for municipal recycling</li></ul></li></ul>"
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
