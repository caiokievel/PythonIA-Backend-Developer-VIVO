arquivo = open(
    'D:\DIO.me\Bootcamps\PythonIA Backend Developer VIVO\manipulando_arquivos\lorem.txt', 'r')
# print(arquivo.read())
# print(arquivo.readline())

# for linha in arquivo.readlines():
#    print(linha)
while (linha := arquivo.readline()):
    print(linha)
arquivo.close()
