FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ 'Europe/Moscow'


RUN apt-get update && apt-get install -y supervisor
COPY ./nginx.conf /etc/nginx/conf.d/weather_entrypoint.conf

#RUN sudo apt-get -y update
#RUN sudo apt-get -y install netcat-openbsd
#RUN sudo apt-get -y install vim
#RUN sudo apt-get -y install nginx
#RUN sudo apt-get -y install supervisor

#RUN apt-get update && apt-get install -y vim mosh tmux htop git curl wget unzip zip gcc build-essential make
COPY ./supervisor/conf.d /etc/supervisor/conf.d
COPY ./docker_start.sh /usr/local/weather_entrypoint/docker_start.sh

#RUN apt-get install -y vim

COPY ./requirements.txt /usr/local/weather_entrypoint/requirements.txt
RUN pip install --upgrade pip && pip install -r /usr/local/weather_entrypoint/requirements.txt

EXPOSE 82
ADD . /usr/local/weather_entrypoint/
WORKDIR /usr/local/weather_entrypoint/
RUN chmod 700 main.py
RUN chmod 700 docker_start.sh
#CMD ["bash", "-n", "-c", "-l", "/etc/supervisor/supervisord.conf"]
#CMD ["bash -n -c -l", "/etc/supervisor/supervisord.conf"]

#CMD["chmod 700","./docker_start.sh"]
#EXPOSE 82
#VOLUME /usr/local/weather_entrypoint/static/

ENTRYPOINT ["/bin/sh", "-c", "bash", "supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
#ENTRYPOINT ["/bin/sh", "-c", "bash", "./docker_start.sh"]