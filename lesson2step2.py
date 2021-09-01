#подключить библиотеку
import urllib.request

#открыть страницу
fid=urllib.request.urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')

#записать в переменную
webpage=fid.read().decode('utf-8').lower()

code_list = []

print(webpage.count('<code>'))

# почему появляется пустой 6 элемент?

while webpage.find('<code>') > -1:
    code_start = webpage.find('<code>')
    code_end = webpage.find('</code>')
    code = webpage[code_start:code_end + 7]
    # пропускать пустые элементы
    if len(code) > 0:
        code_list.append(code)
    print('элементов в листе:', len(code_list), 'counter: ', counter, code)
    
    webpage = webpage[code_end + 7:]

print(len(code_list))