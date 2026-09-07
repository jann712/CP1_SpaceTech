from kit_dados import geracao_solar, baterias, consumo_recursos

def simulador_decisao():
    print("=== SIMULADOR DE SUPORTE À DECISÃO LUNAR ===")
    
    # Input 1: Escolha de condição real existente no kit
    ciclo_num = int(input("Informe o ciclo solar para a simulação (1 a 6): "))
    ciclo = geracao_solar[ciclo_num - 1]  # Dados do kit
    
    # Input 2: Tomada de decisão real
    desligar_secundarios = input("Deseja desligar os módulos de baixa prioridade (Mineração e Depósito)? (s/n): ").strip().lower()

    # Cálculo dos dados do Kit
    energia_gerada = ciclo["geracao_kw"]
    
    # Filtra o consumo com base na decisão do usuário
    consumo_total = 0
    for mod in consumo_recursos:
        if desligar_secundarios == 's' and mod["prioridade"] == 3:
            continue  # Pula os módulos de prioridade 3 (Mineração e Depósito)
        consumo_total += mod["energia_kwh_dia"]
        
    # Capacidade total armazenada nas baterias com saúde e carga ok
    energia_baterias = sum((b["capacidade_kwh"] * (b["carga_pct"] / 100)) for b in baterias)
    
    saldo_energetico = energia_gerada - consumo_total

    print("\n--- RESULTADO DA ANÁLISE ---")
    print(f"Energia Gerada no Ciclo {ciclo_num}: {energia_gerada} kW")
    print(f"Consumo Total Estimado: {consumo_total} kWh/dia")
    print(f"Saldo Energético Diário: {saldo_energetico} kW")

    # Classificação e Recomendação final
    if saldo_energetico >= 0:
        classificacao = "ESTÁVEL / SEGURA"
        recomendacao = "A operação pode prosseguir normalmente. Os sistemas de suporte estão garantidos."
    elif (energia_baterias + saldo_energetico) > 0:
        classificacao = "ALERTA (Sustentado por Baterias)"
        recomendacao = "O consumo excede a geração solar. Recomenda-se reduzir atividades no Laboratório ou realizar manutenção dos painéis para remover poeira."
    else:
        classificacao = "CRÍTICO (Risco de Colapso Energético)"
        recomendacao = "Corte imediatamente a energia do Laboratório e reduza o consumo do Habitat ao mínimo viável."

    print(f"\nClassificação do Cenário: {classificacao}")
    print(f"Recomendação de Ação: {recomendacao}")

simulador_decisao()