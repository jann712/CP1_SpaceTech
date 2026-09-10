from kit_dados import geracao_solar

def analise_solar():

    contagem_atencao = 0
    contagem_critico = 0

    print("===========================================================================")
    for registro in geracao_solar:
        eficiencia = round(registro["geracao_kw"]/registro["consumo_kw"]*100 -100, 2)
        print('Ganho de energia no ciclo', registro["ciclo"], "\t\t\t\t\t", eficiencia,"%")

        interrupcao_ambiental = round(registro["geracao_kw"]/registro["poeira_pct"], 2)
        print("Índice de geração de energia versus porcentagem da poeira", "\t", interrupcao_ambiental)    

        if eficiencia < 0: 
            print("NÍVEL DA EFICIÊNCIA ENERGÉTICA DA GERAÇÃO SOLAR: CRÍTICO")
            contagem_critico += 1

        elif eficiencia <= 4: 
            print("NÍVEL DA EFICIÊNCIA ENERGÉTICA DA GERAÇÃO SOLAR: ATENÇÃO")
            contagem_atencao += 1
        elif eficiencia >= 5: 
            print("NÍVEL DA EFICIÊNCIA ENERGÉTICA DA GERAÇÃO SOLAR: NORMAL")

        if interrupcao_ambiental < 7: 
            print("ÍNDICE DE OBSTRUÇÃO DA POEIRA: CRÍTICO")
            contagem_critico += 1

        elif interrupcao_ambiental <= 10: 
            print("ÍNDICE DE OBSTRUÇÃO DA POEIRA SOLAR: ATENÇÃO")
            contagem_atencao += 1

        elif interrupcao_ambiental >= 11: print("ÍNDICE DE OBSTRUÇÃO DA POEIRA SOLAR: NORMAL")

        print("===========================================================================")  

    if contagem_atencao > 0 or contagem_critico > 0:
        print("!!!Procure realizar a substituição dos paineis de geração solar, além de realizar a limpeza da poeira (ou realocar os geradores para outro lugar)!!!\n")      
