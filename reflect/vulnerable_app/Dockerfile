FROM alpine:3.20

RUN apk update
RUN apk add python3 py-pip
COPY ./src /src
RUN pip install --no-cache-dir -r ./src/requirements.txt --break-system-packages

ENTRYPOINT ["python", "/src/app.py"]