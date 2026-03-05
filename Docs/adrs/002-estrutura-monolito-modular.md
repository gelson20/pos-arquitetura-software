# ADR 002: Organização de Pastas e Padrão de Arquitetura

**Data:** 19/02/2026
**Status:** Aceito
**Contexto:**
Precisamos definir como o código será organizado para garantir que os módulos (Eventos, Usuários, Pagamentos) sejam independentes, facilitando a futura migração para microsserviços e a aplicação de padrões de projeto.

**Decisão:**
Adotaremos uma variação da **Arquitetura Hexagonal (Ports and Adapters)** dentro de um **Monólito Modular** usando Python e FastAPI.

**Estrutura Proposta:**
- `app/core/`: Configurações compartilhadas.
- `app/modules/[nome-do-modulo]/domain/`: Entidades e lógica de negócio pura.
- `app/modules/[nome-do-modulo]/repository/`: Persistência de dados.
- `app/modules/[nome-do-modulo]/router.py/`: Pontos de entrada da API.

**Justificativa:**
Esta estrutura isola o "coração" do software (Domínio) de detalhes externos (Banco de dados e Framework Web). Isso permite testar a lógica de negócio sem depender de infraestrutura e facilita o "recorte" de módulos no futuro.

**Consequências:**
- **Positivas:** Alta testabilidade e baixo acoplamento entre módulos.
- **Negativas:** Maior número de pastas e arquivos iniciais (overhead de estrutura).