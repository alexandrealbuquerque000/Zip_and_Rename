
# Alexandre Maia Aquino de Albuquerque

import os # Para renomear os arquivos
import shutil # Para apagar os arquivos
import zipfile # Para compactar os arquivos
import copy # Para copiar os dados dos arquivos em uma lista
import time # Para dar uma ideia de movimento no loading (meramente estético)
from pathlib import Path # Para verificar se o diretório é válido

'''
Modelo da coleta de dados:
    data=[Título1, Quantidade de capítulos, [[Nome do Capítulo1[Número de páginas, [Nome da página1, Nome da página2...]]], [Nome do Capítulo2[Número de páginas, [Nome da página1, Nome da página2...]]], ...]
'''

# Função para mostrar a tela de carregamento
def loading(aux3):
    os.system("cls")
    if aux3==None:
        # Nesta parte o objetivo era dar a sensação de movimento, mas percebi que dependendo da quantidade de arquivos, atrasava muito o código. Por isso, se preferir tirar, é só deixar o comando 'os.system("cls")' junto com print('Carregando...). Até que também fica um efeito legal.
        loadtime=float(0.055)
        print('Carregando', end='')
        for points in range(3):
            time.sleep(loadtime)
            print('.',end='')
        time.sleep(loadtime)
    else:
        print('Carregando...')
      
# Função para aceitar apenas strings
def leiastr(msg):
    while True:
        print()
        verif=str(input(msg).strip().replace(" ", ""))
        if verif.isalpha() == False:
            print()
            print("ERRO:""\nDigite apenas letras.")
            continue
        else:
            verif=verif.lower()
            return verif

# Função para adicionar ponto à extensão caso não haja
def addpoint(ext):
    if '.' not in ext:
        ext='.'+ext

    return ext

# Função para varrer o diretório e guardar as informações em uma lista
def colectdata(hqpath):
    alldata=[]
    for folder, subfolders, files in os.walk(hqpath):  
            for loop1 in range(len(subfolders)):
                alldata.append([(subfolders[loop1])])
            numtitles=len(alldata)
            break
    loop2=0  
    aux1=0
    for folder, subfolders, files in os.walk(hqpath):
        if aux1<1:
            aux1=aux1+1
            pass
        else:
            alldata[loop2].append(str(len(subfolders)))
            chapnames=[]
            for loop3 in range(len(subfolders)):
                chapnames.append([subfolders[loop3]])
            alldata[loop2].append(chapnames)
            if loop2<numtitles-1:
                loop2=loop2+1
                aux1=-((len(subfolders)-1))
            else:
                break
    loop4=0
    loop5=0
    for folder, subfolders, files in os.walk(hqpath):    
        try:
            aux2
        except (NameError):
            aux2=-1
        else:
            pass
        if aux2<1:
            aux2=aux2+1
            pass
        else:
            if loop4 < numtitles:
                if loop5 < (len(alldata[loop4][2])):
                    alldata[loop4][2][loop5].append(str(len(files)))
                    alldata[loop4][2][loop5].append(files)  
                    loop5=loop5+1   
                else:
                    loop5=0
                    loop4=loop4+1

    return alldata

# Função para compactar os arquivos
def compacthqs(hqpath, exttocompac, delfiles, aux3):

    alldata=copy.deepcopy(colectdata(hqpath))

    for loop6 in range(len(alldata)):
        title=alldata[loop6][0]
        print()
        print('Título: '+title)
        print()
        numcaps=int(alldata[loop6][1])
        for loop7 in range(numcaps):    
            files=alldata[loop6][2][loop7][2]
            cap=alldata[loop6][2][loop7][0]
            titlefolder=(hqpath + '\{}').format(title)
            folder=(titlefolder + '\{}').format(cap) 
            if any((file.lower()).endswith(exttocompac)==True for file in files):
                hq = zipfile.ZipFile(folder+'.zip', 'w')
                print('Compactando '+ cap)
                testpass=1
            else:
                testpass=0
            for file in files:
                if (file.lower()).endswith(exttocompac):
                    hq.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), str(folder)), compress_type = zipfile.ZIP_DEFLATED)
                else:
                    if 's' in delfiles and testpass==1:
                        try:
                            os.mkdir((titlefolder+'./{} (others_extensions)').format(cap))
                        except OSError:
                            pass
                        finally:
                            savefiles=((titlefolder+'./{} (others_extensions)').format(cap))
                        shutil.copy(((folder+'\{}').format(file)), savefiles)
            try:
                hq
            except(UnboundLocalError, NameError):
                pass
            else:
                if testpass==1:
                    hq.close()
            if 's' in delfiles and testpass==1:
                shutil.rmtree(folder)
    if aux3==None:
        input('\nProcesso concluído com sucesso!')
    os.system("cls")

# Função para renomear extensões de arquivos
def renameext(hqpath, exttorename, newext, aux3):
    for folder, subfolders, files in os.walk(hqpath):
        for file in files:
            loading(aux3)
            if (file.lower()).endswith(exttorename):
                try:
                    os.rename((folder+'\{}').format(file), (folder+'\{}').format((((os.path.splitext(file))[0])+((os.path.splitext(file))[1]).lower()).replace(exttorename, newext)))
                except (FileExistsError):
                    os.rename((folder+'\{}').format(file), (folder+'\{}').format((((os.path.splitext(file))[0])+'_(repeated)'+((os.path.splitext(file))[1]).lower()).replace(exttorename, newext)))
    if aux3==None:
        input('\n\nProcesso concluído com sucesso!')

# Função para iniciar o programa
def run():
    reboot='s'
    while 's' in reboot:
        os.system("cls")
        print('-'*16)
        print(' Zip and Rename')
        print('-'*16)
        hqpath=input('\nDigite o diretório da pasta que contém todos os arquivos que deseja manipular: ')
        while ((Path(hqpath)).is_dir())==False:
            print("\nEsse diretório não existe.\n\nTente novamente.")
            hqpath=input('\nDigite o diretório da pasta que contém todos os arquivos que deseja manipular: ')
        compacquestion=leiastr("Deseja compactar arquivos? ")
        if 'hq' in compacquestion:
            compacquestion='s'
            hqmode=1
        else:
            hqmode=0 
        if 's' in compacquestion:
            if hqmode==1:
                exttorename='.png'
                newext='.jpg'
                renameext(hqpath, exttorename, newext, 1)
                exttocompac='.jpg'
                delfiles='s'
                aux3=1
            else:
                exttocompac=addpoint(input('\nDigite o tipo de extensão dos arquivos que deseja compactar: ').lower())
                delfiles=leiastr('Deseja excluir os arquivos após a compactação? ')
                aux3=None
            compacthqs(hqpath, exttocompac, delfiles, aux3)
        if hqmode==1:
            extchange='s'
            pass
        else:
            extchange=leiastr('Deseja renomear algum tipo de extensão? ')
        if 's' in extchange:
            if hqmode==1:
                exttorename='.zip'
                newext='.cbz'
            else:
                exttorename=addpoint(input('\nDigite o tipo de extensão que deseja mudar: ').lower())
                newext=addpoint(input('\nDigite o novo tipo de extensão: ').lower())
            renameext(hqpath, exttorename, newext, None)
        reboot=leiastr("Deseja reiniciar o programa? ")


run()