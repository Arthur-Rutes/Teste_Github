# os = Operational Sistem
import os

# os.remove("atividades/arquivos/teste3.txt")

if os.path.exists("atividades/destruir"):
    print("Sim A Pasta Existe.")
    os.rmdir("atividades/destruir")
else:
    print("Pasta Inexistente.")
    os.mkdir("atividades/destruir")