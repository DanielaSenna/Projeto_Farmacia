import cliente
import medicamento
import arquivos
import time
import pandas as pd

def menuVenda(listaClientes, listaMedicamentos, listaVendas):
    if len(listaClientes) == 0:
        print("Nenhum Cliente foi Cadastrado ...")
        time.sleep(1.2)
    else:
        cpf = cliente.validarCPF()
        if cpf in listaClientes:
            realizarVenda(listaMedicamentos, listaVendas, cpf)
        else:
            print("  Este CPF não está cadastrado...")
            time.sleep(1.2)

def realizarVenda(listaMedicamento, listaVendas, cpf):
    if len(listaMedicamento) > 0:
        condicaoParada = True
        while condicaoParada:
            ium = medicamento.validarIUM()
            
            if ium in listaMedicamento:
                concluirVenda(listaMedicamento, listaVendas, cpf, ium)
                condicaoParada = False
            else:
                print("  Não existe medicamento cadastrado com esse IUM ...")
    else:
        print("  Não existe Medicamentos Cadastrados para realizar a Venda...")
        time.sleep(1.2)
        
def concluirVenda(listaMedicamento, listaVendas, cpf, ium):
    if int(listaMedicamento[ium][4]) > 0:
        condicaoParada = True
        while condicaoParada:
            quantidade = medicamento.validarQuantidade()
    
            if int(quantidade) > 0 and int(quantidade) <= int(listaMedicamento[ium][4]):
                precoTotal = int(quantidade) * float(listaMedicamento[ium][3])
                print("="*10, "NOTA FISCAL", "="*10)
                print(" CPF: {}\n Medicamento: {}\n Quantidade: {}\n Preço Total: {}".format(cpf, listaMedicamento[ium][0], quantidade, precoTotal))
                
                parada = True
                while parada:
                    opcao = input("Deseja Confirmar a Venda (S/N)? ")
                    
                    if opcao == "S":
                        identificador = str(len(listaVendas))
                        listaVendas[identificador] = [cpf, ium, quantidade, str(precoTotal)]
                        arquivos.salvarVenda(listaVendas, identificador)
                        
                        quantidadeRestante = int(listaMedicamento[ium][4]) - int(quantidade)
                        listaMedicamento[ium][4] = str(quantidadeRestante)
                        arquivos.atualizarMedicamento(listaMedicamento)
                        print("Venda realizada com Sucesso ...")
                        time.sleep(1.2)
                        parada = False
                    elif opcao == "N": 
                        parada = False
                    else:
                        print("    Erro ... Digite S ou N\n")
                
                condicaoParada = False
            else:
                print("  Existe apenas {} disponíveis.".format(listaMedicamento[ium][4]))
      
    else:
        print("  O Medicamento necessita de Reposição")
        time.sleep(1.2)

def historicoVendas(listaVendas):
    if len(listaVendas) == 0:
        print("Nenhum Medicamento foi Vendido ...")
        time.sleep(1.2)
    else:
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        print("-"*100) 
        tabela = pd.DataFrame.from_dict(listaVendas, orient="index", columns=["CPF", "IUM DO MEDICAMENTO", "QUANTIDADE", "PREÇO TOTAL"])
        print(tabela) 
        print("-"*100) 
        
        parada = True
        while parada:
            opcao = input("Deseja retornar ao Menu Principal (S para SIM)? ")
            
            if opcao == "S":
                parada = False
            else:
                print("    Erro ... Digite S para retornar ao Menu\n")
