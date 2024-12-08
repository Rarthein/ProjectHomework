"""Вам предоставлен список словарей, в котором перечислены товары.

Напишите функцию average_price_per_category(), которая принимает на вход список продуктов и возвращает новый словарь, где ключи — категории, а значения — средняя цена продуктов в каждой категории.
Округлите результат вычисления до 1 знака после запятой. Если у продукта отсутствует категория, это не должно привести к ошибке."""

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

def average_price_per_category(products):

    categores_total_price = {}
    categores_count = {}
    categoty_avarages = {}

    for elem in products:
        if "category" in elem and "price" in elem:
            categoty = elem["category"]
            price = elem["price"]
        else:
            return {}

        if categoty in categores_total_price:
            categores_total_price[categoty] += price
            categores_count[categoty] += 1
        else:
            categores_total_price[categoty] = price
            categores_count[categoty] = 1
    #return print(categores_total_price), print(categores_count)

    for elem in categores_total_price:
        categoty_avarages[elem] = round(categores_total_price[elem] / categores_count[elem], 1)

    return categoty_avarages

print(average_price_per_category([{}]))
