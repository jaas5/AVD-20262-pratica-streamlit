# Template: Rascunho de Layout → Esqueleto do App Streamlit

## Contexto
Aluno do curso da Cesar School na disciplina de Análise e Visualização de Dados (AVD 2026.2).  
Dataset: **Video Game Sales** com dados históricos tratados em `data/clean/dataset.csv`.  
Objetivo: Construir uma aplicação web analítica interativa no Streamlit estruturada em duas abas principais:
1. **Dashboard 1 (Laboratório de Distribuição e Correlação):** Exploração interativa de dispersão, histograma univariado, matriz de correlação de Spearman e evolução temporal de vendas.
2. **Dashboard 2 (Painel Estratégico de KPIs para Publishers):** Dashboard executivo voltado a gestores e diretores de publicadoras com 4 KPIs essenciais e 4 visualizações de suporte a decisões de negócio.

## Entrada
- Rascunho do Dashboard 1: `entregas/rascunho_dashboard1.png` (também em `prompts/rascunho_dashboard1.png`)
- Rascunho do Dashboard 2: `entregas/rascunho_dashboard2.png` (também em `prompts/rascunho_dashboard2.png`)
- Referência de Estilo Visual Moderno: `prompts/referencia_visual.jpg`
- Colunas do Dataset: `Rank`, `Name`, `Platform`, `Year`, `Genre`, `Publisher`, `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`.

## Restrições
- Construído com a biblioteca oficial **Streamlit** e gráficos interativos em **Plotly** (`plotly.express` / `plotly.graph_objects`).
- Leitura de dados obrigatória e unificada através de `src/data_loader.py` com cache `@st.cache_data`.
- Painel lateral (sidebar) com seletor de variáveis quantitativas e slider de intervalo de período/anos, além de multiselects para Plataforma, Gênero e Publicadora.
- Filtro de corte mínimo/máximo responsivo que atualiza os gráficos instantaneamente sem recarregar o dataset.
- Respeito à identidade visual do arquivo `.streamlit/config.toml` (paleta minimalista com tons `#638CA0`, `#C98279`, `#8DAA91`, `#C4A56E` e tipografia limpa).
- Todos os trechos desenvolvidos com apoio da IA devem conter o comentário obrigatório `# [IA] <ferramenta> – <finalidade>`.

## Formato de Saída
- Código completo de `app.py` modular, robusto, pronto para deploy no Streamlit Community Cloud sem erros e com tratamento de dados vazios.
