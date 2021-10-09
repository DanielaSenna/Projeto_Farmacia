# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:52:03 2021

@author: daany
"""

import pandas as pd
import time
import arquivos


def menuClientes(listaCliente):
    opcao = 0
    while opcao != 6:
        print("_"*50)    
        print("\n{}".format("SISTEMA PARA GERENCIAMENTO DE UMA FARMÁCIA".center(50)))
        print("\n{}".format("***CLIENTES***".center(50)))
        print("_"*50)
        print("\n[1] Cadastrar um Cliente")
        print("[2] Procurar um Cliente")
        print("[3] Excluir um Cliente")
        print("[4] Listar os Clientes")
        print("[5] Alterar Dados do Cliente")
        print("[6] Retornar ao Menu Principal")
        
        opcao = input("Informe uma opção: ")
        if opcao.isnumeric():
            opcao = int(opcao)
            if opcao == 1:
                cadastrarCliente(listaCliente)
                time.sleep(1)
                arquivos.limpaTerminal()
            elif opcao == 2:
                buscarCliente(listaCliente)
                arquivos.limpaTerminal()
            elif opcao == 3:
                excluirCliente(listaCliente)
                arquivos.limpaTerminal()
            elif opcao == 4:
                listarClientes(listaCliente)
                arquivos.limpaTerminal()
            elif opcao == 5:
                alterarCliente(listaCliente)
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
            

def cadastrarCliente(listaCliente):
    print("{}".format("=====INFORMAÇÕES DO CLIENTE====="))
    print("***DADOS PESSOAIS***")
    
    cpf = validarCPF()
        
    if cpf in listaCliente:
        print("Este CPF já foi cadastrado ...")
    else:
        nome = validarNome()
        dataNascimento = validarDataNascimento()
        telefone = validarTelefone()
        
        print("\n***ENDEREÇO***")
        rua = validarRua()
        numero = validarNumero()
        bairro = validarBairro()        
                    
        listaCliente[cpf] = [nome, dataNascimento, telefone, rua, numero, bairro]
        arquivos.salvarCliente(listaCliente, cpf)
        print("Cliente Cadastrado com Sucesso !")
        
        
def buscarCliente(listaCliente):
    if len(listaCliente) == 0:
        print("Nenhum Cliente foi Cadastrado ...")
        time.sleep(1.2)
    else:
        opcao = 0
        print("#"*50)
        print("PROCURAR CLIENTE POR: \n [1] CPF\n [2] Nome\n [3] Retornar ao Menu Clientes")
        while opcao != 3:
            opcao = input("Informe uma opção: ")
            if opcao.isnumeric():
                opcao = int(opcao)
                if opcao == 1:
                    buscarClientePorCPF(listaCliente)
                elif opcao == 2:
                    buscarClientePorNome(listaCliente)
                elif opcao == 3:
                    pass
                else:
                    print("Opção Inválida ... Digite uma opção válida")
            else:
                print("Opção Inválida ... Digite uma opção válida")
               
def buscarClientePorCPF(listaCliente):
    cpf = validarCPF()
        
    if cpf in listaCliente:
        print("="*50)
        print(" CPF: {}\n Nome: {}\n Data de Nascimento: {}\n Telefone: {}\n Rua: {}\n Número: {}\n Bairro: {} ".format(cpf, listaCliente[cpf][0], listaCliente[cpf][1], listaCliente[cpf][2], listaCliente[cpf][3], listaCliente[cpf][4], listaCliente[cpf][5]))
                
    else:
        print("   Este CPF não está cadastrado ...\n")
                    
def buscarClientePorNome(listaCliente):
    nomeCliente = validarNome()
    
    quantNomes = 0
    for cpf, [nome, dataNascimento, telefone, rua, numero, bairro] in listaCliente.items():
        if nome == nomeCliente:
            print("="*50)
            print(" CPF: {}\n Nome: {}\n Data de Nascimento: {}\n Telefone: {}\n Rua: {}\n Número: {}\n Bairro: {} ".format(cpf, nome, dataNascimento, telefone, rua, numero, bairro))
            quantNomes += 1
                        
    if quantNomes == 0:
        print("    Não existe nenhum cliente com o nome {}\n".format(nomeCliente))

def excluirCliente(listaCliente):
    if len(listaCliente) == 0:
        print("Nenhum Cliente foi Cadastrado ...")
        time.sleep(1.2)
    else:
        """Validar o CPF"""
        parada = True
        while parada:
            cpf = input("Informe o CPF do Cliente a ser Excluído ou S para retornar ao menu: ")
            
            if cpf == "S":
                parada = False
            else:
                if cpf.isnumeric() and len(cpf) == 11:
                    parada = False
                else:
                    print("Erro ... O CPF possui 11 números")
        
        if cpf in listaCliente:
            del listaCliente[cpf]
            arquivos.atualizarCliente(listaCliente)
            print("Cliente Excluído com Sucesso !")
            time.sleep(1.2)
        elif cpf.isnumeric():
            print("  Este CPF não está cadastrado ...")
            time.sleep(1.2)


def listarClientes(listaCliente):
    if len(listaCliente) == 0:
        print("Nenhum Cliente foi Cadastrado ...")
        time.sleep(1.2)
    else:
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        print("-"*100) 
        tabela = pd.DataFrame.from_dict(listaCliente, orient="index", columns=["NOME", "DATA DE NASCIMENTO", "TELEFONE", "RUA", "NÚMERO", "BAIRRO"])
        print(tabela) 
        print("-"*100) 
        
        
        parada = True
        while parada:
            opcao = input("Deseja retornar ao Menu Clientes (S para SIM)? ")
            
            if opcao == "S":
                parada = False
            else:
                print("    Erro ... Digite S para retornar ao Menu\n")

def alterarCliente(listaCliente):
    if len(listaCliente) == 0:
        print("Nenhum Cliente foi Cadastrado ...")
        time.sleep(1.2)
    else:
        print("="*50) 
        
        """Validar o CPF"""
        parada = True
        while parada:
            cpf = input("Informe o CPF do Cliente ou S para retornar ao menu: ")
            
            if cpf == "S":
                parada = False
            else:
                if cpf.isnumeric() and len(cpf) == 11:
                    parada = False
                else:
                    print("Erro ... O CPF possui 11 números")
        
        if cpf in listaCliente:
           
            print("="*50)
            print(" CPF: {}\n Nome: {}\n Data de Nascimento: {}\n Telefone: {}\n Rua: {}\n Número: {}\n Bairro: {} ".format(cpf, listaCliente[cpf][0], listaCliente[cpf][1], listaCliente[cpf][2], listaCliente[cpf][3], listaCliente[cpf][4], listaCliente[cpf][5]))
            print("="*50)
    
            print("O QUE DESEJA ALTERAR?")
            print(" [1] CPF\n [2] Nome\n [3] Data de Nascimento\n [4] Telefone\n [5] Rua\n [6] Número\n [7] Bairro\n [8] Retornar ao Menu Clientes")
            
            opcao = 0
            while opcao != 8:
                
                opcao = input("Informe uma opção: ")
                if opcao.isnumeric():
                    opcao = int(opcao)
                    
                    if opcao == 1:
                        novoCPF = validarCPF()
                        if novoCPF != cpf:
                            listaCliente[novoCPF] = listaCliente[cpf]
                            del listaCliente[cpf]
                            print("    CPF Alterado com Sucesso !\n")
                            
                                                
                    elif opcao == 2:
                        novoNome = validarNome()
                        listaCliente[cpf][0] = novoNome
                        print("    Nome Alterado com Sucesso !\n")
                        
                        
                    elif opcao == 3:
                        novaDataNascimento = validarDataNascimento()
                        listaCliente[cpf][1] = novaDataNascimento
                        print("   Data de Nascimento Alterada com Sucesso !\n")
                        
                    elif opcao == 4:
                        novoTelefone = validarTelefone()
                        listaCliente[cpf][2] = novoTelefone
                        print("    Telefone Alterado com Sucesso !\n")
                        
                    elif opcao == 5:
                        novaRua = validarRua()
                        listaCliente[cpf][3] = novaRua
                        print("    Rua Alterada com Sucesso !\n")
                        
                    elif opcao == 6:
                        novoNumero = validarNumero()
                        listaCliente[cpf][4] = novoNumero
                        print("    Número Alterado com Sucesso !\n")
                        
                    elif opcao == 7:
                        novoBairro = validarBairro()
                        listaCliente[cpf][5] = novoBairro
                        print("    Bairro Alterado com Sucesso !\n")
                        
                    elif opcao == 8:
                        #print("Retornado ao Menu Clientes")
                        pass
                    else:
                        print("Opção Inválida ... Digite uma opção válida")
                
                else:
                    print("Opção Inválida ... Digite uma opção válida")
                
                arquivos.atualizarCliente(listaCliente)
                
        elif cpf.isnumeric():
            print("  Este CPF não está cadastrado ...")
            time.sleep(1.2)
    
    

def validarCPF():
    """Validar o CPF"""
    while True:
        cpf = input("CPF: ")
        if cpf.isnumeric() and len(cpf) == 11:
            return cpf
        elif not cpf.isnumeric():
            print("Erro ... Digite apenas números")
        else:
            print("Erro ... O CPF possui 11 números")

def validarNome():
    """Validar o Nome"""
    while True:
        nome = input("Nome: ")
        verifica = all(char.isalpha() or char.isspace() for char in nome)
        if verifica and len(nome) > 0:
            nome = nome.strip()
            return nome
        print("Erro ... Digite apenas letras")
        

def validarDataNascimento():
    """Validar a Data de Nascimento"""
    while True:
        dataNascimento = input("Data de Nascimento (Ex: 04102021): ")
        if dataNascimento.isnumeric() and len(dataNascimento) == 8:
            return dataNascimento
        elif not dataNascimento.isnumeric():
            print("Erro ... Digite apenas números")
        else:
            print("Erro ... A data deve possuir 8 números")
 
def validarTelefone():
    """Validar o Telefone"""
    while True:
        telefone = input("Telefone Ex: 89993781234: ")
        if telefone.isnumeric() and len(telefone) == 11:
            return telefone
        elif not telefone.isnumeric():
            print("Erro ... Digite apenas números")
        else:
            print("Erro ... O telefone deve possui 11 números")
            

def validarRua():
    """Validar a Rua"""
    while True:
        rua = input("Rua: ")
        verifica = all(char.isalpha() or char.isspace() for char in rua)
        if verifica and len(rua) > 0:
            rua = rua.strip()
            return rua
        print("Erro ... Digite apenas letras")

def validarNumero():
    """Validar o Número da Rua"""
    while True:
        numero = input("Número: ")
        if numero.isnumeric():
            return numero
        print("Erro ... Digite apenas números")

def validarBairro():
    """Validar o Bairro"""
    while True:
        bairro = input("Bairro: ")
        verifica = all(char.isalpha() or char.isspace() for char in bairro)
        if verifica and len(bairro) > 0:
            bairro = bairro.strip()
            return bairro
        print("Erro ... Digite apenas letras")