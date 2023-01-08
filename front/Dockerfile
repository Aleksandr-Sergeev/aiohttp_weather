FROM nginx
ENV TZ 'Europe/Moscow'


#RUN apt-get update && apt-get install -y vim mosh tmux htop git curl wget unzip zip gcc build-essential make
#RUN apt-get update && apt-get install -y supervisor netcat-openbsd vim
#RUN rm /etc/nginx/sites-available/default.conf

COPY ./nginx.conf /etc/nginx/conf.d/front.conf
COPY ./front.access.log /var/log/nginx/front.access.log

#CMD ["cat", ">", "/var/log/nginx/front.access.log"]
VOLUME /var/log/nginx
#CMD ["nginx","-t",  "-c", "/data/conf/nginx.conf"]

