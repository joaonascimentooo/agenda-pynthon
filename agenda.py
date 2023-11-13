
agenda =  [] 
def inserir_cpf():
     return(input("Insira aqui seu cpf: "))

def inserir_nome():
     return(input("Insira aqui seu nome: "))

def inserir_idade():
     return(input("Insira aqui sua idade: "))

def inserir_telefone():
     return(input("Insira aqui seu telefone: ")) 

def adicionar():
    global agenda
cpf = inserir_cpf()
nome = inserir_nome()
idade =inserir_idade()
telefone = inserir_telefone()
agenda =  [nome,cpf,idade,telefone] 

print(agenda)




