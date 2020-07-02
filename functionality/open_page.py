import os

def open_page(name):
    valid_names = ["facebook","github","gmail", "google"]
    print(name)
    if not name.lower().strip() in valid_names:
        print("Sorry, that is not a site that I'm allowed to access")
        return
    os.system("google-chrome www.{}.com".format(name.lower().strip()))
    
    