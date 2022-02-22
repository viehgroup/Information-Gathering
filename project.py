import internet_speed
import email_header 
import insta_info
import socail
import ip
import ip_info
import phone_info
import os
import fake

os.system("cls || clear")

print("""

██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║
██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

░██████╗░░█████╗░████████╗██╗░░██╗███████╗██████╗░██╗███╗░░██╗░██████╗░
██╔════╝░██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗██║████╗░██║██╔════╝░
██║░░██╗░███████║░░░██║░░░███████║█████╗░░██████╔╝██║██╔██╗██║██║░░██╗░
██║░░╚██╗██╔══██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗██║██║╚████║██║░░╚██╗
╚██████╔╝██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║██║██║░╚███║╚██████╔╝
░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░


Organization: VIEH Group, @viehgroup
Creator: Chetan Bansal, @Cb-Kali (Github)
""")

ip.public_ip()
internet_speed.speed()

print("""
\t 1. Email Header Analysis
\t 2. Instagram Information
\t 3. Socail Username Check
\t 4. IP Information
\t 5. Phone Number Information
\t 6. Port Scan
\t 7. Web Scraping
\t 8. Fake Information
\t 9. Exit
""")
option = int(input("Enter What You Want: "))
print("\n")
if option == 1:
    email_header.email()
    print("\n You want exit or use another options(yes/no)")
    choose = input("yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 2:
    insta_info.info()
    print("\n You want exit or use another options(yes/no)")
    choose = input("yes Or no: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose ==  "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 3:
    print("""
    \t 1. Instagram
    \t 2. Twitte
    """)
    choose = int(input("Enter What you want: "))
    if choose == 1:
        socail.insta()
        print("\n You want exit or use another options(yes/no)")
        choose = input("yes Or No: ")
        if choose == "yes":
            os.system("cls")
            os.system('python project.py')
        elif choose == "no":
            os.system("cls")
            print("Thank you for using..!!")
    elif choose == 2:
        socail.twitter()
        print("\n You want exit or use another options(yes/no)")
        choose = input("yes Or No: ")
        if choose == "yes":
            os.system("cls")
            os.system('python project.py')
        elif choose == "no":
            os.system("cls")
            print("Thank you for using..!!")
    else:
        print("Wrong option")
    print("\n You want exit or use another options(yes/no)")
    choose = input("yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 4:
    ip_info.ip_info()
    print("\n You want exit or use another options(yes/no)")
    choose = input("Yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 5:
    phone_info.phone_info()
    print("\n You want exit or use another options(yes/no)")
    choose = input("Yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "No" or "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 6:
    ip = input("Enter ip address: ")
    s_p = int(input("Enter starting port number: "))
    e_p = int(input("Enter ending port number: "))
    os.system(f'python port_scanner.py {ip} {s_p} {e_p}')
    print("\n You want exit or use another options(yes/no)")
    choose = input("Yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 7:
    os.system('python Web_scraping.py')
    print("\n You want exit or use another options(yes/no)")
    choose = input("Yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 8:
    fake.Fake()
    print("\n You want exit or use another options(yes/no)")
    choose = input("Yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 9:
    os.system("^")
    os.system("cls")
    print("Thank you for using..!!")

else:  
    print("Wrong option Try angin..!!")
    os.system('python project.py')


