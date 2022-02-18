FROM python:3.8-alpine

RUN pip install flask

WORKDIR /bob
COPY . /bob

ENTRYPOINT ["python"]
CMD ["app.py"]