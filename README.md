# 🕵️ Caso Mansão Blackwood — Jogo de Investigação

Produto final: **2 PDFs profissionais** (nível de produto à venda) para um jogo de
investigação de assassinato em mansão, feito para **2 jogadores adultos**, dificuldade
**médio/difícil**, duração **2h+**.

| Arquivo | Conteúdo |
|---|---|
| `Caso_Mansao_Blackwood_JOGO.pdf` | O jogo completo: dossiê, evidências, fotos, suspeitos, puzzles, ficha de acusação |
| `Caso_Mansao_Blackwood_SOLUCAO.pdf` | Gabarito completo: solução passo a passo, linha do tempo real, explicação de cada puzzle |

---

## ⚙️ ESTADO ATUAL — CONCLUÍDO

- [x] Pesquisa de referências de mercado (Hunt A Killer, Case Files, etc.)
- [x] GitHub CLI instalado e autenticado como `Edubernardino7-recuperacao`
- [x] 36 imagens em `assets/` (cenas, evidências, retratos, mansões)
- [x] HTML do jogo (`jogo.html`) — 32 páginas A4
- [x] HTML da solução (`solucao.html`) — 12 páginas A4
- [x] Conversão HTML → PDF com Chrome headless
- [x] Commit + push para `origin/main`

**Entregáveis**

| Arquivo | Páginas | Conteúdo |
|---|---|---|
| `Caso_Mansao_Blackwood_JOGO.pdf` | 32 | Capa, regras, briefing, planta, laudo, 6 dossiês, 15 provas, 5 puzzles, dicas, ficha de acusação |
| `Caso_Mansao_Blackwood_SOLUCAO.pdf` | 12 | Solução resumida, linha do tempo real, resolução dos 5 puzzles, inocentes, análise da cena |

**Como regerar os PDFs** (após editar os HTML):

```bash
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
ROOT="$(pwd -W)"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer   --print-to-pdf="$ROOT/Caso_Mansao_Blackwood_JOGO.pdf" "file:///$ROOT/jogo.html"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer   --print-to-pdf="$ROOT/Caso_Mansao_Blackwood_SOLUCAO.pdf" "file:///$ROOT/solucao.html"
```

Conferir páginas: `python -c "import pypdfium2 as p;print(len(p.PdfDocument('Caso_Mansao_Blackwood_JOGO.pdf')))"`.

### Notas técnicas
- Imagens por IA estão quebradas (`Invalid credential`) — todas as imagens vêm de acervo livre (Openverse/Flickr).
- Chrome headless **exige caminho absoluto** em `--print-to-pdf` no Windows.
- `@page { size: A4; margin: 0 }` + `.page` com padding manual. Cada seção `.page` = 1 página do PDF (não adicionar conteúdo além de ~297mm).
- `library_newport.jpg` e `library_foace.jpg` são fachadas aéreas, não bibliotecas; use `library_stacks.jpg` / `library_study.jpg` para interiores.

---

## 🎯 DESIGN DO CASO (canon — mantenha consistência)

**Vítima:** Sir Edmund Blackwood, 71, patriarca. Morto na biblioteca da
**Mansão Blackwood**, 22h47 de uma sexta-feira. Descoberto pela governanta Clara.

**Causa real:** Envenenamento por **digoxina** (medicamento cardíaco) no uísque —
não o golpe na cabeça (ferida póstuma, encenação). Fase 1 do laudo sugere
traumatismo; o toxicológico revela a verdade.

**Suspeitos (6):**
1. **Vitória Blackwood** (42) — 2ª esposa, 25 anos mais nova. Motivo: herança +
   affair descoberto (relacionamento com o motorista).
2. **Rafael Blackwood** (38) — filho pródigo, dívidas de jogo. Motivo: corte da herança.
3. **Dr. Henrique Salles** (58) — médico pessoal há 30 anos. **É O CULPADO.**
   Motivo: Edmund descobriu que Salles o envenenava lentamente há anos para
   manter sua dependência/receitas (ou: Edmund ia denunciar fraude em receitas
   controladas / Salles matou a 1ª esposa de Edmund anos antes e Edmund tinha
   a prova). Meio: acesso à digoxina. Oportunidade: janela de 12 min.
4. **Clara Vidal** (55) — governanta, 30 anos de serviço. Motivo: demissão +
   testamento a mude a cláusula dela.
5. **Sérgio Kloss** (61) — sócio de negócios. Motivo: fraude descoberta,
   Edmund ia denunciar na segunda-feira.
6. **Isabel Ferraz** (30) — secretária/amante. Motivo: grávida, não consta
   no testamento, chantagem descoberta.

**Correntes de prova (nível médio/difícil, 2h):**
- **Puzzle 1 — Linha do tempo:** reconstruir 21h–23h a partir de declarações +
  relógio parado (22h43, caiu) + registro de chamadas telefônicas. Mostra a
  janela de 12 minutos (22h35–22h47) em que só Salles não tem álibi verificável.
- **Puzzle 2 — Cifra:** página do caderno de Edmund em cifra de substituição
  (chave: nome da mansão/alfabeto deslocado). Revela: "S.S. sabe. Cofre 1703"
  (data do casamento 17/03) → abre cofre com prova contra Salles.
- **Puzzle 3 — Forense:** toxicológico + pílulas (14 de 30 cápsulas de digoxina
  faltando vs receita mensal) + copo com resíduo → causa real = veneno, não candelabro.
  Ferida sem hemorragia = póstuma (encenação).
- **Puzzle 4 — Álibis mentirosos:** tabela cruzada declarações × registros ×
  fotos. Quem mentiu: Vitória (foto 22h40 mostra o carro do motorista), etc.
- **Puzzle 5 (final) — Acusação:** nome + motivo + meio + oportunidade + prova.

**Dicas escalonadas:** 3 níveis por puzzle (não leia até travar de verdade).

---

## 🖼️ Assets disponíveis (`assets/`)

`cover_night1/2` (mansão noite) · `manor_hatfield`, `manor_mooste` (fachadas) ·
`scene_chalk`, `scene_tape1/2`, `scene_officer` (cena do crime) ·
`library_newport/foace/stacks/study` (biblioteca) · `whisky_jura` ·
`candlestick` (candelabro = arma) · `apothecary`, `pills` (veneno) ·
`letter_old`, `typewriter` (documentos) · `clock_hall`, `clock_only` (relógio) ·
`keys`, `watch`, `magnifier`, `vault` (cofre) · `dinner_candle` (jantar) ·
`portrait_m1-m4`, `portrait_f1-f5`, `portrait_e1`, `biz_thinking` (suspeitos)
