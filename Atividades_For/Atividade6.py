def sem_vogal(texto):
    vogais = "aAeEiIoOuU"
    nova_string = ""
    
    for i in texto:
        if i not in vogais:
            nova_string += i
        
    return nova_string

print(sem_vogal("Eu Acho Que O Felipe E Gay E Viado"))
