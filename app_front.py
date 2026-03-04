import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Configuração de Credenciais (Busca do ambiente ou usa padrão para teste)
USER_ID = os.getenv("APP_USER")
USER_PASS = os.getenv("APP_PASS")

def check_password():
    """Retorna True se o usuário inseriu a senha correta."""
    def password_entered():
        if st.session_state["username"] == USER_ID and st.session_state["password"] == USER_PASS:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Limpa a senha do estado
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # Tela de Login
        st.title("🛡️ Acesso Restrito - AI Threat Modeler")
        st.text_input("Usuário", key="username")
        st.text_input("Senha", type="password", key="password")
        st.button("Entrar", on_click=password_entered)
        return False
    
    elif not st.session_state["password_correct"]:
        # Senha incorreta
        st.title("🛡️ Acesso Restrito - AI Threat Modeler")
        st.text_input("Usuário", key="username")
        st.text_input("Senha", type="password", key="password")
        st.button("Entrar", on_click=password_entered)
        st.error("😕 Usuário ou senha incorretos.")
        return False
    else:
        return True

if check_password():
    # Configurações da Página
    st.set_page_config(page_title="AI Threat Modeler - FIAP", page_icon="🛡️")

    st.title("🛡️ AI Threat Modeler")
    st.subheader("Modelagem de Ameaças STRIDE Automática")

    st.markdown("""
    Esta ferramenta utiliza **IA Multimodal (Gemini 3)** para analisar diagramas de arquitetura, 
    identificar componentes e gerar relatórios de segurança detalhados.
    """)

    # URL da sua API (Local para testes ou a do Render para o deploy final)
    # Exemplo local: http://localhost:8000/analyze
    # Exemplo Render: https://seu-projeto.onrender.com/analyze
    API_URL = "https://fiap-threat-modeler.onrender.com/analyze"

    # st.divider()

    # 1. Seleção do Arquivo
    uploaded_file = st.file_uploader("Selecione o diagrama de arquitetura (PNG, JPG)", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Exibe a imagem selecionada
        st.image(uploaded_file, caption="Diagrama Enviado", use_container_width=True)
        
        # 2. Botão de Processamento
        if st.button("🚀 Analisar e Gerar Relatório"):
            with st.spinner("A IA está analisando sua arquitetura... Isso pode levar alguns segundos."):
                try:
                    # Prepara o arquivo para o envio
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    
                    # Chamada para a API
                    response = requests.post(API_URL, files=files)
                    
                    if response.status_code == 200:
                        st.success("✅ Relatório STRIDE gerado com sucesso!")
                        
                        # 3. Botão de Download do PDF (Recebido da API)
                        pdf_bytes = response.content
                        st.download_button(
                            label="📥 Baixar Relatório PDF",
                            data=pdf_bytes,
                            file_name="Relatorio_STRIDE_FIAP.pdf",
                            mime="application/pdf"
                        )
                    else:
                        st.error(f"❌ Erro na API: {response.status_code} - {response.text} - (Favor entrar em contato pelo email: murilopolli@gmail.com)")
                        
                except Exception as e:
                    st.error(f"❌ Falha ao conectar com a API: {e} - (Favor entrar em contato pelo email: murilopolli@gmail.com)")

    st.divider()
    st.caption("Desenvolvido para o Hackathon FIAP Software Security")