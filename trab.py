import csv
class Usuario:
    def __init__(self,nomeUsu,senha,EhPremium):
        self._nomeUsu=nomeUsu
        self._senha=senha
        self._premium=EhPremium
        self._perfis=[]

    def verificaUsu(self,usuario):
        if usuario == self._nomeUsu:
            return False
        else:
            return True
    def addPerfil(self,perfil):
        if self._premium == "True" and len(self._perfis)<=5:
            self._perfis.append(perfil)
        elif self._premium == "False" and len(self._perfis)<=3:
            self._perfis.append(perfil)
        else:
            print('Não foi possível adicionar o Perfil ao usuário',self._nomeUsu)
    def removePerfil(self,perfil):
        cont=0
        for perfiss in self._perfis:
            if perfiss == perfil:
                del self._perfis[cont]
                print('Perfil removido!')
                break
            cont+=1
    
    def alterarSenha(self):
        self._senha=input('Digite sua Nova senha:')
    
    def alterarPlano(self,tipo):
        self._premium=tipo

    def retornaUsu(self,nome):
        if self._nomeUsu == nome:
            return self
        else:
            return "Falso"
        
    def retornaNome(self):
        return self._nomeUsu

    def salvamentoUsuario(self):
        texto= str(str(self._nomeUsu)+","+str(self._senha)+","+str(self._premium)+'\n')
        f = open('Usuarios.csv', 'a')
        f.write(texto)
        f.close()

    def validaLogin(self,usu,senha):
        if self._nomeUsu==usu and self._senha==senha:
            return self
        else:
            return 'False'
    
    def retornaPerfis(self):
        return self._perfis

class Perfil():
    def __init__(self,nome,idade,usuario):
        self._nome=nome
        self._idade=idade
        self._usuario=usuario
        usuario.addPerfil(self)
        self._favs=[]
        self._ultimos=[]

    def editarPerfil(self,nome,idade):
        self._nome=nome
        self._idade=idade
        print('perfil editado!!!')

    
    def info(self):
        return self._nome
    
    def pegaIdade(self):
        return self._idade

    def addFav(self,midia):
        if len(self._favs)<10:
            self._favs.append(midia)
        else:
            del self._favs[0]
            self._favs.append(midia)
   
    def removeFav(self,midia):
        cont=0
        for midiasFav in self._favs:
            if midiasFav == midia:
                del self._favs[cont]
                break
            cont+=1
   
    def addUltimo(self,midia):
        if len(self._ultimos)<10:
            self._ultimos.append(midia)
        else:
            del self._ultimos[0]
            self._ultimos.append(midia)
    
    def retornaUltimos(self):
        return self._ultimos
    
    def retornaFavs(self):
        return self._favs
   
    def assisti(self,midia):
        midia.assistir()
        self.addUltimo(midia)

    def favoritar(self,midia):
        cont=0
        for mid in self._favs:
            if mid == midia:
                del self._favs[cont]
                break
            cont+=1
        if cont == len(self._favs):
            self._favs.append(midia)

    def salvamentoPerfil(self):
        nomeUsu=self._usuario.retornaNome()
        texto= str(str(self._nome)+","+str(self._idade)+","+nomeUsu+'\n')
        f = open('Perfis.csv', 'a')
        f.write(texto)
        f.close()

class Midia:
    def __init__(self,id,titulo,genero,lancamento,classific):
        self._id=id
        self._titulo=titulo
        self._genero=genero
        self._lancamento=lancamento
        self._classific=classific

    def podeOlhar(self,idade):
        if idade>= self._classific:
            return True
        else:
            return False

    def infoGeral(self):
        texto= 'ID:'+self._id+' Nome:'+self._titulo+' Genero:'+self._genero+' lançado em:'+self._lancamento+' Classificação:'+self._classific
        return texto
    
    def verificaID(self,id):
        if self._id==id:
            return self
        else:
            return 'False'
    
    def assistir(self):
        print('Assistido')

    def buscaTitulo(self,titulo):
        if self._titulo==titulo:
            return True
        else:
            return False

