# AVD-20262-pratica-streamlit — Video Game Analytics

Repositório da atividade prática de **Streamlit** da disciplina **Análise e Visualização de Dados (AVD 2026.2)** da **Cesar School**.

Desenvolvimento de aplicação interativa analítica baseada no dataset de **Video Game Sales**, construída com **Streamlit**, **Plotly** e **Pandas** a partir da Análise Exploratória de Dados (EDA) desenvolvida em aula.

---

## 🚀 Link da Aplicação no Streamlit Community Cloud

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://avd-20262-pratica-streamlit.streamlit.app)

> **Link do App:** [https://avd-20262-pratica-streamlit.streamlit.app](https://avd-20262-pratica-streamlit.streamlit.app)  
> *(Caso ainda esteja realizando o primeiro deploy, basta conectar este repositório no [share.streamlit.io](https://share.streamlit.io/) selecionando `app.py` como arquivo principal).*

**Link do Repositório GitHub:** [https://github.com/jaas5/AVD-20262-pratica-streamlit](https://github.com/jaas5/AVD-20262-pratica-streamlit)

---

## 📊 Estrutura dos Dashboards

A aplicação está organizada em duas abas integradas, permitindo alternar entre uma visão científica e uma visão executiva:

### 🔬 Dashboard 1: Laboratório de Distribuição e Correlação
Voltado para cientistas de dados e analistas explorarem as relações estatísticas do dataset:
- **Painel Lateral com Filtros Reativos:**
  - Seletor de variável quantitativa de vendas (`Global_Sales`, `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`).
  - Slider de intervalo temporal para exclusão de períodos específicos de lançamento.
  - Multiselects para filtragem dinâmica de Plataformas, Gêneros e Publicadoras.
- **Visualizações Mínimas Obrigatórias e Complementares:**
  - **Matriz de Correlação (Heatmap):** Cálculo não-paramétrico de Spearman entre todas as variáveis regionais de vendas.
  - **Histograma de Distribuição Univariada:** Visualização detalhada da variável selecionada, com linha indicadora de mediana e zoom até o percentil 95 para mitigar o impacto visual da assimetria extrema/cauda longa.
  - **Boxplot por Gênero:** Dispersão e quartis entre os diferentes gêneros de jogos.
  - **Ranking de Plataformas (Top 10):** Barras horizontais ordenadas pelo volume de vendas na métrica escolhida.
  - **Evolução Temporal das Vendas:** Gráfico de área interativo mostrando a trajetória anual do faturamento.

### 🎯 Dashboard 2: Painel Estratégico de KPIs (Público: Publishers)
Voltado especificamente para **Executivos e Gerentes de Publicação (Game Publishers e Diretores de Estúdio)** apoiarem decisões de alocação de orçamento e portfólio de lançamentos:
- **4 Métricas Principais (Cards de KPI):**
  1. **Receita Global Total ($ mi):** Faturamento acumulado no recorte filtrado.
  2. **Venda Média por Lançamento ($ mi/jogo):** Benchmark de produtividade unitária por título.
  3. **Taxa de Super Hits (%):** Proporção de títulos que romperam a barreira de 1 milhão de cópias vendidas.
  4. **Catálogo Mapeado:** Contagem total de jogos monitorados.
- **4 Visuais Estratégicos:**
  1. **Top 10 Publicadoras por Faturamento Global:** Gráfico de barras horizontais detalhando a concentração de receita nos grandes concorrentes.
  2. **Market Share Regional de Vendas:** Gráfico de rosca (*donut*) com fatias percentuais de América do Norte, Europa, Japão e Outras Regiões.
  3. **Eficiência de Gênero (Venda Média por Jogo):** Comparativo de rentabilidade média por título lançado entre os gêneros.
  4. **Ranking Dinâmico de Super Hits:** Tabela interativa dos maiores sucessos históricos com detalhes de vendas regionais.

---

## 📁 Estrutura de Arquivos e Entregáveis

```text
AVD-20262-pratica-streamlit/
├── .streamlit/
│   └── config.toml               # Identidade visual, tipografia e paleta minimalista
├── data/
│   ├── raw/                      # Dataset original (ignorado no git)
│   └── clean/
│       └── dataset.csv           # Dataset tratado na EDA e versionado para o deploy
├── entregas/
│   ├── rascunho_dashboard1.png   # Rascunho visual do Dashboard 1
│   ├── rascunho_dashboard2.png   # Rascunho visual do Dashboard 2
│   └── justificativa-metricas.md # Documento formal de justificativa do público e métricas
├── notebooks/
│   └── eda.ipynb                 # Notebook completo com a Análise Exploratória de Dados
├── prompts/
│   ├── declaracao-uso-ia.md      # Registro detalhado da utilização de ferramentas de IA
│   ├── layout-skeleton-prompt.md # Template de prompt do rascunho ao código
│   ├── rascunho_dashboard1.png   # Cópia do rascunho 1
│   ├── rascunho_dashboard2.png   # Cópia do rascunho 2
│   └── referencia_visual.jpg     # Referência estética de design moderno
├── src/
│   ├── __init__.py
│   └── data_loader.py            # Função unificada de carga de dados com cache @st.cache_data
├── app.py                        # Aplicação completa com os dois dashboards em abas
├── README.md                     # Documentação do projeto e instruções
└── requirements.txt              # Dependências do projeto
```

---

## 🛠️ Como Executar Localmente

### 1. Criar e ativar o ambiente virtual

**Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependências e rodar

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

---

## 🤖 Declaração de Uso de IA Generativa

O uso de Inteligência Artificial Generativa neste projeto segue rigorosamente o Plano de Ensino e a Política de Transparência da disciplina:
- **Transparência no Código:** Todo trecho gerado ou aprimorado com apoio de IA está expressamente identificado no código-fonte com a marcação `# [IA] <ferramenta> – <finalidade>`.
- **Autoria Individual das Decisões:** A definição do público-alvo (Publishers), a escolha das métricas (KPIs), as fórmulas de cálculo e a interpretação dos dados foram definidas e validadas individualmente pelo autor do projeto, conforme registrado em `entregas/justificativa-metricas.md`.
- **Registro Detalhado:** Todos os prompts, aceites e alterações encontram-se documentados em `prompts/declaracao-uso-ia.md`.
