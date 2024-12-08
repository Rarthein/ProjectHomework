"""Вам предоставлен список словарей, в котором перечислены товары.

Напишите функцию sort_products_by_quantity(). Функция должна принимать на вход список продуктов и направление сортировки (атрибут должен иметь имя ascending)
со значением по умолчанию False (булевое значение) и сортировать продукты по количеству в порядке возрастания или убывания.
Если в функцию не передан аргумент направления сортировки, сортировка должна проходить в порядке возрастания количества товаров (от меньшего к большему).
Если у продукта не указано количество, это не должно привести к ошибке, при получении значения по ключу, если ключа в словаре нет - количество должно равняться 0 (используйте метод get())."""

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

"""def sort_products_by_quantity(products):
        sorted_products = sorted(products, key=lambda product: product.get("quantity"))
        return sorted_products"""


def sort_products_by_quantity(products, ascending = False):
    if ascending == False:
        sorted_products = sorted(products, key=lambda product: product.get("quantity", 0))
        return sorted_products
    elif ascending is not False:
        sorted_products = sorted(products, key=lambda product: product.get("quantity", 0), reverse=True)
        return sorted_products


sorted_by_quantity = sort_products_by_quantity(products, ascending=True)
print(sorted_by_quantity)