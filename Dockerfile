# Используем официальный образ Python 3.12
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости для сборки расширений Python (например, psycopg2)
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей в контейнер
COPY requirements.txt ./

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код проекта в контейнер
COPY . .

# Команда по умолчанию для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
