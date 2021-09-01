#подключить библиотеку
import urllib.request

#открыть страницу
fid=urllib.request.urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')

#записать в переменную
webpage=fid.read().decode('utf-8').lower()

code_list = []
counter = 0

print(webpage.count('<code>'))

while webpage.find('<code>') > -1:
    counter += 1   
    if counter == 6:
        print()
        print(webpage[:50])
        print()
    code_start = webpage.find('<code>')
    code_end = webpage.find('</code>')
    code = webpage[code_start:code_end + 7]
    code_list.append(code)
    print('элементов в листе:', len(code_list), 'counter: ', counter, code)
    
    webpage = webpage[code_end + 7:]

print(counter)
print(len(code_list))