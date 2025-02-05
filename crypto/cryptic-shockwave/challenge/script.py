from hashlib import md5,sha256
import json
'''
Data format:
{

    username: {"usr_hash":md5(user.encode()).hexdigest(),"password_hash": custom_hash(password),"pwd":password},
    .
    .
    .
}
'''

users=dict()
def get_option():
    return input('''
    Welcome to my login application scaredy cat ! I am using MD5 and my custom hashing to save the passwords in the database.
                          I am more than certain that this is secure.                       
                                   You can't prove me wrong!          
    
    [1] Login
    [2] Register
    [3] Exit

    Option (json format) :: ''')


def main():
    def custom_hash(pwd:str)->str:
                    pwd=sha256(pwd.encode()).digest();
                    pwd= int.from_bytes(pwd);
                    pwd=pwd >> (212);
                    return hex(pwd);
    while True:
        option = json.loads(get_option())

        if 'option' not in option:
            print('[-] please, enter a valid option!')
            continue

        option = option['option']
        if option == 'login':
            creds = json.loads(input('enter credentials (json format) :: '))
            usr, pwd = creds['username'], creds['password']
            usr_hash = md5(usr.encode()).hexdigest()
            pwd_hash= custom_hash(pwd);
            authenticated=False;
            for db_user  in users:
                
                if (usr_hash == users[db_user]["usr_hash"] ) and ( pwd_hash ==users[db_user]["pwd_hash"]):
                    if usr == db_user :
                        print(f'[+] welcome user, {usr} 🤖!')
                        authenticated=True;
                    if   pwd == users[db_user]["pwd"]:
                        print(f'[+] welcome admin user, {usr} 🤖!');
                        authenticated=True;
                    if    (usr != db_user) and (pwd != users[db_user]["pwd"]) :
                            flag = open("flag.txt").read();
                            print(f"[+] what?! this was unexpected. shutting down the system :: {flag} 👽")
                            exit()
                            break
            if not authenticated:
                print('[-] invalid username and/or password!')
        
        elif option == 'register':
            creds = json.loads(input('enter credentials (json format) :: '))

            usr, pwd = creds['username'], creds['password']
            if usr.isalnum() and pwd.isalnum():
                usr_hash = md5(usr.encode()).hexdigest()
                passwords=[users[db_usr]["pwd"] for db_usr in users ]
                if (usr not in users.keys()) and (pwd not in passwords):
                    users[usr] = {"usr_hash":md5(usr.encode()).hexdigest(),"pwd_hash": custom_hash(pwd),"pwd":pwd}
                else:
                    if usr  in users.keys():
                        print('[-] this user  already exists!');
                    if  (pwd not in passwords):
                        print('[-] this password  already exists!');
                        
            else:
                print('[-] your credentials must contain only ascii letters and digits.')

        elif option == 'exit':
            print('byeee.')
            break


if __name__ == '__main__':
    main()
