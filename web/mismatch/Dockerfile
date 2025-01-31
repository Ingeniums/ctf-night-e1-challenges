FROM php:8-fpm-alpine3.20 AS base

WORKDIR /app
COPY src/* .

RUN addgroup player
RUN adduser -G player -S player
RUN chown -R player:player /app
USER player
EXPOSE 8080

CMD [ "php", "-S", "0.0.0.0:8080" ]

