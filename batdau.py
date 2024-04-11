from bs4 import BeautifulSoup

import requests


website = "https://subslikescript.com/movie/The_Breach-14229154"
results = requests.get(website)
content = results.text
# lấy được title và transcript
soup = BeautifulSoup(content, "lxml")
#chỏ được vào trang web
#gọi tập chứa
a = soup.find("")
box = soup.find("article", class_ = "main-article")

title = box.find("h1").get_text()
#đã lấy được title
transcript = box.find("div", class_ = "full-script").get_text()
print(transcript)
#đã lấy được transcript


#tạo từ terminal sang file txt
# tạo 1 file transcript

file = open(title,"a") #a: add 
file.write(transcript)
file.close()
#file này cần phải sử dụng ứng dụng bên ngoài để sử dụng
print(f'{"content"}.txt')
#cách 2 để tạo file
with open(f'{"title"}.txt', 'w' ) as file:
    file.write(transcript)