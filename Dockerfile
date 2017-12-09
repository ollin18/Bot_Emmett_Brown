from gw000/keras:2.1.1-py3-tf-cpu

MAINTAINER Ollin Demian Langle Chimal <ollin.langle@ciencias.unam.mx>

ENV REFRESHED_AT 2017-12-03

RUN apt update && pip3 install tweepy

COPY src/ src/
COPY data/ data/

WORKDIR src

CMD ["./the_bot.py"]
