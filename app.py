# [IA] Gemini – Estrutura base da aplicação, importação de dependências e configuração de página
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.data_loader import load_data

# [IA] Gemini – Configuração da página e metadados no padrão do Streamlit
st.set_page_config(
    page_title="Video Game Analytics | Dashboards Estratégicos",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# [IA] Gemini – Paleta de cores coordenada com o tema (.streamlit/config.toml e referência visual)
PALETTE = {
    "primary": "#638CA0",
    "secondary": "#C98279",
    "accent_green": "#8DAA91",
    "accent_gold": "#C4A56E",
    "accent_purple": "#8D8BA8",
    "grid": "#E7ECEE",
    "text": "#27343A",
    "muted": "#64748B",
    "card_bg": "#FFFFFF",
}

SALES_COLUMNS = ["Global_Sales", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
SALES_LABELS = {
    "Global_Sales": "Vendas Globais",
    "NA_Sales": "América do Norte",
    "EU_Sales": "Europa",
    "JP_Sales": "Japão",
    "Other_Sales": "Outras Regiões",
}


# [IA] Gemini – Função auxiliar de estilização gráfica em Plotly para visual limpo e moderno
def format_chart(fig, height=360):
    fig.update_layout(
        height=height,
        margin=dict(l=16, r=16, t=28, b=16),
        font=dict(family="DM Sans, sans-serif", color=PALETTE["text"], size=12),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        hoverlabel=dict(bgcolor="#FFFFFF", bordercolor=PALETTE["grid"], font_size=12),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    fig.update_xaxes(showgrid=False, zeroline=False, linecolor=PALETTE["grid"])
    fig.update_yaxes(showgrid=True, gridcolor=PALETTE["grid"], zeroline=False)
    return fig


# [IA] Gemini – Carregamento e pré-processamento leve dos dados com cache
df_raw = load_data()
df = df_raw.copy()
if "Year" in df.columns:
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df = df.dropna(subset=["Year"])
    df["Year"] = df["Year"].astype(int)

# ---------------------------------------------------------
# [IA] Gemini – Sidebar: Controles e Filtros Interativos
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("## 🎮 **Game Analytics**")
    st.caption("Painel Analítico e Executivo de Vendas de Jogos")
    st.markdown("---")

    st.markdown("### ⚙️ **Filtros Globais**")

    # Filtro obrigatório de intervalo (Slider)
    ano_min, ano_max = int(df["Year"].min()), int(df["Year"].max())
    intervalo_anos = st.slider(
        "Período de lançamento (Ano)",
        min_value=ano_min,
        max_value=ano_max,
        value=(ano_min, ano_max),
        step=1,
        help="Filtra a base histórica pelo ano de lançamento dos títulos.",
    )

    # Filtros complementares por multiselect
    plataformas_disponiveis = sorted(df["Platform"].dropna().unique().tolist())
    plataformas_selecionadas = st.multiselect(
        "Plataformas",
        options=plataformas_disponiveis,
        placeholder="Todas as plataformas",
    )

    generos_disponiveis = sorted(df["Genre"].dropna().unique().tolist())
    generos_selecionados = st.multiselect(
        "Gêneros",
        options=generos_disponiveis,
        placeholder="Todos os gêneros",
    )

    publicadoras_disponiveis = sorted(df["Publisher"].dropna().unique().tolist())
    publicadoras_selecionadas = st.multiselect(
        "Publicadoras",
        options=publicadoras_disponiveis,
        placeholder="Todas as publicadoras",
    )

    st.markdown("---")
    # Filtro obrigatório do Dashboard 1: Seletor de Variável Quantitativa
    st.markdown("### 🔬 **Variável de Análise (Lab)**")
    variavel_analise = st.radio(
        "Selecione a região/métrica de vendas:",
        options=SALES_COLUMNS,
        format_func=lambda col: SALES_LABELS[col],
        index=0,
        help="Define a variável quantitativa em destaque no Laboratório de Distribuição.",
    )

    st.markdown("---")
    st.caption("💡 *Dica:* Utilize os filtros acima para simular nichos e períodos específicos.")

# [IA] Gemini – Aplicação dos filtros reativos no DataFrame
df_filtrado = df[df["Year"].between(intervalo_anos[0], intervalo_anos[1])]
if plataformas_selecionadas:
    df_filtrado = df_filtrado[df_filtrado["Platform"].isin(plataformas_selecionadas)]
if generos_selecionados:
    df_filtrado = df_filtrado[df_filtrado["Genre"].isin(generos_selecionados)]
if publicadoras_selecionadas:
    df_filtrado = df_filtrado[df_filtrado["Publisher"].isin(publicadoras_selecionadas)]

# ---------------------------------------------------------
# [IA] Gemini – Estrutura Principal: Abas dos 2 Dashboards
# ---------------------------------------------------------
tab_lab, tab_kpi = st.tabs([
    "🔬 Dashboard 1: Laboratório de Distribuição & Correlação",
    "🎯 Dashboard 2: Painel Estratégico de KPIs (Publishers)",
])

# =========================================================
# DASHBOARD 1: LABORATÓRIO DE DISTRIBUIÇÃO E CORRELAÇÃO
# =========================================================
with tab_lab:
    st.markdown("### 🔬 Laboratório de Análise Exploratória")
    st.caption(
        f"Avaliando a variável **{SALES_LABELS[variavel_analise]}** no período de **{intervalo_anos[0]} a {intervalo_anos[1]}**. "
        f"({len(df_filtrado):,} de {len(df):,} jogos filtrados)".replace(",", ".")
    )

    if df_filtrado.empty:
        st.warning("⚠️ Nenhum registro encontrado para a combinação de filtros selecionada. Ajuste as opções na barra lateral.")
    else:
        # [IA] Gemini – Linha 1: Heatmap de Correlação + Histograma de Distribuição Univariada
        col_corr, col_dist = st.columns([1, 1], gap="medium")

        with col_corr:
            with st.container(border=True):
                st.markdown("#### Matriz de Correlação entre Regiões")
                st.caption("Correlação não-paramétrica de Spearman (robusta a outliers)")

                # Cálculo de Spearman
                matriz_corr = df_filtrado[SALES_COLUMNS].corr(method="spearman")
                matriz_corr.index = [SALES_LABELS[c] for c in matriz_corr.index]
                matriz_corr.columns = [SALES_LABELS[c] for c in matriz_corr.columns]

                fig_corr = px.imshow(
                    matriz_corr,
                    text_auto=".2f",
                    color_continuous_scale=[PALETTE["primary"], "#FFFFFF", PALETTE["secondary"]],
                    zmin=-1,
                    zmax=1,
                    aspect="auto",
                )
                fig_corr.update_coloraxes(colorbar_title="Spearman")
                format_chart(fig_corr, height=360)
                st.plotly_chart(fig_corr, use_container_width=True)

        with col_dist:
            with st.container(border=True):
                st.markdown(f"#### Distribuição: {SALES_LABELS[variavel_analise]}")
                st.caption("Histograma com recorte visual no percentil 95 para tratar cauda longa")

                # Zoom até percentil 95 conforme descoberto na EDA
                p95 = df_filtrado[variavel_analise].quantile(0.95)
                dados_zoom = df_filtrado[df_filtrado[variavel_analise] <= p95]

                media_var = df_filtrado[variavel_analise].mean()
                mediana_var = df_filtrado[variavel_analise].median()

                fig_hist = px.histogram(
                    dados_zoom,
                    x=variavel_analise,
                    nbins=35,
                    color_discrete_sequence=[PALETTE["primary"]],
                    labels={variavel_analise: f"{SALES_LABELS[variavel_analise]} (milhões de cópias)", "count": "Quantidade de Jogos"},
                )
                fig_hist.add_vline(
                    x=mediana_var,
                    line_dash="dash",
                    line_color=PALETTE["secondary"],
                    annotation_text=f"Mediana: {mediana_var:.2f}M",
                    annotation_position="top right",
                )
                fig_hist.update_traces(hovertemplate="Faixa de Vendas: %{x:.2f}M<br>Jogos: %{y}<extra></extra>")
                format_chart(fig_hist, height=360)
                st.plotly_chart(fig_hist, use_container_width=True)

        # [IA] Gemini – Linha 2: Boxplot por Gênero + Top Plataformas
        col_box, col_plat = st.columns([1, 1], gap="medium")

        with col_box:
            with st.container(border=True):
                st.markdown(f"#### Comparação por Gênero: {SALES_LABELS[variavel_analise]}")
                st.caption("Dispersão e quartis entre os diferentes gêneros de jogos")

                fig_box = px.box(
                    dados_zoom,
                    x="Genre",
                    y=variavel_analise,
                    color_discrete_sequence=[PALETTE["primary"]],
                    labels={"Genre": "Gênero", variavel_analise: f"{SALES_LABELS[variavel_analise]} (mi)"},
                )
                fig_box.update_traces(boxpoints=False)
                fig_box.update_xaxes(tickangle=-35)
                format_chart(fig_box, height=380)
                st.plotly_chart(fig_box, use_container_width=True)

        with col_plat:
            with st.container(border=True):
                st.markdown(f"#### Top 10 Plataformas: {SALES_LABELS[variavel_analise]}")
                st.caption("Consoles e plataformas com maior volume de vendas")

                top_plat = (
                    df_filtrado.groupby("Platform", as_index=False)[variavel_analise]
                    .sum()
                    .nlargest(10, variavel_analise)
                    .sort_values(variavel_analise, ascending=True)
                )

                fig_plat = px.bar(
                    top_plat,
                    x=variavel_analise,
                    y="Platform",
                    orientation="h",
                    text_auto=".1f",
                    color_discrete_sequence=[PALETTE["secondary"]],
                    labels={"Platform": "Plataforma", variavel_analise: f"{SALES_LABELS[variavel_analise]} (mi)"},
                )
                fig_plat.update_traces(hovertemplate="Plataforma: %{y}<br>Total: %{x:.2f}M cópias<extra></extra>")
                format_chart(fig_plat, height=380)
                st.plotly_chart(fig_plat, use_container_width=True)

        # [IA] Gemini – Linha 3: Evolução Temporal das Vendas
        with st.container(border=True):
            st.markdown(f"#### Evolução Histórica de Lançamentos e Vendas ({SALES_LABELS[variavel_analise]})")
            st.caption("Curva de volume de vendas anuais ao longo das décadas")

            evolucao_anual = (
                df_filtrado.groupby("Year", as_index=False)[variavel_analise]
                .sum()
                .sort_values("Year")
            )

            fig_evol = px.area(
                evolucao_anual,
                x="Year",
                y=variavel_analise,
                markers=True,
                color_discrete_sequence=[PALETTE["primary"]],
                labels={"Year": "Ano de Lançamento", variavel_analise: f"Vendas ({SALES_LABELS[variavel_analise]} em mi)"},
            )
            fig_evol.update_traces(hovertemplate="Ano: %{x}<br>Vendas: %{y:.1f}M<extra></extra>")
            fig_evol.update_xaxes(dtick=2)
            format_chart(fig_evol, height=300)
            st.plotly_chart(fig_evol, use_container_width=True)


# =========================================================
# DASHBOARD 2: PAINEL ESTRATÉGICO DE KPIS (PUBLISHERS)
# =========================================================
with tab_kpi:
    st.markdown("### 🎯 Painel Estratégico de Tomada de Decisão")
    st.caption(
        "Visão executiva voltada a **Lideranças e Gerentes de Publicação (Publishers)** "
        "para identificação de oportunidades de mercado, alocação de investimentos e mitigação de risco."
    )

    if df_filtrado.empty:
        st.warning("⚠️ Nenhum registro encontrado para a combinação de filtros selecionada.")
    else:
        # [IA] Gemini – Cálculo dos 4 KPIs validados individualmente pelo aluno
        receita_total_global = df_filtrado["Global_Sales"].sum()
        total_jogos = len(df_filtrado)
        venda_media_jogo = df_filtrado["Global_Sales"].mean() if total_jogos > 0 else 0
        super_hits = df_filtrado[df_filtrado["Global_Sales"] >= 1.0]
        taxa_super_hits = (len(super_hits) / total_jogos * 100) if total_jogos > 0 else 0

        # [IA] Gemini – 4 Cards de Métricas em Destaque (st.metric)
        col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)

        with col_kpi1:
            with st.container(border=True):
                st.metric(
                    label="Receita Global Total",
                    value=f"{receita_total_global:,.1f}M".replace(",", "."),
                    help="Soma total de vendas globais dos jogos filtrados.",
                )
                st.caption("Volume acumulado de faturamento")

        with col_kpi2:
            with st.container(border=True):
                st.metric(
                    label="Venda Média / Jogo",
                    value=f"{venda_media_jogo:.2f}M cópias",
                    help="Média de cópias vendidas por título lançado.",
                )
                st.caption("Benchmark de produtividade unitária")

        with col_kpi3:
            with st.container(border=True):
                st.metric(
                    label="Taxa de Super Hits",
                    value=f"{taxa_super_hits:.1f}%",
                    help="Percentual de jogos que ultrapassaram a marca de 1 milhão de unidades vendidas.",
                )
                st.caption(f"{len(super_hits):,} títulos com >1M de vendas".replace(",", "."))

        with col_kpi4:
            with st.container(border=True):
                st.metric(
                    label="Catálogo Mapeado",
                    value=f"{total_jogos:,}".replace(",", "."),
                    help="Total de títulos que atendem aos filtros ativos.",
                )
                st.caption(f"De {len(df):,} títulos históricos".replace(",", "."))

        st.markdown("")

        # [IA] Gemini – Visual 1 e Visual 2: Top Publicadoras e Market Share Regional
        col_pub, col_share = st.columns([1.1, 0.9], gap="medium")

        with col_pub:
            with st.container(border=True):
                st.markdown("#### 🏆 Top 10 Publicadoras por Faturamento Global")
                st.caption("Concentração de mercado entre as maiores empresas concorrentes")

                top_publishers = (
                    df_filtrado.groupby("Publisher", as_index=False)["Global_Sales"]
                    .sum()
                    .nlargest(10, "Global_Sales")
                    .sort_values("Global_Sales", ascending=True)
                )

                fig_pubs = px.bar(
                    top_publishers,
                    x="Global_Sales",
                    y="Publisher",
                    orientation="h",
                    text_auto=".1f",
                    color_discrete_sequence=[PALETTE["primary"]],
                    labels={"Publisher": "Publicadora", "Global_Sales": "Vendas Globais (milhões)"},
                )
                fig_pubs.update_traces(hovertemplate="Publicadora: %{y}<br>Vendas: %{x:.2f}M cópias<extra></extra>")
                format_chart(fig_pubs, height=370)
                st.plotly_chart(fig_pubs, use_container_width=True)

        with col_share:
            with st.container(border=True):
                st.markdown("#### 🌍 Market Share por Região de Vendas")
                st.caption("Divisão percentual do volume de vendas acumulado")

                regioes = {
                    "América do Norte": df_filtrado["NA_Sales"].sum(),
                    "Europa": df_filtrado["EU_Sales"].sum(),
                    "Japão": df_filtrado["JP_Sales"].sum(),
                    "Outras Regiões": df_filtrado["Other_Sales"].sum(),
                }
                df_share = pd.DataFrame(list(regioes.items()), columns=["Região", "Vendas"])

                fig_donut = px.pie(
                    df_share,
                    names="Região",
                    values="Vendas",
                    hole=0.55,
                    color="Região",
                    color_discrete_map={
                        "América do Norte": PALETTE["primary"],
                        "Europa": PALETTE["secondary"],
                        "Japão": PALETTE["accent_green"],
                        "Outras Regiões": PALETTE["accent_gold"],
                    },
                )
                fig_donut.update_traces(
                    textposition="inside",
                    textinfo="percent+label",
                    hovertemplate="%{label}: %{value:.1f}M cópias (%{percent})<extra></extra>",
                )
                format_chart(fig_donut, height=370)
                st.plotly_chart(fig_donut, use_container_width=True)

        # [IA] Gemini – Visual 3 e Visual 4: Eficiência por Gênero e Ranking de Super Hits
        col_gen_eff, col_table = st.columns([1, 1], gap="medium")

        with col_gen_eff:
            with st.container(border=True):
                st.markdown("#### 💡 Eficiência de Gênero: Venda Média por Jogo")
                st.caption("Gêneros com melhor retorno médio unitário por lançamento")

                eficiencia_genero = (
                    df_filtrado.groupby("Genre", as_index=False)
                    .agg(Venda_Media=("Global_Sales", "mean"), Quantidade=("Global_Sales", "count"))
                    .sort_values("Venda_Media", ascending=True)
                )

                fig_eff = px.bar(
                    eficiencia_genero,
                    x="Venda_Media",
                    y="Genre",
                    orientation="h",
                    text_auto=".2f",
                    color_discrete_sequence=[PALETTE["secondary"]],
                    labels={"Genre": "Gênero", "Venda_Media": "Venda Média por Jogo (mi)"},
                )
                fig_eff.update_traces(hovertemplate="Gênero: %{y}<br>Média por Jogo: %{x:.2f}M<extra></extra>")
                format_chart(fig_eff, height=380)
                st.plotly_chart(fig_eff, use_container_width=True)

        with col_table:
            with st.container(border=True):
                st.markdown("#### ⭐ Ranking de Super Hits (Top Títulos)")
                st.caption("Títulos de maior impacto comercial e tração histórica")

                cols_display = ["Name", "Platform", "Publisher", "Year", "Global_Sales", "NA_Sales", "EU_Sales", "JP_Sales"]
                df_top_hits = df_filtrado.nlargest(10, "Global_Sales")[cols_display].copy()
                df_top_hits.columns = ["Título", "Plat.", "Publicadora", "Ano", "Global (M)", "NA (M)", "EU (M)", "JP (M)"]

                st.dataframe(
                    df_top_hits,
                    use_container_width=True,
                    hide_index=True,
                    height=340,
                )

# [IA] Gemini – Rodapé Informativo e Conformidade Acadêmica
st.markdown("---")
st.caption(
    "📊 **Projeto Prático AVD 2026.2 — Cesar School** | "
    "Desenvolvido com Streamlit e Plotly. Dados tratados a partir da Análise Exploratória de Dados (EDA) em `notebooks/eda.ipynb`."
)
