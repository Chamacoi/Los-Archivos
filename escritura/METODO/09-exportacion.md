# 09. Exportación

El texto se escribe en Markdown llano y se exporta sin depender de una herramienta concreta. El kit
trae un exportador propio: no necesita Pandoc ni Calibre.

## EPUB

```
nk exportar                 # salida.epub
nk exportar --salida otra.epub
```

Genera un **EPUB 3** válido con:

- `mimetype` sin comprimir, el primero del contenedor (requisito del formato);
- `META-INF/container.xml`;
- `OEBPS/content.opf` con `dc:title`, `dc:creator` (el del colofón, si lo hay), `dc:language`,
  `dc:date` y un identificador **derivable de la obra** (no aleatorio);
- `OEBPS/nav.xhtml` con el índice de capítulos;
- una hoja de estilo única y sobria, sin fuentes incrustadas y sin imágenes;
- un XHTML por capítulo, con el encabezado del capítulo convertido en `h1`.

La exportación es **reproducible**: los ficheros del ZIP llevan fecha fija, así que la misma entrada
produce el mismo EPUB byte a byte. Sirve para comparar versiones.

### Metadatos

```json
"libro": {
  "titulo": "…",
  "autor": "…",
  "idioma": "es-ES",
  "fecha": "AAAA-MM-DD",
  "salida": "salida"
}
```

`colofon` (opcional) se imprime como última página del EPUB: titularidad, año y condiciones. Es el
sitio de la firma editorial, y el único: el relato no lleva firma.

`autor` es **titularidad editorial** (colofón), no autoría del relato: el texto no lleva firma. Si
el libro no debe llevar nombre, se deja vacío y el EPUB sale sin `dc:creator`.

## Markdown combinado

```
nk exportar -f md --salida libro.md
```

Útil para revisión, para contar palabras de todo el libro de una vez o para entregar a un lector
externo.

## Antes de exportar

```
nk verificar --rubrica
nk contar
```

Un EPUB con un dato sensible dentro es un fichero que ya no se puede recoger. La verificación de
`nk` es la última barrera, no la primera: el material de terceros no se guarda en el repositorio.

## Lo que el kit no hace

- No maqueta portada (si hace falta, se añade después con una herramienta de edición).
- No genera PDF ni MOBI.
- No convierte a `.docx`.
- No valida con `epubcheck`: si se quiere validación externa, se instala aparte y se pasa sobre el
  fichero. El kit comprueba estructura y XML bien formado, que es lo que puede comprobar sin
  dependencias.
