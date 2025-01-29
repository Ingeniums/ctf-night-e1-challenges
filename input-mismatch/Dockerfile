FROM php:8-fpm-alpine3.20 AS base

WORKDIR /app
COPY src/* .

RUN addgroup player
RUN adduser -G player -S player
RUN chown -R player:player /app
USER player
EXPOSE 8081

CMD [ "php", "-Slocalhost:8081" ]

