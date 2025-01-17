# Desafio 1: Soma com Índice fixo
print("\nDesafio 1: Soma com Índice fixo")
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print("O valor de SOMA:", SOMA)

# ----------------------------------------------
print("\n--- Próximo Desafio ---\n")  # Indicação de próximo desafio

# Desafio 2: Verificar se um número pertence à sequência de Fibonacci
print("Desafio 2: Verificar se um número pertence à sequência de Fibonacci")

def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

# Entrada do valor
numero = int(input("Informe um número: "))

# Verifica se está na sequência
mensagem = (
    "pertence à sequência de Fibonacci."
    if is_fibonacci(numero)
    else "NÃO pertence à sequência de Fibonacci."
)
print(f"O número {numero} {mensagem}")

# ----------------------------------------------
print("\n--- Próximo Desafio ---\n")  # Indicação de próximo desafio

# Desafio 3: Análise de faturamento mensal
print("\nDesafio 3: Análise de faturamento mensal")

import json

# Dados do faturamento mensal
dados_json = """
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]
"""

# Carrega os dados JSON
dados = json.loads(dados_json)

# Filtra dias com faturamento maior que zero
faturamento = [dia["valor"] for dia in dados if dia["valor"] > 0]

# Calcula o menor e maior faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calcula a média mensal
media_mensal = sum(faturamento) / len(faturamento)

# Calcula o número de dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

# Exibe os resultados
print(f"Menor faturamento: {menor_faturamento:.2f}")
print(f"Maior faturamento: {maior_faturamento:.2f}")
print(f"Media mensal: {media_mensal:.2f}")
print(f"Dias com faturamento acima da media: {dias_acima_da_media}")

# ----------------------------------------------
print("\n--- Próximo Desafio ---\n")  # Indicação de próximo desafio

# Desafio 4: Faturamento de cada estado
print("\nDesafio 4: Faturamento de cada estado")

# Faturamento de cada estado
faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o valor total de faturamento
total_faturamento = sum(faturamento_estado.values())

# Verifique o total de faturamento
print(f"Total de faturamento: R${total_faturamento:.2f}")

# Calcula o percentual de representação de cada estado
percentuais = {}
for estado, faturamento in faturamento_estado.items():
    percentual = (faturamento / total_faturamento) * 100
    percentuais[estado] = percentual

# Exibe o valor total e os percentuais arredondados
print(f"\nValor total do faturamento: R${total_faturamento:.2f}")
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
    
    
    
    # ----------------------------------------------
print("\n--- Próximo Desafio ---\n")  # Indicação de próximo desafio


# Entrada de string
entrada_string = input("Digite uma string para inverter: ")

# Inicializando a string invertida como vazia
string_invertida = ""

# Percorrendo a string de trás para frente
for i in range(len(entrada_string) - 1, -1, -1):
    string_invertida += entrada_string[i]

# Exibe a string invertida
print(f"String invertida: {string_invertida}")

