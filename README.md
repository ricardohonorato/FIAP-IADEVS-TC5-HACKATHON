# FIAP-IADEVS-TC5-HACKATHON
HACKATHON - TC 5 - FIAP

# 🛡️ AI Threat Modeler - Hackathon FIAP

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

Este projeto apresenta um **MVP de Modelagem de Ameaças Automatizada** desenvolvido para a **FIAP Software Security**. A solução utiliza IA Multimodal para interpretar diagramas de arquitetura e gerar relatórios baseados na metodologia **STRIDE**.

---

## 📺 Demonstração do MVP

> **URL de Acesso:** [https://hackaton-fiap-front.onrender.com](https://hackaton-fiap-front.onrender.com)
> 
> **Usuário:** ` ` | **Senha:** ` `

---

## 🏗️ Arquitetura do Sistema

A solução foi desenhada seguindo os princípios de microserviços e isolamento de dependências:


1.  **Frontend (Streamlit):** Interface intuitiva para upload de diagramas e download de relatórios.
2.  **Backend (FastAPI):** API de alta performance que processa a lógica de segurança e geração de PDF.
3.  **IA (Gemini 3 Flash):** Motor de visão computacional que analisa a topologia da rede e sugere contramedidas.

---

## 🛠️ Funcionalidades Chave

| Funcionalidade | Descrição |
| :--- | :--- |
| **Identificação Visual** | Detecta usuários, APIs, Gateways, Bancos de Dados e WAF em imagens. |
| **Análise STRIDE** | Mapeia automaticamente as 6 categorias de ameaças da metodologia. |
| **Relatórios PDF** | Gera documentos técnicos formatados com mitigação e vulnerabilidades. |
| **Segurança Nativa** | Proteção de acesso via login e gestão de segredos via Environment Variables. |

---

## ⚙️ Configuração e Instalação Local

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/fiap-threat-modeler.git
cd fiap-threat-modeler
```
### 2. Configurar Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para garantir que informações sensíveis não sejam expostas no código-fonte, seguindo as diretrizes de **Security by Design**.

1. Na raiz do projeto, crie um arquivo chamado `.env`:
   ```bash
   touch .env
   ```
2. Adicione as seguintes chaves ao arquivo e preencha com seus dados
    ```bash
    GOOGLE_API_KEY=Chave de API obtida no Google AI Studio.
    APP_USER=Nome de usuário para acesso ao Frontend.
    APP_PASS=Senha para acesso ao Frontend.
    ```
### 3. Execução via Docker (Recomendado)
    docker build -t threat-modeler-api .
    docker run -p 8000:8000 --env-file .env threat-modeler-api

---

## 🔒 Segurança e DevSecOps

O desenvolvimento deste MVP seguiu rigorosamente os princípios de **Security by Design**, garantindo que a automação da modelagem de ameaças não se tornasse, ela mesma, uma vulnerabilidade.

### 🛡️ Pilares de Proteção Implementados

| Prática | Descrição Técnica | Objetivo |
| :--- | :--- | :--- |
| **Gestão de Segredos** | Uso de variáveis de ambiente via `python-dotenv`. | Prevenção contra **CWE-798** (Hardcoded Credentials). |
| **Controle de Acesso** | Camada de autenticação (`Auth`) no Frontend. | Proteção de recursos e prevenção de exaustão de cota de API. |
| **Isolamento de Runtime** | Conteinerização completa utilizando **Docker**. | Garantia de imutabilidade e mitigação de *Dependency Confusion*. |
| **Sanitização de Output** | Tratamento de encode (Latin-1/Replace) no gerador PDF. | Prevenção de quebras de processo e potenciais injeções de caracteres. |

---

### 🛡️ Metodologia STRIDE Aplicada
A inteligência do sistema foi instruída a realizar o mapeamento semântico seguindo os seis pilares da Microsoft:

> [!TIP]
> **S**poofing | **T**ampering | **R**epudiation | **I**nformation Disclosure | **D**enial of Service | **E**levation of Privilege

### 🛡️ Práticas de DevSecOps
* **Minimalismo de Imagem:** O `Dockerfile` utiliza uma imagem base `python-slim` para reduzir a superfície de ataque (menor número de binários desnecessários).
* **Segurança de API:** O uso do **FastAPI** permite a validação automática de tipos de dados (Pydantic), prevenindo entradas de dados malformadas.
* **Audit Trail:** Logs de execução estruturados para monitoramento de chamadas e depuração de falhas de processamento da IA.

---

## 📄 Documentação da API (Swagger)

A API de modelagem de ameaças foi desenvolvida com **FastAPI**, o que permite a geração automática de uma documentação interativa e padronizada seguindo a especificação **OpenAPI 3.0**.

### 🛠️ Como acessar e testar

Para validar os endpoints diretamente pelo navegador, sem a necessidade de ferramentas externas como Postman ou Insomnia, siga os passos:

1. Inicie o servidor do backend (Docker ou Local).
2. Acesse a URL: `http://localhost:8000/docs`


### 📤 Endpoint Principal: `/analyze`

O coração da solução reside no endpoint de análise multimodal. No Swagger, você pode testar o fluxo completo:

* **Método:** `POST`
* **Corpo da Requisição (form-data):** Envio do arquivo de imagem (PNG/JPG).
* **Processamento:** A API recebe o binário, invoca o **Gemini 3 Flash** com um System Prompt blindado e processa a lógica de ameaças.
* **Resposta:** A documentação detalha os esquemas de retorno, incluindo o JSON de análise e o stream para download do PDF.

### 🛡️ Vantagens para Segurança
* **Transparência:** Todos os contratos de dados (inputs e outputs) são visíveis e tipados.
* **Auditoria:** Facilita a revisão de código e a análise de como os dados trafegam entre o cliente e o motor de IA.
* **Integrabilidade:** Por seguir o padrão OpenAPI, a documentação permite que o backend seja facilmente consumido por scanners de vulnerabilidades de API (DAST).

---
