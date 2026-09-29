#!/usr/bin/env python3
"""
Inicializa o esqueleto de diretórios de um projeto de survey/tutorial,
conforme a estrutura exigida pela skill survey-writing.

Uso:
    python init_project.py /caminho/para/raiz-do-projeto ["Título provisório do projeto"]

Cria (sem sobrescrever nada que já exista):
    <raiz>/research.md              (a partir de assets/research-md-template.md)
    <raiz>/artigo/sections/         (vazio, populado na Fase 3)
    <raiz>/artigo/figures/          (vazio, populado na Fase 6)
    <raiz>/artigo/refs.bib          (vazio)
    <raiz>/scripts/                 (vazio, populado na Fase 6/2)
    <raiz>/literature/              (vazio, populado na Fase 2)
"""
import sys
import shutil
from pathlib import Path
from datetime import date

SKILL_DIR = Path(__file__).resolve().parent.parent


def init_project(root: str, title: str = "<TÍTULO PROVISÓRIO DO PROJETO>") -> None:
    root_path = Path(root).expanduser().resolve()
    root_path.mkdir(parents=True, exist_ok=True)

    # Subdiretórios
    (root_path / "artigo" / "sections").mkdir(parents=True, exist_ok=True)
    (root_path / "artigo" / "figures").mkdir(parents=True, exist_ok=True)
    (root_path / "scripts").mkdir(parents=True, exist_ok=True)
    (root_path / "literature" / "pdfs").mkdir(parents=True, exist_ok=True)

    # refs.bib vazio (não sobrescreve se já existir)
    refs_bib = root_path / "artigo" / "refs.bib"
    if not refs_bib.exists():
        refs_bib.write_text(
            "% Referências BibTeX do survey — mantidas em sincronia com\n"
            "% literature/literature_matrix.csv (ver references/02-coleta-literatura.md)\n"
        )

    # main.tex a partir do template, se ainda não existir
    main_tex = root_path / "artigo" / "main.tex"
    if not main_tex.exists():
        template = SKILL_DIR / "assets" / "template-article.tex"
        if template.exists():
            shutil.copy(template, main_tex)

    # literature_matrix.csv com cabeçalho
    matrix_csv = root_path / "literature" / "literature_matrix.csv"
    if not matrix_csv.exists():
        matrix_csv.write_text(
            "id,titulo,autores,ano,venue,citacoes,subtema_provisorio,"
            "status_triagem,motivo_exclusao,pdf_status,pdf_fonte_url,pdf_data,base_busca\n"
        )

    # research.md a partir do template
    research_md = root_path / "research.md"
    if not research_md.exists():
        template_md = SKILL_DIR / "assets" / "research-md-template.md"
        content = template_md.read_text()
        content = content.replace("<TÍTULO PROVISÓRIO DO PROJETO>", title)
        content = content.replace("<DATA>", date.today().isoformat())
        research_md.write_text(content)

    print(f"Projeto inicializado em: {root_path}")
    print(" - research.md")
    print(" - artigo/main.tex, artigo/sections/, artigo/figures/, artigo/refs.bib")
    print(" - scripts/")
    print(" - literature/literature_matrix.csv, literature/pdfs/")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    project_root = sys.argv[1]
    project_title = sys.argv[2] if len(sys.argv) > 2 else "<TÍTULO PROVISÓRIO DO PROJETO>"
    init_project(project_root, project_title)
