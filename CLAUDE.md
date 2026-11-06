# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

## What this repository is

Not a software codebase — it is the versioned source for a suite of Claude **Skills** (`SKILL.md` files) and institutional documentation that back the Coordenação de Governança (CGOV/ICMBio)'s work: Notas Técnicas, normative analysis, risk management, AIR/ARR, and related governance instruments. There is no build, lint, or test tooling (no `package.json` or `Makefile`; `scripts/` holds only maintenance helpers) — "tests" are eval cases graded by running a skill against a prompt and checking its output against `expected_output`/`expectations`, not an automated harness.

## Commands

- **Run an eval case**: open `skills/<family>/<skill-name>/evals/evals.json`, take one `prompt`, run it through the corresponding skill, and manually check the output against that case's `expected_output` and `expectations` list. There is no runner script — do this by hand or via a subagent.
- **Validate a `SKILL.md` edit**: confirm the YAML frontmatter still has `name` and `description`; the `description` field has a **1,024-character hard limit** when installed via Customize → Skills in Claude (this has bitten the thematic skills before — see `docs/governance/decision-log.md` §10.3).
- **Git**: single-branch repo (`main`); the repository is **private** (GitHub `lpchagas/cgov-geral`), but `docs/` and `skills/` are kept sanitized as if they were public (plan decision D3). `local/` is fully gitignored — never `git add` anything under it.
- **Publish to operations**: ⏳ until phase 5.3 of the implementation plan (`scripts/publicar_operacao.py`), `scripts/publicar-operacao.sh` is **blocked** (it targets the pre-reorganization `_acervo-escritorio-virtual/` layout and would recreate it); only `--verificar` (installed × source comparison) still runs. Follow the transition procedure in `docs/fluxos-de-trabalho.md` §4.
- **Drive links**: ⏳ `scripts/link-acervo.sh` is **blocked**; the old links `local/normative-sources`, `local/acervo-drive` and `local/analyses` point to folders that no longer exist. New junctions (`local\processos`, `local\normativos`, `local\escritorio`) come in phase 5.1.
- **Maintenance scripts** (Python, run on Windows with `py`): `scripts/reorganizar_cgov.py` (phase 4 reorganization: `--planejar`, `--simular`, `--executar --lote`, `--reverter`, `--limpar-vazias`) and `scripts/gerar_indices.py` (`PROCESSO.md` cards and `_INDICE.md` indexes; `--saida` for a draft copy). Both need `--raiz` or `CGOV_RAIZ`.
- **Implementation plan**: `cgov-geral-plano-implantacao.md` (repo root) is the source of truth for progress; after each step it is updated in full (see its "Regra de manutenção").

## This session is the development flow

Claude Code in this repository (and the Cowork project "Escritório CGOV — Implantação") is the **development** side only (see `docs/fluxos-de-trabalho.md`). Day-to-day CGOV work — Notas Técnicas, SEI process analyses — runs in the Cowork project "Escritório CGOV — Operação" against the CGOV folder on Google Drive, not here.

- Don't produce process work here. Process material lives in the CGOV folder (`01_processos/<processo>/`); editing the operational areas is denied in `.claude/settings.json`. Eval/test output goes to `local/pilots/`.
- The 14 skills whose source lives in `skills/` are hidden from the model here (`skillOverrides`), because the installed copy synced into Claude Code can lag behind the source. Read and test the source `SKILL.md`, not the installed skill.
- Operational feedback arrives in `90_escritorio-virtual/manutencao/PENDENCIAS.md` of the CGOV folder (ask the user for it until the phase 5.1 junction `local\escritorio` exists); development backlog: `docs/governance/pendencias.md`.
- `git commit` and `git push` always ask for confirmation; the user must approve explicitly.

## Architecture

### Four-way split, by publication status

| Path | Role | Change rule |
|---|---|---|
| `skills/cgov-nt/`, `skills/thematic/` | Canonical skill **source** | Edit → run relevant evals → record decision in `docs/governance/decision-log.md` |
| `local/installed-reference/` | Read-only snapshots of *other* skills as actually installed | Reference only; don't edit to "fix" the installed skill |
| `archive/` | Sanitized historical evidence | Append context; never rewrite content |
| `docs/` | Publishable (sanitized) documentation | Keep links, normative citations, and personal-data scrubbing accurate |
| `operacao/` | Source of the navigation layer published into the CGOV folder (`LEIA-ME.md`, `AGENTS.md`, `_LEIA-ME.md`, templates) | Publish without overwriting (previous version to quarantine), SHA-256 checked |
| `local/` | Working acervo: Drive junctions (to be renamed in phase 5.1), pilots, reorganization map/manifests/logs, archive | Gitignored entirely — never committed |

