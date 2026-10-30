# 05. El proceso: del hecho al capítulo

La cadena completa, con un paso de más a propósito. El paso de más es el estudio: es lo que impide
que un capítulo se escriba directamente desde una frase dictada.

```
hecho dictado  →  S-nn (sinopsis)  →  preguntas y respuestas  →  C-n (canon)
                                                        ↓
                                            E-nn (estudio)
                                                        ↓
                                        capítulo (uno, con presupuesto)
```

## 1. Sinopsis (`SINOPSIS/S-nn-*.md`)

- El autor dicta el hecho. Se guarda **literal**: sus palabras, sus faltas, sus dudas. No se
  corrige la voz de quien dicta.
- El mismo fichero lleva cinco preguntas fijas: qué pasó, quién lo hizo, cuándo, qué se conserva,
  qué tono tiene.
- Se contestan por escrito, también literal, en §4. Mientras haya preguntas abiertas, el hecho no
  es canon.

## 2. Canon (`APUNTES.md` §4)

- De las respuestas sale una entrada `C-n` (ver `04-canon.md`), con sus tensiones y su límite de
  estatuto de verdad.
- Se anota en el registro de decisiones (`APUNTES.md` §3), con fecha.

## 3. Estudio (`ESTUDIOS/E-nn-*.md`)

Es el paso que se salta casi todo el mundo y el que hace que el libro aguante. Contiene:

1. El hecho, en una página.
2. Qué parte es verdad de marco y qué parte no puede presentarse como ciencia.
3. Qué documentos se pueden citar y con qué grado de verdad de superficie.
4. **Lo que no se puede narrar**: lo que acusaría a personas reales, lo que convertiría el hecho
   en tesis, lo que el narrador no puede saber.
5. La doble lectura: cómo admite leerse como don y como daño.
6. El coste: quién pierde qué.
7. Los tres o cuatro lugares donde el hecho toca la estructura (anclajes).
8. Preguntas abiertas, sin miedo a dejarlas abiertas.

Un estudio es más largo que el capítulo que produce. Si es más corto, el capítulo va a improvisar.

## 4. Hueco

En `libro.json` (partes, capítulos, anclajes) y en `ESTRUCTURA.md` (bloques y función). El
presupuesto de palabras ya está calculado.

```
nk andamiaje
nk nuevo II.9 --titulo "La siembra" --desde E-03
```

## 5. Capítulo (`MANUSCRITO/NN-parte/KK-capitulo.md`)

- Se escribe de una tirada, por secciones numeradas (`## 1. …`), no por escenas.
- Se citan documentos con `>`, conservando faltas y elisiones.
- Se cierra en imagen, no en tesis.
- Se verifica **antes** de dar por escrito:

```
nk contar            # palabras frente a presupuesto
nk verificar --rubrica
```

Si está fuera del ±20 %, **se anota la desviación**; no se alarga el capítulo siguiente para
compensar (ver `06-conteo.md`).

## 6. Revisión

Se lee como lector, no como autor: ¿se puede describir lo que pasa sin adjetivos? ¿Hay algo que el
narrador esté explicando de más? ¿Alguien pierde algo? La parrilla está en `08-rubrica.md`.

Solo después de la lectura del autor se escribe el capítulo siguiente. Un capítulo aprobado fija la
voz; cinco capítulos sin revisión fijan un error cinco veces.

## 7. Cierre

- `nk informe` → `estado.json` (legible por máquina).
- Commit por capítulo, con recuento real frente a presupuesto y desviación.
- Entrada de tres líneas en `BITACORA.md` y otro commit.
