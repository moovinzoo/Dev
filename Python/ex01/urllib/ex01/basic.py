import urllib
import urllib.request
import os

# encode를 해서 정보를 넘기는 방식을 post라고 한다.
response = urllib.request.urlopen(
        "https://en.wikipedia.org/wiki/Main_Page",
        data = "search=Turing".encode()
        )

text = response.read().decode()

path = "./wiki.html"
with open(path, "w") as f:
    f.write(text)
