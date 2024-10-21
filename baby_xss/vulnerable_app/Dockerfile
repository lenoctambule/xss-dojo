FROM alpine:3.20

RUN apk update
RUN apk add python
RUN pip install --no-cache-dir -r ./src/requirements.txt

COPY ./src /

ENTRYPOINT ["python", "./src/app.py"]