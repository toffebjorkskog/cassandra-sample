FROM python

RUN apt-get update && apt-get install -y python3-dateutil
RUN pip install Twisted[tls]

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -e .
EXPOSE 8000
EXPOSE 8080

CMD python main.py
