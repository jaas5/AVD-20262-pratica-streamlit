# Justificativa de Métricas e Visuais — Dashboard 2 (KPIs)

**Disciplina:** Análise e Visualização de Dados (AVD 2026.2) — Cesar School  
**Projeto:** Aplicação Streamlit com Dashboards de Video Game Sales  
**Aluno:** Jarbas Esteves  
**Dataset:** Video Game Sales (`data/clean/dataset.csv`)  

---

## 1. Definição do Público-Alvo

**Público-alvo escolhido:** **Executivos e Gerentes de Publicação (Publishers / Game Studio Directors)**.

### Por que esse público?
No ecossistema de desenvolvimento e publicação de videogames, decisões estratégicas de alocação de capital e equipe dependem de dados consolidados de desempenho comercial histórico. Executivos de publicadoras precisam responder a questões críticas de negócio, tais como:
- Quais mercados regionais concentram a maior fatia da receita histórica?
- Quais gêneros oferecem maior retorno médio por título publicado (eficiência de portfólio), além do faturamento bruto?
- Qual é a taxa de conversão em "super hits" (> 1 milhão de unidades vendidas), mitigando o risco de projetos que não cobrem custos operacionais?
- Quais são os principais competidores diretos no mercado e qual o benchmark dos jogos mais bem-sucedidos da história?

Este painel foi estruturado para fornecer uma visão executiva clara, sintética e acionável, permitindo simulações interativas através dos filtros de período, plataforma, gênero e publicadora.

---

## 2. Métricas do Dashboard 2 (KPIs)

Foram selecionadas **4 métricas essenciais** exibidas em destaque no topo do painel:

| # | Métrica | Cálculo / Definição | Justificativa de Negócio para o Público-Alvo |
|---|---|---|---|
| 1 | **Receita Global Total ($ mi)** | Soma de `Global_Sales` no período/filtros selecionados. | Avalia o tamanho absoluto do mercado ou do segmento filtrado, fornecendo a dimensão monetária total movimentada. |
| 2 | **Venda Média por Lançamento ($ mi/jogo)** | Média aritmética (`mean()`) de `Global_Sales` dos jogos no segmento. | Permite medir a **produtividade e rentabilidade unitária média** esperada por projeto, evitando ilusões causadas apenas pelo volume bruto de lançamentos. |
| 3 | **Taxa de Super Hits (%)** | Percentual de jogos com `Global_Sales >= 1.0` milhão de unidades sobre o total filtrado. | O mercado de games opera fortemente no modelo de distribuição assimétrica (*power-law* e cauda longa). Saber a probabilidade de um título atingir o patamar de super hit é o principal indicador de apetite ao risco financeiro. |
| 4 | **Total de Títulos Mapeados** | Contagem (`count()`) de registros únicos de jogos. | Contextualiza a base amostral e o volume de concorrência ativa no recorte escolhido. |

---

## 3. Visuais do Dashboard 2

Além dos 4 cards de KPIs no topo, o dashboard apresenta **4 visuais estratégicos integrados**:

### Visual 1: Top 10 Publicadoras por Faturamento Global (Gráfico de Barras Horizontais)
- **Objetivo:** Mapear os líderes de mercado e a concentração de receita entre os maiores concorrentes (ex.: Nintendo, EA, Activision, Sony).
- **Decisão visual:** Barras horizontais ordenadas de forma decrescente com rótulos numéricos diretos facilitam a comparação rápida de market share entre concorrentes.

### Visual 2: Market Share Regional de Vendas (Gráfico de Rosca / Donut)
- **Objetivo:** Mostrar a composição geográfica da receita (América do Norte, Europa, Japão e Outras Regiões).
- **Decisão visual:** O gráfico de rosca exibe a fatia percentual de cada mercado sobre o total global, orientando a estratégia de localização de idioma, campanhas de marketing regional e logística de distribuição física vs. digital.

### Visual 3: Eficiência: Venda Média por Jogo por Gênero (Gráfico de Barras)
- **Objetivo:** Demonstrar quais categorias de jogos trazem o maior retorno médio por lançamento.
- **Decisão visual:** Enquanto gêneros como "Ação" têm grande faturamento bruto em função do enorme número de títulos lançados, gêneros como "Plataforma" e "Shooter" historicamente apresentam média de vendas por título muito superior, sinalizando nichos mais lucrativos por unidade investida.

### Visual 4: Ranking Dinâmico de Super Hits (Tabela Executiva de Destaques)
- **Objetivo:** Exibir os títulos de maior impacto comercial dentro do filtro estabelecido, com dados de plataforma, publicadora e vendas por região.
- **Decisão visual:** Tabela interativa com formatação monetária limpa, permitindo que a liderança inspecione rapidamente os casos de sucesso extremo e identifique padrões de franquias e parcerias bem-sucedidas.

---

## 4. Integração com os Rascunhos

- O rascunho visual do Dashboard 1 encontra-se em `entregas/rascunho_dashboard1.png` e `prompts/rascunho_dashboard1.png`.
- O rascunho visual do Dashboard 2 encontra-se em `entregas/rascunho_dashboard2.png` e `prompts/rascunho_dashboard2.png`.
- A implementação no `app.py` respeita rigorosamente essa arquitetura visual e as restrições da atividade prática da disciplina.
