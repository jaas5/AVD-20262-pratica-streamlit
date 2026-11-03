# AVD-20262-pratica-streamlit — Video Game Analytics

Repositório da atividade prática de **Streamlit** da disciplina **Análise e Visualização de Dados (AVD 2026.2)** da **Cesar School**.

Desenvolvimento de aplicação interativa analítica baseada no dataset de **Video Game Sales**, construída com **Streamlit**, **Plotly** e **Pandas** a partir da Análise Exploratória de Dados (EDA) desenvolvida em aula, apresentando interface moderna em **Dark Mode**.

---

## Link da Aplicação no Streamlit Community Cloud

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://avd-20262-pratica-app-video-game-sales.streamlit.app/)

> **Link do App publicado:** [https://avd-20262-pratica-app-video-game-sales.streamlit.app/](https://avd-20262-pratica-app-video-game-sales.streamlit.app/)

**Link do Repositório GitHub:** [https://github.com/jaas5/AVD-20262-pratica-streamlit](https://github.com/jaas5/AVD-20262-pratica-streamlit)

---

## Estrutura dos Dashboards

A aplicação está organizada em duas abas integradas, estruturadas na seguinte ordem:

### Dashboard 1: Laboratório de Correlação e Distribuição Quantitativa
Voltado estritamente para a análise das **variáveis quantitativas de vendas** (América do Norte, Europa, Japão, Outras Regiões e Vendas Globais):
- **Painel Lateral com Filtros Reativos:**
  - Seletor de variável quantitativa em foco (`NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`).
  - Slider de intervalo temporal para exclusão de períodos específicos de lançamento.
  - Multiselects para filtragem dinâmica de Plataformas, Gêneros e Publicadoras.
- **Visualizações Quantitativas e Boas Práticas:**
  - **Matriz de Correlação Triangular (Heatmap):** Cálculo não-paramétrico de Spearman exibindo apenas o triângulo inferior, eliminando a ambiguidade visual de simetria repetida.
  - **Histograma de Distribuição da Variável Selecionada:** Renderizado na sua respectiva **cor característica fixa**, com corte visual no percentil 95 para tratar a cauda longa de outliers da EDA e linha de mediana vertical destacada.
  - **Dispersão e Tendência Linear:** Gráfico de dispersão (*scatter plot*) da variável quantitativa em relação às Vendas Globais com reta de tendência linear (*numpy.polyfit*).
  - **Distribuição Comparativa das Quatro Regiões:** Comparativo visual das quatro variáveis regionais, cada uma com sua respectiva cor padronizada.

### Dashboard 2: Painel Estratégico de Negócios e KPIs (Público: Publishers)
Voltado especificamente para **Executivos e Gerentes de Publicação (Publishers)** avaliarem decisões de portfólio, plataformas e concorrência com boas práticas de visualização:
- **4 Métricas Principais (Cards de KPI com Glassmorphism):**
  1. **Receita Global Total ($ mi):** Faturamento acumulado no recorte filtrado.
  2. **Venda Média por Lançamento ($ mi/jogo):** Benchmark de produtividade unitária por título.
  3. **Taxa de Super Hits (%):** Proporção de títulos que romperam a barreira de 1 milhão de cópias vendidas.
  4. **Catálogo Mapeado:** Contagem total de jogos monitorados.
- **Visuais Estratégicos e de Mercado:**
  1. **Top 10 Publicadoras por Faturamento Global:** Gráfico de barras horizontais em tom uniforme e rótulos de texto de alto contraste.
  2. **Market Share Regional de Vendas:** Gráfico de rosca (*donut*) com fatias percentuais utilizando rigorosamente as **mesmas cores características** padronizadas das regiões (sem rosa).
  3. **Eficiência de Gênero (Venda Média por Jogo):** Comparativo de rentabilidade média unitária entre os gêneros.
  4. **Comparação por Gênero (Boxplot):** Dispersão e quartis de vendas globais por gênero (migrado do Dashboard 1).
  5. **Top 10 Plataformas em Faturamento:** Consoles líderes em faturamento global (migrado do Dashboard 1).
  6. **Evolução Temporal de Vendas Globais:** Trajetória histórica anual de lançamentos e receita (migrado do Dashboard 1).
  7. **Ranking Dinâmico de Super Hits:** Tabela interativa dos maiores sucessos históricos com dados de plataforma e publicadora.

---

## Estrutura de Arquivos e Entregáveis

```text
AVD-20262-pratica-streamlit/
├── .streamlit/
│   └── config.toml               # Identidade visual, tipografia e tema Dark Mode
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
│   ├── layout-skeleton-prompt.md # Template de prompt do rascunho ao código
│   ├── rascunho_dashboard1.png   # Rascunho 1
│   ├── rascunho_dashboard2.png   # Rascunho 2
│   ├── referencia_visual.jpg     # Referência estética de design moderno
│   └── Declaração de IA.pdf      # Declaração assinada de uso de IA
├── src/
│   ├── __init__.py
│   └── data_loader.py            # Função unificada de carga de dados com cache @st.cache_data
├── app.py                        # Aplicação completa com os dois dashboards em abas
├── README.md                     # Documentação do projeto e instruções
└── requirements.txt              # Dependências do projeto
```

---

## Como Executar Localmente

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

## Declaração de Uso de IA Generativa

O uso de Inteligência Artificial Generativa neste projeto segue rigorosamente o Plano de Ensino e a Política de Transparência da disciplina:
- **Transparência no Código:** Trechos desenvolvidos ou aprimorados com apoio de IA estão identificados no código-fonte com a marcação `# [IA] <ferramenta> – <finalidade>`.
- **Autoria Individual das Decisões:** A definição do público-alvo (Publishers), a escolha das métricas (KPIs), as fórmulas de cálculo e a interpretação dos dados foram definidas e validadas individualmente pelo autor do projeto, conforme registrado em `entregas/justificativa-metricas.md`.
- **Documento Assinado:** A declaração formal preenchida e assinada encontra-se na pasta `prompts/`.
