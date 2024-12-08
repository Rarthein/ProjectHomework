"""Вам предоставлен список словарей, в котором перечислены товары.
Напишите функцию filter_products_by_price(), которая принимает на вход список продуктов и верхний порог цены и
возвращает список продуктов, цена которых не превышает заданную максимальную цену. Если у продукта не указана цена,
это не должно приводить к ошибке, при получении значения по ключу,
если ключа в словаре нет - цена должна равняться 0 (используйте метод get())."""

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


def filter_products_by_price(products, max_price=0):
    list_products = []
    for elem in products:
        if elem.get("price", 0) <= max_price:
            list_products.append(elem)
    return list_products


max_price = 200
print(filter_products_by_price([{"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
                                {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
                                {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
                                {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
                                {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
                                {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25}, ], max_price))
