"""Вам предоставлен список словарей, в котором перечислены товары.
Напишите функцию find_product_by_name(), которая принимает список продуктов и имя для поиска и возвращает информацию о продукте по его имени.
Если продукт не найден в списке, функция возвращает строку «Продукт с таким именем не найден в списке».
Если у продукта отсутствует имя, это не должно привести к ошибке."""

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

def find_product_by_name(products, name = None):
    found_product = ""
    for elem in products:
        if elem.get("name") == name:
            found_product = elem
            break
        elif name == None:
            break
    else:
        print("Продукт с таким именем не найден в списке")
    return found_product

name = "Appleszxczxv"
print(find_product_by_name(products, name))