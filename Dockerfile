FROM python:3.9-slim

WORKDIR /app

# Копіюємо Pipfile та Pipfile.lock в контейнер
COPY Pipfile Pipfile.lock /app/

# Встановлюємо залежності через pipenv
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# Копіюємо весь код у контейнер
COPY . /app/

# Виконання команд
CMD ["make", "train"]
