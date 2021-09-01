#подключить библиотеку
import urllib.request

#открыть страницу
fid=urllib.request.urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')

#записать в переменную
webpage=fid.read().decode('utf-8').lower()

code_list = []
counter = 0

print(webpage.count('<code>'))

while webpage.find('<code>') > 0:
    code_start = webpage.find('<code>')
    code_end = webpage.find('</code>')
    code = webpage[code_start:code_end]
    print(code)
    code_list.append(code)
    counter += 1
    webpage = webpage[code_end + 1:]

print(counter)
print(len(code_list))