# Ficha da Missão
## Sistema de Suporte à Decisão Energética e Hídrica para Robôs Lunares de Coleta de Água

**Projeto:** Robô Lunar Autônomo para Exploração e Coleta de Água  
**Documento:** Proposta Programa 1 e Programa 2  
**Nome da Empresa:** SpaceTech  
**Turma:** 1ECA  
**Tema Escolhido:** Água e Energia  

### Integrantes (Nome e RM):
* João Augusto do Nascimento Neto (571580)
* Guilherme Lopes Ferreira (569292)
* Jorge Luiz Marques Araujo (573754)
* Priscila de Jesus Brayner (568913)
* Dalexandro Ciceron (568784)

---

## Nome da Solução e Tema Escolhido

* **Nome:** Sistema de Suporte à Decisão Energética e Hídrica - Módulo de Diagnóstico e Simulação para o Robô Lunar Autônomo.
* **Tema:** Autonomia energética (geração solar e baterias) e gestão do recurso hídrico (nível dos reservatórios, qualidade da água e autonomia em dias) aplicadas à missão de exploração e coleta de água descrita no roteiro do projeto.

---

## Objetivo

O roteiro do projeto define que as maiores ameaças à missão são a falta de energia do robô longe do posto de recarga — seja por degradação de painéis, poeira lunar ou perda de saúde das baterias — e o desabastecimento hídrico da base por falhas na coleta, capacidade dos reservatórios ou consumo excessivo dos módulos.

Nosso objetivo é transformar os dados brutos do kit em diagnósticos precisos sobre a saúde energética e hídrica da base e fornecer recomendações de ação claras para apoiar a tomada de decisão: continuar a coleta, reduzir consumo de módulos secundários, monitorar reservatórios ou realizar manutenção nos equipamentos.

---

## Dados Selecionados

* **`geracao_solar`**: Geração x consumo de energia, poeira acumulada e ciclo. Usado para diagnosticar a eficiência energética e o impacto da obstrução por poeira lunar nos painéis solares.
* **`baterias`**: Capacidade, carga e taxa de saúde de cada unidade. Usado para acompanhar a degradação e a retenção de carga, evitando paralisações operacionais.
* **`reservatorios`**: Nível atual de água coletada (L), capacidade total (L) e porcentagem de qualidade da água. Usado para controlar limites de extração/coleta e garantir a potabilidade/qualidade da água.
* **`consumo_recursos`**: Consumo diário de água (L/dia) e energia (kWh/dia) por módulo (Habitat, Laboratório, Mineração, Médico, Comunicação, Depósito) e suas respectivas prioridades. Usado na estimativa de autonomia hídrica total e na simulação de corte seletivo de energia para módulos de baixa prioridade.

---

## Indicadores e Diagnósticos

### Programa 1: Diagnóstico Geral (`program1.py`)
O Programa 1 centraliza os diagnósticos dos quatro eixos do sistema:

1. **Geração Solar (`analise_solar`)**:
   * **Ganho de eficiência energética:**  
     Ganho (%) = (geracao_kw / consumo_kw * 100) - 100  
     Classificado em **NORMAL**, **ATENÇÃO** ou **CRÍTICO**.
   * **Índice de obstrução por poeira:**  
     Índice = geracao_kw / poeira_pct  
     Classificado em **NORMAL**, **ATENÇÃO** ou **CRÍTICO**, recomendando limpeza, reposicionamento ou substituição dos painéis.

2. **Saúde das Baterias (`analise_bateria`)**:
   * **Eficiência em relação à saúde:**  
     Eficiência = capacidade_kwh / saude_pct  
     Classificada em **NORMAL**, **ATENÇÃO** ou **CRÍTICO**, emitindo alertas para substituição de unidades degradadas.

3. **Monitoramento dos Reservatórios (`analise_reservatorio`)**:
   * **Nível percentual de água:**  
     Porcentagem = (nivel_l / capacidade_l) * 100  
     Emite alertas automáticos para interrupção imediata da coleta (>= 100%), desaceleração da extração (>= 90%) ou continuação da coleta pelo robô.
   * **Qualidade da água (%):** Classificada em **BOA** (>= 98%), **ATENÇÃO** (< 98%) ou **CRÍTICA** (< 95%).

4. **Autonomia Hídrica da Base (`analise_autonomia_agua`)**:
   * **Autonomia estimada (dias):**  
     Autonomia = Água Total Disponível (L) / Consumo Total Diário (L/dia)
   * **Classificação da situação hídrica:**
     * **CRÍTICA** (< 10 dias): Recomendação para redução imediata do consumo nos módulos de menor prioridade.
     * **ATENÇÃO** (<= 20 dias): Recomendação para monitorar o consumo e aumentar a coleta de água.
     * **ESTÁVEL** (> 20 dias): A base possui uma reserva de água adequada no momento.
---

### Programa 2: Simulação de Decisão (`program2.py` / `simulador_decisao`)
Permite ao operador simular cenários operacionais em tempo real:
* **Entradas do Usuário:** Seleção do ciclo solar (1 a 6) e decisão de desligar ou não os módulos de menor prioridade (Mineração e Depósito - Prioridade 3).
* **Cálculos:**
  * Consumo total de energia estimado considerando a opção de corte dos módulos secundários.
  * Saldo energético diário = Energia Gerada - Consumo Total.
  * Capacidade total acumulada nas baterias com saúde e carga operacionais.
* **Classificação do Cenário e Recomendação:**
  * **ESTÁVEL / SEGURA:** Saldo energético >= 0; a operação pode prosseguir normalmente.
  * **ALERTA (Sustentado por Baterias):** O consumo excede a geração solar, mas é coberto pelas baterias; recomendação para reduzir atividades no Laboratório ou realizar manutenção nos painéis.
  * **CRÍTICO (Risco de Colapso Energético):** Saldo e baterias insuficientes; recomendação para corte imediato de energia no Laboratório e redução do consumo no Habitat ao mínimo viável.

---

## Decisão Esperada

O sistema orienta a equipe de controle e a autonomia do robô para:
* Identificar quando interromper ou desacelerar a coleta de água com base no limite dos reservatórios.
* Detectar perdas de qualidade na água armazenada.
* Avaliar a autonomia hídrica da base em dias e orientar a redução de consumo em cenários de atenção ou críticos.
* Diagnosticar painéis solares obstruídos por poeira ou baterias degradadas.
* Simular o desligamento estratégico de módulos de baixa prioridade (Mineração e Depósito) para manter a integridade energética dos módulos essenciais.

---

## Relação entre os dois Programas Desenvolvidos

O **Programa 1** atua como uma **central de diagnóstico automatizada**, realizando a varredura completa da saúde dos componentes físicos e dos recursos armazenados (painéis solares, baterias, níveis/qualidade de reservatórios e autonomia global de água).

O **Programa 2** atua como um **simulador de tomada de decisão interativo**, permitindo ao operador testar hipóteses (como o ciclo solar em questão e o desligamento de cargas secundárias) para verificar o impacto no saldo energético e obter a melhor recomendação de ação antes que ocorra um colapso no sistema.

Juntos, formam uma solução completa de monitoramento e suporte à decisão, garantindo a sustentabilidade e a segurança da missão lunar.