class Serie(Midia):
    def __init__(self,id,titulo,genero,lancamento,classific,numEpi,episodios):
        super().__init__(id,titulo,genero,lancamento,classific)
        self._episodios=episodios
        self._numEpi=numEpi
    
    def infoGeral(self):
        texto=super().infoGeral()+' Episodio:'+self._numEpi+' Total episodios'+self._episodios
        return texto
    

class Documentario(Midia):
    def __init__(self,id,titulo,genero,lancamento,classific,tema):
        super().__init__(id,titulo,genero,lancamento,classific)
        self._tema=tema
    
    def infoGeral(self):
        texto=super().infoGeral()+' Tema:'+self._tema
        return texto

class Animacao(Midia):
    def __init__(self,id,titulo,genero,lancamento,classific,estudio):
        super().__init__(id,titulo,genero,lancamento,classific)
        self._estudio=estudio 
    
    def infoGeral(self):
        texto=super().infoGeral()+' Estudio:'+self._estudio
        return texto

class Filme(Midia):
    def __init__(self,id,titulo,genero,lancamento,classific,diretor,produtor):
        super().__init__(id,titulo,genero,lancamento,classific)
        self._diretor=diretor
        self._produtor=produtor
    
    def infoGeral(self):
        texto=super().infoGeral()+' Diretor:'+self._diretor+' Produtor'+self._produtor
        return texto


class Programa(Midia):
    def __init__(self,id,titulo,genero,lancamento,classific,numEpi,episodios):
        super().__init__(id,titulo,genero,lancamento,classific)
        self._episodios=episodios
        self._numEpi=numEpi
        
    def infoGeral(self):
        texto=super().infoGeral()+' Episodio:'+self._numEpi+' Total episodios'+self._episodios
        return texto 

class Catalogo:
    def __init__(self):
        self._lSeries=[]
        self._lFilmes=[]
        self._lDocumentarios=[]
        self._lAnimacoes=[]
        self._lProgramas=[]
    
    def addMidia(self,midia,tipo):
        if tipo == 1:
            self._lSeries.append(midia) 
        elif tipo == 2:
            self._lFilmes.append(midia)
        elif tipo == 3:
            self._lDocumentarios.append(midia)
        elif tipo == 4:
            self._lAnimacoes.append(midia)
        elif tipo == 5:
            self._lProgramas.append(midia)
        else:
            print('TIPO INVÁLIDO')
    
    def obterLista(self,tipo):
        if tipo == 1:
            return self._lSeries 
        elif tipo == 2:
            return self._lFilmes
        elif tipo == 3:
            return self._lDocumentarios
        elif tipo == 4:
            return self._lAnimacoes
        elif tipo == 5:
            return self._lProgramas
        else:
            print('TIPO INVÁLIDO')


def serializarMidia():
    global midias
    catalogo=Catalogo()
    f = open('Midias.csv', newline='')
    reader = csv.reader(f)
    tabela=[linha for linha in reader]
    for i in range(0,(len(tabela))) :
        if tabela[i][2]=='Serie':
            serie=Serie(tabela[i][0],tabela[i][1],tabela[i][2],tabela[i][3],tabela[i][4],tabela[i][5],tabela[i][6])
            catalogo.addMidia(serie,1)
            midias.append(serie)
        if tabela[i][2]=='Filme':
            filme=Filme(tabela[i][0],tabela[i][1],tabela[i][2],tabela[i][3],tabela[i][4],tabela[i][5],tabela[i][6])
            catalogo.addMidia(filme,2)
            midias.append(filme)
        if tabela[i][2]=='Documentario':
            documentario=Documentario(tabela[i][0],tabela[i][1],tabela[i][2],tabela[i][3],tabela[i][4],tabela[i][5])
            catalogo.addMidia(documentario,3)
            midias.append(documentario)
        if tabela[i][2]=='Animacao':
            animacao=Animacao(tabela[i][0],tabela[i][1],tabela[i][2],tabela[i][3],tabela[i][4],tabela[i][5])
            catalogo.addMidia(animacao,4)
            midias.append(animacao)
        if tabela[i][2]=='Programa':
            programa=Programa(tabela[i][0],tabela[i][1],tabela[i][2],tabela[i][3],tabela[i][4],tabela[i][5],tabela[i][6])
            catalogo.addMidia(programa,5)
            midias.append(programa)
    return catalogo

