import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Home',
    page_icon='🎲'
)

#image_path = '/Users/jz1nn/John/Formação em Ciência de Dados/Codigos-Comunidade-Data-Science/'
image = Image.open('logo.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown('# Curry Company')
st.sidebar.markdown('## Fastest Delivery in Town!')
st.sidebar.markdown("""---""")

st.write('# Curry Company Growth Dashboard')

st.markdown(
    """
    Growth Dashboard foi construído para acompanhar as métricas de crescimento dos Entregadores e Restraurantes.
    ### Como utilizar esse Growth Dashboard?
    - Visão Empresa:
        - Visão gerencial: Métricas gerais de comportamento.
        - Visão Tática: Indicadores semanais de crescimento.
        - Visão Geográfica: Insights de geolocalização.
    - Visão Entregador:
        - Acompanhamento dos indicadores semanais de crescimento.
    - Visão Restaurante:
        - Indicadores semanais de crescimento dos restaurantes.
    ### Precisa de ajuda?
    - John (xx)xxxxx-xxxx
    """)
