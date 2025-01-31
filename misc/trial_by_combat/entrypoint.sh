#!/bin/sh

EXEC="./script.sh"
PORT=1337

socat -dd -T300 tcp-listen:"$PORT",reuseaddr,fork,keepalive exec:"$EXEC",stderr
