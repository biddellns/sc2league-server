FROM python:3.5-alpine

RUN apk add --no-cache postgresql-dev gcc python3-dev

RUN mkdir /config
RUN mkdir /src
COPY requirements.txt /config/
RUN pip install --upgrade pip
RUN pip install -r /config/requirements.txt

#ENV PYTHONUNBUFFERED 1
#RUN mkdir /config
#ADD /config/requirements.pip /config/
#RUN pip install -r /config/requirements.pip
#RUN mkdir /src;
#WORKDIR /src
