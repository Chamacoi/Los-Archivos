# 01. El contrato de reproducibilidad

Este kit no genera un libro. Genera las condiciones para que **otra persona escriba el mismo tipo
de libro** y para que el resultado se pueda comparar con el original sin discutir de gusto.

Conviene decir qué se puede repetir y qué no, porque la palabra «programar» promete de más.

## Lo que es determinista

| Elemento | Dónde vive | Se puede repetir |
|---|---|---|
| Número de partes y capítulos | `libro.json` | sí, exacto |
| Palabras por capítulo y tolerancia | `libro.json` | sí, exacto |
| Reparto de bloques y anclajes | `libro.json` + `ESTRUCTURA.md` | sí, exacto |
| Formato de encabezados y nombres de fichero | `METODO/` + `nk` | sí, exacto |
| Recuento y desviación | `nk contar` | sí, exacto |
| Registro de lo decidido | `APUNTES.md` §3 | sí, por fecha |
| Canon | `APUNTES.md` §4 | sí, literal |
| Invariantes del texto (prohibiciones, datos sensibles) | `libro.json` | sí, comprobable |
| EPUB | `nk exportar` | sí, byte a byte con la misma entrada |
| Prosa | `MANUSCRITO/` | **no** |

## Lo que no es determinista

La prosa. Dos personas con el mismo canon y el mismo estudio escriben dos capítulos distintos. Eso
no es un defecto del método: es lo que hace que el libro sea de alguien. El método no promete el
mismo texto; promete que el texto resultante **pase las mismas pruebas**.

## Qué significa «resultado similar»

Tres niveles, de más exigente a menos:

1. **R1 — mismo texto.** No se pretende. Solo sería posible grabando la prosa en el repositorio,
   y entonces el kit no sería un método sino una copia.
2. **R2 — misma voz verificable.** El capítulo pasa la rúbrica (`METODO/08-rubrica.md`): tercera
   persona sin «yo», proporción de documentos citados dentro de rango, secciones numeradas, sin
   valoración del narrador, sin moraleja de cierre, presupuesto de palabras dentro del ±20 %,
   ningún dato sensible, ninguna frase prohibida. **Esto es lo que el kit garantiza.**
3. **R3 — mismo esqueleto.** Mismas partes, mismos capítulos, mismos huecos, mismas anclas de los
   hechos, mismo reparto de palabras. Lo garantiza `libro.json`.

Si alguien escribe el libro entero con este kit y obtiene R3 y R2, el resultado será «similar» en
el único sentido que importa: se podrá leer como el mismo género de archivo, con la misma
disciplina, y se podrá comparar capítulo a capítulo con el original sin hablar de impresiones.

## De dónde sale cada capítulo

Regla dura, ya probada en la obra de origen:

- **Capítulos de hecho:** salen de un **estudio** (`ESTUDIOS/E-nn`), que a su vez sale de una
  **sinopsis literal** del autor (`SINOPSIS/S-nn`). Nunca de la sinopsis directamente.
- **Capítulos de marco:** salen de **canon + estructura**. No tienen sinopsis porque no narran un
  hecho dictado: narran el presente del archivo.

Un capítulo que no pueda señalar su entrada —`<!-- fuente: E-03 -->`, o el canon que lo autoriza—
no se escribe.

## Las entradas son el programa

El kit no «sabe» escribir. Lo que hace es obligar a que la entrada esté completa antes de la
salida:

1. Un hecho dictado, literal, sin corregir la voz de quien lo dicta (`SINOPSIS/`).
2. Sus preguntas y respuestas, también literales.
3. El canon que fija (`C-n`), con sus tensiones anotadas.
4. El estudio, que separa lo que se puede narrar de lo que no (`ESTUDIOS/`).
5. El hueco en la estructura, con presupuesto y ancla (`libro.json`, `ESTRUCTURA.md`).
6. La prosa, y la verificación.

Saltearse un paso no acelera: desplaza el error al capítulo, donde cuesta más.

## Límite honesto

Un clon del repositorio no produce el libro: produce **el mismo andamiaje, las mismas reglas y las
mismas comprobaciones**. El texto hay que escribirlo. Lo que el kit arregla es que ese texto no
pueda ser arbitrario sin que se note.
