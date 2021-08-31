import urllib.request

fid=urllib.request.urlopen('https://stepik.org/media/attachments/lesson/209717/1.html')

webpage=fid.read().decode('utf-8')

cpp = str(webpage).count('C++')
python = str(webpage).lower().count('python')

if cpp > python:
    print('C++')
elif cpp < python:
    print('python')
else:
    print('')