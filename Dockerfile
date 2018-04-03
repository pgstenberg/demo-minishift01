FROM python:2

EXPOSE 8080

COPY server.py .
CMD python server.py
