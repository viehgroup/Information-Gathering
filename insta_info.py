def info():
    import requests
    username = input("enter: ")
    r = requests.get("https://www.instagram.com/"+ username +"/?__a=1")
    if r.status_code == 200:
        res = r.json()['graphql']['user']
        print("\nUsername: " + res['username'])
        print("Full Name: "+res['full_name'])
        try:
            print("Business Category: "+res['edge_follow']['business_category_name'])
        except Exception as e:
            print("Account :"+" Private" + str(e))
        finally:
            print("Biograph: " + res['biography'])
            print("URL: "+ str(res['external_url']))
            print("Followers: "+str(res['edge_followed_by']['count']))
            print("Following: "+str(res['edge_follow']['count']))
            print("Profile Picture HD: " + res['profile_pic_url_hd'])
    elif r.status_code == 404:
        print("Error: Profile Not Found")
    else:
        print("Error: Something Went Wrong")
    print("\n")

