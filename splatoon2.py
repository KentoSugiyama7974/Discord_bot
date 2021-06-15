import requests
from bs4 import BeautifulSoup

class Stage():
    def __init__(self):
        target_url = "https://splatoon.caxdb.com/schedule2.cgi"
        r = requests.get(target_url)
        soup = BeautifulSoup(r.text, "lxml")
        li = soup.find_all("li")
        li = [l.text for l in li]
        self.stage = list()
        for index in range(len(li)//10):
            self.stage.append(li[index*10:index*10+10])

    def get_now(self):
        return self.stage[0]

    def get_next(self):
        return self.stage[1]

    def get_all(self):
        return self.stage

    def get_time(self,time):
        for s in self.stage:
            if s[0].split(" ")[1].split(":")[0] == time:
                return s

if __name__ == "__main__":
    stage = Stage()
    now = stage.get_time('17')
    print(stage.stage)

