[tool.poetry]
name = "projecthomework"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.13"
requests = "^2.32.3"

[tool.poetry.group.lint.dependencies]
flake8 = "^7.1.1"
mypy = "^1.13.0"
black = "^24.10.0"
isort = "^5.13.2"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true
no_implicit_optional = true
warn_return_any = true
warn_unreachable = true
exclude = 'venv'

[tool.isort]
line_length = 119

[tool.black]
line-length = 119
exclude = """(/(\.git|\.venv))"""
exclude = '''
(
  /(
      \.eggs         # Исключить несколько общих каталогов
    | \.git          # в корне проекта
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | dist
  )/
  | foo.py           # Также отдельно исключить файл с именем foo.py
                     # в корне проекта
)
'''
