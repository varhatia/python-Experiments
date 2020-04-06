import time
from datetime import datetime as dt 

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
website_block = ['facebook.com', 'www.facebook.com', 'linkedin.com', 'mail.google.com']
redirect = "127.0.0.1"

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() <= dt(dt.now().year, dt.now().month, dt.now().day, 10):
        print("Working Hours!!!")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_block:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_block):
                    file.write(line)
            file.truncate()
        print("Free Hours!!!")
    time.sleep(5)
