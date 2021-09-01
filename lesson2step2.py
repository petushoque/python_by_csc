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
    elif c == 'c' and temp == '<':
        temp += 'c'
    elif c == 'o' and temp == '<c':
        temp += 'o'
    elif c == 'd' and temp == '<co':
        temp += 'd'
    elif c == 'e' and temp == '<cod':
        temp += 'e'
    elif c == '>' and temp == '<code':
        temp += '>'
    if temp == '<code>':
        print(temp)
        state += 1
        temp = ''
        print(state)
print(state)