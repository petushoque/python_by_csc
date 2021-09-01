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
    if c == 'c' and temp == '<':
        temp += 'c'
    if c == 'o' and temp == '<c':
        temp += 'o'
    if c == 'd' and temp == '<co':
        temp += 'd'
    if c == 'e' and temp == '<cod':
        temp += 'e'
    if c == '>' and temp == '<code':
        temp += '>'
    if temp == 'code':
        state += 1
print(state)