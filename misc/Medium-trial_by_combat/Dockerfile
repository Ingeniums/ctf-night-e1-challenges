FROM alpine

RUN apk update && \
	apk add socat bash sudo
RUN adduser --disabled-password -s /bin/bash ctf

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./challenge/flag.txt /flag.txt
RUN chmod 666 /flag.txt

RUN mkdir /challenge/

WORKDIR /challenge/

COPY ./challenge/script.sh ./

RUN chmod -R 500 .

EXPOSE 1337

ENTRYPOINT ["/entrypoint.sh"]
