from kit_dados import geracao_solar, baterias

#geração solar
#baterias

#indicadores geracao solar
# 1. eficiencia de geração de energia (geracao_kw/consumo_kw)
# 2. porcentagem da poeira x geracao_kw (interrupção ambiental)

#indicadores baterias
# 3. eficiência da bateria em relação à saude (capacidade_kwh / saude_pct)
# 4. quantidade total da bateria (capacidade_kwh x 100 -carga_pct )

def analise_solar():
    for registro in geracao_solar:
        eficiencia = round(registro["geracao_kw"]/registro["consumo_kw"]*100 -100, 2)
        print('Ganho de energia no ciclo', registro["ciclo"], "\t\t\t\t\t", eficiencia,"%")

        interrupcao_ambiental = round(registro["geracao_kw"]/registro["poeira_pct"], 2)
        print("Índice de geração de energia versus porcentagem da poeira", "\t", interrupcao_ambiental)            

#analise_solar()

def analise_bateria():
    for registro in baterias:
        eficiencia = round(registro["capacidade_kwh"]/registro["saude_pct"], 2)
        print ('Eficiência da bateria em relação à saúde', registro["id"], eficiencia)

#analise_bateria()

 