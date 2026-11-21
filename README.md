# explica-tema

Skill para Claude Code que convierte un tema de teoría de ingeniería o ciencias (PDF,
apuntes, diapositivas) en una versión **explicada**: el mismo contenido y el mismo
vocabulario técnico, pero entendible.

**📄 [Explicación visual de la skill](https://g2004goitia-collab.github.io/explica-tema/)** · [Plantilla de ejemplo](https://g2004goitia-collab.github.io/explica-tema/ejemplo.html)

## Qué hace

- **Cada concepto en tres capas:** intuición (analogía o imagen mental), formal (definición y
  ecuaciones con la notación exacta del temario y su página) y aplicación (problemas, casos reales).
- **Recursos gráficos:** recupera todas las figuras del tema con su página, propone figuras nuevas
  (mapa del tema, esquemas redibujados, gráficas calculadas) y añade laboratorios interactivos.
- **Receta para resolver problemas, dudas para el profesor y glosario.** Las posibles erratas de la
  fuente se señalan como duda; nunca se corrigen en silencio.
- **Revisión de fidelidad obligatoria:** un agente independiente compara la versión explicada con la
  fuente, ecuación a ecuación, antes de entregar.
- **Dos formatos:** HTML interactivo y PDF A4.

## Instalación

```bash
git clone https://github.com/g2004goitia-collab/explica-tema.git ~/.claude/skills/explica-tema
```

Necesita `poppler-utils` (`pdftotext`, `pdftoppm`), ImageMagick (`montage`), Python 3 con Pillow
y Google Chrome o Chromium (para el PDF). Después, en Claude Code:

```
/explica-tema ~/apuntes/fisica/tema3.pdf
```

## Perfil personal (opcional)

Lo personal vive fuera de la skill, en `~/.claude/explica-tema/perfil.md`: dónde están tus apuntes,
dónde guardar, tus asignaturas y tus preferencias. Parte de `references/perfil-plantilla.md`. El
`.gitignore` impide subir un perfil por error.

## Estructura

```
SKILL.md                         flujo de 6 pasos
scripts/recortar_figuras.py      recorta las figuras de un PDF a partir de cajas en fracciones de página
scripts/renderizar_pdf.sh        HTML → PDF A4 con Chrome headless y comprobación de errores de KaTeX
assets/plantilla.html            plantilla: capas, marcas, laboratorio, impresión, temas claro y oscuro
references/perfil-plantilla.md   plantilla del perfil personal
docs/                            página explicativa (GitHub Pages)
```

## Derechos

El material que genera reutiliza figuras y contenido del profesorado: es material de estudio para
compartir dentro de la asignatura, no para publicarlo abiertamente.

## Licencia

MIT. Ver `LICENSE`.
