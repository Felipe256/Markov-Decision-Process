estados = {"S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13", "S14"}
acoes = {
"S0":{"right": {"S1": {-1 : 1}}, "down": {"S4": {-1 : 1}}}, 
"S1":{"right": {"S2": {-1 : 1}}, "down": {"S5": {-1 : 1}}, "left": {"S0": {-1 : 1}}}, 
"S2":{"right": {"S3": {-1 : 1}}, "down": {"S6": {-1 : 1}}, "left": {"S1": {-1 : 1}}}, 
"S3":{"down": {"S7": {-1 : 1}}, "left": {"S2": {-1 : 1}}}, 
"S4":{"right": {"S5": {-1 : 1}}, "down": {"S8": {-1 : 1}}, "up": {"S0": {-1 : 1}}},
"S5":{"right": {"S6": {-1 : 1}}, "down": {"S9": {-1 : 1}}, "left": {"S4": {-1 : 1}}, "up": {"S1": {-1 : 1}}},
"S6":{"right": {"S7": {-1 : 1}}, "down": {"S10": {-1 : 1}}, "left": {"S5": {-1 : 1}}, "up": {"S2": {-1 : 1}}},
"S7":{"down": {"S11": {-1 : 1}}, "left": {"S6": {-1 : 1}}, "up": {"S3": {-1 : 1}}},
"S8":{"right": {"S9": {-1 : 1}}, "down": {"S12": {-1 : 1}}, "up": {"S4": {-1 : 1}}},
"S9":{"right": {"S10": {-1 : 1}}, "down": {"S13": {-1 : 1}}, "left": {"S8": {-1 : 1}}, "up": {"S5": {-1 : 1}}},
"S10":{"right": {"S11": {-1 : 1}}, "down": {"S14": {-1 : 1}}, "left": {"S9": {-1 : 1}}, "up": {"S6": {-1 : 1}}},
"S11":{"down": {"Sfinal": {-1 : 1}}, "left": {"S10": {-1 : 1}}, "up": {"S7": {-1 : 1}}},
"S12":{"right": {"S13": {-1 : 1}}, "up": {"S8": {-1 : 1}}},
"S13":{"right": {"S14": {-1 : 1}}, "left": {"S12": {-1 : 1}}, "up": {"S9": {-1 : 1}}},
"S14":{"right": {"Sfinal": {-1 : 1}}, "left": {"S13": {-1 : 1}}, "up": {"S10": {-1 : 1}}} 
}
acoesPolitica = {
"S0" : {"right"}, 
"S1" : {"right"}, 
"S2" : {"right"},
"S3" : {"down"}, 
"S4" : {"down"}, 
"S5" : {"left"}, 
"S6" : {"left"}, 
"S7" : {"left"}, 
"S8" : {"down"}, 
"S9" : {"right"}, 
"S10" : {"right"}, 
"S11" : {"down"}, 
"S12" : {"right"}, 
"S13" : {"up"}, 
"S14" : {"right"}
}
desconto = 1
politica = {estado: {acao: 1 for acao in acoesPolitica[estado]} for estado in estados}

def iterativePolicyEvaluation(theta, politica):
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

def policyIteration(politica):
    politicaEstavel = False
    while not politicaEstavel:
        politicaEstavel = True
        values = iterativePolicyEvaluation(0.001, politica)
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

def valueInteration(theta):
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


print(valueInteration(0.001))

#teste = iterativePolicyEvaluation(0.001, politica)  
#print(dict(sorted(teste.items(), key=lambda item: item[1])))
