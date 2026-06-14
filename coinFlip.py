import ProgramacaoDinamicaMDP as pdMDP

import graficos


valorMaximo = 4
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
politica = {numEstadoParaNome[i]: {min(i, valorMaximo - i)  : 1} for i in range(0, valorMaximo)}
acoesPolitica = {numEstadoParaNome[i]: {0} for i in range(0, valorMaximo)}
#print("politica: " + str(politica))
#convergencia = pdMDP.valueIteration(0.001, -500, estados, acoes, 1, acoesPolitica, "Sfinal")
convergencia = pdMDP.policyIteration(-500, politica, estados, acoes, 1, "Sfinal")

graficos.mostraGraficos(convergencia)