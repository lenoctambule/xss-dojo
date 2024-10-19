FROM alpine:3.12

RUN apt update -y && apt install -y python3

COPY src ./src
COPY ./src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["flask", "run"]