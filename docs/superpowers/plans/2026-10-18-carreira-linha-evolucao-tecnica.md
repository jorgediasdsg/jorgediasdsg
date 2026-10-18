# Linha de evolução técnica sem exposição pessoal — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Atualizar o perfil GitHub para apresentar uma sequência técnica de redes e sistemas até operação, sem nomes de empresas, clientes ou projetos identificáveis.

**Architecture:** O README será a única superfície de apresentação. A evolução será uma tabela Markdown de seis etapas, com tecnologias e práticas verificáveis, acompanhada por uma stack agrupada por capacidade. Um teste em Python usando apenas a biblioteca padrão validará a ordem, a presença das práticas e a ausência dos identificadores editoriais proibidos.

**Tech Stack:** Markdown, Python 3 (unittest), JSON, Git.

**Spec:** Issue `github:jorgediasdsg/jorgediasdsg#14`, especificações de negócio/QA fornecidas no pedido.

## Global Constraints

- Não citar nomes de empresas, clientes ou projetos identificáveis.
- Usar somente tecnologias, práticas e capacidades verificáveis.
- Não inventar métricas, cargos ou resultados.
- Manter linguagem profissional, objetiva, acessível e sem exageros.
- A sequência deve conter redes e sistemas, desenvolvimento, arquitetura, automação, DevOps e operação.
- O handoff deve conter `manifest_ref`, `tests_passed: true` e `homologation_url` HTTP(S).

## Review Focus

- A ordem da linha deve ser compreensível para RH e para uma pessoa técnica; o teste verifica as seis etapas em ordem.
- A linha não deve criar uma narrativa de cargos ou resultados; o teste verifica que cada etapa usa capacidade, tecnologia ou prática.
- O README não deve expor nomes de projetos, clientes ou empresas; o teste verifica uma lista de identificadores removidos.
- A publicação precisa apontar para a branch efetivamente disponibilizada; a verificação final consulta o commit remoto e a URL pública.

---

### Task 1: Perfil, contrato editorial e handoff de homologação

**Files:**
- Create: `tests/test_profile_readme.py`
- Modify: `README.md`
- Create: `.flywheel/manifest.json`
- Create: `.flywheel/delivery-handoff.json`

**Interfaces:**
- Consumes: conteúdo atual de `README.md` e os critérios da issue.
- Produces: README em Markdown estável, manifesto local e handoff aceito pelo client.

- [ ] **Step 1: Write the failing test**

  Criar `tests/test_profile_readme.py` com verificações de: título da seção de evolução; ordem exata das seis etapas; termos técnicos em cada etapa; ausência dos nomes de projetos/empresas conhecidos do README anterior; ausência de métricas e cargos inventados.

- [ ] **Step 2: Run test to verify it fails**

  Run: `python3 -m unittest discover -s tests -v`
  Expected: FAIL porque o README atual contém projetos identificáveis e não possui a linha de evolução requerida.

- [ ] **Step 3: Implement the profile update**

  Substituir a seção de projetos por uma linha Markdown enxuta, remover links pessoais desnecessários e manter apenas tecnologias/práticas verificáveis já sustentadas pelo perfil.

- [ ] **Step 4: Run test to verify it passes**

  Run: `python3 -m unittest discover -s tests -v`
  Expected: PASS com zero falhas.

- [ ] **Step 5: Write manifest and handoff**

  Criar `.flywheel/manifest.json` com issue, arquivos alterados, comando de teste e resultado; criar `.flywheel/delivery-handoff.json` apontando para esse manifesto, com `tests_passed: true` e URL HTTP(S) da branch publicada.

- [ ] **Step 6: Verify and commit**

  Rodar o teste completo, validar o JSON com `python3 -m json.tool`, conferir o diff e commitar na branch da issue.

- [ ] **Step 7: Publish and verify homologation**

  Publicar a branch no remoto sem alterar `master`, consultar o commit remoto e validar a URL pública do README; atualizar o handoff com o endereço efetivamente publicado e repetir a suíte antes do commit final, se necessário.
