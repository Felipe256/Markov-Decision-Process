import ProgramacaoDinamicaMDP as pdMDP

import matplotlib.pyplot as plt

valorMaximo = 100
numEstado = {i for i in range(1, valorMaximo)}
numEstadoParaNome = {estado : "S"+str(estado) for estado in numEstado}
numEstadoParaNome[0] ="Sderrota"
copiaEstados = numEstadoParaNome.copy()
estados = copiaEstados.values()
numEstadoParaNome[valorMaximo] ="Sfinal"
probabilidadeCara = 0.3
acoes = {numEstadoParaNome[estado]:
            {aposta : 
                {numEstadoParaNome[estado + aposta]: 
                    {1 if estado + aposta == valorMaximo else 0 : 
                        probabilidadeCara}, 
                numEstadoParaNome[estado - aposta]: 
                    {0 : 
                        1 - probabilidadeCara}} 
        for aposta in range(0, min(estado, valorMaximo - estado) + 1)} for estado in numEstado}
acoes["Sderrota"] = {1: {"Sfinal": {0: 1}}}
for estado in numEstadoParaNome.values():
    if estado == "Sfinal":
        continue
    acoes[estado][0] = {estado: {0: 1}}

#print("acoes: " + str(acoes))
politica = {numEstadoParaNome[i]: {0  : 1} for i in range(0, valorMaximo)}
acoesPolitica = {numEstadoParaNome[i]: {0} for i in range(0, valorMaximo)}
#print("politica: " + str(politica))
#print(pdMDP.valueInteration(0.001, estados, acoes, 1, acoesPolitica, "Sfinal"))
convergencia = pdMDP.policyIteration(politica, estados, acoes, 1, "Sfinal")

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
plt.ylabel("Acao")
plt.title("Ações de cada estado")
plt.show()