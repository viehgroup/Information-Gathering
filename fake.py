def Fake():
    from faker import Faker
    fake = Faker()
    print("-----x-----x-----x-----","\n")
    print("Email: ",fake.email())
    print("Name: ",fake.name())
    print("URL: ",fake.url())
    print("Country: ",fake.country(),"\n")
    print("-----x-----x-----x-----")
    print("\n")




