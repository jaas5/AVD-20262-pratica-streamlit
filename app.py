# [IA] Gemini – Estrutura base da aplicação, importação de dependências e configuração de página
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from src.data_loader import load_data

# [IA] Gemini – Configuração da página e metadados no padrão do Streamlit (sem emojis)
st.set_page_config(
    page_title="Video Game Analytics | Dark Edition",
    page_icon=":material/analytics:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# [IA] Gemini – Injeção de CSS Customizado para Tema Dark Mode com Gradientes e Efeito Glassmorphism (sem tons de rosa)
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

    /* Cards de KPI Customizados com Efeito Glass e Barra Superior */
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
    .bar-amber { background: linear-gradient(90deg, #F59E0B, #FBBF24); }

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

# [IA] Gemini – Paleta de Cores Consistente para todas as variáveis quantitativas e dashboards (sem rosa)
REGION_COLORS = {
    "NA_Sales": "#38BDF8",       # América do Norte (Sky Blue)
    "EU_Sales": "#6366F1",       # Europa (Indigo)
    "JP_Sales": "#10B981",       # Japão (Emerald Green)
    "Other_Sales": "#F59E0B",    # Outras Regiões (Amber)
    "Global_Sales": "#818CF8",   # Vendas Globais (Soft Slate / Indigo)
}

REGION_LABELS_PT = {
    "América do Norte": "#38BDF8",
    "Europa": "#6366F1",
    "Japão": "#10B981",
    "Outras Regiões": "#F59E0B",
}

SALES_COLUMNS = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
SALES_LABELS = {
    "NA_Sales": "América do Norte",
    "EU_Sales": "Europa",
    "JP_Sales": "Japão",
    "Other_Sales": "Outras Regiões",
    "Global_Sales": "Vendas Globais",
}

PALETTE = {
    "primary": "#6366F1",
    "secondary": "#38BDF8",
    "accent_green": "#10B981",
    "accent_gold": "#F59E0B",
    "grid": "rgba(255, 255, 255, 0.07)",
    "text": "#E2E8F0",
    "text_muted": "#94A3B8",
}


# [IA] Gemini – Função auxiliar de estilização gráfica em Plotly com boas práticas visuais
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
# [IA] Gemini – Sidebar: Controles e Filtros Interativos (sem emojis)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("## **Game Analytics**")
    st.caption("Painel Executivo e Laboratório Quantitativo")
    st.markdown("---")

    st.markdown("### **Filtros Globais**")

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
    st.markdown("### **Variável Quantitativa em Foco**")
    variavel_analise = st.radio(
        "Selecione a região de vendas para análise detalhada:",
        options=SALES_COLUMNS,
        format_func=lambda col: SALES_LABELS[col],
        index=0,
        help="Define a variável quantitativa em destaque no Laboratório de Correlação.",
    )

    st.markdown("---")
    st.caption("*Dica:* Utilize os filtros acima para refinar os períodos e nichos desejados.")

# [IA] Gemini – Aplicação dos filtros reativos no DataFrame
df_filtrado = df[df["Year"].between(intervalo_anos[0], intervalo_anos[1])]
if plataformas_selecionadas:
    df_filtrado = df_filtrado[df_filtrado["Platform"].isin(plataformas_selecionadas)]
if generos_selecionados:
    df_filtrado = df_filtrado[df_filtrado["Genre"].isin(generos_selecionados)]
if publicadoras_selecionadas:
    df_filtrado = df_filtrado[df_filtrado["Publisher"].isin(publicadoras_selecionadas)]

# ---------------------------------------------------------
# [IA] Gemini – Cabeçalho Principal Estilizado (sem emojis)
# ---------------------------------------------------------
st.markdown('<div class="hero-title">Video Game Intelligence Hub</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="hero-subtitle">Visualização analítica de <b>{len(df_filtrado):,}</b> jogos no período de <b>{intervalo_anos[0]} a {intervalo_anos[1]}</b>.</div>'.replace(",", "."),
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# [IA] Gemini – Estrutura Principal: Abas dos 2 Dashboards (Dashboard 1 antes do Dashboard 2)
# ---------------------------------------------------------
tab_lab, tab_kpi = st.tabs([
    "Dashboard 1: Laboratório de Correlação e Distribuição Quantitativa",
    "Dashboard 2: Painel Estratégico de Negócios e KPIs (Publishers)",
])

# =========================================================
# DASHBOARD 1: LABORATÓRIO DE CORRELAÇÃO E VARIÁVEIS QUANTITATIVAS
# =========================================================
with tab_lab:
    st.markdown("### Laboratório de Correlação e Análise Quantitativa")
    st.caption(
        "Análise estritamente focada nas variáveis quantitativas de vendas (América do Norte, Europa, Japão, Outras Regiões e Vendas Globais). "
        "Cada região possui uma cor característica padronizada para facilitar a identificação visual em todo o aplicativo."
    )

    if df_filtrado.empty:
        st.warning("Nenhum registro encontrado para a combinação de filtros selecionada. Ajuste as opções na barra lateral.")
    else:
        # [IA] Gemini – Linha 1: Matriz de Correlação Triangular (sem ambiguidade de simetria) + Histograma com cor característica
        col_corr, col_dist = st.columns([1, 1], gap="medium")

        with col_corr:
            with st.container(border=True):
                st.markdown("#### Matriz de Correlação Triangular de Spearman")
                st.caption("Triângulo inferior sem simetria repetida, evitando ambiguidade visual.")

                # Cálculo de Spearman
                matriz_corr = df_filtrado[SALES_COLUMNS].corr(method="spearman")
                matriz_corr.index = [SALES_LABELS[c] for c in matriz_corr.index]
                matriz_corr.columns = [SALES_LABELS[c] for c in matriz_corr.columns]

                # [IA] Gemini – Máscara triangular inferior para eliminar simetria ambígua
                mask = np.triu(np.ones_like(matriz_corr, dtype=bool), k=1)
                matriz_corr_triangular = matriz_corr.mask(mask)

                # Texto de exibição apenas onde não é nulo
                text_matrix = np.where(pd.isna(matriz_corr_triangular), "", matriz_corr_triangular.round(2).astype(str))

                fig_corr = px.imshow(
                    matriz_corr_triangular,
                    color_continuous_scale=[
                        [0.0, "#0F172A"],
                        [0.5, "#1E293B"],
                        [0.75, "#312E81"],
                        [1.0, "#38BDF8"],
                    ],
                    zmin=-1,
                    zmax=1,
                    aspect="auto",
                )
                fig_corr.update_traces(
                    text=text_matrix,
                    texttemplate="%{text}",
                    hoverongaps=False,
                    hovertemplate="<b>%{y} x %{x}</b><br>Spearman: %{z:.2f}<extra></extra>",
                )
                fig_corr.update_coloraxes(colorbar_title="Spearman", colorbar_tickfont=dict(color=PALETTE["text_muted"]))
                format_chart(fig_corr, height=370)
                st.plotly_chart(fig_corr, use_container_width=True)

        with col_dist:
            with st.container(border=True):
                cor_selecionada = REGION_COLORS.get(variavel_analise, "#38BDF8")
                st.markdown(f"#### Distribuição de Vendas: {SALES_LABELS[variavel_analise]}")
                st.caption(f"Histograma com recorte visual no percentil 95 (Cor característica: {SALES_LABELS[variavel_analise]}).")

                p95 = df_filtrado[variavel_analise].quantile(0.95)
                dados_zoom = df_filtrado[df_filtrado[variavel_analise] <= p95]
                mediana_var = df_filtrado[variavel_analise].median()

                fig_hist = px.histogram(
                    dados_zoom,
                    x=variavel_analise,
                    nbins=35,
                    color_discrete_sequence=[cor_selecionada],
                    labels={variavel_analise: f"{SALES_LABELS[variavel_analise]} (milhões de cópias)", "count": "Quantidade de Jogos"},
                )
                fig_hist.add_vline(
                    x=mediana_var,
                    line_dash="dash",
                    line_color="#FFFFFF",
                    line_width=1.8,
                    annotation_text=f"Mediana: {mediana_var:.2f}M",
                    annotation_position="top right",
                    annotation_font_color="#FFFFFF",
                )
                fig_hist.update_traces(
                    marker=dict(line=dict(color="rgba(255,255,255,0.2)", width=0.8)),
                    hovertemplate="Faixa de Vendas: %{x:.2f}M<br>Jogos: %{y}<extra></extra>",
                )
                format_chart(fig_hist, height=370)
                st.plotly_chart(fig_hist, use_container_width=True)

        # [IA] Gemini – Linha 2: Dispersão e Correlação Bivariada com Tendência Linear + Comparativo das Regiões
        col_scatter, col_panel = st.columns([1, 1], gap="medium")

        with col_scatter:
            with st.container(border=True):
                st.markdown(f"#### Dispersão e Correlação: {SALES_LABELS[variavel_analise]} vs Vendas Globais")
                st.caption("Avaliando o alinhamento da região com o mercado global com reta de tendência linear.")

                # Amostragem para alta performance de renderização
                p95_x = df_filtrado[variavel_analise].quantile(0.95)
                p95_y = df_filtrado["Global_Sales"].quantile(0.95)
                df_scatter_zoom = df_filtrado[(df_filtrado[variavel_analise] <= p95_x) & (df_filtrado["Global_Sales"] <= p95_y)]
                sample_scatter = df_scatter_zoom.sample(min(800, len(df_scatter_zoom)), random_state=42)

                fig_scatter = px.scatter(
                    sample_scatter,
                    x=variavel_analise,
                    y="Global_Sales",
                    opacity=0.6,
                    color_discrete_sequence=[cor_selecionada],
                    labels={
                        variavel_analise: f"{SALES_LABELS[variavel_analise]} (mi)",
                        "Global_Sales": "Vendas Globais (mi)",
                    },
                )
                # Cálculo da linha de tendência linear com numpy.polyfit
                if len(sample_scatter) > 1 and sample_scatter[variavel_analise].nunique() > 1:
                    slope, intercept = np.polyfit(sample_scatter[variavel_analise], sample_scatter["Global_Sales"], 1)
                    x_vals = np.linspace(sample_scatter[variavel_analise].min(), sample_scatter[variavel_analise].max(), 50)
                    y_vals = slope * x_vals + intercept
                    fig_scatter.add_trace(go.Scatter(
                        x=x_vals,
                        y=y_vals,
                        mode="lines",
                        name="Tendência Linear",
                        line=dict(color="#E2E8F0", dash="dash", width=2),
                    ))

                fig_scatter.update_traces(
                    marker=dict(size=6, line=dict(width=0.5, color="rgba(255,255,255,0.3)")),
                    hovertemplate=f"<b>{SALES_LABELS[variavel_analise]}:</b> %{{x:.2f}}M<br><b>Global:</b> %{{y:.2f}}M<extra></extra>",
                )
                format_chart(fig_scatter, height=360)
                st.plotly_chart(fig_scatter, use_container_width=True)

        with col_panel:
            with st.container(border=True):
                st.markdown("#### Distribuição Comparativa das Quatro Regiões")
                st.caption("Visão integrada das quatro variáveis regionais, cada uma com sua respectiva cor padronizada.")

                # Comparativo das 4 regiões com cores características
                reg_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
                df_melted = df_filtrado.melt(
                    value_vars=reg_cols,
                    var_name="Região",
                    value_name="Vendas",
                )
                df_melted["Região"] = df_melted["Região"].map(SALES_LABELS)
                # Recorte visual para comparação proporcional
                limite_p95_geral = df_melted["Vendas"].quantile(0.95)
                df_melted_zoom = df_melted[df_melted["Vendas"] <= limite_p95_geral]

                fig_comp = px.histogram(
                    df_melted_zoom,
                    x="Vendas",
                    color="Região",
                    barmode="overlay",
                    nbins=30,
                    opacity=0.65,
                    color_discrete_map=REGION_LABELS_PT,
                    labels={"Vendas": "Vendas por Título (milhões de cópias)", "count": "Frequência"},
                )
                fig_comp.update_traces(marker=dict(line=dict(width=0.5, color="rgba(255,255,255,0.2)")))
                format_chart(fig_comp, height=360)
                st.plotly_chart(fig_comp, use_container_width=True)


# =========================================================
# DASHBOARD 2: PAINEL ESTRATÉGICO DE KPIS E NEGÓCIOS (PUBLISHERS)
# =========================================================
with tab_kpi:
    st.markdown("### Painel Estratégico de Negócios e Tomada de Decisão")
    st.caption(
        "Visão voltada a **Executivos e Gerentes de Publicação (Publishers)** para análise de mercado, "
        "plataformas, gêneros e competidores históricos com boas práticas de visualização."
    )

    if df_filtrado.empty:
        st.warning("Nenhum registro encontrado para a combinação de filtros selecionada. Ajuste as opções na barra lateral.")
    else:
        # [IA] Gemini – Cálculo dos 4 KPIs validados pelo aluno
        receita_total_global = df_filtrado["Global_Sales"].sum()
        total_jogos = len(df_filtrado)
        venda_media_jogo = df_filtrado["Global_Sales"].mean() if total_jogos > 0 else 0
        super_hits = df_filtrado[df_filtrado["Global_Sales"] >= 1.0]
        taxa_super_hits = (len(super_hits) / total_jogos * 100) if total_jogos > 0 else 0

        # [IA] Gemini – 4 Cards de Métricas em Destaque (cores consistentes: indigo, cyan, emerald e amber - sem rosa)
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
                    <div class="kpi-bar bar-amber"></div>
                    <div class="kpi-title">Catálogo Monitorado</div>
                    <div class="kpi-val">{total_jogos:,}</div>
                    <div class="kpi-sub">De {len(df):,} títulos históricos</div>
                </div>
                """.replace(",", "."),
                unsafe_allow_html=True,
            )

        st.markdown("")

        # [IA] Gemini – Linha 1: Top 10 Publicadoras (cor sólida, texto legível) + Market Share Regional (Donut com cores consistentes)
        col_pub, col_share = st.columns([1.1, 0.9], gap="medium")

        with col_pub:
            with st.container(border=True):
                st.markdown("#### Top 10 Publicadoras por Faturamento Global")
                st.caption("Volume total de vendas dos maiores concorrentes (cor sóbria para melhor contraste com os rótulos).")

                top_publishers = (
                    df_filtrado.groupby("Publisher", as_index=False)["Global_Sales"]
                    .sum()
                    .nlargest(10, "Global_Sales")
                    .sort_values("Global_Sales", ascending=True)
                )

                # Boas práticas: cor uniforme consistente para rótulo legível
                fig_pubs = px.bar(
                    top_publishers,
                    x="Global_Sales",
                    y="Publisher",
                    orientation="h",
                    text_auto=".1f",
                    color_discrete_sequence=["#6366F1"],
                    labels={"Publisher": "Publicadora", "Global_Sales": "Vendas Globais ($ mi)"},
                )
                fig_pubs.update_traces(
                    textposition="inside",
                    insidetextanchor="middle",
                    textfont=dict(color="#FFFFFF", size=11, family="Plus Jakarta Sans"),
                    hovertemplate="<b>%{y}</b><br>Faturamento: %{x:.2f}M cópias<extra></extra>",
                )
                format_chart(fig_pubs, height=360)
                st.plotly_chart(fig_pubs, use_container_width=True)

        with col_share:
            with st.container(border=True):
                st.markdown("#### Market Share por Região de Vendas")
                st.caption("Composição percentual das regiões, utilizando as mesmas cores padronizadas.")

                regioes = {
                    "América do Norte": df_filtrado["NA_Sales"].sum(),
                    "Europa": df_filtrado["EU_Sales"].sum(),
                    "Japão": df_filtrado["JP_Sales"].sum(),
                    "Outras Regiões": df_filtrado["Other_Sales"].sum(),
                }
                df_share = pd.DataFrame(list(regioes.items()), columns=["Região", "Vendas"])

                # Cores estritamente padronizadas e sem rosa
                fig_donut = px.pie(
                    df_share,
                    names="Região",
                    values="Vendas",
                    hole=0.6,
                    color="Região",
                    color_discrete_map=REGION_LABELS_PT,
                )
                fig_donut.update_traces(
                    textposition="inside",
                    textinfo="percent+label",
                    hovertemplate="<b>%{label}</b>: %{value:.1f}M cópias (%{percent})<extra></extra>",
                    marker=dict(line=dict(color="#0B0F19", width=2.5)),
                )
                format_chart(fig_donut, height=360)
                st.plotly_chart(fig_donut, use_container_width=True)

        # [IA] Gemini – Linha 2: Eficiência por Gênero + Boxplot de Dispersão por Gênero (Movido do Dashboard 1)
        col_gen_eff, col_box = st.columns([1, 1], gap="medium")

        with col_gen_eff:
            with st.container(border=True):
                st.markdown("#### Eficiência por Gênero: Retorno Médio por Jogo")
                st.caption("Média de faturamento por lançamento (cor sólida suave garantindo contraste com o texto).")

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
                    color_discrete_sequence=["#38BDF8"],
                    labels={"Genre": "Gênero", "Venda_Media": "Venda Média / Jogo ($ mi)"},
                )
                fig_eff.update_traces(
                    textposition="inside",
                    insidetextanchor="middle",
                    textfont=dict(color="#0B0F19", size=11, family="Plus Jakarta Sans"),
                    hovertemplate="<b>%{y}</b><br>Média por Jogo: %{x:.2f}M<extra></extra>",
                )
                format_chart(fig_eff, height=370)
                st.plotly_chart(fig_eff, use_container_width=True)

        with col_box:
            with st.container(border=True):
                st.markdown("#### Comparação de Dispersão por Gênero (Boxplot)")
                st.caption("Distribuição e quartis de vendas globais por gênero (movido do Dashboard 1).")

                p95_global = df_filtrado["Global_Sales"].quantile(0.95)
                dados_box_zoom = df_filtrado[df_filtrado["Global_Sales"] <= p95_global]

                fig_box = px.box(
                    dados_box_zoom,
                    x="Genre",
                    y="Global_Sales",
                    color_discrete_sequence=["#6366F1"],
                    labels={"Genre": "Gênero", "Global_Sales": "Vendas Globais (mi)"},
                )
                fig_box.update_traces(boxpoints=False)
                fig_box.update_xaxes(tickangle=-35)
                format_chart(fig_box, height=370)
                st.plotly_chart(fig_box, use_container_width=True)

        # [IA] Gemini – Linha 3: Top 10 Plataformas + Evolução Temporal (Movidos do Dashboard 1)
        col_plat, col_evol = st.columns([1, 1], gap="medium")

        with col_plat:
            with st.container(border=True):
                st.markdown("#### Top 10 Plataformas em Faturamento")
                st.caption("Consoles e plataformas líderes em vendas globais (movido do Dashboard 1).")

                top_plat = (
                    df_filtrado.groupby("Platform", as_index=False)["Global_Sales"]
                    .sum()
                    .nlargest(10, "Global_Sales")
                    .sort_values("Global_Sales", ascending=True)
                )

                fig_plat = px.bar(
                    top_plat,
                    x="Global_Sales",
                    y="Platform",
                    orientation="h",
                    text_auto=".1f",
                    color_discrete_sequence=["#38BDF8"],
                    labels={"Platform": "Plataforma", "Global_Sales": "Vendas Globais (mi)"},
                )
                fig_plat.update_traces(
                    textposition="inside",
                    insidetextanchor="middle",
                    textfont=dict(color="#0B0F19", size=11, family="Plus Jakarta Sans"),
                    hovertemplate="Plataforma: %{y}<br>Total: %{x:.2f}M cópias<extra></extra>",
                )
                format_chart(fig_plat, height=360)
                st.plotly_chart(fig_plat, use_container_width=True)

        with col_evol:
            with st.container(border=True):
                st.markdown("#### Evolução Temporal de Vendas Globais")
                st.caption("Trajetória histórica de lançamentos ao longo dos anos (movido do Dashboard 1).")

                evolucao_anual = (
                    df_filtrado.groupby("Year", as_index=False)["Global_Sales"]
                    .sum()
                    .sort_values("Year")
                )

                fig_evol = px.area(
                    evolucao_anual,
                    x="Year",
                    y="Global_Sales",
                    markers=True,
                    color_discrete_sequence=["#6366F1"],
                    labels={"Year": "Ano de Lançamento", "Global_Sales": "Vendas Globais (mi)"},
                )
                fig_evol.update_traces(
                    hovertemplate="Ano: %{x}<br>Vendas: %{y:.1f}M<extra></extra>",
                    line=dict(width=2.5, color="#818CF8"),
                )
                fig_evol.update_xaxes(dtick=5)
                format_chart(fig_evol, height=360)
                st.plotly_chart(fig_evol, use_container_width=True)

        # [IA] Gemini – Linha 4: Ranking Dinâmico de Super Hits (Tabela Executiva)
        with st.container(border=True):
            st.markdown("#### Ranking de Super Hits (Top Títulos)")
            st.caption("Jogos com maior tração comercial e volume de unidades vendidas no segmento filtrado.")

            cols_display = ["Name", "Platform", "Publisher", "Year", "Global_Sales", "NA_Sales", "EU_Sales", "JP_Sales"]
            df_top_hits = df_filtrado.nlargest(10, "Global_Sales")[cols_display].copy()
            df_top_hits.columns = ["Título", "Plataforma", "Publicadora", "Ano", "Global (M)", "NA (M)", "EU (M)", "JP (M)"]

            st.dataframe(
                df_top_hits,
                use_container_width=True,
                hide_index=True,
                height=310,
            )

# [IA] Gemini – Rodapé Informativo e Conformidade Acadêmica
st.markdown("---")
st.caption(
    "**Projeto Prático AVD 2026.2 — Cesar School** | "
    "Edição Dark Mode desenvolvida com Streamlit e Plotly. Base tratada a partir da Análise Exploratória (EDA)."
)