def serializarUsu():
    usuarios=[]
    f = open('Usuarios.csv', newline='')
    reader = csv.reader(f)
    tabela=[linha for linha in reader]
    for i in range(0,(len(tabela))) :
        usuario=Usuario(tabela[i][0],tabela[i][1],tabela[i][2])
        usuarios.append(usuario)
    return usuarios

def serializarPerfis(usuarios):
    perfis=[]
    f = open('perfis.csv', newline='')
    reader = csv.reader(f)
    tabela=[linha for linha in reader]
    for i in range(0,(len(tabela))) :
        for usu in usuarios:
            retorno = usu.retornaUsu(tabela[i][2])
            if retorno != "Falso":
                perfil=Perfil(tabela[i][0],tabela[i][1],retorno)
                perfis.append(perfil)
    return perfis

def login(usu,senha,usuarios):
    for usus in usuarios:
        usuarioLogado=usus.validaLogin(usu,senha)
        if usuarioLogado != 'False':
            return usuarioLogado
    print('Usuário ou senha Inválidos')
    return 'False'
        
            

op=0
midias=[]
catalogo=serializarMidia()
while op!=3:
    op=int(input('Menu\n 1 - Acessar\n 2 - Criar Conta\n 3 - Sair\nDIGITE: '))
    usuarios=serializarUsu()
    perfis=serializarPerfis(usuarios)



    if op == 1:
        usu=input('Usuário:')
        senha=input('Senha:')
        usuarioLogado=login(usu,senha,usuarios)
        if usuarioLogado!='False':
            print('Olá',usuarioLogado.retornaNome())
            while op != 6:
                print('PERFIS:')
                for perfisUsuLogado in usuarioLogado.retornaPerfis():
                    print(perfisUsuLogado.info())
                op=int(input('Menu\n 1 - Alterar assinatura\n 2 - Acessar Perfil\n 3 - Editar Perfil\n 4 - Adicionar Perfil\n 5 - Remover Perfil\n 6 - VOLTAR\nDIGITE: '))
                if op==1:
                    assinatura=int(input('Qual assinatura deseja: \n1 - Simples \n2 - PREMIUM\nDIGITE:'))
                    if assinatura ==1:
                        usuarioLogado.alterarPlano('False')
                        print('Assinatura: SIMPLES')
                    elif assinatura==2:
                        usuarioLogado.alterarPlano('True')
                        print('Assinatura: PREMIUM')
                    else:
                        print('opção inválida')
                elif op==2:
                    perfiLogado=input('Qual o nome do perfil você deseja: ')
                    for perfisUsuLogado in usuarioLogado.retornaPerfis():
                        if perfiLogado==perfisUsuLogado.info():
                            perfiLogado=perfisUsuLogado
                            op=999
                elif op==3:
                    perfilEditar=input('Qual o nome do perfil você deseja: ')
                    for perfisUsuLogado in usuarioLogado.retornaPerfis():
                        if perfilEditar==perfisUsuLogado.info():
                            nome=input('Digite o novo Nome: ')
                            idade=input('Digite a Idade nova: ')
                            perfisUsuLogado.editarPerfil(nome,idade)

                elif op==4:
                    nome = input('Qual nome do novo perfil: ')
                    idade = input('Qual idade do novo perfil: ')
                    perfiLogado=Perfil(nome,idade,usuarioLogado)
                    perfis.append(perfiLogado)
                
                elif op==5:
                    perfilExcluir=input('Digite o nome do Perfil que deseja excluir:')
                    for perfisUsuLogado in usuarioLogado.retornaPerfis():
                        if perfilExcluir==perfisUsuLogado.info():
                            usuarioLogado.removePerfil(perfisUsuLogado)
                if op==999:
                    print('Conta: ',usuarioLogado.retornaNome(),'\nPerfil: ',perfiLogado.info())
                    while op != 9:
                        op=int(input('Menu\n 1 - Busca por nome\n 2 - Ultimos assistidos\n 3 - Favoritos\n 4 - Filmes\n 5 - Series\n 6 - Documentarios\n 7 - Animacoes\n 8 - Programas de TV\n 9 - VOLTAR\nDIGITE: '))
                        id='0'
                        if op==1:
                            titulo=input('Digite o titulo: ')
                            for mid in midias:
                                if mid.buscaTitulo(titulo)==True:
                                    print(mid.infoGeral())

                        if op==2:
                            print('ULTIMOS ASSISTIDOS:')
                            for mid in perfiLogado.retornaUltimos():
                                print(mid.infoGeral())
                        if op==3:
                            print('FAVORITOS:')
                            for mid in perfiLogado.retornaFavs():
                                print(mid.infoGeral())
                        if op==4:
                            for mid in catalogo.obterLista(2):
                                if mid.podeOlhar(perfiLogado.pegaIdade())==True:
                                    print(mid.infoGeral())
                            id=input('Digite o ID do Filme que desejas: ')
                        if op==5:
                            for mid in catalogo.obterLista(1):
                                if mid.podeOlhar(perfiLogado.pegaIdade())==True:
                                    print(mid.infoGeral())
                            id=input('Digite o episódio da Série que desejas: ')
                        if op==6:
                            for mid in catalogo.obterLista(3):
                                if mid.podeOlhar(perfiLogado.pegaIdade())==True:
                                    print(mid.infoGeral())
                            id=input('Digite o ID do Documentário que desejas: ')
                        if op==7:
                            for mid in catalogo.obterLista(4):
                                if mid.podeOlhar(perfiLogado.pegaIdade())==True:
                                    print(mid.infoGeral())
                                id=input('Digite o ID da Animação que desejas: ')
                        if op==8:
                            for mid in catalogo.obterLista(5):
                                if mid.podeOlhar(perfiLogado.pegaIdade())==True:
                                    print(mid.infoGeral())
                            id=input('Digite o ID do capitulo do Programa que desejas: ')
                        if id!='0':
                            for mid in midias:
                                if mid.verificaID(id)!='False':
                                    op=int(input('OPÇÕES: \n 1 - Assistir \n 2 - Favoritar\nDIGITE: '))
                                    if op==1:
                                        perfiLogado.assisti(mid)
                                        mid.infoGeral()
                                    elif op==2:
                                        perfiLogado.addFav(mid)
                                        mid.infoGeral()
    elif op==2:
        nome=input('Digite seu usuário: ')
        senha=input('Sua senha: ')
        i=0
        for usu in usuarios:
            if usu.verificaUsu(nome)==False:
                i+=1
        if i==0:
            usuario=Usuario(nome,senha,'False')
            usuarios.append(usuario)
            print('Usuário criado com sucesso') 
        else:
            print('Este nome de usuário já existe')

    f = open('Usuarios.csv', 'w') #apaga as assinaturas do arquivo
    f.write('')
    f.close()
    f = open('Perfis.csv', 'w') #apaga as assinaturas do arquivo
    f.write('')
    f.close()          
    for usu in usuarios:
        usu.salvamentoUsuario()
        for perf in usu.retornaPerfis():
            perf.salvamentoPerfil()
        
            


