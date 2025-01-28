#!/bin/sh

# Script execution variables
EXEC="python3 script.py"
PORT=1337

# Start socat to serve the script
exec socat -dd -T300 tcp-listen:"$PORT",reuseaddr,fork,keepalive,su=nobody exec:"$EXEC",stderr
