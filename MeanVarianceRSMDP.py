def iterativePolicyEvaluation(theta, valorInicialEstados, politica, estados, acoes, desconto, nomeUltimoEstado):
    delta = float("inf")
    values = {estado: valorInicialEstados for estado in estados}
    values[nomeUltimoEstado] = 0
    while delta >= theta:
        delta = 0
        for estado in estados:
            v = values[estado]
            valorAtual = 0
            values[estado] = 0
            for acao in list(politica[estado].keys()):
                for estado_proximo in list(acoes[estado][acao].keys()):
                    for recompensa in list(acoes[estado][acao][estado_proximo].keys()):
                        valorAtual = recompensa
                        if estado_proximo == estado:
                            continue
                        probabilidade = acoes[estado][acao][estado_proximo][recompensa]
                        valorProximoEstado = values[estado_proximo] 
                        values[estado] += (probabilidade * (desconto * valorProximoEstado))
            values[estado] += valorAtual
            delta = max(delta, abs(v - values[estado]))
    return values

def iterativeVariancePolicyEvaluation(theta, valorInicialEstados, politica, estados, acoes, desconto, nomeUltimoEstado, expectation):
    delta = float("inf")
    values = {estado: valorInicialEstados for estado in estados}
    values[nomeUltimoEstado] = 0
    while delta >= theta:
        delta = 0
        for estado in estados:
            v = values[estado]
            values[estado] = 0
            somatorio = 0
            somaFixa = 0
            somaValorProx = 0
            recompensaValorProx = 0
            for acao in list(politica[estado].keys()):
                for estado_proximo in list(acoes[estado][acao].keys()):
                    for recompensa in list(acoes[estado][acao][estado_proximo].keys()):
                        somaFixa = recompensa**2 - (expectation[estado])**2 
                        recompensaValorProx = recompensa
                        if estado_proximo == estado:
                            continue
                        probabilidade = acoes[estado][acao][estado_proximo][recompensa]
                        valorProximoEstado = values[estado_proximo] 
                        somaValorProx += (probabilidade * (desconto * expectation[estado_proximo])) 
                        somatorio += (probabilidade * (desconto * valorProximoEstado))
                        somatorio += (probabilidade * (desconto * expectation[estado_proximo] ** 2))
                        
            values[estado] += somatorio + somaFixa + 2 * recompensaValorProx * somaValorProx
            delta = max(delta, abs(v - values[estado]))
    return values