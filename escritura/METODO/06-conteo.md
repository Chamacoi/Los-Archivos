# 06. Recuento, presupuesto y desviación

## Cómo se cuentan las palabras

`nk` define el recuento así: se elimina el *frontmatter*, se quitan las marcas de Markdown
(encabezados, `>`, viñetas, numeración de listas, barras de tabla, `*`, comillas invertidas, enlaces
e imágenes), y se cuentan las **secuencias de letras o cifras**. Los signos sueltos no cuentan.

Se cuentan **todas** las palabras del capítulo: narración y documentos citados. Un documento citado
es tan parte del libro como la narración, y a veces más.

### Por qué no se usa `wc -w`

`wc -w` cuenta también las marcas de Markdown y los signos separados por espacios. En el capítulo
I.1 de la obra de origen:

| Método | Palabras |
|---|---|
| `wc -w` | 2.851 |
| `nk` (`palabras`, secuencias de letras o cifras) | 2.798 |

La diferencia (53) son `>`, `—`, `##`, `1.` y demás marcas, más los compuestos con guion que
`wc -w` separa. Con presupuestos de 3.025, un 1,9 % de ruido no cambia nada; con capítulos de
1.200, sí. La obra de origen adoptó el método limpio el 2026-10-30 y recalibró su primer capítulo. El kit usa el método limpio y elige **un método
por libro**, declarado en `libro.json`:

```json
"conteo": { "metodo": "palabras" }     // o "tokens" para reproducir `wc -w`
```

Si un libro viene de otro método, se puede cambiar, pero entonces **hay que recalibrar**: se anota
la fecha del cambio y se recuentan los capítulos ya escritos. Cambiar de método a mitad del libro
sin anotarlo es falsear el registro.

## Presupuesto

- `objetivo_palabras` en `libro.json` es el total del libro.
- Se reparte por partes (`palabras`) y por capítulos. Si una parte declara `presupuesto.reparto`
  (por ejemplo `{"3025": 40, "3024": 23}`), se usa ese reparto exacto; si no, se reparte a partes
  iguales con el resto en los primeros capítulos.
- Tolerancia por capítulo: `±20 %` por defecto (`presupuesto.tolerancia`).

## Regla de la desviación

**La desviación se anota. No se compensa.**

Un capítulo corto no se arregla alargando el siguiente: se anota el hueco y se decide, al cerrar la
parte, si se recupera con un capítulo más o si el total baja. Compensar sobre la marcha produce
capítulos inflados y un total que nadie sabe de dónde sale.

## Qué hace `nk`

```
nk contar                # tabla: palabras, presupuesto, desviación, acumulado por parte
nk contar --todo         # incluye los capítulos que aún no existen
nk contar --actualizar   # reescribe el bloque nk:recuento de ESTRUCTURA.md
nk contar --json         # la misma tabla, legible por máquina
nk contar --wc           # compara con `wc -w`
```

El bloque de `ESTRUCTURA.md` se reescribe entre `<!-- nk:recuento -->` y `<!-- /nk:recuento -->`;
lo que esté fuera no se toca.

## Control de totales

```
total = Σ partes = Σ capítulos (presupuesto × n)
```

`nk informe` escribe `estado.json` con el desglose y marca los capítulos fuera de tolerancia. Es la
fuente para cualquier gráfico o informe externo: no hace falta parsear Markdown.

## ¿Cifra exacta, techo o referencia?

`libro.json` lo declara, porque cambia lo que significa cumplir:

```json
"libro": {
  "objetivo_palabras": 381104,
  "objetivo_tipo": "referencia",
  "tolerancia_total": 0.10
}
```

- **`exacta`**: el total se persigue; el reparto por capítulos lo hace cuadrar y la última página debe
  llegar justo. Sirve cuando la cifra es parte del proyecto (un pastiche medido, una imitación
  declarada).
- **`referencia`**: la cifra es el **resultado aproximado** que se espera, no un objetivo que se
  fuerza. Los presupuestos por capítulo siguen siendo guía y la desviación se sigue anotando, pero
  nadie alarga ni recorta el final para cuadrar. Cuando el libro está completo, `nk verificar`
  compara el total con la referencia y avisa solo si se aleja más de `tolerancia_total`.
- **`techo`**: la cifra es un máximo; pasarse es el error, quedarse corto no.

El modo `referencia` es el honesto para una obra de esta clase: el número orienta la arquitectura y
después se deja que el libro diga lo que tenga que decir. Lo que **no** cambia con el modo: la
desviación por capítulo se anota siempre, y nunca se compensa alargando el siguiente.
