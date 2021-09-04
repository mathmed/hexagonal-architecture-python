FROM python:3.9

COPY . /src

WORKDIR /src

RUN pip install -r src/requirements.txt

EXPOSE 80

CMD ["flask" "run" "--host=0.0.0.0"]
