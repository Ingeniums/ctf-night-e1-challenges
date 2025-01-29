FROM python:3-alpine



RUN apk add --no-cache socat

RUN adduser -D -u 1000 challengeuser

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

WORKDIR /challenge/
COPY ./challenge/ .

RUN chmod 400 /challenge/flag.txt && \
    chmod 555 /challenge/script.py

RUN chown -R challengeuser:challengeuser /challenge/

USER challengeuser

EXPOSE 1337

ENTRYPOINT ["/entrypoint.sh"]
