# Teste
import streamlit as st

import base64

# Dados fictícios de usuários e permissões
users = {
    "Jerome": {"senha": "@salmo8318", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Carlos Alberto": {"senha": "@aijalon10", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Armando": {"senha": "@edom1", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Carlos Montesino": {"senha": "@gibeon2", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "David Affonso": {"senha": "@zion12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Ederson": {"senha": "@hebron11", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Edson": {"senha": "@siloe21", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Felipe Carneiro": {"senha": "@tarsis5", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Francisco Lezcano": {"senha": "@mambre54", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Gilmar": {"senha": "@betel7", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Giovani": {"senha": "@jerico20", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "José Francisco": {"senha": "@galileia5", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Marcos Ribeiro": {"senha": "@tabor12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Marcos Woicjki": {"senha": "@egito1", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Paulo Carvalho": {"senha": "@nazare22", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Paulo Franco": {"senha": "@edom33", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Raphael Madeira": {"senha": "@hermom44", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Renato Horning": {"senha": "@sinai54", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Sergio Santos": {"senha": "@sidom21", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Anderson Alencar": {"senha": "@cadess12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Anderson Valle": {"senha": "@moabe566", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Aparecida Spina": {"senha": "@samaria56", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Arileide": {"senha": "@sarepta56", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Arlene": {"senha": "@tiberias54", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Bibiane": {"senha": "@galatia32", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Varina": {"senha": "@bereia2", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Clarice": {"senha": "@jerusalem13", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Studzuski": {"senha": "@samuel23", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Cleusa": {"senha": "@babel58", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Daiane": {"senha": "@corinto13", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Daiane Graciela": {"senha": "@juda33", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Daniele": {"senha": "@magdala6", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Daniele Rodrigues": {"senha": "@samaria411", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Davides": {"senha": "@nazir23", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Derli": {"senha": "@mara10", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Dilene": {"senha": "@jave15", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Doris": {"senha": "@arao123", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Dulce": {"senha": "@rute321", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Edilene": {"senha": "@sarai123", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Eduarda": {"senha": "@dbora411", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Emilly": {"senha": "@ester235", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Erica": {"senha": "@ligia4", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Esli": {"senha": "@gade22", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Ester": {"senha": "@hama41", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Eva": {"senha": "@adao245", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Felipe Gobato": {"senha": "@jair33", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Fernanda Machado": {"senha": "@joabe12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Fernanda Madeira": {"senha": "@moises57", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Gabriela Ribeiro": {"senha": "@levi55", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Gicelle": {"senha": "@sela54", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Gisele": {"senha": "@noga55", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Heitor": {"senha": "@urias50", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Herminio": {"senha": "@aram44", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Isabela": {"senha": "@tamar22", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Ivonice": {"senha": "@eneias011", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Jahina": {"senha": "@maom44", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "João Batista": {"senha": "@nazaro55", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Josnei": {"senha": "@rebeca57", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Jucimere": {"senha": "@sodoma57", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Ketlin": {"senha": "@egito877", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Lara": {"senha": "@judite55", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Laura": {"senha": "@ismael44", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Lucas Daniel": {"senha": "@adriel66", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Luciana": {"senha": "@mical112", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Luis Claudio": {"senha": "@salao77", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Luiz Eleutério": {"senha": "@apolo7", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Luiz Nogueira": {"senha": "@asa4", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Marcia": {"senha": "@goel21", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Maria": {"senha": "@fe23", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Maria Dione": {"senha": "@orfa98", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Marli": {"senha": "@rute44", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Millena": {"senha": "@metusala12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Miriam": {"senha": "@eva22", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Nadir": {"senha": "@tamar14", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Natalia": {"senha": "@cain78", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Nicolas": {"senha": "@jope33", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Noemia": {"senha": "@noe54", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Patricia": {"senha": "@jairo12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Rafaela": {"senha": "@tiro99", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Regina": {"senha": "@hadasa76", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Rose Coutinho": {"senha": "@daniel77", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Roseli": {"senha": "@jonas25", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Roseni": {"senha": "@debora77", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Santina": {"senha": "@rabi55", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Silmara": {"senha": "@joel43", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Silvana": {"senha": "@simao34", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Simone": {"senha": "@mara76", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Thalita": {"senha": "@palma12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Valdir": {"senha": "@bara12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Vanda": {"senha": "@sal91", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Yamilet": {"senha": "@eloim57", "permissoes": ["a", "b", "c", "d", "e", "f"]},
}

quadros = {
    "a": {"titulo": "Reuniões para o Serviço de Campo", "arquivo": "servico_campo.png"},
    "b": {"titulo": "Designações de Discurso Público", "arquivo": "discurso_publico.png"},
    "c": {"titulo": "Anúncios e Lembretes", "arquivo": "anuncios.png"},
    "d": {"titulo": "Designações Reuniões Flamboyant", "arquivo": "reunioes_flamboyant.png"},
    "e": {"titulo": "Programação da Reunião do Meio de Semana", "arquivo": "programacao_meio_semana.png"},
    "f": {"titulo": "Designações para Limpeza do Salão do Reino", "arquivo": "limpeza_salao.png"},
}

# Adicionando CSS para personalizar o layout


# Adicionando CSS para personalizar o layout
# Adicionando CSS atualizado para personalizar o layout
def add_css():
    st.markdown(
        """
        <style>

        /* Botões principais */
        .stButton>button {
            background-color: #007BFF; /* Azul padrão */
            color: #ffffff; /* Texto branco */
            border-radius: 10px;
            border: none;
            padding: 10px 15px;
            font-size: 16px;
            font-weight: bold;
            margin: 10px auto;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #0056b3; /* Azul mais escuro */
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
            transform: scale(1.05); /* Efeito de zoom ao passar o mouse */
        }

        /* Links */
        a {
            color: #FFD700; /* Links dourados */
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            color: #FFC107; /* Alteração de tom ao passar o mouse */
            text-decoration: underline;
        }

        /* Títulos */
        h1, h2, h3 {
            color:rgb(236, 235, 225); /* Dourado */
            text-align: center;
        }

        /* Estilizando o texto de boas-vindas com fundo claro */


        /* Layout de cartões */
        .stMarkdown {
            background-color:rgb(205, 207, 221); /* Fundo dos cartões */
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
            text-align: left;
        }

        /* Iframe para PDFs */
        iframe {
            border: 2px solid #FFD700; /* Borda dourada ao redor do PDF */
            border-radius: 8px;
            margin-top: 20px;
        }

        </style>
        """,
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
        if usuario in users and users[usuario]["senha"] == senha:
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
        permissoes = users[usuario]["permissoes"]
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
