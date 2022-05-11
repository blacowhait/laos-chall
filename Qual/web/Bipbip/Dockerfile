FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3

RUN python3 -m pip install flask

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
