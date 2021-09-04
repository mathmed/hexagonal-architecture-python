FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install -r app/requirements.txt

EXPOSE 80

CMD ["flask" "run" "--host=0.0.0.0"]
