FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV DEBUG False
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
