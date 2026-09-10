from kit_dados import baterias

def analise_bateria():

    contagem_atencao = 0
    contagem_critico = 0

    print("===========================================================================")  

    for registro in baterias:
        eficiencia = round(registro["capacidade_kwh"]/registro["saude_pct"], 2)
        print ('Eficiência da bateria em relação à saúde', registro["id"], eficiencia)

        if eficiencia < 3: 
            print("ÍNDICE DE SAÚDE DA BATERIA: CRÍTICO")
            contagem_critico += 1
        
        elif eficiencia < 4: 
            print("ÍNDICE DE SAÚDE DA BATERIA: ATENÇÃO")
            contagem_atencao += 1
        
        elif eficiencia >= 5: print("ÍNDICE DE SAÚDE DA BATERIA: NORMAL")

        print("===========================================================================")  

    if contagem_atencao > 0 or contagem_critico > 0:
        print("!!!Realize a troca das baterias com saúde degradada!!!\n")     