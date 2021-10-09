import pandas as pd
import time
import arquivos


def menuMedicamentos(listaMedicamento):
    opcao = 0
    while opcao != 6:
        print("_"*50)    
        print("\n{}".format("SISTEMA PARA GERENCIAMENTO DE UMA FARMÁCIA".center(50)))
        print("\n{}".format("***MEDICAMENTOS5***".center(50)))
        print("_"*50)
        print("\n[1] Cadastrar um Medicamento")
        print("[2] Procurar um Medicamento")
        print("[3] Excluir um Medicamento")
        print("[4] Listar os Medicamentos")
        print("[5] Repor um Medicamento")
        print("[6] Retornar ao Menu Principal")
        
        opcao = input("Informe uma opção: ")
        if opcao.isnumeric():
            opcao = int(opcao)
            if opcao == 1:
                cadastrarMedicamento(listaMedicamento)
                time.sleep(1)
                arquivos.limpaTerminal()
            elif opcao == 2:
                buscarMedicamento(listaMedicamento)
                arquivos.limpaTerminal()
            elif opcao == 3:
                excluirMedicamento(listaMedicamento)
                arquivos.limpaTerminal()
            elif opcao == 4:
                listarMedicamento(listaMedicamento)
                arquivos.limpaTerminal()
            elif opcao == 5:
                reporMedicamento(listaMedicamento)
                arquivos.limpaTerminal()
            elif opcao == 6:
                #print("Retornado ao Menu Principal")
                arquivos.limpaTerminal()
            else:
                print("Opção Inválida ... Digite uma opção válida")
                time.sleep(1.2)
                arquivos.limpaTerminal()
        else:
            print("Opção Inválida ... Digite uma opção válida")
            time.sleep(1.2)
            arquivos.limpaTerminal()


def cadastrarMedicamento(listaMedicamentos):
    print("{}".format("=====INFORMAÇÕES DO MEDICAMENTO====="))
    
    IUM = validarIUM()
    
    if IUM in listaMedicamentos:
        print("Este medicamento já cadastrado ...")
    else:
        nome = validarNome()
        tarja = validarTarja()
        vencimento = validarDataVencimento()
        quantidade = validarQuantidade()
        preco = validarPreco()
        subtipo = validarSubtipo()
        listaMedicamentos[IUM] = [nome, tarja, vencimento, preco, quantidade, subtipo]
        arquivos.salvarMedicamento(listaMedicamentos, IUM)
        print("Medicamento Cadastrado com Sucesso !")

def buscarMedicamento(listaMedicamentos):
    if len(listaMedicamentos) == 0:
        print("Nenhum Medicamento foi Cadastrado ...")
        time.sleep(1.2)
    else:
        ium = validarIUM()
        
        if ium in listaMedicamentos:
            print("#"*50)
            print(" Nome: {}\n Tarja: {}\n Vencimento: {}\n Quantidade: {}\n Preço: {}\n Subtipo: {}\n".format(listaMedicamentos[ium][0], listaMedicamentos[ium][1],listaMedicamentos[ium][2], listaMedicamentos[ium][3], listaMedicamentos[ium][4], listaMedicamentos[ium][5]))
         
            parada = True
            while parada:
                opcao = input("Deseja retornar ao Menu Medicamentos (S para SIM)? ")
                
                if opcao == "S":
                    parada = False
                else:
                    print("    Erro ... Digite S para retornar ao Menu\n")
                    
        else:
            print("   Esse IUM não está cadastrado ...")
            time.sleep(1.4)
            
def excluirMedicamento(listaMedicamentos):
    if len(listaMedicamentos) == 0:
        print("Nenhum Medicamento foi Cadastrado ...")
        time.sleep(1.2)
    else:
        print("====Informe o IUM do Medicamento para Excluir====")
        ium = validarIUM()
       
        if ium in listaMedicamentos:
            del listaMedicamentos[ium]
            arquivos.atualizarMedicamento(listaMedicamentos)
            print("Medicamento Excluído com Sucesso !")
            time.sleep(1.3)
        else:
            print("    Este IUM não está cadastrado ...")
            time.sleep(1.3)                     

