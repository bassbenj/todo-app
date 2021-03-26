FROM python:3.9-slim-buster

EXPOSE 5000

WORKDIR /todoweb

COPY requirements.txt /todoweb
RUN pip install -r requirements.txt

COPY . /todoweb

CMD python app.py