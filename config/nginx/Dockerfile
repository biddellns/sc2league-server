FROM nginx:stable

RUN rm /etc/nginx/nginx.conf
RUN rm /etc/nginx/mime.types
COPY conf.d/nginx.conf /etc/nginx/nginx.conf
COPY conf.d/mime.types /etc/nginx/mime.types

RUN rm /etc/nginx/conf.d/default.conf
COPY sites-available/default.conf /etc/nginx/sites-available/
COPY sites-available/default.conf /etc/nginx/conf.d/

CMD ["nginx", "-g", "daemon off;"]
