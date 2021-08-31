#подключить библиотеку
import urllib.request

#открыть страницу
fid=urllib.request.urlopen('https://stepik.org/media/attachments/lesson/209717/1.html')

#записать в переменную
webpage=fid.read().decode('utf-8')

#посчитать количество упоминаний
cpp = str(webpage).count('C++')
python = str(webpage).lower().count('python')

#вывести более часто встречающийся язык
if cpp > python:
    print('C++')
elif cpp < python:
    print('python')
else:
    print('')