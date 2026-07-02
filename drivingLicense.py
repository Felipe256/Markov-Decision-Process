import ProgramacaoDinamicaMDP as pdMDP
import ExponentialUtilityFunctionRSMDP as EUF
import PiecewiseLinearTransformationRSMDP as PLT
import ValueAtRiskRSMDP as VaT
import numpy as np
import graficos

def calculaValorPoliticaEUT(politica, comeco, fim, quantidade, estados, acoes, nomeUltimoEstado):
    intervalo = np.linspace(comeco, fim, num = quantidade)
    valores = [[] for i in range(len(politica))]
    cores = ["blue", "green", "red", "cyan", "pink", "black", "blue", "green", "red", "cyan", "pink", "black"]
    estilosLinha = ["-", "-", "-", "-", "-", "-", "--", "--", "--", "--", "--", "--"]
    for num in intervalo:
        for i in range(len(politica)):
            valorS0 = EUF.iterativePolicyEvaluation(num, 0.00001, 500, politica[i], estados, acoes, 1, nomeUltimoEstado)["S0"]
            valores[i].append(np.log(valorS0)/ (num if num != 0 else 1))
    graficos.geraGrafico(intervalo, valores, "Interações de lambda sobre a politica", "lambda", "log(value)/lambda", cores, estilosLinha)

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
politicas = [
    {'S0': {4: 1}, 'S1': {4: 1}, 'S2': {3: 1}, 'S3': {2: 1}, 'S4': {1: 1}, 'S5': {0: 1}, 'S6': {0: 1}, 'S7': {0: 1}, 'S8': {0: 1}, 'S9': {0: 1}, 'S10': {0: 1}} 
    ,{'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {3: 1}, 'S4': {2: 1}, 'S5': {1: 1}, 'S6': {0: 1}, 'S7': {0: 1}, 'S8': {0: 1}, 'S9': {0: 1}, 'S10': {0: 1}}, 
    {'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {4: 1}, 'S4': {3: 1}, 'S5': {2: 1}, 'S6': {1: 1}, 'S7': {0: 1}, 'S8': {0: 1}, 'S9': {0: 1}, 'S10': {0: 1}}, 
    {'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {4: 1}, 'S4': {4: 1}, 'S5': {3: 1}, 'S6': {2: 1}, 'S7': {1: 1}, 'S8': {0: 1}, 'S9': {0: 1}, 'S10': {0: 1}}, 
    {'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {4: 1}, 'S4': {4: 1}, 'S5': {4: 1}, 'S6': {3: 1}, 'S7': {2: 1}, 'S8': {1: 1}, 'S9': {0: 1}, 'S10': {0: 1}}, 
    {'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {4: 1}, 'S4': {4: 1}, 'S5': {4: 1}, 'S6': {4: 1}, 'S7': {3: 1}, 'S8': {2: 1}, 'S9': {1: 1}, 'S10': {0: 1}}, 
    {'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {4: 1}, 'S4': {4: 1}, 'S5': {4: 1}, 'S6': {4: 1}, 'S7': {4: 1}, 'S8': {3: 1}, 'S9': {2: 1}, 'S10': {1: 1}}, 
    {'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {4: 1}, 'S4': {4: 1}, 'S5': {4: 1}, 'S6': {4: 1}, 'S7': {4: 1}, 'S8': {4: 1}, 'S9': {3: 1}, 'S10': {0: 1}} 
    ,{'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {4: 1}, 'S4': {4: 1}, 'S5': {4: 1}, 'S6': {4: 1}, 'S7': {4: 1}, 'S8': {4: 1}, 'S9': {3: 1}, 'S10': {1: 1}}, 
    {'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {4: 1}, 'S4': {4: 1}, 'S5': {4: 1}, 'S6': {4: 1}, 'S7': {4: 1}, 'S8': {4: 1}, 'S9': {3: 1}, 'S10': {2: 1}}, 
    {'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {4: 1}, 'S4': {4: 1}, 'S5': {4: 1},'S6': {4: 1}, 'S7': {4: 1}, 'S8': {4: 1}, 'S9': {4: 1}, 'S10': {3: 1}}, 
    {'S0': {4: 1}, 'S1': {4: 1}, 'S2': {4: 1}, 'S3': {4: 1}, 'S4': {4: 1}, 'S5': {4: 1}, 'S6': {4: 1}, 'S7': {4: 1}, 'S8': {4: 1}, 'S9': {4: 1}, 'S10': {4: 1}}
    ]

'''kPLT = -0.2
convergencia = PLT.policyIteration(kPLT, 500, politica, estados, acoes, 1, "Sfinal")
graficos.mostraGraficos(convergencia)'''
heuristica = {estado: 0.1 for estado in estados}
heuristica["Sfinal"] = 0
print(VaT.ForPECVaR(heuristica, 0.05, politicas[0], estados, acoes, 1, "S0", "Sfinal"))