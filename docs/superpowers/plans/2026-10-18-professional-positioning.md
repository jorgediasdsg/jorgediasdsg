# Posicionamento profissional claro e pesquisável Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reescrever a primeira tela do README para comunicar rapidamente backend, automação, DevOps e integração com frontend, com stack pesquisável e sem identificadores de empresas, clientes ou projetos.

**Architecture:** O perfil continuará sendo um Markdown simples, com um hero textual acessível e estável no GitHub. Um teste `unittest` lerá o README e validará a hierarquia inicial, a presença da stack exigida e a ausência dos identificadores removidos.

**Tech Stack:** Markdown renderizado pelo GitHub; Python 3 `unittest` para o contrato editorial.

**Spec:** Issue `github:jorgediasdsg/jorgediasdsg#11`, incluindo a Spec de negócio — PO e a Spec técnica — QA fornecidas na solicitação.

## Global Constraints

- Headline curta, humana e compatível com buscas de recrutamento técnico.
- Destacar Go, Python, Node.js, React, Docker, Kubernetes, Terraform, Ansible, CI/CD e GitOps.
- Não citar empresas, clientes ou nomes identificáveis de projetos.
- Não inventar métricas, cargos ou resultados.
- Manter linguagem profissional, objetiva, acessível e estável em desktop e celular no GitHub.
- A branch principal não será alterada diretamente.

## Review Focus

- Primeira tela sem uma das tecnologias de busca: coberto pelo teste de stack no bloco inicial.
- Hierarquia que empurre o posicionamento abaixo da dobra: coberto pelo teste do primeiro elemento e limite do bloco inicial.
- Regressão de nomes de projetos antigos ou links identificáveis: coberto pelo teste de identificadores proibidos.
- README continuar sendo Markdown válido e renderizável: coberto pela execução do `unittest` e smoke HTTP da branch publicada.

---

### Task 1: Contrato editorial e hero do perfil

**Files:**
- Create: `tests/test_readme.py`
- Modify: `README.md`

**Interfaces:**
- Consumes: o conteúdo atual de `README.md`.
- Produces: README com o hero textual exigido e teste executável via `python3 -m unittest discover -s tests -v`.

- [ ] **Step 1: Write the failing test**

  Criar testes que exijam a headline `Engenheiro de Software | Backend, Automação e DevOps`, as dez tecnologias na primeira tela, a hierarquia iniciada por `<h1>` e a ausência de nomes/links de projetos identificáveis.

- [ ] **Step 2: Run test to verify it fails**

  Run: `python3 -m unittest discover -s tests -v`

  Expected: FAIL porque o README atual não contém Python, React, CI/CD e GitOps no bloco inicial e ainda lista projetos nomeados.

- [ ] **Step 3: Implement the README rewrite**

  Substituir o topo por um hero textual curto e reorganizar as seções de competências para listar as tecnologias por capacidade. Remover links e nomes de projetos, empresas e clientes, preservando apenas capacidades e formação verificáveis.

- [ ] **Step 4: Run test to verify it passes**

  Run: `python3 -m unittest discover -s tests -v`

  Expected: PASS sem falhas.

- [ ] **Step 5: Commit**

  ```bash
  git add README.md tests/test_readme.py docs/superpowers/plans/2026-10-18-professional-positioning.md
  git commit -m "feat: clarify professional profile positioning"
  ```

### Task 2: Handoff e homologação pública

**Files:**
- Create: `.flywheel/delivery-handoff.json`

**Interfaces:**
- Consumes: resultado verde da Task 1 e branch publicada.
- Produces: handoff com `manifest_ref`, `tests_passed: true` e URL HTTP(S) acessível para revisão.

- [ ] **Step 1: Run the complete editorial test**

  Run: `python3 -m unittest discover -s tests -v`

- [ ] **Step 2: Publish the isolated branch**

  Enviar somente `flywheel/github-jorgediasdsg-jorgediasdsg-11` ao remoto, sem escrever `master`.

- [ ] **Step 3: Smoke-test the published README**

  Confirmar via HTTP(S) que a URL publicada retorna o README alterado e contém a headline esperada.

- [ ] **Step 4: Write the delivery handoff**

  Gravar `manifest_ref` como `.flywheel/delivery-handoff.json`, `tests_passed` como booleano `true` e `homologation_url` como a URL HTTP(S) da branch publicada.

- [ ] **Step 5: Validate the handoff JSON**

  Executar validação JSON e confirmar os três campos obrigatórios antes da conclusão.

---
