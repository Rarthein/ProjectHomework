import pytest

from src.decorators import log


def test_my_function_success_console(capsys):
    """Функция успешного выполнения my_function с логированием в консоль"""

    @log()
    def test_func(x, y):
        return x + y

    result = test_func(1, 2)

    captured = capsys.readouterr()

    assert result == 3
    assert "test_func ok" in captured.out


def test_my_function_success_file(tmp_path):
    """Функция успешного выполнения my_function с логированием в файл"""
    log_file = tmp_path / "my_log.txt"

    @log(filename=str(log_file))
    def test_func(x, y):
        return x + y

    result = test_func(1, 2)

    assert result == 3
    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
    assert "test_func ok" in log_content


def test_my_function_exception_console(capsys):
    """Функция обработки исключений в my_function с логированием в консоль"""

    @log()
    def test_func(x, y):
        return x + y

    with pytest.raises(TypeError):
        test_func(1, 'a')

    captured = capsys.readouterr()

    assert "test_func error: TypeError. Inputs: (1, 'a'), {}" in captured.out


def test_my_function_exception_file(tmp_path):
    """Функция обработки исключений в my_function с логированием в файл"""
    log_file = tmp_path / "my_log.txt"

    @log(filename=str(log_file))
    def test_func(x, y):
        return x + y

    with pytest.raises(TypeError):
        test_func(1, 'a')

    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
    assert "test_func error: TypeError. Inputs: (1, 'a'), {}" in log_content
