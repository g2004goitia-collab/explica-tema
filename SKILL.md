---
name: explica-tema
description: >
  Convierte un tema de teoría de ingeniería o ciencias (PDF, apuntes, diapositivas) en una
  versión explicada que conserva todo el contenido y el vocabulario técnico pero se entiende:
  cada concepto en tres capas (intuición, formal con la notación del temario, aplicación),
  las figuras del tema recuperadas con su página, figuras e interactivos nuevos marcados como
  propuesta, receta para resolver problemas, dudas para el profesor y glosario. Entrega HTML
  interactivo y PDF A4, y pasa una revisión de fidelidad independiente contra la fuente.
  Usar cuando alguien diga «explícame este tema», «hazme una versión fácil de la teoría»,
  «no entiendo estos apuntes», «simplifica el tema X», «teoría ilustrada de…»,
  «/explica-tema», o pase un PDF de teoría pidiendo entenderlo, aunque no diga «skill».
  No usar para fotos de la pizarra de una clase (eso son apuntes nuevos, no teoría) ni
  para resolver ejercicios sueltos.
---

# /explica-tema — La teoría, entendible y completa

**Simplificar el lenguaje, no el contenido.** El alumno tiene que acabar dominando el
vocabulario técnico, así que ningún término, ecuación o ejemplo del temario desaparece:
se presenta. Una explicación sencilla pero equivocada es peor que ninguna, por eso la
revisión de fidelidad no es opcional.

## 0. Perfil

Si existe `~/.claude/explica-tema/perfil.md`, léelo: rutas de los apuntes (fuente, solo
lectura) y de destino, asignaturas, estilo visual preferido, fechas de examen. Si no,
pregunta solo dónde está la fuente y dónde guardar, y ofrece crear el perfil al final
con `references/perfil-plantilla.md`.

## 1. Leer la fuente entera

- `pdftotext -layout` para el texto. Las ecuaciones de PDFs antiguos salen desordenadas:
  renderiza las páginas (`pdftoppm -r 110`) y míralas para leer cada ecuación bien.
- Monta hojas de contactos (`montage`) para localizar todas las figuras sin leer página a página.
- La fuente es de solo lectura: trabaja en una carpeta temporal.

## 2. Mapear antes de explicar

Escribe (para ti) el mapa del tema: conceptos, de qué depende cada uno, ecuaciones con su
página, figuras con su página, términos técnicos, ejemplos y preguntas abiertas del
temario. Apunta aquí cualquier posible errata o ambigüedad de la fuente: irá a «Dudas para
el profesor». **Nunca corrijas la fuente en silencio**: si usas la forma estándar, dilo.

## 3. Escribir la versión explicada

Parte de `assets/plantilla.html` (estructura, estilos, capas, laboratorios y
modo de impresión ya resueltos). Estructura:

1. Cómo leer el documento (leyenda de capas y marcas) y **mapa del tema** (figura propuesta).
2. Una sección por bloque del temario, en orden de dependencias. Cada concepto en capas:
   - **Intuición**: analogía o imagen mental, del mundo real o del campo del alumno.
   - **Formal**: definición y ecuaciones **con la notación exacta del temario** y su página.
   - **Aplicación**: uso en problemas, caso real, o respuesta a las preguntas que deja el temario.
   - Cajas de **error típico** donde el temario o la experiencia los señalan.
3. **Receta para resolver problemas** del tema (propuesta), si el tema es de problemas.
4. **Dudas para el profesor**: posibles erratas, notación inconsistente, términos ambiguos.
5. **Glosario** de todos los términos técnicos.

Marca todo lo añadido con la etiqueta «Propuesta» y todo lo del temario con «Temario p. N».
Ecuaciones en LaTeX (KaTeX): `\( … \)` en línea y `$$ … $$` en bloque. No uses `·` dentro de
`\text{}`; escribe unidades con `\mathrm{kg\,m\,s^{-2}}`.

## 4. Recursos gráficos

- **Recuperados**: todas las figuras del tema. Recorta con `scripts/recortar_figuras.py`
  y **revisa una hoja de contactos de los recortes**: casi siempre hay que afinar alguno que
  arrastra texto vecino. Si una figura está mezclada con texto, redibújala en SVG limpio.
- **Propuestos**: mapa del tema, esquemas redibujados, comparativas, gráficas calculadas.
- **Interactivos** (solo HTML): 2–4 laboratorios con controles deslizantes donde ver el efecto
  de un parámetro ayude a entender (fuerzas en un plano, una curva que tiende a un límite…).
  En el PDF se muestran en su estado inicial, con una nota que lo dice.

## 5. Revisión de fidelidad (obligatoria)

Lanza un agente revisor independiente (que no haya escrito el documento) con la fuente y
la versión explicada. Debe comprobar: cada ecuación atribuida al temario frente a la
fuente; cada afirmación conceptual; la física y el álgebra de lo «Propuesto»; omisiones;
las dudas para el profesor; y que el código de los laboratorios calcula bien. Aplica sus
correcciones y menciona al usuario las que no apliques y por qué.

## 6. Generar y entregar

```bash
scripts/renderizar_pdf.sh tema.html   # PDF A4 + comprobación de errores de KaTeX (debe dar 0)
```

Si además se publica como página web en un servicio con política de contenido estricta (por ejemplo, un artifact de claude.ai, que solo admite hojas de estilo de Google Fonts), incrusta en el HTML la hoja de KaTeX con sus fuentes como `data:` URI; si no, las fórmulas se ven sin estilo.

Guarda en la carpeta de destino `tema-explicado.html`, `tema-explicado.pdf` y `figuras/`.
Si el destino es un vault de Obsidian, añade una nota corta con el PDF incrustado.

Entrega al usuario: dónde está, qué contiene (secciones, nº de figuras recuperadas y
propuestas, laboratorios), las dudas para el profesor y lo que corrigió la revisión.

## Derechos

Las figuras y el texto del temario son del profesorado: el resultado es material de
estudio para la asignatura y se comparte con compañeros, no se publica abiertamente.
