#!/usr/bin/env bash
echo -e "\x1b[34;1;4mOfficer:\x1b[0m You've proven to be quite a nuisance, hacker. We now realize keeping you jailed is not an option, so we'll opt for trial by combat."
echo -e "\x1b[34;1;4mOfficer:\x1b[0m Prove your skill by battling increasingly strict restrictions while reading a part of the flag on /flag.txt each time."


flag_1='ingeniums{Br3ak_'
flag_2='L0ck$_'
flag_3='N0t_'
flag_4='l4wS}'

echo ===========================
echo -e "\x1b[46;1;4mLevel 1\x1b[0m"
echo ===========================

echo $flag_1 > /flag.txt

echo -e "\x1b[37;1mThis is basic. You have a normal bash shell. Just read /flag.txt.\x1b[0m"

continue=true
while $continue
do
    read -p "$ " command
    output=$(sudo -u ctf /bin/bash -c "$command")

    echo -e "\x1b[42;1;4;3m$output\x1b[0m"

    if [[ "$output" == *"$flag_1"* ]]; then
        echo -e "\x1b[32;1;4;3mYou Passed Level 1!\x1b[0m"
        continue=false
    fi
done

echo ===========================
echo -e "\x1b[46;1;4mLevel 2\x1b[0m"
echo ===========================

echo $flag_2 > /flag.txt

echo -e "\x1b[37;1mNow I've disabled cat. Read /flag.txt.\x1b[0m"

continue=true
while $continue
do
    read -p "$ " command

    if [[ "$command" == *cat* ]]; then
        echo "BANNED"
    else
        output=$(sudo -u ctf /bin/bash -c "$command")

        echo -e "\x1b[42;1;4;3m$output\x1b[0m"

        if [[ "$output" == *"$flag_2"* ]]; then
            echo -e "\x1b[32;1;4;3mYou Passed Level 2!\x1b[0m"
            continue=false
        fi
    fi
done


echo ===========================
echo -e "\x1b[46;1;4mLevel 3\x1b[0m"
echo ===========================

echo $flag_3 > /flag.txt

echo -e "\x1b[37;1mI've disabled cat, head, tail, tac, strings, more, less, grep, tr, dd, sed, awk, xxd, base64 and base32. Let's see how you'll do this.\x1b[0m"

continue=true
while $continue
do
    read -p "$ " command

    if [[ "$command" == *cat* || "$command" == *head* || "$command" == *tail* || "$command" == *tac* || "$command" == *strings* || "$command" == *more* || "$command" == *less* || "$command" == *sed* || "$command" == *awk* || "$command" == *base64* || "$command" == *base32* || "$command" == *tr* || "$command" == *dd* || "$command" == *grep* || "$command" == *xxd* ]]; then
        echo "BANNED"
    else
        output=$(sudo -u ctf /bin/bash -c "$command")

        echo -e "\x1b[42;1;4;3m$output\x1b[0m"

        if [[ "$output" == *"$flag_3"* ]]; then
            echo -e "\x1b[32;1;4;3mYou Passed Level 3!\x1b[0m"
            continue=false
        fi
    fi
done

echo ===========================
echo -e "\x1b[46;1;4mFinal Level\x1b[0m"
echo ===========================

echo $flag_4 > /flag.txt

echo -e "\x1b[37;1mFor your final level, there is no flag. You are now stuck in this empty cave with only your \x1b[37;43;1mecho\x1b[0m\x1b[37;1m to keep you company\x1b[0m"

continue=true
while $continue
do
    read -p "$ " inp

    if [[ "$inp" == *\`* || "$inp" == *\$*  || "$inp" == *\<* ]]; then
        echo "BANNED"
    else
        output=$(sudo -u ctf /bin/bash -c "echo $inp")

        echo -e "\x1b[42;1;4;3m$output\x1b[0m"

        if [[ "$output" == *"$flag_4"* ]]; then
            echo -e "\x1b[32;1;4;3mYou Sure Are a nuisance. You're free again, hacker...!\x1b[0m"
            continue=false
        fi
    fi
done
