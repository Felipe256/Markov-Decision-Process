import numpy as np

def iterativePolicyEvaluation(lmbda, theta, valorInicialEstados, politica, estados, acoes, desconto, nomeUltimoEstado):
    delta = float("inf")
    values = {estado: valorInicialEstados for estado in estados}
    values[nomeUltimoEstado] = -1 * np.sign(lmbda) if lmbda < 0 else 1 * np.sign(lmbda)
    while delta >= theta and not (values["S0"] == float("inf") or values["S0"] == float("-inf")):
        delta = 0
        for estado in estados:
            v = values[estado]
            values[estado] = 0
            for acao in list(politica[estado].keys()):
                for estado_proximo in list(acoes[estado][acao].keys()):
                    for recompensa in list(acoes[estado][acao][estado_proximo].keys()):
                        probabilidade = acoes[estado][acao][estado_proximo][recompensa]
                        valorProximoEstado = values[estado_proximo] if estado_proximo != estado else v
                        values[estado] += (politica[estado][acao] * probabilidade * (np.exp(lmbda * recompensa) * desconto * valorProximoEstado))
            delta = max(delta, abs(v - values[estado]))
    return values

def policyIteration(lmbda, theta, valorInicialEstados, politica, estados, acoes, desconto, nomeUltimoEstado):
    politicaEstavel = False
    while not politicaEstavel:
        politicaEstavel = True
        values = iterativePolicyEvaluation(lmbda, theta, valorInicialEstados, politica, estados, acoes, desconto, nomeUltimoEstado)
        for estado in estados:
            acaoAntiga = list(politica[estado].keys())[0]
            custoMelhorAcao = float("inf")
            melhorAcao = acaoAntiga
            for acao in list(acoes[estado].keys()):
                custoAcao = sum(acoes[estado][acao][estado_proximo][recompensa] * (np.exp(-lmbda * recompensa) * desconto * values[estado_proximo]) for estado_proximo in acoes[estado][acao] for recompensa in list(acoes[estado][acao][estado_proximo].keys()) )
                if custoMelhorAcao > custoAcao:
                    custoMelhorAcao = custoAcao
                    melhorAcao = acao
            if melhorAcao != acaoAntiga:
                politica[estado] = {melhorAcao: 1}
                politicaEstavel = False  
    return [politica, values]

'''
lamda = 0 ; 0.5
'''


