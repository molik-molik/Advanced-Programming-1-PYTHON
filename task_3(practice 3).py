import re
a=1
def check_pass(pswd):
    if (len(pswd) < 8): ##check for length
        print("The password is too short!")
        
    res = any(chr.isdigit() for chr in pswd)
    if res==False: ##check for numbers(digits)
        print("The password must have numbers in it!")
        
    lc = re.search('[a-z]', pswd)
    if(lc is None):##check for lowercase letters
        print("There must be at least one lowercase letter!")
    uc = re.search('[A-Z]', pswd)
    if(uc is None):##check for uppercase letters
        print("There must be at least one uppercase letter!")

    special_chr = "*-#"
    if any(chr in special_chr for chr in pswd) == False:
              print("There must be at least one special character(*-#)!")
              
    spec_chr = "!@$%^&()+?_=,<>/"
    if any(chr in spec_chr for chr in pswd):
        print("Use only allowed special characters! *, - or #")


    if (a==1):##check whether password is perfect or not
        if (len(pswd)>=8 and res==True
            and any(chr in special_chr for chr in pswd)
            and (uc is not None) and (lc is not None)):
            print("*saved*\nPassword is perfect!")

while(a==1):
    pswd = input("Enter your password: ")
    check_pass(pswd)


    
