import os
# dicionario
pessoa = {'Nome': input('Nome: '),
          'CPF': input('CPF: '),
          'RG': input('RG: '),
          'Data de nascimento': input('Data de nascimento: '),
          'Gênero': input('Gênero: '),
          'E-mail': input('E-mail: '),
          'Telefone': input('Telefone: '),
          'Tipo sanguíneo': input('Tipo sanguíneo: '),
          'Profissão': input('Profissão: '),
          'Empresa': input('Empresa: ')
 }

os.system('cls')

# exibe na tela
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')