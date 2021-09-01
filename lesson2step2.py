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
    if code_list[i] == pop1 or code_list[i] == pop2 or code_list[i] == pop3:
        continue
    if code_list.count(code_list[i]) > pop1_count:
        pop3 = pop2
        pop3_count = pop2_count
        pop2 = pop1
        pop2_count = pop1_count
        pop1 = code_list[i]
        pop1_count = code_list.count(code_list[i])
        continue
    if code_list.count(code_list[i]) > pop2_count:
        pop3 = pop2
        pop3_count = pop2_count
        pop2 = code_list[i]
        pop2_count = code_list.count(code_list[i])
        continue        
print(pop1)
print(pop1_count)
print(pop2)
print(pop2_count)