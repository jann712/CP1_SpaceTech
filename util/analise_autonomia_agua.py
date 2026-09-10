from kit_dados import consumo_recursos, reservatorios


def analise_autonomia_agua():

    print("=== ANÁLISE DE CONSUMO E AUTONOMIA DA ÁGUA ===\n")

    # Soma toda a água disponível atualmente nos reservatórios
    agua_total = 0

    for reservatorio in reservatorios:
        agua_total += reservatorio["nivel_l"]

    # Soma o consumo diário de água de todos os módulos
    consumo_total_dia = 0

    for modulo in consumo_recursos:
        consumo_total_dia += modulo["agua_l_dia"]

    # Calcula por quantos dias a água atual consegue sustentar a base
    autonomia_dias = round(agua_total / consumo_total_dia, 2)

    print("Água total disponível:", agua_total, "L")
    print("Consumo total diário:", consumo_total_dia, "L/dia")
    print("Autonomia estimada:", autonomia_dias, "dias\n")

    # Classificação da situação da base
    if autonomia_dias < 10:
        print("SITUAÇÃO HÍDRICA: CRÍTICA")
        print("RECOMENDAÇÃO: Reduzir imediatamente o consumo de água dos módulos de menor prioridade.")

    elif autonomia_dias <= 20:
        print("SITUAÇÃO HÍDRICA: ATENÇÃO")
        print("RECOMENDAÇÃO: Monitorar o consumo e aumentar a coleta de água.")

    else:
        print("SITUAÇÃO HÍDRICA: ESTÁVEL")
        print("RECOMENDAÇÃO: A base possui uma reserva de água adequada no momento.")
