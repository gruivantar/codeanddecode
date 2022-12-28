codes = {'а':'1', 'б':'9', 'в':'!', 'г':'@',  #код для шифрофки
         'д':'#', 'е':'%', 'ё':'^', 'ж':'*',
         'з':'(', 'и':'-', 'й':'_', 'к':'=',
         'л':'+', 'м':'/', 'н':'.', 'о':',',
         'п':';', 'р':':', 'с':'`', 'т':'<',
         'у':'>', 'ф':'2', 'х':'3', 'ц':'4',
         'ч':'5', 'ш':'6', 'щ':'7', 'ы':'8',
         'ь':')', 'ъ':'[', 'э':']', 'ю':'{', 'я':'}', ' ':' '}

uncodes = {k: v for v, k in codes.items()} #код для дешифровки

def codetext(text): #функция кодирует текст
    coded_text = ''
    for ch in text:
        if ch.lower() in codes:
            coded_text += codes[ch.lower()]
        else:
            coded_text += ch
    return coded_text

def uncodetext(code): #декодирует ранее зашифрованный текст
    ucoded_text = ''
    for ch in code:
        ucoded_text += uncodes[ch]
    return ucoded_text

print('Программа кодирует и декодироует текст в файле')
print('Кодировка текста в файле text.txt, создает файл coded_text.txt')
print('Декодировка кода в файле coded_text.txt, создает файл decoded_text.txt')
print('*************************************************************************')
print('Кодируемый текст должен быть на русском, без символов и цифр')
print('*************************************************************************')
print('Что вы хотите сделать?') #Предлагает выбрать что сделать с текстом
print('1 - закодировать текст')
print('2 - декодировать текст')
choose = input('Выбор: ')
while choose != '1' and choose != '2': #Проверка на допустимость значения
    print('Только 1 или 2')
    choose = input('Выбор: ')
if choose == '1': #Кодировка файла
    infile = open('text.txt', 'r')
    text_line = infile.readline().rstrip('\n')
    text = text_line
    while text_line != '':
        text_line = infile.readline().rstrip('\n')
        text += text_line
    infile.close()

    outfile = open('coded_text.txt', 'w')
    outfile.write(codetext(text))
    outfile.close()
elif choose == '2': #Декодировка файла
    infile = open('coded_text.txt', 'r')
    text_line = infile.readline().rstrip('\n')
    code = text_line
    while text_line != '':
        text_line = infile.readline().rstrip('\n')
        code += text_line
    infile.close()

    outfile = open('decoded_text.txt', 'w')
    outfile.write(uncodetext(code))
    outfile.close()