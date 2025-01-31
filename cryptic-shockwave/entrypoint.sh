#!/bin/sh

EXEC="python3 /challenge/script.py"
PORT=1337

exec socat -dd -T300 tcp-listen:"$PORT",reuseaddr,fork,keepalive exec:"$EXEC",stderr
