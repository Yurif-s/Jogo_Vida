from random import randint, choice

class Personagem:
   def __init__(self, nome, idade, sexo, saude, felicidade, aparencia, nacionalidade, dinheiro) -> None:
      self.__nome = nome
      self.__idade = idade
      self.__sexo = sexo
      self.__saude = saude
      self.__felicidade = felicidade
      self.__aparencia = aparencia
      self.__nacionalidade = nacionalidade
      self.__dinheiro = dinheiro

   def getNome(self):
      return self.__nome
   
   def getIdade(self):
      return self.__idade
   
   def getSexo(self):
      return self.__sexo
   
   def getSaude(self):
      return self.__saude
   
   def getFelicidade(self):
      return self.__felicidade
   
   def getAparencia(self):
      return self.__aparencia
   
   def getNacionalidade(self):
      return self.__nacionalidade
   
   def getContaBancaria(self):
      return self.__dinheiro
   
   def reducaoSaude(self, dano=None):
      if dano is None:
         dano = randint(1, 5)
      self.__saude -= dano
      if self.__saude < 0:
         self.__saude = 0

   def aumentarFelicidade(self, aumento):
      self.__felicidade += aumento
      if self.__felicidade > 100:
         self.__felicidade = 100

   def reduzirFelicidade(self, reducao):
      self.__felicidade -= reducao
      if self.__felicidade < 0:
         self.__felicidade = 0

   def reduzirAparencia(self, reducao):
      self.__felicidade -= reducao
      if self.__felicidade < 0:
         self.__felicidade = 0

   def aumentarDinheiro(self, aumento):
      self.__dinheiro += aumento

   def reduzirDinheiro(self, reducao):
      self.__dinheiro -= reducao
      if self.__dinheiro < 0:
         self.__dinheiro = 0

   def trabalhar(self, aumento):
      self.__dinheiro += aumento
      return print(f'Você trabalhou e ganhou {aumento}')

   def opcaoCrescer(self):
      self.__idade += 1
   
   def exibirDetalhes(self):
      return f'''\nNome: {self.getNome()}
Idade: {self.getIdade()}
Sexo: {self.getSexo()}
Saúde: {self.getSaude()}
Felicidade: {self.getFelicidade()}
Nacionalidade: {self.getNacionalidade()}
Saldo: {self.getContaBancaria()}'''
   

class Jogo:
   def __init__(self) -> None:
      self.personagem = Personagem(nome=nome, idade=18, sexo=genero, saude=randint(75, 100), 
                                    felicidade=randint(75, 100), 
                                    aparencia=randint(75, 100),
                                    nacionalidade=nacionalidade,
                                    dinheiro=0)

   def iniciarJogo(self):
      while self.personagem.getSaude() > 0:
         print(self.personagem.exibirDetalhes())
         escolha = input('Deseja aumentar um ano? [S/N] ').lower()
         if escolha == 's':
            self.personagem.opcaoCrescer()
            self.ocorrenciaDeEvento()
            print('Você pagou os boletos')
            self.personagem.reduzirDinheiro(300)
            self.personagem.reducaoSaude()
         else:
            escolha = input('Deseja trabalhar? [S/N] ').lower()
            if escolha == 's':
               self.personagem.trabalhar(randint(10, 500))


      if self.personagem.getSaude() <= 0:
         if self.personagem.getContaBancaria() < 0:
            print('Você morreu devendo dinheiro!')
         else:
            print('\nVocê morreu!')


   def ocorrenciaDeEvento(self):
      eventos = {
         "Você encontrou um amigo!": (self.personagem.aumentarFelicidade, 10),
         "Você ficou doente!": (self.personagem.reducaoSaude, randint(10, 30)),
         "Você foi promovido no trabalho!": (self.personagem.aumentarFelicidade, 20),
         "Você sofreu um acidente!": (self.personagem.reducaoSaude, randint(20, 50)),
         "Você ganhou na loteria!": (self.personagem.aumentarDinheiro, 250),
         "Você foi roubado!": (self.personagem.reduzirDinheiro, 30)
      }
      ocorrencia_de_evento = randint(1, 3)
      if ocorrencia_de_evento == 1:
         descricao_evento = choice(list(eventos.keys()))
         metodo, valor = eventos[descricao_evento]
         print(f'\nAconteceu um Evento: {descricao_evento}')
         metodo(valor)

nome = input('\nDigite o nome do seu personagem: ')
sexo = ['Masculino', 'Feminino']
genero = input('Escolha o sexo do seu personagem [M/F]: ').lower()

if genero == 'm':
   genero = sexo[0]
elif genero == 'f':
   genero = sexo[1]
else:
   genero = 'Indefinido'
nacionalidade = input('Digite a nacionalidade de seu personagem: ')

jogo = Jogo()
jogo.iniciarJogo()
