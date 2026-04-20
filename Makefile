# Переменные
PYTHON = venv/bin/python
PIP = venv/bin/pip
UVICORN = venv/bin/uvicorn

# Установка зависимостей
install:
	$(PIP) install --upgrade pip
	$(PIP) install "fastapi[all]" sqlalchemy alembic

# Запуск сервера разработки
run:
	$(UVICORN) app.main:app --reload

# Очистка временных файлов
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf venv

# Создание виртуального окружения "с нуля"
setup:
	python3 -m venv venv
	$(MAKE) install