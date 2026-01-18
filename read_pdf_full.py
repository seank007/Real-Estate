from __future__ import annotations

import sys
from pathlib import Path

from pypdf import PdfReader


def main() -> int:
    here = Path(__file__).resolve().parent

    # Usage:
    #   python read_pdf_full.py [pdf_path] [output_path]
    pdf_path = Path(sys.argv[1]) if len(sys.argv) >= 2 else (here / "홍대 에어비앤비 사업 수익성 분석 1.pdf")
    output_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else (here / "pdf_full_content.txt")

    try:
        reader = PdfReader(str(pdf_path))
        with open(output_path, "w", encoding="utf-8") as f:
            for page in reader.pages:
                text = page.extract_text() or ""
                f.write(text + "\n\n")
        print(f"Successfully wrote content to {output_path}")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
