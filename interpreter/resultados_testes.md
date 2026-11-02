# Resultados dos Testes do Interpretador — Sprint 4

## Testes de erros

### Teste 1 — Ataque contra personagem inexistente

**Situação:** Arthur tenta atacar um personagem que não foi criado.

**Resultado esperado:**
```text
Erro semântico: personagem 'Goblin' não foi criado
```

**Resultado:** ✅ Teste aprovado.

---

### Teste 2 — Defesa de personagem inexistente

**Situação:** O comando `DEFENDER Goblin` é executado sem que Goblin tenha sido criado.

**Resultado esperado:**
```text
Erro semântico: personagem 'Goblin' não foi criado
```

**Resultado:** ✅ Teste aprovado.

---

### Teste 3 — Condição com personagem inexistente

**Situação:** Uma condição consulta a vida de Goblin, que não foi criado.

**Resultado esperado:**
```text
Erro semântico: personagem 'Goblin' não foi criado
```

**Resultado:** ✅ Teste aprovado.

---

### Teste 4 — Movimento de personagem inexistente

**Situação:** O comando `MOVER Goblin DIREITA` é executado sem que Goblin tenha sido criado.

**Resultado esperado:**
```text
Erro semântico: personagem 'Goblin' não foi criado
```

**Resultado:** ✅ Teste aprovado.

---

### Teste 5 — Habilidade de personagem inexistente

**Situação:** O comando `HABILIDADE Goblin GOLPE_FORTE` é executado sem que Goblin tenha sido criado.

**Resultado esperado:**
```text
Erro semântico: personagem 'Goblin' não foi criado
```

**Resultado:** ✅ Teste aprovado.

---

### Teste 6 — Criação de personagem duplicado

**Situação:** O personagem Arthur é criado duas vezes.

**Resultado esperado:**
```text
Erro semântico: personagem 'Arthur' já foi criado
```

**Resultado:** ✅ Teste aprovado.

---

## Resumo

Foram realizados **6 testes de erro semântico no interpretador**.

Todos os testes apresentaram o comportamento esperado:

**6/6 testes aprovados.**
