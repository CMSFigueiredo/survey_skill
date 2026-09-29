#!/usr/bin/env python3
"""
Gera a tabela LaTeX de classificação da taxonomia (Fase 3/6 da skill
survey-writing) a partir de literature/literature_matrix.csv.

Cada linha da tabela de saída corresponde a uma subseção do corpo
principal (taxonomia adotada, eixos principais, transversais), na
mesma ordem em que essas subseções foram confirmadas com o usuário
na Fase 3, e lista as chaves de citação de todas as referências
incluídas (status_triagem == "incluido") que foram atribuídas àquela
subseção pela coluna `subtema_provisorio`.

IMPORTANTE: `subtema_provisorio` deve estar atualizada, na Fase 3,
com o nome FINAL da subseção confirmada (não o rótulo provisório da
Fase 2) — este script não infere nem corrige rótulos.

Uso:
    python3 scripts/gen_taxonomia_table.py \
        --matrix literature/literature_matrix.csv \
        --out artigo/figures/tabela_taxonomia.tex \
        --ordem "Taxonomia adotada" "Eixo 1" "Eixo 2" "Transversal 1"

Se --ordem não for passado, a ordem das subseções na tabela segue a
ordem de primeira aparição de `subtema_provisorio` no CSV (garanta,
nesse caso, que o CSV já reflita a ordem confirmada na Fase 3).
"""

import argparse
import csv
import sys
from collections import OrderedDict
from pathlib import Path


def carregar_referencias_incluidas(matrix_path: Path):
    if not matrix_path.exists():
        sys.exit(f"Erro: matriz de literatura não encontrada em {matrix_path}")

    referencias = []
    with matrix_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        campos_esperados = {"id", "subtema_provisorio", "status_triagem"}
        faltando = campos_esperados - set(reader.fieldnames or [])
        if faltando:
            sys.exit(
                f"Erro: colunas obrigatórias ausentes em {matrix_path}: {faltando}"
            )
        for linha in reader:
            if (linha.get("status_triagem") or "").strip().lower() not in (
                "incluido",
                "incluído",
                "incluida",
                "incluída",
            ):
                continue
            chave = (linha.get("id") or "").strip()
            subsecao = (linha.get("subtema_provisorio") or "").strip()
            if not chave:
                continue
            if not subsecao:
                sys.exit(
                    f"Erro: referência '{chave}' está incluída mas sem "
                    "subtema_provisorio preenchido — atualize a matriz na "
                    "Fase 3 antes de gerar a tabela (nenhuma referência "
                    "incluída pode ficar sem subseção atribuída)."
                )
            referencias.append((chave, subsecao))
    return referencias


def agrupar(referencias, ordem_forcada):
    grupos = OrderedDict()
    if ordem_forcada:
        for nome in ordem_forcada:
            grupos[nome] = []

    for chave, subsecao in referencias:
        grupos.setdefault(subsecao, []).append(chave)

    if ordem_forcada:
        extras = [s for s in grupos if s not in ordem_forcada]
        if extras:
            sys.stderr.write(
                "Aviso: subseções presentes no CSV mas ausentes de --ordem, "
                f"adicionadas ao final: {extras}\n"
            )
    return grupos


def escrever_tabela(grupos, out_path: Path):
    total = sum(len(v) for v in grupos.values())
    linhas = []
    linhas.append("% Gerado automaticamente por scripts/gen_taxonomia_table.py")
    linhas.append("% NÃO editar manualmente — regenerar o script após mudar a taxonomia.")
    linhas.append("\\begin{table}[t]")
    linhas.append("  \\centering")
    linhas.append("  \\caption{Classificação das referências incluídas segundo a taxonomia adotada.}")
    linhas.append("  \\label{tab:taxonomia-classificacao}")
    linhas.append("  \\small")
    linhas.append("  \\begin{tabular}{@{}lp{0.55\\linewidth}c@{}}")
    linhas.append("    \\toprule")
    linhas.append("    \\textbf{Subseção} & \\textbf{Referências} & \\textbf{Nº} \\\\")
    linhas.append("    \\midrule")
    for subsecao, chaves in grupos.items():
        if not chaves:
            continue
        cites = ",".join(chaves)
        linhas.append(
            f"    {subsecao} & \\cite{{{cites}}} & {len(chaves)} \\\\"
        )
    linhas.append("    \\midrule")
    linhas.append(f"    \\textbf{{Total}} & & \\textbf{{{total}}} \\\\")
    linhas.append("    \\bottomrule")
    linhas.append("  \\end{tabular}")
    linhas.append("\\end{table}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--matrix", default="literature/literature_matrix.csv", type=Path)
    parser.add_argument("--out", default="artigo/figures/tabela_taxonomia.tex", type=Path)
    parser.add_argument("--ordem", nargs="*", default=None, help="Ordem das subseções confirmada na Fase 3")
    args = parser.parse_args()

    referencias = carregar_referencias_incluidas(args.matrix)
    if not referencias:
        sys.exit(
            "Erro: nenhuma referência com status_triagem=incluido encontrada "
            f"em {args.matrix} — nada a tabular."
        )
    grupos = agrupar(referencias, args.ordem)
    escrever_tabela(grupos, args.out)
    print(f"Tabela de classificação da taxonomia gerada em: {args.out}")
    print(f"Total de referências tabuladas: {sum(len(v) for v in grupos.values())}")


if __name__ == "__main__":
    main()
