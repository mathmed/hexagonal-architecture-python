FROM python:3.9

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 755 /usr/local/bin/entrypoint.sh \
    && ln -s /usr/local/bin/entrypoint.sh /

EXPOSE 80

ENTRYPOINT [ "entrypoint.sh" ]