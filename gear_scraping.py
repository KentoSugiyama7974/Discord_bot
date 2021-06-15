import requests
from bs4 import BeautifulSoup

class Gear():
    def __init__(self):
        res = requests.get("https://wikiwiki.jp/splatoon2mix/%E6%A4%9C%E8%A8%BC/%E3%82%AE%E3%82%A2%E3%83%91%E3%83%AF%E3%83%BC")
        soup = BeautifulSoup(res.text, 'html.parser')
        self.scrollable = soup.find_all('div',class_="h-scrollable")

    def sub_ink_efficiency(self):
        self.sub_ink_efficiency = {}
        table = self.scrollable[4].find("table")
        th_list = table.find_all("th")
        td_list = table.find_all("td")

        for index in range(len(th_list)):
            self.sub_ink_efficiency[th_list[index].text] = []
            for text in td_list[index*9:(index*9)+9]:
                self.sub_ink_efficiency[th_list[index].text].append(text.text)

        return self.sub_ink_efficiency

    def weapon_weight(self):
        self.weapon_weight = {}
        table = self.scrollable[13].find("table")
        th_list = table.find_all("th")
        td_list = table.find_all("td")

        for index,text in enumerate(td_list[3::3]):
            self.weapon_weight[text.text] = td_list[4+(index*3)].text

        return self.weapon_weight         

if __name__ == "__main__":
    gear = Gear()
    g = gear.sub_ink_efficiency()
    print(g)