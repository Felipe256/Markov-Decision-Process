import matplotlib.pyplot as plt

def geraGrafico(x, y, titulo, xlabel, ylabel, cor, linestyle):
    fig, axs = plt.subplots(1, 1, sharex=True, sharey=True, layout="constrained")
    for i in range(len(y)):
        axs.plot(x, y[i], color=cor[i], lw=1.0, label="Politica "+str(i+1), linestyle=linestyle[i])
    axs.legend()
    axs.set_xlabel(xlabel)
    axs.set_ylabel(ylabel)

    plt.savefig('GraficoValorPolitica.png', dpi=300, bbox_inches='tight')
    plt.show()

def mostraGraficos(convergencia):
    politica = convergencia[0]
    acoesPolitica = {}
    for estado in politica.keys():
        acoesPolitica[estado] = list(politica[estado].keys())
    estadoValues = convergencia[1].keys()
    values = convergencia[1].values()

    fig, axs = plt.subplots(1, 1, sharex=True, sharey=True, layout="constrained")


    axs.scatter(estadoValues, values, s=80, marker=".")
    axs.set_title("Convergência do Valor")
    axs.set_xlabel("Estado")
    axs.set_ylabel("Valor")
    plt.show()

    ''' plt.plot(estadoValues, values)
    plt.xlabel("Estado")
    plt.ylabel("Valor")
    plt.title("Convergência do Valor")
    plt.show()'''

    plt.plot(acoesPolitica.keys(), acoesPolitica.values())
    plt.xlabel("Estado")
    plt.ylabel("Acao")
    plt.title("Ações de cada estado")
    plt.show()