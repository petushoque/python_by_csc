#подключить библиотеку
import urllib.request

#открыть страницу
fid=urllib.request.urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')

#записать в переменную
webpage=fid.read().decode('utf-8').lower()

state = 0
temp = ''

for c in webpage:
    if c == '<' and temp == '':
        temp += '<'
    if c = 'c' and temp == '<':
        temp += 'c'
    
print(webpage)