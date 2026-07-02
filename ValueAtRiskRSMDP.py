import ProgramacaoDinamicaMDP as pdMDP
from queue import PriorityQueue

class StateInfo:
    def __init__(self, estado, custo, probabilidade, historico, tempo):
        self.estado = estado
        self.custo = custo
        self.probabilidade = probabilidade
        self.historico = historico
        self.tempo = tempo
    



def ForPECVaR(heuristica, alfa, politica, estados, acoes, desconto, nomePrimeiroEstado, nomeUltimoEstado):
    ProbAtX = 0
    valueAtMostX = 0
    queue = PriorityQueue()

    yAtX = 1
    valueAtX = {nomePrimeiroEstado: {}}
    x = 0
    
    queue.put((0, StateInfo(nomePrimeiroEstado, 0, 1, [nomePrimeiroEstado], 0)))
    valuesMean = pdMDP.iterativePolicyEvaluation(0.001, 500, politica, estados, acoes, desconto, nomeUltimoEstado)
    while 1 - ProbAtX > alfa:
        d = queue.get()[1]
        if d.estado != nomeUltimoEstado:
            acao = list(politica[d.estado].keys())[0]
            for estado_proximo in list(acoes[d.estado][acao].keys()):
                recompensa = list(acoes[d.estado][acao][estado_proximo].keys())[0]
                historico = d.historico.copy()
                historico.extend([acao, recompensa])
                custo = d.custo +  (desconto ** d.tempo) * recompensa
                probabilidade = d.probabilidade * acoes[d.estado][acao][estado_proximo][recompensa]
                novoState = StateInfo(estado_proximo, custo, probabilidade, historico, d.tempo + 1)
                queue.put(( (novoState.custo + (desconto ** d.tempo) * heuristica[estado_proximo]), novoState))
        else:
            valueAtMostX = (valueAtMostX * ProbAtX + d.custo * d.probabilidade) / (ProbAtX + d.probabilidade)
            ProbAtX += d.probabilidade
            yAtX = 1 - ProbAtX
            valueAtX[nomePrimeiroEstado][yAtX] =  (valuesMean[nomePrimeiroEstado] - valueAtMostX * ProbAtX) / yAtX
            x = d.custo
    value = {}
    value[nomePrimeiroEstado] = {alfa: (yAtX * valueAtX[nomePrimeiroEstado][yAtX] + (alfa - yAtX) * x) / alfa }
    return(value, x, valueAtX)

