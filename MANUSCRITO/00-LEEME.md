# MANUSCRITO

Aquí va el texto de la obra, en Markdown llano, un fichero por parte o capítulo.

Empieza I.1: «Capítulo 1. Inventario», **2.798 palabras** con el método limpio de recuento
(decisión 28, 2026-10-30; 2.851 medidas con `wc -w`), **revisado y aprobado por el autor** (v17).
Sigue I.2: «Capítulo 2. Los otros días», **2.727 palabras**, aprobado por el autor (v35, decisión 48).

Desde v18 el texto se comprueba con el kit vendorizado en `../escritura/`:

```
../escritura/bin/nk estado
../escritura/bin/nk nuevo I.3 --titulo "La división"
../escritura/bin/nk contar
../escritura/bin/nk verificar --rubrica
```

El encabezado de cada capítulo es `# Capítulo N. Título`, con el número del fichero.
Los capítulos pendientes no se crean a mano: los abre `nk nuevo`, que pone el presupuesto.
El punto 1 de `../APUNTES.md` (voz, autoría y alocución), el criterio de selección (punto 3), el
reparto de palabras (escenario A) y la forma de la demostración están cerrados. Los capítulos de
hecho salen de un estudio de `../ESTUDIOS/`; los de marco (I.1, II.1…) salen de canon y
estructura. Un capítulo no se escribe directamente desde una sinopsis.

Convención de nombres:

    01-parte-I/
      01-capitulo.md
      02-capitulo.md
    02-parte-II/
      ...

Materiales de trabajo (transcripciones, recortes, notas sueltas) **no** van aquí: van a
`../MATERIALES/` cuando se cree.
