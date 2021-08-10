FROM python:3.8
COPY . /scrapy
WORKDIR /scrapy

RUN pip install beautifulsoup4
RUN pip install requests
RUN pip install selenium


CMD python ./scrapy.py