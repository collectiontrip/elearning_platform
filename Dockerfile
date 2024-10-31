FROM python:3.12-slim

WORKDIR /APP

COPY  Pipfile Pipfile.lock /APP/

RUN pip install pipenv && pipenv install --deploy --ignore-Pipfile

COPY . .

EXPOSE 8000

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]