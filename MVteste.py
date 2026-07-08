import MeanVarianceRSMDP as MV

estados = {"S0", "S1"}
porcentagem = 0.3
acoes = {"S0": 
            {1: 
                {"S0" : 
                    {2 : porcentagem}, 
                 "S1" : 
                    {2 : 1 - porcentagem}
                }
            }, 
        "S1":
            {1: 
                {"S1" : 
                    {3 : porcentagem}, 
                 "Sfinal" : 
                    {3 : 1 - porcentagem}
                }
            }
        }
politica = {"S0": {1: 1}, "S1": {1: 1}}

valores = MV.iterativePolicyEvaluation(0.001, 500, politica, estados, acoes, 1, "Sfinal")
variancia = MV.iterativeVariancePolicyEvaluation(0.001, 500, politica, estados, acoes, 1, "Sfinal", valores)
print(valores, "\n", variancia)