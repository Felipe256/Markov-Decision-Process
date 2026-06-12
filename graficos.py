import matplotlib.pyplot as plt

def mostraGraficos(convergencia):
    politica = convergencia[0]
    acoesPolitica = {}
    for estado in politica.keys():
        acoesPolitica[estado] = list(politica[estado].keys())
    estadoValues = convergencia[1].keys()
    values = convergencia[1].values()

    plt.plot(estadoValues, values)
    plt.xlabel("Estado")
    plt.ylabel("Valor")
    plt.title("Convergência do Valor")
    plt.show()

    plt.plot(acoesPolitica.keys(), acoesPolitica.values())
    plt.xlabel("Estado")
    plt.ylabel("Acao")
    plt.title("Ações de cada estado")
    plt.show()