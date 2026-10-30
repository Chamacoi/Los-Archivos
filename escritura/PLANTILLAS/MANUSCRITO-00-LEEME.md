# MANUSCRITO — «{{TITULO}}»

Texto de la obra en Markdown llano, un fichero por capítulo:

```
01-parte-I/
  01-capitulo.md
  02-capitulo.md
02-parte-II/
  ...
```

Convenciones que `nk` comprueba:

- El encabezado es `# Capítulo N. Título`, y N coincide con el número del fichero.
- Secciones: `## 1. …`, `## 2. …`, de 3 a 6.
- Documentos citados con `>`, conservando faltas y elisiones marcadas.
- Sin nombres propios de personas que no consten en `../PERSONAS.md`.
- Material de trabajo no literario **no** va aquí: va a una carpeta ignorada por git.
