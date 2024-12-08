"""Вам предоставлен список словарей в котором перечислены товары.

Напишите функцию group_products_by_category(products), которая принимает на вход список продуктов и возвращает словарь,
где ключи — категории, а значения — списки продуктов в каждой категории. Если у продукта отсутствует категория, это не должно привести к ошибке.
Такой продукт игнорируется программой."""

products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]

def group_products_by_category(products):

    dict_products = {}

    for elem in products:
        if "category" in elem:
            categoty = elem["category"]
        else:
            continue

        if categoty in dict_products:
            dict_products[categoty].append(elem)

        else:
            dict_products[categoty] = [elem]


    return dict_products

grouped_by_category = group_products_by_category(products)
print(grouped_by_category)