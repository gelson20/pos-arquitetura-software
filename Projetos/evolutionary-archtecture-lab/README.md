# Evolutionary Architecture Lab 🚀

Este projeto é o laboratório prático desenvolvido durante a **Pós-Graduação em Arquitetura de Software**. O objetivo é demonstrar a evolução de um sistema partindo de um **Monólito Modular** até uma arquitetura de **Microsserviços**, aplicando padrões modernos e boas práticas de engenharia.

## 📌 Objetivo do Projeto
Construir um sistema de gestão de eventos resiliente, escalável e de fácil manutenção, servindo como portfólio para as disciplinas de:
- Engenharia de Requisitos
- Modelagem de Dados
- Arquitetura de Software e Nuvem
- DevOps e Microserviços

## 🛠️ Stack Tecnológica
- **Linguagem:** Python 3.13+
- **Framework Web:** FastAPI (Assíncrono)
- **Validação de Dados:** Pydantic v2
- **ORM:** SQLAlchemy 2.0
- **Banco de Dados:** PostgreSQL (Planejado)
- **Servidor:** Uvicorn

## 🏗️ Estrutura do Projeto (Arquitetura)
O projeto utiliza uma abordagem de **Arquitetura Hexagonal (Ports and Adapters)** para garantir o desacoplamento entre a lógica de negócio e a infraestrutura.

```text
src/
├── core/            # Configurações globais e segurança
├── modules/         # Módulos independentes (Contextos Delimitados)
│   └── events/      # Módulo de Gestão de Eventos
│       ├── domain/  # Entidades e Regras de Negócio (Puro Python)
│       ├── schemas/ # Contratos de entrada/saída (Pydantic)
│       ├── services/# Casos de Uso (Lógica da Aplicação)
│       └── router.py# Adaptador de entrada (API HTTP)
└── main.py          # Ponto de entrada da aplicação