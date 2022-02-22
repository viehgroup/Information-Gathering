def email():
    import re
    def matchre(data,*args):
        for regstr in args:
            matchObj = re.search( regstr+'.*', data, re.M|re.I)
            if matchObj:
                print(matchObj.group(0).lstrip().rstrip())
            else:
                print("No" ,regstr,"found")
    print("\n Email Header Program by Chetan")
    filename= input("Enter path for email header file: ")
    fo = open(filename, "r") 
    data=fo.read()
    matchre(data,"MIME-version","Date:","Subject:","delivered-to:","From:","^to:")
    fo.close()
    print("\n")