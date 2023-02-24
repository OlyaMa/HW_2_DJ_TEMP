from django.shortcuts import render
from django.http import HttpResponseNotFound

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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def ingredients(request, dish):
    if dish not in DATA:
        return HttpResponseNotFound(f'Блюдо "{dish}" в списке рецептов не найдено')
    servings = request.GET.get('servings')
    voc = {}
    if servings:
        for key, value in DATA[dish].items():
            voc[key] = value * int(servings)
        context = {
            'recipe': voc
        }
    else:
        context = {
            'recipe': DATA[dish]
        }
    return render(request, 'calculator/index.html', context)
