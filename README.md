[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2022/03/campus_marica.png)](https://universidadedevassouras.edu.br/campus-marica/)

# Engenharia de Software
### Leandro Loffeu Pereira Costa - mat. 202212089
### Complexidade de Algoritmos - 8º Período
### Professor: Márcio Guarrido


# Trabalho de Complexidade de Algoritmos

## Algoritmo RecomendaFacil - Vassouras Tech

**Professor:** Marcio Guarrido  
**Aluno:** Leandro Loffeu Pereira Costa - Mat. 202212089

Este é um trabalho acadêmico sobre análise de complexidade de algoritmos, implementando e analisando o algoritmo de recomendação da empresa Vassouras Tech.

## 📋 Objetivos

1. **Calcular o limite** da função f(n) = 2n - 1 quando n tende a 10
2. **Analisar a complexidade** assintótica do algoritmo
3. **Discutir a escalabilidade** do sistema de recomendação
4. **Implementar** o algoritmo RecomendaFacil conforme especificação

## 🚀 Como executar

### Opção 1: Windows (mais fácil)
```
Duplo clique em executar.bat
```

### Opção 2: Terminal
```bash
python trabalho.py
```

## 📁 Arquivos do Projeto

- `trabalho.py` - **Código principal** com toda a análise matemática
- `grafico.png` - **Gráfico** da função f(n) = 2n - 1
- `README.md` - **Documentação** completa (este arquivo)
- `executar.bat` - **Script Windows** para execução fácil

## 🔍 O Algoritmo RecomendaFacil

```python
def gerarRecomendacoes(historico):
    n = tamanho do historico
    return 2 * n - 1
```

**Entrada:** Histórico de compras do usuário (lista de itens)  
**Saída:** Número de recomendações personalizadas

## 📊 Resultados da Análise

### 1. Cálculo do Limite
- **Função:** f(n) = 2n - 1
- **Limite quando n → 10:** 19
- **Interpretação:** Cliente com 10 compras recebe 19 recomendações

### 2. Complexidade Assintótica
- **Tipo:** O(n) - Linear
- **Crescimento:** Proporcional ao histórico de compras
- **Avaliação:** Eficiente e previsível

### 3. Exemplos Práticos
- **João (3 compras):** 5 recomendações
- **Maria (10 compras):** 19 recomendações  
- **Pedro (15 compras):** 29 recomendações

### 4. Escalabilidade
- **100 compras:** 199 recomendações
- **1.000 compras:** 1.999 recomendações
- **10.000 compras:** 19.999 recomendações

## 📈 Visualização

O arquivo `grafico.png` contém:
- Gráfico da função f(n) = 2n - 1
- Crescimento linear destacado
- Ponto específico para n = 10 (19 recomendações)
- Comportamento previsível e eficiente

## ✅ Conclusão

### Resumo dos Resultados:
1. **Limite calculado:** lim f(n) = 19 quando n → 10
2. **Complexidade identificada:** O(n) - linear
3. **Escalabilidade avaliada:** Adequada para e-commerce
4. **Algoritmo implementado:** Conforme especificação

### Características do Algoritmo:
- ✅ **Eficiente:** Complexidade linear O(n)
- ✅ **Previsível:** Crescimento proporcional ao histórico
- ✅ **Escalável:** Adequado para grandes volumes
- ⚠️ **Consideração:** Pode gerar muitas recomendações para clientes ativos

### Requisitos Atendidos:
- ✅ Cálculo do limite quando n tende a 10
- ✅ Análise da complexidade assintótica O(n)
- ✅ Discussão sobre escalabilidade do sistema
- ✅ Implementação do algoritmo RecomendaFacil
- ✅ Geração de gráfico da função


**Professor:** Marcio Guarrido  
**Aluno:** Leandro Loffeu Pereira Costa - Mat. 202212089
