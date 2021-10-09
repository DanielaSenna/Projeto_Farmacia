import cliente
import arquivos
import medicamento
import time
import venda


def menuPrincipal():
    arquivos.limpaTerminal()
    listaClientes  = arquivos.lerArquivoCliente()
    listaMedicamentos = arquivos.lerArquivoMedicamento()
    listaVendas = arquivos.lerArquivoVendas()
    
    opcao = 0
    while opcao != 5:
        print("_"*50)    
        print("\n{}".format("SISTEMA PARA GERENCIAMENTO DE UMA FARMÁCIA".center(50)))
        print("_"*50)
        print("[1] Medicamentos")
        print("[2] Clientes")
        print("[3] Realizar uma Venda")
        print("[4] Histórico de Vendas")
        print("[5] Sair")
        print("_"*50)  
        
        opcao = input("Informe uma opção: ")
        if opcao.isnumeric():
            opcao = int(opcao)
            if opcao == 1:
                arquivos.limpaTerminal()
                medicamento.menuMedicamentos(listaMedicamentos)
            elif opcao == 2:
                arquivos.limpaTerminal()
                cliente.menuClientes(listaClientes)
            elif opcao == 3:
                venda.menuVenda(listaClientes, listaMedicamentos, listaVendas)
                arquivos.limpaTerminal()
            elif opcao == 4:
                venda.historicoVendas(listaVendas)
                arquivos.limpaTerminal()
            elif opcao == 5:
                print("Saindo do Sistema ... Até breve!")
            else:
                print("Opção Inválida ... Digite uma opção válida")
                time.sleep(1.2)
                arquivos.limpaTerminal()
        else:
            print("Opção Inválida ... Digite uma opção válida")
            time.sleep(1.2)
            arquivos.limpaTerminal()

if __name__ == '__main__':
    menuPrincipal()