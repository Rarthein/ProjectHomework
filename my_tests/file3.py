# def strip_string(strip_chars=" "):
#     def do_strip(string):
#         return string.strip(strip_chars)
#
#     return do_strip
#
# strip1 = strip_string()
# strip2 = strip_string(" !?,.;")
#
# print(strip1(" hello python!.. "))
# print(strip2(" hello python!.. "))

# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("----- 1 -----")
#         func(*args, **kwargs)
#         print("----- 2 -----")
#
#     return wrapper
#
# def some_func(title):
#     print(f"title = {title}")
#
#
# some_func = func_decorator(some_func)
# some_func("Python forever!")

# def retry_decorator(max_retries):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(max_retries):
#                 try:
#                     result = func(*args, **kwargs)
#                     return result
#                 except Exception as e:
#                     print(f"Retrying... ({e})")
#             raise Exception(f"Max retries exceeded")
#         return wrapper
#     return decorator
#
# @retry_decorator(max_retries=3)
# def example_function():
#     # some potentially failing operation
#     raise ValueError("Something went wrong!")
