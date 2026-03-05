# ADR 001: Escolha da Arquitetura Inicial (Monólito Modular vs. Microsserviços)

- **Data:** 19/02/2026  
- **Status:** Proposto  

---

## 📌 Contexto
Estamos iniciando o desenvolvimento do **Sistema de Gestão de Eventos Tech**.  
O sistema precisa lidar com:
- Cadastro de usuários  
- Inscrições  
- Processamento de pagamentos  

Como estamos no início do projeto e focando na disciplina de *Evolução e Arquitetura de Software*, precisamos decidir como estruturar o código inicialmente.

---

## 📝 Decisão
Decidimos iniciar com um **Monólito Modular (Modular Monolith)** em vez de Microsserviços distribuídos nesta fase inicial.

---

## 🎯 Justificativa
- **Redução de Complexidade Cognitiva:** Como o foco inicial da pós-graduação é em Engenharia de Requisitos e Design Patterns, um monólito permite aplicar padrões de projeto (GoF) sem a sobrecarga de rede, latência e serialização de dados entre serviços.  
- **Velocidade de Desenvolvimento:** Permite validar as regras de negócio mais rapidamente.  
- **Facilidade de Refatoração:** É mais fácil mover código entre módulos dentro de um único repositório antes de definir os limites finais (*Bounded Contexts*) para uma futura migração para Microsserviços.  
- **Alinhamento com o Plano Pedagógico:** O curso sugere entender a "Evolução" dos sistemas. Começar com um monólito bem estruturado e depois "quebrá-lo" demonstra maturidade arquitetural no portfólio.  

---

## ⚖️ Consequências

### ✅ Positivas
- Deploy simplificado  
- Testes de integração mais fáceis  
- Depuração direta  

### ❌ Negativas
- Escalabilidade limitada a uma única unidade de deploy (inicialmente)  
- Requer disciplina rigorosa para manter os módulos independentes e evitar um *Big Ball of Mud*  