FROM python:2

MAINTAINER Matheus Moreti
MAINTAINER Kim Kawasaki
MAINTAINER Ligia Araujo
MAINTAINER Rodrigo Rossi

ADD api.py requirements.txt /
RUN pip install -r ./requirements.txt

ENV PORT=5000

EXPOSE $PORT
HEALTHCHECK CMD curl --fail http://localhost:$PORT || exit 1

CMD [ "./api.py" ]
