FROM charact3/python-cassandra-driver

RUN apt-get update
RUN pip install Twisted[tls]

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -e .
EXPOSE 8000
EXPOSE 8080

CMD python app
