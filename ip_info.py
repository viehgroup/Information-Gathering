def ip_info():
    import webbrowser
    new = 2
    url = ("https://ipinfo.io/")
    term = input("Enter IP Addr. : ")
    webbrowser.open(url+term,new=new)