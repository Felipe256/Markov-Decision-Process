import ProgramacaoDinamicaMDP as pdMDP

valorMaximo = 100
numEstado = {i for i in range(1, valorMaximo)}
numEstadoParaNome = {estado : "S"+str(estado) for estado in numEstado}
copiaEstados = numEstadoParaNome.copy()
estados = copiaEstados.values()
numEstadoParaNome[0] ="Sfinal"
numEstadoParaNome[valorMaximo] ="Sfinal"
probabilidadeCara = 0.3
acoes = {numEstadoParaNome[estado]:
            {aposta : 
                {numEstadoParaNome[estado + aposta]: 
                    {1 if estado + aposta == valorMaximo else 0 : 
                        probabilidadeCara}, 
                numEstadoParaNome[estado - aposta]: 
                    {1 if estado - aposta == 0 else 0 : 
                        1 - probabilidadeCara}} 
        for aposta in range(0, min(estado, valorMaximo - estado) + 1)} for estado in numEstado}
acoes["Sderrota"] = {1: {"Sfinal": {0: 1}}}

print(pdMDP.valueInteration(0.001, estados, acoes, 0, {numEstadoParaNome[i]: {min(50, i, 100-i)} for i in range(1, valorMaximo)}, "Sfinal"))
#print(pdMDP.iterativePolicyEvaluation(0.001,{estado: {1 : 1} for estado in estados}, estados, acoes, 0, "Sfinal"))