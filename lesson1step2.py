import urllib.request

fid=urllib.request.urlopen('https://stepik.org/media/attachments/lesson/209717/1.html')

webpage=fid.read().decode('utf-8')

print(webpage)

cpp = str(webpage).count('C++')
python = str(webpage).lower().count('python')

print(cpp)
print(python)