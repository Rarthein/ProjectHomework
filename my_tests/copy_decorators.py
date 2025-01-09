import os
from functools import wraps
from typing import Any, Optional


def log(filename: Optional[str] = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_message: str = ''
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                raise
            finally:
                if filename:
                    os.makedirs(os.path.dirname(filename), exist_ok=True)
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{log_message}\n")
                else:
                    print(log_message)

        return wrapper

    return decorator


# Пример использования
@log(filename="logs/my_log.txt")
def my_function(x: int, y: int) -> int:
    return x + y


print(my_function(1, 2))
try:
    print(my_function(1, 'a'))
except TypeError:
    print("Ошибка типа!")
