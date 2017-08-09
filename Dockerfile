FROM python:3.5-alpine

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt


RUN apk add --no-cache --virtual .build-deps \
	gcc \
	make \
	libc-dev \
	musl-dev \
	linux-headers \
	pcre-dev \
	postgresql-dev \
	python3-dev \
	&& pip install -r requirements.txt \
    	&& find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    	&& runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    	)" \
    	&& apk add --virtual .rundeps $runDeps \
    	&& apk del .build-deps	 

RUN apk add --no-cache bash        

COPY manage.py /manage.py

RUN mkdir /config
RUN mkdir /src
COPY config/ /config/
COPY .coveragerc /.coveragerc

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
