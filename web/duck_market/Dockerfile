FROM python:3.13.1-alpine
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install flask
COPY ./app /app
COPY ./flag.txt /flag.txt
EXPOSE 1337
CMD ["flask","run"]
