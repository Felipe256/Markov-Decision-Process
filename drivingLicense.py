import ProgramacaoDinamicaMDP as pdMDP
import ExponentialUtilityFunctionRSMDP as EUF
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
#graficos.mostraGraficos(pdMDP.policyIteration(500, politica, estados, acoes, 1, "Sfinal"))
#pdMDP.valueIteration(0.001, 500, estados, acoes, 1, acoesPolitica, "Sfinal")

lmbda = 0.5
print(str(lmbda)+" "+str(EUF.policyIteration(lmbda, 0.00001, 500, politica, estados, acoes, 1, "Sfinal")[0])+"\n")
'''convergencia = 
graficos.mostraGraficos(convergencia)'''