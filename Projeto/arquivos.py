# -*- coding: utf-8 -*-

import os.path

arquivoCliente = "Projeto/clientes.txt"
arquivoMedicamento = "Projeto/medicamentos.txt"
arquivoVenda = "Projeto/vendas.txt"
    
def verificaExistenciaDoAquivo(nomeArquivo):
    if (not os.path.isfile(nomeArquivo)):
        arquivo = open(nomeArquivo, "a")
        arquivo.close()

def lerArquivoMedicamento():
    verificaExistenciaDoAquivo(arquivoMedicamento)
    
    listaMedicamentos = {}
    arquivo = open(arquivoMedicamento, "r")
    for linha in arquivo:
        linha = linha.strip().split("|")
        listaMedicamentos[linha[0]] = linha[1:]
    arquivo.close()
    
    return listaMedicamentos

def salvarMedicamento(listaMedicamentos, ium):
    arquivo = open(arquivoMedicamento, "a")
    for index in range(len(listaMedicamentos[ium])):
        if index == 0:
            arquivo.write(ium + "|" + listaMedicamentos[ium][index] + "|")  
        elif index == len(listaMedicamentos[ium]) - 1:
            arquivo.write(listaMedicamentos[ium][index] + "\n")   
        else:
            arquivo.write(listaMedicamentos[ium][index] + "|")
        arquivo.flush()
    arquivo.close()

def atualizarMedicamento(listaMedicamentos):
    arquivo = open(arquivoMedicamento, "w")
    for ium, [nome, tarja, vencimento, preco, quantidade, subtipo] in listaMedicamentos.items():
        arquivo.write(ium + "|" + nome + "|" + tarja + "|" + vencimento + "|" + preco + "|" + quantidade + "|" + subtipo + "\n")  
        arquivo.flush()
    arquivo.close()
    
    
def lerArquivoCliente():
    verificaExistenciaDoAquivo(arquivoCliente)
        
    listaArquivoCliente = {}
    arquivo = open(arquivoCliente, "r")
    for linha in arquivo:
        linha = linha.strip().split("|")
        listaArquivoCliente[linha[0]] = linha[1:]
    arquivo.close()
    
    return listaArquivoCliente
   
def salvarCliente(listaCliente, cpf):
    arquivo = open(arquivoCliente, "a")
    for index in range(len(listaCliente[cpf])):
        if index == 0:
            arquivo.write(cpf + "|" + listaCliente[cpf][index] + "|")  
        elif index == len(listaCliente[cpf]) - 1:
            arquivo.write(listaCliente[cpf][index] + "\n")   
        else:
            arquivo.write(listaCliente[cpf][index] + "|")
        arquivo.flush()
    arquivo.close()
   
def atualizarCliente(listaCliente):
    arquivo = open(arquivoCliente, "w")
    for cpf, [nome, dataNascimento, telefone, rua, numero, bairro] in listaCliente.items():
        arquivo.write(cpf + "|" + nome + "|" + dataNascimento + "|" + telefone + "|" + rua + "|" + numero + "|" + bairro + "\n")  
        arquivo.flush()
    arquivo.close()


def lerArquivoVendas():
    verificaExistenciaDoAquivo(arquivoVenda)
    
    listaArquivoVenda = {}
    arquivo = open(arquivoVenda, "r")
    for linha in arquivo:
        linha = linha.strip().split("|")
        listaArquivoVenda[linha[0]] = linha[1:]
    arquivo.close()
    
    return listaArquivoVenda
    
    
def salvarVenda(listaVendas, identificador):
    arquivo = open(arquivoVenda, "a")
    for index in range(len(listaVendas[identificador])):
        if index == 0:
            arquivo.write(identificador + "|" + listaVendas[identificador][index] + "|")  
        elif index == len(listaVendas[identificador]) - 1:
            arquivo.write(listaVendas[identificador][index] + "\n")   
        else:
            arquivo.write(listaVendas[identificador][index] + "|")
        arquivo.flush()
    arquivo.close()
    
def limpaTerminal():
    os.system("cls")        
        