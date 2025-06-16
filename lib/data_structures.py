spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [spicy['heat_level'] for spicy in spicy_foods if spicy == 6 and spicy == 9]
    pass

def print_spicy_foods(spicy_foods):
    for spice in spicy_foods:
        heat_emojis = "🌶" * spice["heat_level"]
        print(f"{spice['name']} ({spice['cuisine']}) | Heat Level: {heat_emojis}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food_dict in spicy_foods:
        if food_dict["cuisine"].lower() == cuisine.lower():
            return food_dict
    pass

def print_spiciest_foods(spicy_foods):
    for spice_food in spicy_foods:
        if spice_food["heat_level"] > 5:
            heat_meter = "🌶" * spice_food["heat_level"]
            print(f"{spice_food["name"]} ({spice_food["cuisine"]}) | Heat Level: {heat_meter}")
    pass

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    number_of_foods = len(spicy_foods)
    return total_heat // number_of_foods
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
