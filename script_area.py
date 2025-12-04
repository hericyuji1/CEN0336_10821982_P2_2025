#Programa para calcular a média de uma disciplina com 10 notas
#Inicializa as variáveis, onte TOTAL é o acumulador das notas e CONTADOR_NOTAS é o contador de quantas notas foram lançadas

TOTAL = 0
CONTADOR_NOTAS = 0

#Loop para entrada de 10 notas

while CONTADOR_NOTAS < 10:   # Condiciona que enquanto o contador for menor que 10
    try: #pede para o código tentar fazer as seguintes condicionantes:
        # -Solicitar a entrada da nota
        nota = float(input(f"Digite a nota {CONTADOR_NOTAS + 1}: "))
        
        # Controle da entrada: verifica se a nota está entre 0 e 10 e printa uma mensagem de erro caso a nota esteja fora dos padrões desejados
        if nota < 0 or nota > 10:
            print("Erro: a nota deve estar entre 0 e 10. Tente novamente.")
            continue  # Volta para pedir a nota novamente
        
        # Soma a nota ao total do valor de notas
        TOTAL += nota
        
        # Adiciona mais uma nota inserida ao contador de notas
        CONTADOR_NOTAS += 1
    
    except ValueError:
        # Tratamento de erro caso o usuário não digite um número válido
        print("Erro: entrada inválida. Digite apenas números.")
        continue

# Calcula a média da disciplina.
media = TOTAL / 10

# Exibe o resultado da média das notas 
print(f"A média da disciplina é: {media:.2f}")

# OBS: Caso quisesse utilizar esse código em uma disciplina com menos notas ao longo do semestre, seria necessário somente alterar o valor da linha 09  (CONTADOR_NOTAS <10) para o número de notas da disciplina.  
