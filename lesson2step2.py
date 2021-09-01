#подключить библиотеку
import urllib.request

#открыть страницу
fid=urllib.request.urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')

#записать в переменную
webpage=fid.read().decode('utf-8').lower()

code_list = []

while webpage.find('<code>') > 0:
    code_start = webpage.find('<code>')
    code_end = webpage.find('</code>')
print(code_string)
print(webpage[17712:17720])

print(state)