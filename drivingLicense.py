import ProgramacaoDinamicaMDP as pdMDP
import ExponentialUtilityFunctionRSMDP as EUF
import PiecewiseLinearTransformationRSMDP as PLT
import ValueAtRiskRSMDP as VaT
import graficos

numEstado = {i for i in range(0,11)}
numEstadoParaNome = {estado : "S"+str(estado) for estado in numEstado}
estados = numEstadoParaNome.values()
todasAcoes = {0, 1, 2, 3, 4}
acoes = {numEstadoParaNome[estado] :
            {acao:
                {numEstadoParaNome[min(estado+acao, 10)]:
                    { (2 + acao):
                        (100 - (8*estado + 4*acao))/100
                    },
                "Sfinal":
                    { (2 + acao):
                        (8*estado + 4*acao)/100
                    }
                } 
            for acao in todasAcoes 
            }   
        for estado in numEstado 
        }
politica = {numEstadoParaNome[i]: {0  : 1} for i in numEstado}
acoesPolitica = {numEstadoParaNome[i]: {1} for i in numEstado}
heuristica = {numEstadoParaNome[i]: 1 for i in numEstado}
heuristica["Sfinal"] = 0
#graficos.mostraGraficos(pdMDP.costPolicyIteration(500, politica, estados, acoes, 1, "Sfinal"))

lmbda = [0.7, 0.5, 0.4, 0.3, 0.2, 0.1, 0, -0.1, -0.2, -0.3, -0.4, -0.5, -0.6]
{ print(str(lb)+" "+str(EUF.policyIteration(lb, 0.00001, 500, politica, estados, acoes, 1, "Sfinal")[0])+"\n")  for lb in lmbda }

'''kPLT = -0.2
convergencia = PLT.policyIteration(kPLT, 500, politica, estados, acoes, 1, "Sfinal")
graficos.mostraGraficos(convergencia)
print(VaT.ForPECVaR(heuristica, 0.05, politica, estados, acoes, 1, "S0", "Sfinal"))'''