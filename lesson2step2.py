#подключить библиотеку
import urllib.request

#открыть страницу
fid=urllib.request.urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')

#записать в переменную
webpage=fid.read().decode('utf-8').lower()

code_list = []

while webpage.find('<code>') > -1:
    code_start = webpage.find('<code>')
    code_end = webpage.find('</code>')
    code = webpage[code_start + 6:code_end]
    # пропускать пустые элементы
    if len(code) > 0:
        code_list.append(code)    
    webpage = webpage[code_end + 7:]

pop1 = ''
pop1_count = 0
pop2 = ''
pop2_count = 0
pop3 = ''
pop3_count = 0

for i in range(len(code_list)):
    code_list[i].count > pop