def listarMedicamento(listaMedicamentos):
    if len(listaMedicamentos) == 0:
        print("Nenhum Medicamento foi Cadastrado ...")
        time.sleep(1.2)
    else:
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        print("-"*100) 
        tabela = pd.DataFrame.from_dict(listaMedicamentos, orient="index", columns=["NOME", "TARJA", "VENCIMENTO", "PREÇO", "QUANTIDADE", "SUBTIPO"])
        print(tabela) 
        print("-"*100) 
        
        parada = True
        while parada:
            opcao = input("Deseja retornar ao Menu Medicamentos (S para SIM)? ")
            
            if opcao == "S":
                parada = False
            else:
                print("    Erro ... Digite S para retornar ao Menu\n")

def reporMedicamento(listaMedicamentos):
    if len(listaMedicamentos) == 0:
        print("Nenhum Medicamento foi Cadastrado ...")
        time.sleep(1.2)
    else:
        print("====Informe o IUM do Medicamento para Reposição====")
        ium = validarIUM()
       
        if ium in listaMedicamentos:
            quantidade = validarQuantidade()
            listaMedicamentos[ium][4] = quantidade
            arquivos.atualizarMedicamento(listaMedicamentos)
            print("    Reposição Concluída !\n")
            time.sleep(1.3)  
        else:
            print("    Este IUM não está cadastrado ...")
            time.sleep(1.3)   
     
 
def validarIUM():
    """Validar IUM"""
    while True:
        ium = input("Identificador (IUM): ")
        if ium.isnumeric():
            return ium
        print("Erro ... Digite apenas números")
        

def validarNome():
    """Validar o Nome"""
    while True:
        nome = input("Nome: ")
        verifica = all(char.isalpha() or char.isspace() for char in nome)
        if verifica and len(nome) > 0:
            nome = nome.strip()
            return nome
        print("Erro ... Digite apenas letras")
        
def validarTarja():
    """Validar o Tarja"""
    while True:
        tarja = input("Tarja: ")
        verifica = all(char.isalpha() or char.isspace() for char in tarja)
        if verifica and len(tarja) > 0:
            tarja = tarja.strip()
            return tarja
        print("Erro ... Digite apenas letras")
        
def validarDataVencimento():
    """Validar a Data de Vencimento"""
    while True:
        dataVencimento = input("Data de Vencimento (Ex: 04102021): ")
        if dataVencimento.isnumeric() and len(dataVencimento) == 8:
            return dataVencimento
        elif not dataVencimento.isnumeric():
            print("Erro ... Digite apenas números")
        else:
            print("Erro ... A data deve possuir 8 números")

def validarPreco():
    """Validar o Preco"""
    while True:
        preco = input("Preço: ")
        if preco.replace('.','',1).isnumeric():
            if float(preco) > 0:
                return preco
            else:
                print("Erro .. Informe um valor válido para o preço")
        else:
            print("Erro ... Digite apenas números")
       
def validarQuantidade():
    """Validar a Quantidade"""
    while True:
        quant = input("Quantidade: ")
        if quant.isnumeric():
            if int(quant) > 0:
                return quant
            else:
                print("Erro .. Informe um valor maior que zero para a quantidade")
        else:
            print("Erro ... Digite apenas números")     


def validarSubtipo():
    """Validar o Subtipo"""
    while True:
        subtipo = input("Subtipo:\n [1] Analgésico\n [2] Antibiótico\n [3] Antiflamatorio\n >> ")
        if subtipo.isnumeric():
            if int(subtipo) > 0 and int(subtipo) < 4:
                if int(subtipo) == 1:
                    return "Analgésico"
                elif int(subtipo) == 2:
                    return "Antibiótico"
                elif int(subtipo) == 3:
                    return "Antiflamatório"
            else:
                print("Erro ... Digite uma das opções acima ...")
        elif not subtipo.isnumeric():
            print("Erro ... Digite apenas números")     
