#Crie Uma Função Que Simule Uma Lista De Tarefas Com Um Menu Simples:
#1.Adicionar Tarefa 2.Remover Tarefa 3.Mostrar Tarefas 4.Sair
#Use Um While Para Manter O Programa Funcionando Até O Usuário Escolher Sair.


tarefas = []
    
while True:
    print("===== Lista De Tarefas ===== \n1.Adicionar Tarefa \n2.Remover Tarefa \n3.Mostrar Tarefas \n4.Sair")
    fazer = int(input("(1)Adicionar(2)Remover(3)Mostrar(4)Sair: "))
    
    if fazer == 1:
        adicionar = input("O Que Desejas Fazer Hoje: ")
        tarefas.append(adicionar)
        print("Tarefa Adicionada")
        
    if fazer == 2:
        tarefas.remove
        
    if fazer == 3:
        print(f"Tarefas Atuais: \n{tarefas}")
        
    if fazer == 4:
        break
    
    
    #Necessita De Ser Corrigido
    
    