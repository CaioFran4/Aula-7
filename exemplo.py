valores = [20,71,100,30]
alunos = ["Ana", "Hugo", "Mariana", "Pedro", "Ana Paula"]

produto = "Mouse Gamer WIFI"


print("---- Produtos ----")
procurar_produto = input("Qual produto você procura?: ")
if "Mouse".lower() in produto.lower():
    print("Produto Encontrado")
    print (produto)

else:
    print("Produto não encontrado")

def dobrar(valor):
    resultado = valor * 2
    return resultado
valores_novos = []

for valor in valores:
    valores_novos.append(dobrar(valor))

print(valores_novos)
print(valores)

print("---- Alunos ----")
aluno_procurado = input("Digite um nome...").lower() .strip()
alunos_encontrados = []
for aluno in alunos:
    alunos_encontrados .append(aluno)
print(alunos_encontrados)
