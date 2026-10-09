chamados = [
  { "id": 1, "titulo": "Erro no login", "prioridade": "Alta", "status": "Aberto", "usuario": "Ana Silva" },
  { "id": 2, "titulo": "Tela branca no app", "prioridade": "Crítica", "status": "Aberto", "usuario": "Bruno Costa" },
  { "id": 3, "titulo": "Atualizar cadastro", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Carlos Souza" },
  { "id": 4, "titulo": "Boleto não gerado", "prioridade": "Média", "status": "Aberto", "usuario": "Daniela Lima" },
  { "id": 5, "titulo": "Botão quebrado", "prioridade": "Baixa", "status": "Aberto", "usuario": "Eduardo Rocha" },
  { "id": 6, "titulo": "Lentidão na busca", "prioridade": "Média", "status": "Em progresso", "usuario": "Fernanda Alves" },
  { "id": 7, "titulo": "Recuperar senha", "prioridade": "Alta", "status": "Aberto", "usuario": "Gabriel Santos" },
  { "id": 8, "titulo": "Erro no Pix", "prioridade": "Crítica", "status": "Aberto", "usuario": "Amanda Melo" },
  { "id": 9, "titulo": "Mudar foto de perfil", "prioridade": "Baixa", "status": "Fechado", "usuario": "Igor Ribeiro" },
  { "id": 10, "titulo": "Exportar PDF falhou", "prioridade": "Média", "status": "Aberto", "usuario": "Juliana Vieira" },
  { "id": 11, "titulo": "Carrinho esvaziando", "prioridade": "Alta", "status": "Em progresso", "usuario": "Lucas Martins" },
  { "id": 12, "titulo": "Cupom inválido", "prioridade": "Média", "status": "Aberto", "usuario": "Mariana Dias" },
  { "id": 13, "titulo": "Página 404 no FAQ", "prioridade": "Baixa", "status": "Aberto", "usuario": "Nicolas Ferreira" },
  { "id": 14, "titulo": "Atraso na entrega", "prioridade": "Alta", "status": "Aberto", "usuario": "Patricia Gomes" },
  { "id": 15, "titulo": "Email de boas-vindas", "prioridade": "Baixa", "status": "Fechado", "usuario": "Rodrigo Ramos" },
  { "id": 16, "titulo": "Estorno pendente", "prioridade": "Alta", "status": "Em progresso", "usuario": "Sabrina Oliveira" },
  { "id": 17, "titulo": "Alerta de segurança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Thiago Barbosa" },
  { "id": 18, "titulo": "Link quebrado no menu", "prioridade": "Baixa", "status": "Aberto", "usuario": "Vanessa Cunha" },
  { "id": 19, "titulo": "Nota fiscal sumiu", "prioridade": "Média", "status": "Aberto", "usuario": "Willian Cardoso" },
  { "id": 20, "titulo": "Modo escuro travando", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Yasmim Lopes" },
  { "id": 21, "titulo": "Erro na API de CEP", "prioridade": "Alta", "status": "Aberto", "usuario": "Arthur Antunes" },
  { "id": 22, "titulo": "Notificação duplicada", "prioridade": "Baixa", "status": "Aberto", "usuario": "Beatriz Mendes" },
  { "id": 23, "titulo": "Sessão expirando rápido", "prioridade": "Média", "status": "Em progresso", "usuario": "Caio Nogueira" },
  { "id": 24, "titulo": "Erro no cartão de crédito", "prioridade": "Crítica", "status": "Aberto", "usuario": "Diana Prince" },
  { "id": 25, "titulo": "Traduzir termo em inglês", "prioridade": "Baixa", "status": "Fechado", "usuario": "Elton John" },
  { "id": 26, "titulo": "Chat de suporte offline", "prioridade": "Alta", "status": "Aberto", "usuario": "Fábio Assunção" },
  { "id": 27, "titulo": "Upload de comprovante", "prioridade": "Média", "status": "Aberto", "usuario": "Gisele Bündchen" },
  { "id": 28, "titulo": "Histórico sumiu", "prioridade": "Alta", "status": "Em progresso", "usuario": "Heitor Villa" },
  { "id": 29, "titulo": "Termos de uso desatualizados", "prioridade": "Baixa", "status": "Aberto", "usuario": "Isabela Garcia" },
  { "id": 30, "titulo": "Erro 500 no checkout", "prioridade": "Crítica", "status": "Aberto", "usuario": "Jorge Ben" },
  { "id": 31, "titulo": "Ajustar margem do header", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Karina Bacchi" },
  { "id": 32, "titulo": "Filtro por data quebrado", "prioridade": "Média", "status": "Aberto", "usuario": "Leonardo Dicaprio" },
  { "id": 33, "titulo": "Assinatura não renovada", "prioridade": "Alta", "status": "Aberto", "usuario": "Marta Vieira" },
  { "id": 34, "titulo": "Áudio do vídeo não funciona", "prioridade": "Média", "status": "Aberto", "usuario": "Neymar Junior" },
  { "id": 35, "titulo": "Atualizar política de privacidade", "prioridade": "Baixa", "status": "Fechado", "usuario": "Otávio Mesquita" },
  { "id": 36, "titulo": "Queda do servidor interno", "prioridade": "Crítica", "status": "Em progresso", "usuario": "Paula Toller" },
  { "id": 37, "titulo": "Convite por email falhou", "prioridade": "Baixa", "status": "Aberto", "usuario": "Quintino Aires" },
  { "id": 38, "titulo": "Extrato em branco", "prioridade": "Alta", "status": "Aberto", "usuario": "Renata Vasconcellos" },
  { "id": 39, "titulo": "ícone errado no painel", "prioridade": "Baixa", "status": "Aberto", "usuario": "Samuel Rosa" },
  { "id": 40, "titulo": "Duplicidade de cobrança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Tais Araújo" },
  { "id": 41, "titulo": "Validação de CNPJ", "prioridade": "Média", "status": "Em progresso", "usuario": "Umberto Eco" },
  { "id": 42, "titulo": "Mensagem de erro confusa", "prioridade": "Baixa", "status": "Aberto", "usuario": "Valéria Valenssa" },
  { "id": 43, "titulo": "Problema com fonte negrito", "prioridade": "Baixa", "status": "Aberto", "usuario": "Wagner Moura" },
  { "id": 44, "titulo": "Links de redes sociais fora do ar", "prioridade": "Média", "status": "Aberto", "usuario": "Xuxa Meneghel" },
  { "id": 45, "titulo": "Sem sinal de geolocalização", "prioridade": "Alta", "status": "Em progresso", "usuario": "Yuri Gagarin" },
  { "id": 46, "titulo": "Página recarregando sozinha", "prioridade": "Alta", "status": "Aberto", "usuario": "Zeca Pagodinho" },
  { "id": 47, "titulo": "Gráfico de vendas travado", "prioridade": "Média", "status": "Aberto", "usuario": "Alinne Moraes" },
  { "id": 48, "titulo": "Impossível remover endereço", "prioridade": "Média", "status": "Em progresso", "usuario": "Beto Jamaica" },
  { "id": 49, "titulo": "Vazamento de memória na aba", "prioridade": "Crítica", "status": "Aberto", "usuario": "Cláudia Raia" },
  { "id": 50, "titulo": "Ajustar alinhamento do rodapé", "prioridade": "Baixa", "status": "Fechado", "usuario": "Dado Dolabella" }
]

def pesquisar_usuario():
    print("===== PESQUISAR POR USUARIOS =====")
    pergunta = input("Que usuario você procura?: ").lower() .strip()

    for chamado in chamados:
        if chamado["usuario"].lower() == pergunta:
            
            print(f"ID:{chamado['id']} | Titulo: {chamado['titulo']} | Prioridade: {chamado['prioridade']} | Status: {chamado['status']} | Usuario: {chamado['usuario']}")
            

def pesquisar_prioridade():
    print("===== PESQUISAR POR PRIORIDADES =====")
    pergunta = input("Por qual prioridade você está procurando?: (Crítica, Alta, Média, Baixa) ").lower() .strip()

    for chamado in chamados:
        if chamado["prioridade"].lower() == pergunta:
            print (f"ID: {chamado['id']} | Titulo: {chamado['titulo']} | Prioridade: {chamado['prioridade']}")

def pesquisar_status():
    print("===== PESQUISANDO STATUS =====")
    pergunta = input("Por qual Status você está procurando?: (Aberto, Em Progresso, Fechado) ").lower() .strip()

    for chamado in chamados:
        if chamado["status"].lower() == pergunta:
            print (f"ID: {chamado['id']} | Titulo: {chamado['titulo']} | Status: {chamado['status']}")
    
def pesquisar_urgentes():
    print("===== CHAMADAS URGENTES =====")
    for chamado in chamados:
        if chamado ["status"] == "Aberto" and chamado ["prioridade"] == "Crítica":
            print(f"ID: {chamado['id']} | Titulo: {chamado['titulo']} | Usuario: {chamado['usuario']} | Prioridade: {chamado['prioridade']} | Status: {chamado['status']}")
 
def adicionar_chamado():
    print("===== ADICIONAR CHAMADA =====")
    pergunta_titulo = input("Qual chamada você gostaria de adicionar?: ")
    pergunta_prioridade = input("Qual a prioridade da adicionar?: ")
    pergunta_usuario = input("Qual o usuario?: ")
    novo_id = chamados[-1]['id'] + 1 if chamados else 1

    cadastrar = {
        "id": novo_id,
        "titulo": pergunta_titulo,
        "prioridade": pergunta_prioridade,
        "status": "Aberto",
        "usuario": pergunta_usuario
    }
    chamados.append(cadastrar)
    print(chamados)

def resolver_chamada():
    while True:
        print("===== CHAMADOS EM ANDAMENTO (EM PROGRESSO) =====")
        chamados_em_progresso = False

        for chamado in chamados:
            if chamado['status'].lower() == "em progresso":
                print(f"Chamados Em Progresso: {chamado['titulo']} | {chamado['status']} Usuario: {chamado['usuario']}")
                chamados_em_progresso = True
        if not chamados_em_progresso:
            print("Não tem Nenhum chamado 'Em progresso' no momento").lower() .strip()
            print("Retornando ao Menu...")
            break

        pergunta = input("\nQual usuário você gostaria de resolver a chamada?: ").lower().strip()
        encontrado = False
        

        for chamado in chamados:
            if chamado['usuario'].lower() == pergunta and chamado['status'].lower() == "em progresso":
                chamado['status'] = "Fechado"
                print(f"-> O Chamado {chamado['id']} ('{chamado['titulo']}') ('{chamado['usuario']}) alterado para Fechado!")
                encontrado = True
                
        if not encontrado:
            print(f"Nenhum chamado 'Em progresso' foi encontrado para o usuário '{pergunta}'.")
        
        
        continuar = input("\nGostaria de resolver chamados de mais algum usuário? (sim/não): ").lower().strip()
        
        if continuar == "não" or continuar == "nao":
            print("Saindo da resolução de chamados...")
            break

def fechar_chamada():
    while True:

        print("\n===== CHAMADOS ABERTOS =====")
        tem_abertos = False
        for chamado in chamados:
            if chamado["status"].lower() == "aberto":
                print(f"ID: {chamado['id']} | Usuário: {chamado['usuario']} | Título: {chamado['titulo']} | Prioridade: {chamado['prioridade']} | Status: {chamado['status']}")
                tem_abertos = True
        
        if not tem_abertos:
            print("Não há nenhum chamado 'Aberto' no momento.")
            print("Retornando ao menu principal...")
            break
        print("==============================")

       
        pergunta_id = input("\nQual o ID do chamado que você deseja fechar?: ").strip()
        

        if not pergunta_id.isdigit():
            print("Por favor, digite um número de ID válido.")
            continue
            
        id_busca = float(pergunta_id)
        encontrado = False


        for chamado in chamados:
            if chamado["id"] == id_busca:
                encontrado = True
                if chamado["status"].lower() == "fechado":
                    print(f"O chamado ID {id_busca} já está Fechado!")
                else:
                    chamado["status"] = "Fechado"
                    print(f"-> Sucesso! Chamado ID {id_busca} alterado para Fechado.")
                break
        
        if not encontrado:
            print(f"Nenhum chamado com o ID {id_busca} foi encontrado.")


        continuar = input("\nGostaria de fechar mais algum chamado? (sim/não): ").lower().strip()
        if continuar in ["não", "nao"]:
            print("Voltando ao Menu")
            break
        




        
            





while True:

    print("1 - Pequisar por Usuário")
    print("2 - Pequisar por Prioridade")
    print("3 - Pequisar por Status")
    print("4 - Chamadas urgentes (Critica e Abertos)")
    print("5 - Adicionar Chamado ")
    print("6 - Resolver Chamada")
    print("7 - Fechar chamada")
    print("0 - Sair")

    opcao = input("Qual opção você deseja?: ")

    if opcao == "1":
        pesquisar_usuario()

    elif opcao == "2":
        pesquisar_prioridade()
   
    elif opcao == "3":
        pesquisar_status()
    
    elif opcao == "4":
        pesquisar_urgentes()

    elif opcao == "5":
        adicionar_chamado()
    
    elif opcao == "6":
        resolver_chamada()

    elif opcao == "7":
        fechar_chamada()

    elif opcao == "0":
        print("==== Saindo do Sistema.... ====")
        break
