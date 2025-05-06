from math import comb
import matplotlib.pyplot as plt

# Configurações iniciais
num_caras = 4
num_lancamentos = 5
prob_cara = 0.5

# Função para criar imagens dos passos
def visualize_steps():
    # Passo 1: Representação dos lançamentos observados
    fig, ax = plt.subplots(figsize=(10, 2))
    faces = ['CARA']*4 + ['COROA']
    colors = {'CARA': 'gold', 'COROA': 'silver'}
    
    for i, face in enumerate(faces):
        circle = plt.Circle((i*1.5, 1), 0.4, color=colors[face], ec='black')
        ax.add_patch(circle)
        ax.text(i*1.5, 1, face[0], ha='center', va='center', fontsize=12)
    
    ax.set_xlim(-0.5, 7)
    ax.set_ylim(0, 2)
    ax.axis('off')
    plt.title('Passo 1: Seus Resultados - 4 Caras e 1 Coroa')
    plt.savefig('passo1_resultados.png', bbox_inches='tight')
    plt.close()

    # Passo 2: Todas sequências possíveis com 4 caras
    fig, ax = plt.subplots(figsize=(10, 4))
    sequences = [
        ['C', 'C', 'C', 'C', 'K'],
        ['C', 'C', 'C', 'K', 'C'],
        ['C', 'C', 'K', 'C', 'C'],
        ['C', 'K', 'C', 'C', 'C'],
        ['K', 'C', 'C', 'C', 'C']
    ]
    
    for row, seq in enumerate(sequences):
        for col, face in enumerate(seq):
            color = 'gold' if face == 'C' else 'silver'
            circle = plt.Circle((col*1.5, 3-row), 0.4, color=color, ec='black')
            ax.add_patch(circle)
            ax.text(col*1.5, 3-row, face, ha='center', va='center', fontsize=10)
    
    ax.set_xlim(-0.5, 7)
    ax.set_ylim(-1, 4)
    ax.axis('off')
    plt.title('Passo 2: Todas 5 Sequências Possíveis com 4 Caras')
    plt.savefig('passo2_sequencias.png', bbox_inches='tight')
    plt.close()

    # Passo 3: Cálculo das probabilidades
    fig, ax = plt.subplots(figsize=(8, 4))
    labels = ['1 Sequência', '5 Sequências com 4C', '1 Sequência com 5C']
    sizes = [1, 5, 1]
    colors = ['lightgray', 'gold', 'darkgoldenrod']
    
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.0f', startangle=90)
    ax.axis('equal')
    plt.title('Passo 3: Contagem de Sequências\nTotal: 32 possibilidades (2^5)')
    plt.savefig('passo3_contagem.png', bbox_inches='tight')
    plt.close()

    # Passo 4: Cálculo do p-value
    fig, ax = plt.subplots(figsize=(8, 5))
    results = ['0C', '1C', '2C', '3C', '4C', '5C']
    counts = [1, 5, 10, 10, 5, 1]
    prob = [c/32 for c in counts]
    
    bars = ax.bar(results, prob, color=['red' if x in [4,5] else 'blue' for x in range(6)])
    ax.set_ylabel('Probabilidade')
    ax.set_title('Passo 4: Distribuição de Probabilidades\nP-value = Prob(4C) + Prob(5C)')
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.4f}', ha='center', va='bottom')
    
    plt.savefig('passo4_pvalue.png', bbox_inches='tight')
    plt.close()

# Executar a visualização
visualize_steps()

# Cálculo final do p-value
p_value = (comb(5, 4) + comb(5, 5)) / 2**5
print(f"\nO p-value para observar 4 ou mais caras em 5 lançamentos é: {p_value:.4f} ({(p_value*100):.1f}%)")