**The critical gotcha**: editing a file in `skills/` does **not** change the skill as installed in a Claude account. Skills are installed via Customize → Skills, and source/installed can drift silently — this has happened repeatedly (decision-log §§10–11, 14) and produced skills that contradicted the actual norm they were meant to implement. Any skill edit requires: revise source → run evals → reinstall with overwrite → confirm the reinstalled version matches source → log it.

### The `cgov-nt` pipeline and its state file

`cgov-nt-01-triagem` is the mandatory entry point for any Nota Técnica; it classifies the demand against Art. 37 of Portaria ICMBio nº 5.592/2025 and creates `NT_ESTADO.md`, which subsequent skills (`cgov-nt-02` through `07`, invoked conditionally per the routing `cgov-nt-01` writes into `NT_ESTADO.md`) read and update. Since the phase 4 reorganization (decision-log §28) this state file lives in the CGOV folder at `01_processos/SEI_<órgão>.<número>_<ano>-<dv>_<apelido>/trabalho/NT_ESTADO.md` — **not** in the skill directories and **not** at the repo root. The skill sources still say `local/analyses/SEI_…/` and the installed `cgov-nt-01` says `CGOV_Processos/…/_CGOV_NT/` (source × installed drift, phase 6.1); the CGOV folder's `AGENTS.md` translates both until the skills become path-neutral (phase 6.3, ADR-006). The 74 process folders there are real working folders, not examples.

Fixed drafting conventions the whole suite enforces (validated against a real, filed Nota Técnica — not invented): present tense in NT prose (future tense only inside the text of a normative act itself); chapters as `### Capítulo N`, subsections `#### N.1` restarting per chapter (never subordinate numbering like `4.1.1` — this was tried and rejected); final proposition in lowercase roman numerals `(i) (ii) (iii)`; never invent a law/decree/portaria/article number — flag the gap with ⚠️ instead.

### Multi-platform instruction layering

This repo already serves more than one assistant surface, and the layering matters if you're asked to touch any of these files:

- **`AGENTS.md`** (repo root) — the cross-tool rules file, read natively by Antigravity (rules since IDE 1.20.5) and by OpenAI Codex/ChatGPT's coding surface. Claude Code does **not** read `AGENTS.md` natively — this `CLAUDE.md` pulls it in via the `@AGENTS.md` import above so it doesn't have to be duplicated. Keep `AGENTS.md` itself as pointers, not full instructions — its own text says so.
- **`docs/system-instructions/escritorio-cgov-operacao.md`** — the instructions of the Cowork project "Escritório CGOV — Operação" (paste the block into the project's **Instructions** field). That project is linked to the CGOV folder on Google Drive, **not** this repo; the path translation for the skills lives in the CGOV folder's `AGENTS.md` (source: `operacao/AGENTS.md`). The previous `escritorio-cgov.md` is archived in `archive/system-instructions/`. The instructions of the Cowork project "Escritório CGOV — Implantação" (development) are Appendix A of the implementation plan.
- **`docs/system-instructions/analista-governanca.md`** (v3.0, ~1,200 lines) — a **self-contained** system-instructions document with the normative base (Art. 37 full text, risk-methodology tables, AIR/ARR non-incidência vs. dispensa distinction, etc.) internalized inline, for assistants with **no file access** at all (Gemini Gems, ChatGPT GPTs/Projects). It exists precisely because a prior version assumed the model "knew" ICMBio's internal norms and it silently invented plausible-but-wrong details (decision-log §11.6 calls this out explicitly as the lesson learned). If you edit governance facts anywhere in this repo, this file is a second place they need to stay in sync — it does not re-read the rest of the repo at runtime.
- **`docs/system-instructions/analista-processos-sei.md`** — companion instructions for SEI process triage, integrated with the above.

### Sigla (acronym) discipline

CGOV governance work depends on strictly not confusing similarly-named instruments. This is fixed vocabulary, not house style — get it wrong and a citation in a real Nota Técnica is wrong: **PGR** = Programa de Gestão para Resultados e Inovação (Portaria nº 1.572/2023, Art. 37-VIII); **PGRI** = Política de Gestão de Riscos e Integridade (Portaria nº 255/2020, Art. 37-IX); **PGD** = Programa de Gestão e Desempenho / teletrabalho (IN ICMBio nº 14/2025, Art. 37-VII); **PGE** = Política de Gestão Estratégica, Portaria nº 768/2020 — **revoked**, do not cite as current (decision-log §14.2).

### Conventions (from `CONTRIBUTING.md`)

- New skills/docs: lowercase, hyphen-separated names.
- New process folders only in the CGOV folder under `01_processos/`, named `SEI_<órgão>.<número>_<ano>-<dv>_<apelido>/`, with a `PROCESSO.md` card — created by the Operação project, never from this repo.
- Superseded versions go to `archive/` — never delete them.
- No personal data, matrículas, SEI drafts, or non-redistributable source copies in anything destined for `docs/` or `skills/` (those are the publishable paths, kept sanitized even though the repository is private).
