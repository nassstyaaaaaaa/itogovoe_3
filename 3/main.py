str1 =str(input('Пожалуйста, введите строку, по отношению к которой будет рассчитываться расстояние Хэмминга'))
filename = str(input('Пожалуйста, введите полное имя файла для расчётов без кавычек(при необходимости и полный путь к нему). Например, input_file.txt'))
input_file = data = open(filename,'r')

line = input_file.read()
input_file.close()
lines = line.split()
print('Данные из файла\"' + str(filename) +  '\" успешно загружены...')
output = open('output.txt','w')
a=[]
b=[]
q=[]
def Hamming_distance_sort(str1, lines):
    print('Расчёт расстояний Хэмминга начался...')
    for i in range(len(lines)):
        if len(str1) == len(lines[i]):
            d = sum(1 for (a, b) in zip(str1, lines[i]) if a != b)
            print(d)
            a.append(d)
            b.append(d)
            b.append(lines[i])
        else:
            q.append(i)
    a.sort()
    print('Сортировка результатов...')
    for x in range (len(a)):
        string=b.index(a[x])+1
        output.write(b[string] + '\n')
        b.pop(string)
        b.pop(string-1)
    output.close() 
    print('Расчёты и сортировка по возрастанию расстояния Хэмминга завершены успешно. Данные импортированы в файл \'output.txt\'')
    if len(q)>0: 
        print('Внимание! номера строк исходного файла:', q , 'содержат неравное со сравниваемой строкой количество символов. Расчёты по ним не производились, и в сортировку они включены не были.')
    return
Hamming_distance_sort(str1,lines) 