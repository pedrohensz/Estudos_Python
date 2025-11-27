# 📚 Estudos de Python

Este repositório documenta minha jornada de aprendizado em Python — desde os fundamentos da linguagem até tópicos mais avançados como Programação Orientada a Objetos e criação/consumo de APIs.

---

## 🚀 Projetos Principais

### **1. Sabor Express**
Aplicação de console para gerenciamento de restaurantes, evoluindo junto com os estudos.

#### **Versão Procedural**  
_Local: `Introdução Python/Sabor Express`_  
Primeira implementação baseada em funções, listas e dicionários. Funcionalidades:
- Cadastro de novos restaurantes  
- Listagem dos restaurantes cadastrados  
- Ativar/desativar um restaurante  

#### **Versão Orientada a Objetos**  
_Locais: `Orientação a Objetos/OO_Sabor_Express` e `OO_E_API/Modulo_1_2`_  
Refatoração completa aplicando POO.  
Inclui:
- Classes como `Restaurante`, `Avaliacao` e `ItemCardapio`
- Herança e polimorfismo (`Prato`, `Bebida`)
- Uso de propriedades (`@property`)
- Melhor organização e encapsulamento

---

### **2. API de Cardápios**

#### **Consumo de API**
_Local: `OO_E_API/Modulo_4_Requisicoes`_  
Estudo prático com a biblioteca **requests**:
- Consumo de uma API externa com dados de cardápios  
- Processamento e salvamento dos dados em arquivos `.json`  

#### **Criação de API com FastAPI**
_Local: `OO_E_API/Modulo_5_FastApi`_  
Construção de um backend simples utilizando FastAPI:
- Endpoint `/api/restaurantes/`  
- Filtragem de cardápios por nome de restaurante  
- Documentação automática via `/docs`  

---

## 📁 Estrutura do Repositório

pedrohensz-estudos_python/

|── Introdução Python/Conceitos básicos, loops, condicionais, funções, estruturas de dados.

|── Orientação a Objetos/ ` Exercícios e versão OO do Sabor Express.`

|── OO_E_API/ `Módulos avançados e estudo de APIs.`
 
    |── Exercícios/ `Herança, classes abstratas, práticas de POO.`

    |── Modulo_1_2/ ` Sabor Express com POO e cardápio.`

    |├── Modulo_4_Requisicoes/ `Consumo de API externa (requests).`

    |└── Modulo_5_FastApi/ ` API criada com FastAPI.`
|
|└── requirements.txt ` Dependências do projeto FastAPI.`



---

## 🧠 Conceitos Abordados

### **Fundamentos de Python**
- Variáveis, tipos de dados, operadores  
- Listas, dicionários, tuplas  
- Loops (`for`, `while`)  
- Condicionais (`if`, `elif`, `else`)  

### **Programação Orientada a Objetos**
- Classes e objetos  
- Método construtor (`__init__`)  
- Encapsulamento  
- Propriedades (`@property`)  
- Métodos de classe e estáticos  
- Herança e polimorfismo  
- Classes abstratas (ABC)  

### **Manipulação de APIs**
- Requisições HTTP com `requests`  
- Manipulação e parsing de JSON  

### **Desenvolvimento Backend**
- Criação de APIs REST com FastAPI  
- Rotas, parâmetros e responses  
- Servidor com Uvicorn  

---

## 🛠️ Como Executar

### **Pré-requisitos**
- Python 3.x  
- Git  

---

### **Clone o repositório**
git clone https://github.com/pedrohensz/estudos_python.git
cd estudos_python
Executar um projeto de console (ex: Sabor Express)

cd "Introdução Python/Sabor Express"
python app.py
Executar a API com FastAPI
Instale as dependências:



cd OO_E_API
pip install -r requirements.txt
Execute a API:


cd Modulo_5_FastApi
uvicorn main_api:app --reload
Acesse a documentação interativa:



http://127.0.0.1:8000/docs

