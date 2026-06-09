import ProgramacaoDinamicaMDP

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

print(ProgramacaoDinamicaMDP.valueInteration(0.001, estados, acoes, desconto, acoesPolitica))
