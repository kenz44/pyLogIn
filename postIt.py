
# post it log in info

def account():
    accountState = input("Log in or sign up? l = log in, s = sign up: ")
    
    if (accountState in ["l", "L"]):
        logIn()
    elif (accountState in ["s", "S"]):
        signUp()

def signUp():
    global usernames
    global passwords
    usernames = []
    passwords = []
    
    print("Sign Up:\n")
    createName = input("Enter a username: ")
    usernames.append(createName)
    
    createPass = input("Enter a password: ")
    passwords.append(createPass)
    logIn()
    
    
def logIn():
    global passwords
    global usernames
    print("Log In:\n")
    
    userName = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if (userName in usernames and password in passwords):
        print("Log in successful.")
    else:
        print("Incorrect username or password. Please try again.")
        logIn()
    

    
account()
