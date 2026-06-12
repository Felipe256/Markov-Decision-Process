import ProgramacaoDinamicaMDP as pdMDP
import graficos

numEstado = {i for i in range(0,11)}
numEstadoParaNome = {estado : "S"+str(estado) for estado in numEstado}
estados = numEstadoParaNome.values()
todasAcoes = {0, 1, 2, 3, 4}
acoes = {numEstadoParaNome[estado] :
            {acao:
                {numEstadoParaNome[min(estado+acao, 10)]:
                    {-1 * (2 + acao):
                        (100 - (8*estado + 4*acao))/100
                    },
                "Sfinal":
                    {-1 * (2 + acao):
                        (8*estado + 4*acao)/100
                    }
                } 
            for acao in todasAcoes 
            }   
        for estado in numEstado 
        }
politica = {numEstadoParaNome[i]: {1  : 1} for i in numEstado}
acoesPolitica = {numEstadoParaNome[i]: {1} for i in numEstado}
#graficos.mostraGraficos(pdMDP.policyIteration(politica, estados, acoes, 1, "Sfinal"))
graficos.mostraGraficos(pdMDP.valueInteration(0.000001, estados, acoes, 1, acoesPolitica, "Sfinal"))