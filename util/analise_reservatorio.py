from kit_dados import reservatorios

# análise do nível e da qualidade da água nos reservatórios

def analise_reservatorio():

    print("=== ANÁLISE DOS RESERVATÓRIOS DE ÁGUA ===\n")

    for registro in reservatorios:
        print("Reservatório:", registro["id"])

        porcentagem_nivel = round(registro["nivel_l"] / registro["capacidade_l"] * 100, 2)

        print("Nível atual:", porcentagem_nivel, "%")

        if porcentagem_nivel >= 100:
            print("\tNÍVEL DE ÁGUA COLETADA ATINGIU OU PASSOU DO LIMITE DEMARCADO DE COLETA, INTERROMPENDO PROCESSO IMEDIATAMENTE")
        elif porcentagem_nivel >= 90:
            print("\tNÍVEL DE ÁGUA COLETADA PRÓXIMO DO LIMITE MÁXIMO, PREPARANDO PARA REDUZIR A VELOCIDADE DE EXTRAÇÃO")
        else:
            print("\tNÍVEL DE ÁGUA COLETADA AINDA ABAIXO DO LIMITE, O ROBÔ CONTINUARÁ COLETANDO")


        qualidade = registro["qualidade_pct"]

        print("Qualidade da água:", qualidade, "%")

        if qualidade < 95:
            print("\tQUALIDADE DA ÁGUA: CRÍTICA")
        elif qualidade < 98:
            print("\tQUALIDADE DA ÁGUA: ATENÇÃO")
        else:
            print("\tQUALIDADE DA ÁGUA: BOA")

        print("--------------------------------------------------")