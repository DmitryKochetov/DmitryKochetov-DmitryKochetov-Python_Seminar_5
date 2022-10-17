# Напишите программу, удаляющую из текста все слова, содержащие ""абв""


stroka = 'абв вбвба абвб бабв'
splitted_string = []

splitted_string = stroka.split(' ')

for i in splitted_string:
    if 'абв' in i:
        splitted_string.remove(i)


print(splitted_string)

# или так


stroka_1 = 'абв вбвба абвб бабв fff'
ret_elem = []

splitted_string_1 = stroka_1.split(' ')

ret_elem = list(filter(lambda x: not 'абв' in x, splitted_string_1))
print(ret_elem)