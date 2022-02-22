import requests
def insta():
    username = input("enter: ")
    r = requests.get("https://www.facebook.com/" + username)
    print(r.status_code)
    print("\n")

def twitter():
    username = input("enter: ")
    r = requests.get("https://twitter.com/" + username)
    print(r.status_code)
    print("\n")
