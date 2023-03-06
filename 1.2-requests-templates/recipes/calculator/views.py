from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_view(request, recipes_name):
    if recipes_name in DATA:
        data = DATA[recipes_name]
        servings = request.GET.get('servings', None)
        if servings:
            result = dict()
            for item, value in data.items():
                new_value = value * int(servings)
                result[item] = round(new_value, 2)
            context = {
                'dish_name': recipes_name,
                'recipe': result
            }
        else:
            context = {
                'dish_name': recipes_name,
                'recipe': data
            }
    else:
        context = None
    return render(request, template_name='calculator/index.html', context=context)
