def custom_write(file_name, strings):
    strings_positions={}
    n = 1
    file = open(file_name, 'w', encoding='Utf-8')
    for i in strings:
        pos = file.tell()
        key = (n, pos)
        strings_positions[key] =i
        file.write(f'{i}\n')
        n = n+1
    file.close()
    return strings_positions





info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
