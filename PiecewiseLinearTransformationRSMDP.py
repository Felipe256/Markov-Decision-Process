def valorPiecewiseLinearTransformation(k, x):
    if x < 0:
        return (1 - k)
    else:
        return (1 + k)

def iterativePolicyEvaluation(k, theta, valorInicialEstados, politica, estados, acoes, desconto, nomeUltimoEstado):
    delta = float("inf")
    values = {estado: valorInicialEstados for estado in estados}
    values[nomeUltimoEstado] = 0
    while delta >= theta:
        delta = 0
        for estado in estados:
            v = values[estado]
            values[estado] = 0
            for acao in list(politica[estado].keys()):
                totalDivisao = 0
                for estado_proximo in list(acoes[estado][acao].keys()):
                    for recompensa in list(acoes[estado][acao][estado_proximo].keys()):
                        probabilidade = acoes[estado][acao][estado_proximo][recompensa]
                        valorProximoEstado = values[estado_proximo] if estado_proximo != estado else v
                        valorPLT = valorPiecewiseLinearTransformation(k, recompensa + desconto * valorProximoEstado - v)
                        totalDivisao += probabilidade * valorPLT
                        values[estado] += (politica[estado][acao] * probabilidade * valorPLT * (recompensa + desconto * valorProximoEstado))
                if totalDivisao != 0:
                    values[estado] /= totalDivisao
            delta = max(delta, abs(v - values[estado]))
    return values

def policyIteration(k, valorInicialEstados, politica, estados, acoes, desconto, nomeUltimoState):
    politicaEstavel = False
    while not politicaEstavel:
        politicaEstavel = True
        values = iterativePolicyEvaluation(k, 0.001, valorInicialEstados, politica, estados, acoes, desconto, nomeUltimoState)
        for estado in estados:
            acaoAntiga = list(politica[estado].keys())[0]
            custoMelhorAcao = float("-inf")
            melhorAcao = acaoAntiga
            for acao in list(acoes[estado].keys()):
                custoAcao = 0
                totalDivisao = 0
                for estado_proximo in acoes[estado][acao]:
                    for recompensa in list(acoes[estado][acao][estado_proximo].keys()):
                        probabilidade = acoes[estado][acao][estado_proximo][recompensa]
                        valorPLT = valorPiecewiseLinearTransformation(k, recompensa + desconto * values[estado_proximo] - values[estado])
                        totalDivisao += probabilidade * valorPLT
                        custoAcao += probabilidade * valorPLT * (recompensa + desconto * values[estado_proximo])
                if totalDivisao != 0:
                    custoAcao /= totalDivisao
                if custoMelhorAcao < custoAcao:
                    custoMelhorAcao = custoAcao
                    melhorAcao = acao
            if melhorAcao != acaoAntiga:
                politica[estado] = {melhorAcao: 1}
                politicaEstavel = False  
    return [politica, values]
