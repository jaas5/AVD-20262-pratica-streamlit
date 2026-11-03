# [IA] Gemini – Estrutura base da aplicação, importação de dependências e configuração de página
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.data_loader import load_data

# [IA] Gemini – Configuração da página e metadados no padrão do Streamlit
st.set_page_config(
    page_title="Video Game Analytics | Dark Edition",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# [IA] Gemini – Injeção de CSS Customizado para Tema Dark Mode com Gradientes e Efeito Glassmorphism
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Fundo com gradiente radial sutil */
    .stApp {
        background: radial-gradient(circle at 15% 15%, rgba(99, 102, 241, 0.08) 0%, transparent 45%),
                    radial-gradient(circle at 85% 85%, rgba(56, 189, 248, 0.06) 0%, transparent 45%),
                    #0B0F19 !important;
        color: #E2E8F0 !important;
    }

    /* Barra lateral estilizada em degradê escuro */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F1524 0%, #0B0F19 100%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
    }

    /* Título principal com gradiente luminoso */
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF 15%, #A5B4FC 55%, #38BDF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.025em;
        margin-bottom: 0.2rem;
    }

    .hero-subtitle {
        color: #94A3B8;
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
    }

    /* Cards de KPI Customizados com Efeito Glass e Gradiente Superior */
    .kpi-container {
        background: linear-gradient(135deg, rgba(19, 26, 42, 0.75) 0%, rgba(15, 21, 36, 0.85) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 1.25rem 1.4rem;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(12px);
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.35);
        transition: all 0.25s ease-in-out;
        margin-bottom: 0.5rem;
    }

    .kpi-container:hover {
        transform: translateY(-3px);
        border-color: rgba(99, 102, 241, 0.45);
        box-shadow: 0 10px 30px -4px rgba(99, 102, 241, 0.25);
    }

    .kpi-bar {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3.5px;
    }

    .bar-indigo { background: linear-gradient(90deg, #6366F1, #818CF8); }
    .bar-cyan { background: linear-gradient(90deg, #38BDF8, #0EA5E9); }
    .bar-emerald { background: linear-gradient(90deg, #10B981, #34D399); }
    .bar-purple { background: linear-gradient(90deg, #A855F7, #EC4899); }

    .kpi-title {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #94A3B8;
        margin-bottom: 0.4rem;
    }

    .kpi-val {
        font-size: 1.85rem;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -0.02em;
        line-height: 1.2;
        margin-bottom: 0.3rem;
    }

    .kpi-sub {
        font-size: 0.8rem;
        color: #64748B;
        font-weight: 500;
    }

    /* Cards e Containers com Borda Arredondada */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(135deg, rgba(19, 26, 42, 0.65) 0%, rgba(15, 21, 36, 0.75) 100%) !important;
        border: 1px solid rgba(255, 255, 255, 0.07) !important;
        border-radius: 14px !important;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.25) !important;
        backdrop-filter: blur(12px) !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(99, 102, 241, 0.3) !important;
        box-shadow: 0 8px 25px -2px rgba(0, 0, 0, 0.4) !important;
    }

    /* Customização das Abas (Pill Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(15, 21, 36, 0.75);
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.07);
        margin-bottom: 1.5rem;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 8px 20px;
        color: #94A3B8;
        font-weight: 600;
        font-size: 0.92rem;
        border: none !important;
        background: transparent;
        transition: all 0.2s ease;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 18px rgba(99, 102, 241, 0.4);
    }

    .stTabs [data-baseweb="tab-highlight"] {
        display: none;
    }

    /* Divisórias suaves */
    hr {
        border-color: rgba(255, 255, 255, 0.06) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# [IA] Gemini – Paleta de Cores Dark Mode vibrante e elegante
PALETTE = {
    "primary": "#6366F1",       # Indigo elétrico
    "secondary": "#38BDF8",     # Cyan brilhante
    "accent_rose": "#EC4899",   # Rosa magenta
    "accent_green": "#10B981",  # Verde esmeralda
    "accent_gold": "#F59E0B",   # Âmbar dourado
    "accent_purple": "#A855F7", # Roxo neon
    "bg_dark": "#0B0F19",
    "card_dark": "#131A2A",
    "grid": "rgba(255, 255, 255, 0.07)",
    "text": "#E2E8F0",
    "text_muted": "#94A3B8",
}

SALES_COLUMNS = ["Global_Sales", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
SALES_LABELS = {
    "Global_Sales": "Vendas Globais",
    "NA_Sales": "América do Norte",
    "EU_Sales": "Europa",
    "JP_Sales": "Japão",
    "Other_Sales": "Outras Regiões",
}


# [IA] Gemini – Função auxiliar de estilização gráfica em Plotly configurada para Dark Mode
def format_chart(fig, height=360):
    fig.update_layout(
        height=height,
        margin=dict(l=16, r=16, t=28, b=16),
        font=dict(family="Plus Jakarta Sans, DM Sans, sans-serif", color=PALETTE["text"], size=12),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        hoverlabel=dict(
            bgcolor="#1E293B",
            bordercolor="rgba(255, 255, 255, 0.15)",
            font_size=12,
            font_color="#F8FAFC",
            font_family="Plus Jakarta Sans, sans-serif",
        ),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color=PALETTE["text_muted"])),
    )
    fig.update_xaxes(showgrid=False, zeroline=False, linecolor=PALETTE["grid"], tickfont=dict(color=PALETTE["text_muted"]))
    fig.update_yaxes(showgrid=True, gridcolor=PALETTE["grid"], zeroline=False, tickfont=dict(color=PALETTE["text_muted"]))
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
    st.caption("Painel Executivo & Laboratório de Dados")
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
# [IA] Gemini – Cabeçalho Principal Estilizado
# ---------------------------------------------------------
st.markdown('<div class="hero-title">Video Game Intelligence Hub</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="hero-subtitle">Visualização analítica de <b>{len(df_filtrado):,}</b> jogos no período de <b>{intervalo_anos[0]} a {intervalo_anos[1]}</b>.</div>'.replace(",", "."),
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# [IA] Gemini – Estrutura Principal: Abas dos 2 Dashboards
# ---------------------------------------------------------
tab_kpi, tab_lab = st.tabs([
    "🎯 Dashboard 2: Painel Estratégico de KPIs (Publishers)",
    "🔬 Dashboard 1: Laboratório de Distribuição & Correlação",
])

# =========================================================
# DASHBOARD 2: PAINEL ESTRATÉGICO DE KPIS (PUBLISHERS)
# =========================================================
with tab_kpi:
    st.markdown("### 🎯 Visão Executiva & Indicadores de Negócio")
    st.caption(
        "Painel desenvolvido para **Executivos e Gerentes de Publicação (Publishers)** "
        "com foco em alocação de investimento, rentabilidade de catálogo e mitigação de risco."
    )

    if df_filtrado.empty:
        st.warning("⚠️ Nenhum registro encontrado para a combinação de filtros selecionada. Ajuste as opções na barra lateral.")
    else:
        # [IA] Gemini – Cálculo dos 4 KPIs validados individualmente pelo aluno
        receita_total_global = df_filtrado["Global_Sales"].sum()
        total_jogos = len(df_filtrado)
        venda_media_jogo = df_filtrado["Global_Sales"].mean() if total_jogos > 0 else 0
        super_hits = df_filtrado[df_filtrado["Global_Sales"] >= 1.0]
        taxa_super_hits = (len(super_hits) / total_jogos * 100) if total_jogos > 0 else 0

        # [IA] Gemini – 4 Cards de Métricas em Destaque com Gradiente Superior e Glassmorphism
        col_k1, col_k2, col_k3, col_k4 = st.columns(4)

        with col_k1:
            st.markdown(
                f"""
                <div class="kpi-container">
                    <div class="kpi-bar bar-indigo"></div>
                    <div class="kpi-title">Receita Global Total</div>
                    <div class="kpi-val">{receita_total_global:,.1f}M</div>
                    <div class="kpi-sub">Faturamento acumulado ($ mi)</div>
                </div>
                """.replace(",", "."),
                unsafe_allow_html=True,
            )

        with col_k2:
            st.markdown(
                f"""
                <div class="kpi-container">
                    <div class="kpi-bar bar-cyan"></div>
                    <div class="kpi-title">Venda Média / Jogo</div>
                    <div class="kpi-val">{venda_media_jogo:.2f}M</div>
                    <div class="kpi-sub">Benchmark de retorno unitário</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_k3:
            st.markdown(
                f"""
                <div class="kpi-container">
                    <div class="kpi-bar bar-emerald"></div>
                    <div class="kpi-title">Taxa de Super Hits</div>
                    <div class="kpi-val">{taxa_super_hits:.1f}%</div>
                    <div class="kpi-sub">{len(super_hits):,} títulos > 1M de vendas</div>
                </div>
                """.replace(",", "."),
                unsafe_allow_html=True,
            )

        with col_k4:
            st.markdown(
                f"""
                <div class="kpi-container">
                    <div class="kpi-bar bar-purple"></div>
                    <div class="kpi-title">Catálogo Monitorado</div>
                    <div class="kpi-val">{total_jogos:,}</div>
                    <div class="kpi-sub">De {len(df):,} títulos históricos</div>
                </div>
                """.replace(",", "."),
                unsafe_allow_html=True,
            )

        st.markdown("")

        # [IA] Gemini – Visual 1 e Visual 2: Top Publicadoras e Market Share Regional
        col_pub, col_share = st.columns([1.1, 0.9], gap="medium")

        with col_pub:
            with st.container(border=True):
                st.markdown("#### 🏆 Top 10 Publicadoras por Faturamento Global")
                st.caption("Concentração de receita entre os maiores competidores do setor")

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
                    color="Global_Sales",
                    color_continuous_scale=["#312E81", "#6366F1", "#38BDF8"],
                    labels={"Publisher": "Publicadora", "Global_Sales": "Vendas Globais ($ mi)"},
                )
                fig_pubs.update_traces(hovertemplate="<b>%{y}</b><br>Faturamento: %{x:.2f}M cópias<extra></extra>")
                fig_pubs.update_coloraxes(showscale=False)
                format_chart(fig_pubs, height=370)
                st.plotly_chart(fig_pubs, use_container_width=True)

        with col_share:
            with st.container(border=True):
                st.markdown("#### 🌍 Market Share por Região de Vendas")
                st.caption("Composição percentual do faturamento entre mercados geográficos")

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
                    hole=0.6,
                    color="Região",
                    color_discrete_map={
                        "América do Norte": "#6366F1",
                        "Europa": "#38BDF8",
                        "Japão": "#10B981",
                        "Outras Regiões": "#F59E0B",
                    },
                )
                fig_donut.update_traces(
                    textposition="inside",
                    textinfo="percent+label",
                    hovertemplate="<b>%{label}</b>: %{value:.1f}M cópias (%{percent})<extra></extra>",
                    marker=dict(line=dict(color="#0B0F19", width=2.5)),
                )
                format_chart(fig_donut, height=370)
                st.plotly_chart(fig_donut, use_container_width=True)

        # [IA] Gemini – Visual 3 e Visual 4: Eficiência por Gênero e Ranking de Super Hits
        col_gen_eff, col_table = st.columns([1, 1], gap="medium")

        with col_gen_eff:
            with st.container(border=True):
                st.markdown("#### 💡 Eficiência de Gênero: Retorno Médio por Jogo")
                st.caption("Média de faturamento por lançamento (identifica nichos mais rentáveis)")

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
                    color="Venda_Media",
                    color_continuous_scale=["#831843", "#DB2777", "#F472B6"],
                    labels={"Genre": "Gênero", "Venda_Media": "Venda Média / Jogo ($ mi)"},
                )
                fig_eff.update_traces(hovertemplate="<b>%{y}</b><br>Média por Jogo: %{x:.2f}M<extra></extra>")
                fig_eff.update_coloraxes(showscale=False)
                format_chart(fig_eff, height=380)
                st.plotly_chart(fig_eff, use_container_width=True)

        with col_table:
            with st.container(border=True):
                st.markdown("#### ⭐ Ranking de Super Hits (Top Títulos)")
                st.caption("Jogos com maior tração comercial e volume de unidades vendidas")

                cols_display = ["Name", "Platform", "Publisher", "Year", "Global_Sales", "NA_Sales", "EU_Sales", "JP_Sales"]
                df_top_hits = df_filtrado.nlargest(10, "Global_Sales")[cols_display].copy()
                df_top_hits.columns = ["Título", "Plataforma", "Publicadora", "Ano", "Global (M)", "NA (M)", "EU (M)", "JP (M)"]

                st.dataframe(
                    df_top_hits,
                    use_container_width=True,
                    hide_index=True,
                    height=340,
                )

# =========================================================
# DASHBOARD 1: LABORATÓRIO DE DISTRIBUIÇÃO E CORRELAÇÃO
# =========================================================
with tab_lab:
    st.markdown("### 🔬 Laboratório de Análise Exploratória")
    st.caption(
        f"Avaliando a métrica quantitativa **{SALES_LABELS[variavel_analise]}** sob diferentes prismas estatísticos."
    )

    if df_filtrado.empty:
        st.warning("⚠️ Nenhum registro encontrado para a combinação de filtros selecionada.")
    else:
        # [IA] Gemini – Linha 1: Heatmap de Correlação + Histograma de Distribuição Univariada
        col_corr, col_dist = st.columns([1, 1], gap="medium")

        with col_corr:
            with st.container(border=True):
                st.markdown("#### Matriz de Correlação entre Mercados Regionais")
                st.caption("Correlação não-paramétrica de Spearman (robusta a outliers)")

                matriz_corr = df_filtrado[SALES_COLUMNS].corr(method="spearman")
                matriz_corr.index = [SALES_LABELS[c] for c in matriz_corr.index]
                matriz_corr.columns = [SALES_LABELS[c] for c in matriz_corr.columns]

                fig_corr = px.imshow(
                    matriz_corr,
                    text_auto=".2f",
                    color_continuous_scale=[
                        [0.0, "#0F172A"],
                        [0.5, "#312E81"],
                        [0.75, "#6366F1"],
                        [1.0, "#38BDF8"],
                    ],
                    zmin=-1,
                    zmax=1,
                    aspect="auto",
                )
                fig_corr.update_coloraxes(colorbar_title="Spearman", colorbar_tickfont=dict(color=PALETTE["text_muted"]))
                format_chart(fig_corr, height=360)
                st.plotly_chart(fig_corr, use_container_width=True)

        with col_dist:
            with st.container(border=True):
                st.markdown(f"#### Distribuição de Vendas: {SALES_LABELS[variavel_analise]}")
                st.caption("Histograma com recorte visual no percentil 95 para mitigar cauda longa")

                p95 = df_filtrado[variavel_analise].quantile(0.95)
                dados_zoom = df_filtrado[df_filtrado[variavel_analise] <= p95]

                mediana_var = df_filtrado[variavel_analise].median()

                fig_hist = px.histogram(
                    dados_zoom,
                    x=variavel_analise,
                    nbins=35,
                    color_discrete_sequence=["#6366F1"],
                    labels={variavel_analise: f"{SALES_LABELS[variavel_analise]} (milhões de cópias)", "count": "Quantidade de Jogos"},
                )
                fig_hist.add_vline(
                    x=mediana_var,
                    line_dash="dash",
                    line_color="#38BDF8",
                    line_width=2,
                    annotation_text=f"Mediana: {mediana_var:.2f}M",
                    annotation_position="top right",
                    annotation_font_color="#38BDF8",
                )
                fig_hist.update_traces(
                    marker=dict(line=dict(color="#818CF8", width=1)),
                    hovertemplate="Faixa de Vendas: %{x:.2f}M<br>Jogos: %{y}<extra></extra>",
                )
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
                    color_discrete_sequence=["#38BDF8"],
                    labels={"Genre": "Gênero", variavel_analise: f"{SALES_LABELS[variavel_analise]} (mi)"},
                )
                fig_box.update_traces(boxpoints=False)
                fig_box.update_xaxes(tickangle=-35)
                format_chart(fig_box, height=380)
                st.plotly_chart(fig_box, use_container_width=True)

        with col_plat:
            with st.container(border=True):
                st.markdown(f"#### Top 10 Plataformas: {SALES_LABELS[variavel_analise]}")
                st.caption("Consoles e plataformas líderes na métrica selecionada")

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
                    color=variavel_analise,
                    color_continuous_scale=["#1E1B4B", "#6366F1", "#818CF8"],
                    labels={"Platform": "Plataforma", variavel_analise: f"{SALES_LABELS[variavel_analise]} (mi)"},
                )
                fig_plat.update_coloraxes(showscale=False)
                fig_plat.update_traces(hovertemplate="Plataforma: %{y}<br>Total: %{x:.2f}M cópias<extra></extra>")
                format_chart(fig_plat, height=380)
                st.plotly_chart(fig_plat, use_container_width=True)

        # [IA] Gemini – Linha 3: Evolução Temporal das Vendas
        with st.container(border=True):
            st.markdown(f"#### Evolução Histórica de Lançamentos e Vendas ({SALES_LABELS[variavel_analise]})")
            st.caption("Trajetória de faturamento ao longo das décadas no período filtrado")

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
                color_discrete_sequence=["#6366F1"],
                labels={"Year": "Ano de Lançamento", variavel_analise: f"Vendas ({SALES_LABELS[variavel_analise]} em mi)"},
            )
            fig_evol.update_traces(
                hovertemplate="Ano: %{x}<br>Vendas: %{y:.1f}M<extra></extra>",
                line=dict(width=2.5, color="#818CF8"),
            )
            fig_evol.update_xaxes(dtick=2)
            format_chart(fig_evol, height=310)
            st.plotly_chart(fig_evol, use_container_width=True)

# [IA] Gemini – Rodapé Informativo e Conformidade Acadêmica
st.markdown("---")
st.caption(
    "📊 **Projeto Prático AVD 2026.2 — Cesar School** | "
    "Edição Dark Mode desenvolvida com Streamlit e Plotly. Base tratada a partir da Análise Exploratória (EDA)."
)
