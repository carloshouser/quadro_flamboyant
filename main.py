# Dados de deploy
"""  
Repositorio:
  carloshouser/quadro_flamboyant
Branch: 
  main
main file path:
  main.py
app url:  
  https://flamboyant-anuncios.streamlit.app/
  https://   flamboyant-anuncios   .streamlit.app/
"""
from constantes import usuarios, estilo
import streamlit as st
import base64

quadros = {
    "a": {"titulo": "Reuniões para o Serviço de Campo", "arquivo": "servico_campo.png"},
    "b": {"titulo": "Designações de Discurso Público", "arquivo": "discurso_publico.png"},
    "c": {"titulo": "Anúncios e Lembretes", "arquivo": "anuncios.png"},
    "d": {"titulo": "Designações Reuniões Flamboyant", "arquivo": "reunioes_flamboyant.png"},
    "e": {"titulo": "Programação da Reunião do Meio de Semana", "arquivo": "programacao_meio_semana.png"},
    "f": {"titulo": "Designações para Limpeza do Salão do Reino", "arquivo": "limpeza_salao.png"},
}

# Adicionando CSS atualizado para personalizar o layout


def add_css():
    st.markdown(
        estilo,
        unsafe_allow_html=True,
    )


# Adicionar o CSS ao aplicativo
add_css()

# Página de login
if "logado" not in st.session_state:
    st.title("Flamboyant - Quadro de Anúncios")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.session_state["pagina"] = "home"
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
else:
    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "home"

    if st.session_state["pagina"] == "home":
        st.title("Flamboyant - Quadro de Anúncios")
        # st.markdown("### Bem-vindo!")
        usuario = st.session_state["usuario"]
        permissoes = usuarios[usuario]["permissoes"]
        st.write(f'Saudações {st.session_state['usuario']}')

        # Layout em 2 colunas e 3 linhas
        col1, col2 = st.columns(2)

        with col1:
            for chave in ["a", "b", "c"]:
                if chave in permissoes:
                    quadro = quadros[chave]
                    if st.button(quadro["titulo"], key=f"abrir_{chave}"):
                        st.session_state["pagina"] = "visualizar"
                        st.session_state["quadro_atual"] = chave
                        st.rerun()

        with col2:
            for chave in ["d", "e", "f"]:
                if chave in permissoes:
                    quadro = quadros[chave]
                    if st.button(quadro["titulo"], key=f"abrir_{chave}"):
                        st.session_state["pagina"] = "visualizar"
                        st.session_state["quadro_atual"] = chave
                        st.rerun()

        # Link para o Dropbox
        st.markdown('<a href="https://www.dropbox.com/sh/g7i0hvmnbcd495i/AAC_vF7im3ke8-lvRGfjYQRRa?dl=0" target="_blank" style="margin-top: 20px;">📂 Acessar Designações</a>', unsafe_allow_html=True)

        # Botão para sair
        if st.button("Sair"):
            del st.session_state["logado"]
            del st.session_state["pagina"]
            st.rerun()

    elif st.session_state["pagina"] == "visualizar":
        chave = st.session_state["quadro_atual"]
        quadro = quadros[chave]

        st.title(quadro["titulo"])

        with open(quadro["arquivo"], "rb") as file:
            # Verifica o tipo de arquivo e processa de forma diferente
            if quadro["arquivo"].endswith(".png"):
                # Lê o arquivo PNG e exibe
                img_data = file.read()
                # Usando use_container_width
                st.image(
                    img_data, caption=quadro["titulo"], use_container_width=True)
            elif quadro["arquivo"].endswith(".pdf"):
                # Lê o arquivo PDF e exibe em um iframe
                pdf_data = file.read()
                pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')
                st.markdown(
                    f'<iframe src="data:application/pdf;base64,{
                        pdf_base64}" width="100%" height="1000px"></iframe>',
                    unsafe_allow_html=True,
                )

        if st.button("Voltar"):
            st.session_state["pagina"] = "home"
            st.rerun()
