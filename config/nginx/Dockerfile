FROM nginx:stable

RUN apk update && apk add \
    python3 \
    openssl \
    && python3 -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --upgrade pip setuptools \
    && rm -rf /var/cache/apk/*

RUN pip3 install Jinja2==2.8

RUN rm /etc/nginx/nginx.conf
RUN rm /etc/nginx/mime.types
COPY conf.d/nginx.conf /etc/nginx/nginx.conf
COPY conf.d/mime.types /etc/nginx/mime.types

RUN rm /etc/nginx/conf.d/default.conf
COPY api.conf /etc/nginx/conf.d/

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
