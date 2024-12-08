"""Вам предоставлен список словарей, в котором перечислены товары.

Напишите функцию update_product_info(), которая обновляет информацию о продукте по его имени и возвращает обновленный список продуктов.

Функция принимает следующие аргументы: список продуктов, имя продукта, информацию, по которому нужно обновить, и словарь с данными, которые требуется обновить.
За один вызов функция может обновить только один продукт. Если продукт не найден в списке, функция возвращает строку «Продукт с таким именем не найден в списке».
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

def update_product_info(products, name = None, product_info = None):
    for elem in products:
        if elem.get("name", "n/a") == name:
            elem.update(product_info)
            return products
    else:
        print("Продукт с таким именем не найден в списке")
        return ""

product_to_update = "Broccoli"
new_info = {"quantity": 10, "organic": False}
update_result = update_product_info(products, product_to_update, new_info)
print(update_result)