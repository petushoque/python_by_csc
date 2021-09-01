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
    counter += 1    
    code_start = webpage.find('<code>')
    code_end = webpage.find('</code>')
    code = webpage[code_start + 6:code_end]
    code_list.append(code)
    print('элементов в листе:', len(code_list), 'counter: ', counter, code)
    
    webpage = webpage[code_end + 1:]

print(counter)
print(len(code_list))