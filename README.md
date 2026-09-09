# Ficha da Missão
## Sistema de Suporte à Decisão Energética para Robôs Lunares de Coleta de Água

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

* **Nome:** Sistema de Suporte à Decisão Energética - Módulo de Diagnóstico e Simulação para o Robô Lunar Autônomo.
* **Tema:** Autonomia energética (geração solar e baterias) aplicada à missão de exploração e coleta de água descrita no roteiro do projeto, na qual dois robôs cooperam por meio de um posto intermediário de recarga.

---

## Objetivo

O roteiro do projeto define que a maior ameaça à missão é o robô ficar sem energia longe do posto de recarga — seja pela degradação dos painéis solares (poeira lunar), pela perda de saúde das baterias, ou pelo consumo excessivo dos módulos do sistema.

Nosso objetivo é resolver exatamente esse problema: transformar os dados brutos do kit em diagnóstico de saúde energética e em uma recomendação de ação clara, para apoiar a decisão de continuar a missão, reduzir consumo ou retornar ao posto de recarga.

---

## Dados Selecionados

* **`geracao_solar`**: Geração x consumo de energia, poeira acumulada e temperatura dos painéis a cada ciclo. Usado porque o roteiro aponta a poeira lunar e a eficiência dos painéis como o principal risco à autonomia energética (item 7 do roteiro).
* **`baterias`**: Capacidade, carga e saúde de cada unidade. Usado porque o roteiro exige acompanhamento constante do nível da bateria para evitar que um robô fique sem energia longe do posto de recarga (item 2 do roteiro).
* **`consumo_recursos`**: Consumo de água e energia por módulo (Habitat, Laboratório, Mineração, Médico, Comunicação, Depósito) e sua prioridade. Usado para simular o corte seletivo de módulos de baixa prioridade quando a energia disponível for insuficiente.

> *Nota: As bases de reservatórios e mapa de prioridades não foram usadas nesta etapa, pois o foco escolhido foi o eixo energético (geração, armazenamento e consumo), que é o gargalo identificado no roteiro para viabilizar a coleta de água.*

---

## Indicadores

### Programa 1: Diagnóstico (`analise_solar` e `analise_bateria`)
* **Ganho de eficiência de geração solar:** $	ext{Ganho (\%)} = \left(rac{	ext{geração\_kw}}{	ext{consumo\_kw}} 	imes 100
ight) - 100$, classificado em **NORMAL**, **ATENÇÃO** ou **CRÍTICO**.
* **Índice de obstrução por poeira:** $rac{	ext{geração\_kw}}{	ext{poeira\_pct}}$, classificado em **NORMAL**, **ATENÇÃO** ou **CRÍTICO**.
* **Eficiência da bateria em relação à saúde:** $rac{	ext{capacidade\_kwh}}{	ext{saude\_pct}}$, classificado em **NORMAL**, **ATENÇÃO** ou **CRÍTICO**, com alerta final para troca de baterias degradadas.

### Programa 2: Simulação de Decisão (`simulador_decisao`)
* Energia gerada no ciclo escolhido e consumo total estimado (com opção de desligar módulos de prioridade 3).
* Saldo energético diário ($	ext{geração} - 	ext{consumo}$) e energia total disponível nas baterias.
* **Classificação do cenário:** **ESTÁVEL/SEGURA**, **ALERTA** (sustentado por baterias) ou **CRÍTICO** (risco de colapso energético).

---

## Decisão Esperada

O sistema deverá indicar, para cada ciclo solar simulado, se a operação pode prosseguir normalmente, se é necessário reduzir atividades (por exemplo, no Laboratório) e realizar manutenção dos painéis, ou se é preciso cortar imediatamente o consumo de módulos não essenciais e priorizar o retorno ao posto de recarga, reproduzindo em código o comportamento de segurança descrito no item 9 do roteiro (avisos por energia, distância e obstáculos).

---

## Relação entre os dois Programas Desenvolvidos

O **Programa 1** funciona como diagnóstico de saúde dos componentes físicos (painéis solares e baterias), avaliando ciclo a ciclo e bateria a bateria, se estão operando em condição normal, de atenção ou crítica.

O **Programa 2** usa esses mesmos dados de `geracao_solar` e `baterias` agora somados ao consumo dos módulos (`consumo_recursos`) para simular uma decisão operacional concreta diante de uma entrada do usuário (ciclo escolhido e opção de desligar módulos secundários).

Juntos, os dois programas formam o sistema de avisos e segurança descrito no roteiro: o Programa 1 identifica quando um componente está se degradando, e o Programa 2 traduz essa condição em uma recomendação de ação para a missão continuar com segurança.
