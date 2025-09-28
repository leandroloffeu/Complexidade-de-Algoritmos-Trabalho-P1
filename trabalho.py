"""
Trabalho de Complexidade de Algoritmos
Aluno: [Seu Nome]
Matéria: Complexidade de Algoritmos
Professor: [Nome do Professor]

Análise do algoritmo RecomendaFácil da empresa Vassouras Tech
"""

import matplotlib.pyplot as plt
import numpy as np

def algoritmo_recomenda_facil(historico_compras):
    """
    Algoritmo RecomendaFácil da Vassouras Tech
    
    Entrada: Lista com histórico de compras
    Saída: Número de recomendações
    """
    n = len(historico_compras)  # Tamanho do histórico
    recomendacoes = 2 * n - 1   # Fórmula do algoritmo
    return recomendacoes

def calcular_limite_n_10():
    """
    Calcula o limite quando n tende a 10
    """
    print("=== CÁLCULO DO LIMITE ===")
    print("Função: f(n) = 2n - 1")
    print("Queremos saber: lim f(n) quando n → 10")
    print()
    
    # Substituindo n = 10 na função
    n = 10
    limite = 2 * n - 1
    print(f"f(10) = 2(10) - 1 = {limite}")
    print(f"Portanto: lim f(n) = {limite} quando n → 10")
    print()
    
    return limite

def analisar_complexidade():
    """
    Analisa a complexidade do algoritmo
    """
    print("=== ANÁLISE DE COMPLEXIDADE ===")
    print("Função: f(n) = 2n - 1")
    print()
    print("Para analisar a complexidade, vamos ver como a função cresce:")
    print()
    
    # Testando com diferentes valores de n
    valores_n = [1, 5, 10, 50, 100, 1000]
    
    print("n\t| f(n) = 2n-1")
    print("-" * 20)
    for n in valores_n:
        f_n = 2 * n - 1
        print(f"{n}\t| {f_n}")
    
    print()
    print("OBSERVAÇÕES:")
    print("• A função cresce linearmente (proporcionalmente a n)")
    print("• Quando n dobra, f(n) também dobra")
    print("• Isso significa que a complexidade é O(n)")
    print("• O(n) é uma complexidade linear - boa para algoritmos")

def criar_grafico():
    """
    Cria gráfico da função f(n) = 2n - 1
    """
    print("=== CRIANDO GRÁFICO ===")
    
    # Valores de n de 1 a 20
    n = np.arange(1, 21)
    f_n = 2 * n - 1
    
    # Criar o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(n, f_n, 'b-o', linewidth=2, markersize=4, label='f(n) = 2n - 1')
    
    # Destacar o ponto n = 10
    plt.plot(10, 19, 'ro', markersize=8, label='n = 10, f(10) = 19')
    
    # Configurar o gráfico
    plt.xlabel('Número de compras anteriores (n)')
    plt.ylabel('Número de recomendações')
    plt.title('Algoritmo RecomendaFácil - Função f(n) = 2n - 1')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Adicionar anotações
    plt.annotate('Limite: f(10) = 19', 
                xy=(10, 19), 
                xytext=(12, 25),
                arrowprops=dict(arrowstyle='->', color='red'))
    
    plt.tight_layout()
    plt.savefig('grafico.png', dpi=150)
    plt.show()
    
    print("Gráfico salvo como 'grafico.png'")

def exemplo_pratico():
    """
    Mostra exemplos práticos do algoritmo
    """
    print("=== EXEMPLOS PRÁTICOS ===")
    print()
    
    # Exemplos de históricos de compras
    exemplos = [
        ("João", [1, 2, 3]),  # 3 compras
        ("Maria", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),  # 10 compras
        ("Pedro", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])  # 15 compras
    ]
    
    print("Simulando o algoritmo com diferentes clientes:")
    print()
    
    for nome, historico in exemplos:
        recomendacoes = algoritmo_recomenda_facil(historico)
        print(f"Cliente: {nome}")
        print(f"Histórico: {len(historico)} compras")
        print(f"Recomendações geradas: {recomendacoes}")
        print(f"Fórmula: 2 × {len(historico)} - 1 = {recomendacoes}")
        print("-" * 40)

def main():
    """
    Função principal - executa todo o trabalho
    """
    print("=" * 60)
    print("TRABALHO DE COMPLEXIDADE DE ALGORITMOS")
    print("Algoritmo RecomendaFácil - Vassouras Tech")
    print("=" * 60)
    print()
    
    # 1. Cálculo do limite
    limite = calcular_limite_n_10()
    
    # 2. Análise de complexidade
    analisar_complexidade()
    
    # 3. Exemplos práticos
    exemplo_pratico()
    
    # 4. Criar gráfico
    criar_grafico()
    
    # 5. Conclusão
    print("=== CONCLUSÃO ===")
    print()
    print("1. LIMITE:")
    print(f"   O limite da função f(n) = 2n - 1 quando n tende a 10 é {limite}")
    print("   Isso significa que um cliente com 10 compras recebe 19 recomendações")
    print()
    print("2. COMPLEXIDADE:")
    print("   A complexidade do algoritmo é O(n) - linear")
    print("   Isso é bom porque o algoritmo cresce de forma previsível")
    print()
    print("3. ESCALABILIDADE:")
    print("   O algoritmo funciona bem mesmo com muitos clientes")
    print("   Para cada compra nova, gera 2 recomendações a mais")
    print("   É adequado para sistemas de e-commerce")
    print()
    print("4. OBSERVAÇÕES:")
    print("   • O algoritmo é simples e eficiente")
    print("   • Pode gerar muitas recomendações para clientes ativos")
    print("   • Seria bom ter um limite máximo de recomendações")
    print()
    print("=" * 60)

if __name__ == "__main__":
    main()
