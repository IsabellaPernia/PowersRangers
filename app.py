import streamlit as st
from utils import load_data, load_image
from config import *

# Page Configuration
st.set_page_config(
    page_title="WNBAmarket",
    layout="wide"
)

def main():
    st.title("WNBA Player Statistics (2016-2024)")

    # Load data
    data = load_data(DATA_URL)
    if data is None:
        st.error("Failed to load data. Please try again later.")
        return

    # Create three main sections using columns
    col1, col2 = st.columns([2, 1])

    with col1:
        # Data Table Section
        with st.container():
            st.subheader("Estadísticas de jugadoras")
            st.dataframe(data, height=400)

        # Contract Statistics Section
        with st.container():
            st.subheader("Contrato vs. Estadísticas Análisis")
            contract_image = load_image(CONTRACT_GRAPH_URL)
            if contract_image:
                st.image(contract_image, use_column_width=True)

    with col2:
        # Individual Player Analysis Section
        with st.container():
            st.subheader("Jugadoras individuales")
            player = st.selectbox(
                "Seleccione un jugadora:",
                options=data['Nombre'].unique()
            )
            
            player_graph_url = f"{INDIVIDUAL_GRAPHS_DIR}{player.replace(' ', '_')}.png"
            player_image = load_image(player_graph_url)
            if player_image:
                st.image(player_image, use_column_width=True)

        # Yearly Statistics Section
        with st.container():
            st.subheader("Datos de Liga por año")
            stat = st.selectbox(
                "Seleccione una estadística:",
                options=STATS_COLUMNS
            )
            
            stat_graph_url = f"{YEARLY_GRAPHS_DIR}{stat.replace(' ', '_')}.png"
            stat_image = load_image(stat_graph_url)
            if stat_image:
                st.image(stat_image, use_column_width=True)

if __name__ == "__main__":
    main()
