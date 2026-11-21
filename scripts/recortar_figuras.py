"""Recorta figuras de un PDF renderizado.
Uso: python3 recortar_figuras.py <pdf> <cajas.json> <carpeta_salida> [ppp]
cajas.json: {"f04-plano-inclinado": [pagina, x0, y0, x1, y1], ...} en fracciones (0–1) de la página.
Renderiza a 200 ppp por defecto y añade un margen pequeño. Revisa siempre el resultado en una hoja de contactos."""
import json, subprocess, sys, tempfile, pathlib
from PIL import Image
pdf, cajas, out = sys.argv[1], json.load(open(sys.argv[2])), pathlib.Path(sys.argv[3])
ppp = int(sys.argv[4]) if len(sys.argv) > 4 else 200
out.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory() as t:
    subprocess.run(['pdftoppm', '-png', '-r', str(ppp), pdf, f'{t}/p'], check=True)
    pags = sorted(pathlib.Path(t).glob('p-*.png'))
    for nombre, (pag, x0, y0, x1, y1) in cajas.items():
        im = Image.open(pags[pag - 1]); w, h = im.size; m = 0.008
        im.crop((int(max(0, x0 - m) * w), int(max(0, y0 - m) * h), int(min(1, x1 + m) * w), int(min(1, y1 + m) * h))).save(out / f'{nombre}.png')
        print(nombre)
