#!/usr/bin/env bash
echo -e "\x1b[34;1;4mOfficer:\x1b[0m You've proven to be quite a nuisance, hacker. We now realize keeping you jailed is not an option, so we'll opt for trial by combat."
echo -e "\x1b[34;1;4mOfficer:\x1b[0m Prove your skill by battling increasingly strict restrictions while reading a part of the flag on /flag.txt each time."


flag_1='ingeniums{M1gh7_'
flag_2='M4k3s_'
flag_3='R1Ght}'

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

    if [[ "$output" == "$flag_1" || "$(echo $output | base64 -d 2>/dev/null)" == "$flag_1" ]]; then
        echo -e "\x1b[32;1;4;3mYou Passed Level 3!\x1b[0m"
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
        echo "\x1b[41mBANNED\x1b[0m"
    else
        output=$(sudo -u ctf /bin/bash -c "$command")

        echo -e "\x1b[42;1;4;3m$output\x1b[0m"

        if [[ "$output" == "$flag_2" || "$(echo $output | base64 -d 2>/dev/null)" == "$flag_2" ]]; then
            echo -e "\x1b[32;1;4;3mYou Passed Level 2!\x1b[0m"
            continue=false
        fi
    fi
done


echo ===========================
echo -e "\x1b[46;1;4mLevel 3 (Final Level)\x1b[0m"
echo ===========================

echo $flag_3 > /flag.txt

echo -e "\x1b[37;1mFinally, I've disabled cat, head, tail, tac, strings, more, and less. Let's see how you'll do this.\x1b[0m"

continue=true
while $continue
do
    read -p "$ " command

    if [[ "$command" == *cat* || "$command" == *head* || "$command" == *tail* || "$command" == *tac* || "$command" == *strings* || "$command" == *more* || "$command" == *less* ]]; then
        echo "\x1b[41mBANNED\x1b[0m"
    else
        output=$(sudo -u ctf /bin/bash -c "$command")

        echo -e "\x1b[42;1;4;3m$output\x1b[0m"

        if [[ "$output" == "$flag_3" || "$(echo $output | base64 -d 2>/dev/null)" == "$flag_3" ]]; then
            echo -e "\x1b[32;1;4;3mYou Passed Level 3!\x1b[0m"
            continue=false
        fi
    fi
done
