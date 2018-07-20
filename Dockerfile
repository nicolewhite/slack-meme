FROM python:3

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system --deploy

CMD ["gunicorn", "-b 0.0.0.0:5000", "wsgi"]
