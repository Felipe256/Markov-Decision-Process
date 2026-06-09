def iterativePolicyEvaluation(theta, politica, estados, acoes, desconto):
    delta = float("inf")
    values = {estado: 500 for estado in estados}
    values["Sfinal"] = 0
    while delta >= theta:
        delta = 0
        for estado in estados:
            v = values[estado]
            values[estado] = 0
            for acao in list(politica[estado].keys()):
                for estado_proximo in acoes[estado][acao]:
                    for recompensa in list(acoes[estado][acao][estado_proximo].keys()):
                        probabilidade = acoes[estado][acao][estado_proximo][recompensa]
                        values[estado] += (politica[estado][acao] * probabilidade * (recompensa + desconto * values[estado_proximo]))
            delta = max(delta, abs(v - values[estado]))
    return values

def policyIteration(politica, estados, acoes, desconto):
    politicaEstavel = False
    while not politicaEstavel:
        politicaEstavel = True
        values = iterativePolicyEvaluation(0.001, politica, estados, acoes, desconto)
        for estado in estados:
            acaoAntiga = list(politica[estado].keys())[0]
            custoMelhorAcao = values[estado]
            melhorAcao = acaoAntiga
            for acao in list(acoes[estado].keys()):
                custoAcao = sum(acoes[estado][acao][estado_proximo][recompensa] * (recompensa + desconto * values[estado_proximo]) for estado_proximo in acoes[estado][acao] for recompensa in list(acoes[estado][acao][estado_proximo].keys()) )
                if custoMelhorAcao < custoAcao:
                    custoMelhorAcao = custoAcao
                    melhorAcao = acao
            if melhorAcao != acaoAntiga:
                politica[estado] = {melhorAcao: 1}
                politicaEstavel = False  
    return [politica, values]

def valueInteration(theta, estados, acoes, desconto, acoesPolitica):
    delta = float("inf")
    values = {estado: 500 for estado in estados}
    values["Sfinal"] = 0
    politicaOtima = {estado: {acao: 1 for acao in acoesPolitica[estado]} for estado in estados}
    while delta >= theta:
        delta = 0
        for estado in estados:
            
            v = values[estado]
            values[estado] = float("-inf")
            #values[estado] = max(sum(acoes[estado][acao][estado_proximo][recompensa] * (recompensa + desconto * values[estado_proximo]) for estado_proximo in acoes[estado][acao] for recompensa in list(acoes[estado][acao][estado_proximo].keys()) ) for acao in list(acoes[estado].keys()))
            for acao in list(acoes[estado].keys()):
                custoAcao = sum(acoes[estado][acao][estado_proximo][recompensa] * (recompensa + desconto * values[estado_proximo]) for estado_proximo in acoes[estado][acao] for recompensa in list(acoes[estado][acao][estado_proximo].keys()) )
                if values[estado] < custoAcao:
                    values[estado] = custoAcao
                    politicaOtima[estado] = {acao: 1}
            delta = max(delta, abs(v - values[estado]))
    return [politicaOtima, values]



#teste = iterativePolicyEvaluation(0.001, politica)  
#print(dict(sorted(teste.items(), key=lambda item: item[1])))'''
