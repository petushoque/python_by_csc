#подключить библиотеку
import urllib.request

#открыть страницу
fid=urllib.request.urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')

#записать в переменную
webpage=fid.read().decode('utf-8').lower()

code_list = []
counter = 0

while webpage.find('<code>') > 0:
    code_start = webpage.find('<code>')
    code_end = webpage.find('</code>')
    counter += 1
    webpage = webpage[code_end + 7:]

print(counter)