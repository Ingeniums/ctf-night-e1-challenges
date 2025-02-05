grep -o 'q=[^ ]*' files/chall | cut -d= -f2 | tr -d "\n" | xxd -r -p
