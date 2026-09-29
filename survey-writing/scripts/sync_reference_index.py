#!/usr/bin/env python3
"""
Regenera a seção "Índice de Referências" de research.md a partir de
literature/literature_matrix.csv, sem tocar no restante do arquivo
(o Log de Atividades, que é append-only).

Uso:
    python sync_reference_index.py /caminho/para/raiz-do-projeto

Espera encontrar:
    <raiz>/literature/literature_matrix.csv
    <raiz>/research.md   (com os marcadores INDICE-REFERENCIAS:START/END —
                           já presentes se o projeto foi criado com
                           init_project.py / assets/research-md-template.md)
"""
import csv
import sys
from pathlib import Path

START_MARKER = "<!-- INDICE-REFERENCIAS:START -->"
END_MARKER = "<!-- INDICE-REFERENCIAS:END -->"

PDF_STATUS_LABELS = {
    "baixado": "✅ `literature/pdfs/{id}.pdf`",
    "indisponivel_pago": "❌ indisponível (acesso pago) — {url}",
    "indisponivel_nao_encontrado": "❌ não encontrado — {url}",
    "pendente": "⏳ pendente",
    "nao_aplicavel": "— (não incluído)",
}


def format_pdf_status(row: dict) -> str:
    status = (row.get("pdf_status") or "pendente").strip()
    template = PDF_STATUS_LABELS.get(status, status or "⏳ pendente")
    return template.format(id=row.get("id", ""), url=row.get("pdf_fonte_url", "") or "URL não registrada")


def build_table(csv_path: Path) -> str:
    if not csv_path.exists():
        return "_(literature_matrix.csv ainda não existe — nada para indexar.)_"

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader if (r.get("status_triagem") or "").strip() == "incluído"]

    if not rows:
        return "_(nenhuma referência marcada como \"incluído\" ainda.)_"

    lines = [
        "| ID | Título | Ano | Venue | PDF local |",
        "|---|---|---|---|---|",
    ]
    for row in sorted(rows, key=lambda r: (r.get("ano") or "", r.get("id") or "")):
        lines.append(
            "| {id} | {titulo} | {ano} | {venue} | {pdf} |".format(
                id=row.get("id", ""),
                titulo=row.get("titulo", ""),
                ano=row.get("ano", ""),
                venue=row.get("venue", ""),
                pdf=format_pdf_status(row),
            )
        )
    return "\n".join(lines)


def sync(root: str) -> None:
    root_path = Path(root).expanduser().resolve()
    csv_path = root_path / "literature" / "literature_matrix.csv"
    research_md = root_path / "research.md"

    if not research_md.exists():
        print(f"research.md não encontrado em {root_path} — rode init_project.py primeiro.")
        sys.exit(1)

    content = research_md.read_text(encoding="utf-8")
    if START_MARKER not in content or END_MARKER not in content:
        print(
            "Marcadores INDICE-REFERENCIAS:START/END não encontrados em research.md. "
            "Adicione-os manualmente (ver assets/research-md-template.md) antes de rodar este script."
        )
        sys.exit(1)

    table = build_table(csv_path)
    new_block = (
        f"{START_MARKER}\n"
        "## Índice de Referências\n\n"
        "_Gerado automaticamente por `scripts/sync_reference_index.py` a partir de "
        "`literature/literature_matrix.csv`. Não editar manualmente — rode o script "
        "novamente após qualquer mudança na matriz._\n\n"
        f"{table}\n\n"
        f"{END_MARKER}"
    )

    pre, _, rest = content.partition(START_MARKER)
    _, _, post = rest.partition(END_MARKER)
    new_content = pre + new_block + post

    research_md.write_text(new_content, encoding="utf-8")
    print(f"Índice de Referências atualizado em {research_md}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    sync(sys.argv[1])
