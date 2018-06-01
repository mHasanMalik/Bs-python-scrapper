import requests
from bs4 import BeautifulSoup

def getCategories(URL):
    if(URL != ""):
        try:
            status = requests.get(URL)

            if(status.status_code == 200):
               parser_object = BeautifulSoup(status.content,"html.parser")
               
               div_tag_list = parser_object.find_all('div',{'class':'ty-menu__submenu-item-main-header'})
               for div in div_tag_list:
                   a_tag = div.find_all('a')
                   for a in a_tag:
                       print(a['href'])
                       print(a.text)
                       print("_________________")


        except requests.ConnectionError:
            print("ERROR !")
        


#___________________________#
def main():
    URL = "https://www.infinitecables.com/"

    getCategories(URL)


#___________________________#
if __name__ == "__main__":
    main()

