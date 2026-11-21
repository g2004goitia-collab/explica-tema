#!/usr/bin/env bash
# Uso: renderizar_pdf.sh <tema.html>  → genera <tema.pdf> al lado y comprueba que KaTeX no dejó errores.
set -euo pipefail
html="$(realpath "$1")"; pdf="${html%.html}.pdf"
chrome="$(command -v google-chrome || command -v chromium || command -v chromium-browser)"
"$chrome" --headless=new --disable-gpu --no-sandbox --run-all-compositor-stages-before-draw \
  --virtual-time-budget=15000 --no-pdf-header-footer --print-to-pdf="$pdf" "file://$html" 2>/dev/null
dom="$(mktemp)"; "$chrome" --headless=new --disable-gpu --no-sandbox --virtual-time-budget=15000 --dump-dom "file://$html" 2>/dev/null > "$dom"
ok=$( (grep -o 'class="katex"' "$dom" || true) | wc -l); err=$( (grep -o 'katex-error' "$dom" || true) | wc -l); rm -f "$dom"
echo "PDF: $pdf ($(pdfinfo "$pdf" | awk '/Pages/{print $2}') páginas) · fórmulas: $ok · errores KaTeX: $err"
[ "$err" -eq 0 ]
