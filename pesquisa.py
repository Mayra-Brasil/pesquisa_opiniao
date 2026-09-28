# Pesquisa de opinião quantitativa

# Atividade da agenda 8 em Desenvolvimento de Sistemas


# Entrada de dados da pesquisa

print("Prezado entrevistado, gostariamos de saber mais sobre você e sua opinião, por favor peço que responda às perguntas a seguir!")

EXCELENTE = 0
BOM = 0
RUIM = 0



for _ in range(50):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = input("Escolha uma nota para nosso atendimento sendo \"EXCELENTE\", \"BOM\" ou \"RUIM\": ").upper()
 # Processamento de dados da pesquisa e contabilização das respostas
    if opiniao == "EXCELENTE":
        EXCELENTE += 1
    elif opiniao == "BOM":
        BOM += 1
    elif opiniao == "RUIM":
        RUIM += 1
    else:
        print("Opção inválida. Por favor, responda com EXCELENTE, BOM ou RUIM.")

# if e else para validar a entrada de dados e contabilizar as respostas usando "==" pois puxará o valor da variavel opiniao e comparará com a string digitada pelo usuário, caso seja igual, a variável será incrementada em 1.
# variavel BOM, EXCELENTE e RUIM para contabilizar as respostas utilizando o operador de incremento += 1, lendo se igual e/ou mais de uma vez tendo a variavel inserida pelo usuario no loop for.





# Resultados da pesquisa e sáida de dados

print(f"Quantidade de pessoas que avaliaram o atendimento como EXCELENTE: {EXCELENTE}")
print(f"Quantidade de pessoas que avaliaram o atendimento como BOM: {BOM}")
print(f"Quantidade de pessoas que avaliaram o atendimento como RUIM: {RUIM}")

# print f"" dentro dos parenteses para exibir uma variavel dentro de uma string/frase, utilizando a sintaxe f"{}" para interpolar/incluir as variáveis e exibir os resultados da pesquisa de opinião quantitativa.