# 🕵️ Caso Mansão Blackwood — Jogo de Investigação

Produto final: **2 PDFs profissionais** (nível de produto à venda) para um jogo de
investigação de assassinato em mansão, feito para **2 jogadores adultos**, dificuldade
**médio/difícil**, duração **2h+**.

| Arquivo | Conteúdo |
|---|---|
| `Caso_Mansao_Blackwood_JOGO.pdf` | O jogo completo: dossiê, evidências, fotos, suspeitos, puzzles, ficha de acusação |
| `Caso_Mansao_Blackwood_SOLUCAO.pdf` | Gabarito completo: solução passo a passo, linha do tempo real, explicação de cada puzzle |

---

## ⚙️ ESTADO ATUAL (snapshot para outra IA verificar)

- [x] Pesquisa de referências de mercado (Hunt A Killer, Case Files, etc.)
- [x] GitHub CLI instalado e **autenticado** como `Edubernardino7-recuperacao`
- [x] Repo git init em `C:\Users\eduardo\Desktop\detetive`
- [x] **36 imagens** baixadas em `assets/` (cenas, evidências, retratos, mansões)
- [x] Escrever HTML dos 2 PDFs (`jogo.html` 32 páginas · `solucao.html` 7 páginas)
- [x] Converter HTML → PDF (Chrome headless) — **validado página a página** com
      `pypdfium2` (`_render.py` gera PNGs em `_pages/`, `_sheet.py` monta folha de contato)
- [x] **PDFs conferidos visualmente**: JOGO = **32 páginas** (1 por seção),
      SOLUÇÃO = 7 páginas. Sem transbordamento.
- [x] Commit + push dos PDFs para `origin/main` (commits `b1516aa`, `ac6913e`)

### ✅ Correção aplicada (validação pós-geração)
- O primeiro PDF do jogo saiu com **6 páginas** (leitura truncada) e depois com
  **33 páginas** (seção "Três níveis de ajuda" com 15 caixas de dica transbordava
  a A4). Corrigido com `.hint-cols { column-count: 2 }` → agora **32 páginas exatas**.
- Sempre revalidar após regenerar: `python _render.py` e contar páginas.

### ⚠️ Nota técnica importante
- A geração de imagens por IA (`experimental_image_generate`) está **quebrada**
  (erro `Invalid credential`) — NÃO usar. Todas as imagens vêm da internet
  (Openverse/Flickr, licenças livres), baixadas via `curl.exe` com User-Agent.
- `System.Drawing` NÃO existe nesta máquina (PowerShell 7 / .NET sem Windows Forms).
  Para ler dimensões de imagem usar Python Pillow ou ignorar.
- PowerShell: NÃO usar `foreach` sobre `@{}` hashtables com `Invoke-WebRequest`
  (bug de interpretação) — usar lista de strings `nome|url` e `curl.exe`.
- Chrome em: `C:\Program Files\Google\Chrome\Application\chrome.exe`
  Conversão: `chrome --headless --disable-gpu --print-to-pdf=arquivo.pdf file:///caminho.html`

---

## 📖 INSTRUÇÕES DE CONTINUAÇÃO (para a IA verificadora)

Se este projeto parou no meio, faça NESTA ordem:

1. **Verifique o progresso**: `Get-ChildItem C:\Users\eduardo\Desktop\detetive`
   - Se existir `Caso_Mansao_Blackwood_*.pdf` → pule para o passo 5.
   - Se existir `jogo.html` / `solucao.html` mas sem PDF → passe para o passo 4.
   - Se não existir HTML → continue do passo 2.

2. **Crie o HTML do jogo** (`jogo.html`) — A4, português, design dark/cinema,
   fontes serifadas para documentos, carimbo "CONFIDENCIAL".
   Estrutura (~30-40 páginas):
   - Capa (foto mansão à noite + título)
   - Briefing/objetivo + regras + dica de tempo (2h) + níveis de dica
   - Resumo do caso + foto cena do crime + planta da mansão
   - Laudo policial preliminar
   - 6 dossiês de suspeitos (retrato + bio + declaração + segredo)
   - Evidências numeradas: fotos (cena, copo, candelabro, pílulas, relógio, chaves),
     cartas, testamento, registro telefônico, caderno cifrado, recibo
   - 4-5 puzzles: linha do tempo, cifra de substituição, dedução forense
     (veneno vs. ferimento), "quem mentiu", planta/localização
   - Ficha de acusação final preenchível (culpado, motivo, meio, oportunidade)

3. **Crie o HTML da solução** (`solucao.html`) — gabarito com:
   - Solução resumida no topo
   - Narrativa real dos acontecimentos (linha do tempo completa)
   - Passo a passo de cada puzzle
   - Por que cada suspeito é inocente/excluído
   - Como acusar corretamente

4. **Converta para PDF** com Chrome headless (comando acima).

5. **Commit e push**:
   ```powershell
   cd C:\Users\eduardo\Desktop\detetive
   git add -A
   git commit -m "feat: PDFs do jogo Caso Mansao Blackwood"
   git push origin main
   ```
   Remoto já configurado (`origin` → github.com/Edubernardino7-recuperacao/detetive).
   Se o repo não existir: `gh repo create detetive --public --source=. --remote=origin --push`

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
