unames=['a','b','c','d']
paaswords=['abc','xyz','pqr','lmno']
ind=-1
uname=input('Enter your username: ')
if uname in unames:
    password=input('Enter your password: ')
    ind=unames.index(uname)
    if password==paaswords[ind]:
        print('You are logged in')
    else:
        print('Wrong password')
else:
    print('Wrong username')
