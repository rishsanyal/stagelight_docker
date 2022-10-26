FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN python3 -m pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /stagelite
RUN ls
ADD ./stagelite/stage /stagelite/stage
ADD ./stagelite/stagelite /stagelite/stagelite
ADD ./stagelite/topics /stagelite/topics
ADD ./stagelite/__init__.py /stagelite/__init__.py
ADD ./stagelite/manage.py /stagelite/manage.py
ADD ./stagelite/requirements.txt /stagelite/requirements.txt

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r /stagelite/requirements.txt
WORKDIR /stagelite
