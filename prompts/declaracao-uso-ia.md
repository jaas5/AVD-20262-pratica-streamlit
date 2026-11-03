# Declaração de Uso de Inteligência Artificial Generativa

**Atividade:** Streamlit AVD – 2026.2 – Dashboards com Streamlit (Aulas 21 a 23)  
**Instituição:** Cesar School  
**Disciplina:** Análise e Visualização de Dados (AVD)  

---

## 1. Identificação

| Campo | Preenchimento |
|---|---|
| **Turma** | ☐ 5A ☒ 5B |
| **Nome Completo** | Jarbas Esteves |
| **E-mail** | jarbasneto8@gmail.com |
| **Repositório (link)** | [https://github.com/jaas5/AVD-20262-pratica-streamlit](https://github.com/jaas5/AVD-20262-pratica-streamlit) |
| **Data de entrega** | 03/11/2026 |

---

## 2. Declaração Geral

- [ ] Não utilizei nenhuma ferramenta de IA generativa em nenhuma etapa do projeto.
- [x] **Utilizei IA generativa, somente nas situações permitidas, e registrei todos os usos nas seções abaixo.**

---

## 3. Ferramentas Utilizadas

| Ferramenta | Versão / Plano | Em que parte da atividade |
|---|---|---|
| **Gemini / Antigravity Assistant** | Gemini 3.8 | Esqueleto do `app.py`, sintaxe de gráficos Plotly, geração de wireframe do Dashboard 2, estilização do layout e documentação |
| **Streamlit Skills** | Oficial Streamlit CLI | Orientação de boas práticas de componentes, layout e cache (`@st.cache_data`) |

---

## 4. Registro de Usos (Bloco a Bloco)

### Uso nº 1
- **Data:** 03/11/2026
- **Ferramenta:** Gemini / Antigravity
- **Parte da atividade:** `app.py` (Estrutura e layout com abas)
- **Finalidade (Permitida):** Gerar o esqueleto do `app.py` a partir do rascunho de layout usando o template de prompt.
- **O que foi pedido:** Estruturar a aplicação com duas abas principais (`st.tabs`), sendo a primeira um laboratório de correlação e distribuição, e a segunda um painel de KPIs executivo, com barra lateral de filtros reativos (slider de ano, seletor de variável e multiselects).
- **O que foi aproveitado e o que foi modificado:** Foi aproveitada a arquitetura em abas e os containers com borda (`st.container(border=True)`). Ajustei o encadeamento dos filtros para garantir que filtros vazios não excluíssem dados e configurei a resposta para quando a filtragem resultar em zero registros.
- **Como verifiquei que estava correto:** Executei localmente via `streamlit run app.py` e testei a reatividade ao mover o slider e alternar as abas no navegador.

### Uso nº 2
- **Data:** 03/11/2026
- **Ferramenta:** Gemini / Antigravity
- **Parte da atividade:** Sintaxe de visualização dos gráficos (`app.py`)
- **Finalidade (Permitida):** Apoio com a sintaxe de bibliotecas de visualização (Plotly Express e Graph Objects).
- **O que foi pedido:** Sintaxe correta para criar a matriz de correlação com escala customizada, histograma com marcação de mediana, gráfico de rosca (donut chart) com percentuais internos e gráficos de barras horizontais ordenadas.
- **O que foi aproveitado e o que foi modificado:** Aproveitei os templates de código do Plotly. Modifiquei as cores para que seguissem estritamente os tons sóbrios definidos no `.streamlit/config.toml` (`#638CA0`, `#C98279`, `#8DAA91`) e formatei os tooltips com `hovertemplate` amigável em português.
- **Como verifiquei que estava correto:** Inspecionei visualmente cada gráfico renderizado, conferindo se os valores batiam exatamente com a agregação manual no pandas.

### Uso nº 3
- **Data:** 03/11/2026
- **Ferramenta:** Gemini / Antigravity
- **Parte da atividade:** Geração do wireframe mockup (`entregas/rascunho_dashboard2.png`)
- **Finalidade (Permitida):** Apoio na criação de identidade visual e rascunho de layout do Dashboard 2.
- **O que foi pedido:** Script para gerar uma imagem de wireframe do Dashboard 2 respeitando o layout de 4 cards de KPIs no topo, dois gráficos intermediários (barras de publishers e donut de mercado) e dois gráficos inferiores (eficiência de gênero e ranking de super hits).
- **O que foi aproveitado e o que foi modificado:** Aproveitei o desenho gerado em Pillow/Matplotlib. Ajustei os textos dos cards para refletir com fidelidade as métricas escolhidas por mim e mantive o arquivo na pasta `entregas/` e `prompts/`.
- **Como verifiquei que estava correto:** Abri a imagem gerada e validei a hierarquia visual frente à referência estética moderna (`prompts/referencia_visual.jpg`).

---

## 5. Trechos de Código Feitos com Apoio de IA

| Arquivo / parte | Teve apoio de IA? | Tipo de apoio |
|---|---|---|
| `app.py` (esqueleto) | ☒ Sim ☐ Não | Estruturação de abas, sidebar e containers com base nas skills do Streamlit |
| Dashboard 1 (correlação + distribuição) | ☒ Sim ☐ Não | Sintaxe de `px.imshow`, `px.histogram` com anotação vertical e boxplot |
| Dashboard 2 (KPIs) | ☒ Sim ☐ Não | Sintaxe de `st.metric`, donut chart (`px.pie`) e tabela formatada |
| Deploy / configuração | ☒ Sim ☐ Não | Validação de dependências no `requirements.txt` e configuração do `config.toml` |

---

## 6. Reflexão Individual (10 linhas)

A Inteligência Artificial Generativa atuou como um tutor técnico e acelerador de desenvolvimento de interface, auxiliando na sintaxe específica de componentes do Streamlit e de estilizações gráficas com Plotly Express. Durante a elaboração do Dashboard 2, a IA sugeriu inicialmente diferentes conjuntos genéricos de indicadores para o público de investidores, mas rejeitei propostas que não conversavam diretamente com as particularidades observadas na minha Análise Exploratória de Dados (EDA). 

Para garantir a autoria e relevância do trabalho, decidi focar no público de **Executivos e Gerentes de Publicação (Publishers)** e selecionei intencionalmente as métricas de Eficiência por Gênero (Venda Média por Lançamento) e a Taxa de Super Hits (> 1 milhão de cópias). Essa escolha reflete diretamente a forte assimetria positiva (*power-law*) e a presença de outliers legítimos comprovados nos testes estatísticos da EDA. Todos os cálculos agregados foram validados manualmente contra os resultados obtidos no notebook, assegurando que o painel final representa minha própria visão analítica do negócio de games.

---

## 7. Termo de Responsabilidade

Declaro que as informações deste documento são verdadeiras e completas; que compreendo e sei explicar todo o código, as saídas e as análises entregues, inclusive os trechos feitos com apoio de IA; e que estou ciente de que uso não declarado, uso proibido, Skill não declarada, ou incapacidade de explicar o trabalho resultam nas consequências estabelecidas nas diretrizes da disciplina.

- **Nome:** Jarbas Esteves
- **Assinatura:** Jarbas Esteves *(Assinatura Digital / Declaração Submetida via Repositório e Classroom)*
- **Data:** 03/11/2026
