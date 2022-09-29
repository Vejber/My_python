# как работать с файлами
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи/ перезаписи данных
# w+, r+

# запись данных:
# colors = ['red ', 'green ', 'blue ']
# data = open('file.txt', 'a') 
# название файла, что с ним делать
#   если файла не существует, то "а" его автоматически создаст
# data.writelines(colors)
# data.write('\nLINE 121 \n')
# data.write('LINE 131\n')
# data.close() # обязательно завершить процесс

# еще способ:
# with open('file.txt', 'w') as data:
#     data.write('line1\n')
#     data.write('line 2 \n')

# чтение данных:
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()