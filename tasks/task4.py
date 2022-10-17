# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# в этом кодже есть только одно ограничение, предполагается, что последовательность 
# символов будет не более 9 при разархивации

with open('file_task4_input.txt', 'r') as f:
    line_1 = f.readline()

f.close()

print(line_1)
new_line = ''
line_1 += ' '

i = 1
while i < (len(line_1)):
    count = 0
    
    if line_1[i] != line_1[len(line_1)-1]:
        while (line_1[i-1] == line_1[i]):
            count += 1
            i += 1
        new_line = new_line + str(count+1) + line_1[i-1]
    
    else:
        while (i < (len(line_1)-1)):
            count += 1
            i += 1
        new_line = new_line + str(count+1) + line_1[i-1]
    
    i += 1
    
print(new_line)

with open('file_task4_output.txt', 'w') as f:
    f.write(new_line)
f.close()

with open('file_task4_output.txt', 'r') as f:
    line_2 = f.readline()

line_3 = ''

for n in range(0, len(line_2),2):
    line_3 = line_3 + int(line_2[n]) * line_2[n+1]
    
 
print(line_3)

with open('file_task4_output_unpacked.txt', 'w') as f:
    f.write(line_3)
f.close()
