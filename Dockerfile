FROM python:3.8
MAINTAINER moon.wu
WORKDIR /project
COPY ./requirements.txt /project/requirements.txt
RUN pip install -r requirements.txt
CMD ['python','manage.py','runserver','0.0.0.0:8080']