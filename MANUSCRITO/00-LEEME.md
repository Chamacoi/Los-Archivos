# MANUSCRITO

Aquí va el texto de la obra, en Markdown llano, un fichero por parte o capítulo.

Empieza I.1: «Capítulo 1. Inventario», **2.798 palabras** con el método limpio de recuento
(decisión 28, 2026-10-30; 2.851 medidas con `wc -w`), **revisado y aprobado por el autor** (v17).
Sigue I.2: «Capítulo 2. Los otros días», **2.727 palabras**, aprobado por el autor (v35, decisión 48).
Sigue I.3: «Capítulo 3. La división», **2.920 palabras**, aprobado por el autor y publicado el
2026-10-30 (v37, decisiones 50 y 51).
Sigue I.4: «Capítulo 4. La consola», **2.926 palabras**, aprobado por el autor y publicado el
2026-10-30 (v38, decisiones 52 y 53).
Sigue I.5: «Capítulo 5. El registro», **2.818 palabras**, escrito el 2026-11-01 (decisión 56),
revisado con el autor (decisión 57) y **aprobado** (decisión 58).

Sigue I.6: «Capítulo 6. Los de fuera», **3.269 palabras**, escrito el 2026-11-01 (decisión 60) y
aprobado el 2026-11-02 (decisión 61). Dossier de material en `../APUNTES.md` §0 septies.

Sigue I.7: «Capítulo 7. Las cuentas», **3.055 palabras**, escrito el 2026-11-02 (decisión 63) y
aprobado el 2026-11-02 (decisión 68). Dossier en `../APUNTES.md` §0 octies.

Sigue I.8: «Capítulo 8. El año que no se escribió», **3.368 palabras**, escrito el 2026-11-02
(decisión 72) y **aprobado el 2026-11-03** (decisión 77). Cierra el bloque I.1. Dossier en
`../APUNTES.md` §0 nonies.

Empieza I.2: «Capítulo 9. La hoja de oído», **3.009 palabras** (3.015 hasta la errata de la fórmula,
corregida el 2026-11-06, decisión 99), escrito el 2026-11-03 (decisión 78)
con las prácticas P2, P5 y P8 de E-05 (decisión 76) y **aprobado el 2026-11-04** (decisión 82).
Dossier en `../APUNTES.md` §0 decies.

Sigue I.10: «Capítulo 10. Los testigos», **2.825 palabras**, escrito el 2026-11-04 (decisión 83) con
las prácticas P1, P2 y P6 de E-05 y **aprobado el 2026-11-05** (decisión 84). Dossier en
`../APUNTES.md` §0 undecies.

Sigue I.11: «Capítulo 11. El nombre», **3.040 palabras**, escrito el 2026-11-05 (decisión 87) con las
prácticas P2, P5 y P8 de E-05 y **aprobado el 2026-11-05** (decisión 88), con el nombre propio a
criterio del texto. Dossier en `../APUNTES.md` §0 duodecies.

Sigue I.12: «Capítulo 12. Lo que no trae prueba», **2.794 palabras**, escrito el 2026-11-05 (decisión
93) con las prácticas P1, P6 y P8 de E-05 y **aprobado el 2026-11-06** (decisión 95). Dossier en
`../APUNTES.md` §0 terdecies.

Sigue I.13: «Capítulo 13. Lo que se dice de pie», **2.807 palabras**, escrito el 2026-11-06 (decisión
98) con las prácticas P6, P2 y P1 de E-05 y **aprobado** el 2026-11-07 (decisión 100). Dossier en
`../APUNTES.md` §0 quaterdecies.

Sigue I.14: «Capítulo 14. Los discos», **3.206 palabras**, escrito el 2026-11-07 (decisión 102) con
las prácticas P6, P1 y P2 de E-05 y un porcentaje de la sinopsis `S-02` usado como argumento (orden
del autor, decisión 101). **Aprobado** el 2026-11-08 (decisión 105). Dossier en `../APUNTES.md` §0
quindecies.

Sigue I.15: «La lista de los teléfonos», **pendiente de escritura**, séptimo del bloque I.2. Dossier de
material en `../APUNTES.md` §0 sedecies (decisión 106); no necesita decisiones del autor.

Desde v18 el texto se comprueba con el kit vendorizado en `../escritura/`:

```
../escritura/bin/nk estado
../escritura/bin/nk nuevo I.6 --titulo "Los de fuera"
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
