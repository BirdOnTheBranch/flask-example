FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1

# App setup
ADD . /hello
WORKDIR /hello

# Requirements installation
RUN pip install -r requirements.txt

#COPY ./entrypoint.sh /
#ENTRYPOINT ["entrypoint.sh"]
EXPOSE 5000
CMD python hello.py


