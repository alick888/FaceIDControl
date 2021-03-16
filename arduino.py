from urllib.request import urlopen

class Arduino:
    def __init__(self, url):
        self.url = url

    def open_door(self):
        try:
            urlopen(self.url+"/open").read()
        except:
            print('failed to open door')