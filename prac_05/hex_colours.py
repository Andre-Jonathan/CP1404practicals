COLOURS = {
    "Absolute Zero": "#0048ba",
    "Amethyst": "#9966cc",
    "Bone": "#e3dac9",
    "Burnt Sienna": "#e97451",
    "Camouflage Green": "#78866b",
    "Celeste": "#b2ffff",
    "Deep Chestnut": "#b94e48",
    "Denim": "#1560bd",
    "Ebony": "#555d50",
    "Emerald": "#50c878"}

colour = input("Name a colour: ").title()
while colour != "":
    try:
        print(COLOURS[colour])
        colour = input("Name a colour: ").title()
    except:
        print("Invalid colour")
        colour = input("Name a colour: ").title()
