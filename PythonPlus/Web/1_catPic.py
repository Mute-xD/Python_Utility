import urllib.request
response = urllib.request.urlopen('https://placekitten.com/g/1920/1080')
print('Code: ', response.getcode())
catPic = response.read()
with open('catPic.jpg', 'wb') as file:
    file.write(catPic)
