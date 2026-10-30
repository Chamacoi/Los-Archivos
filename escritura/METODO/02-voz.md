# 02. La voz

La voz se fija **antes** del primer capítulo y no se cambia a mitad del libro. Estas son las
decisiones que la obra de origen tomó y que el kit propone como punto de partida editable.

## Los cuatro parámetros

1. **Persona y focalización.** Tercera persona, narrador exterior a la comunidad y a su fuente,
   con **focalización total**: sabe lo que piensa cualquiera y lo que la fuente calla. No hay
   «yo» autoral, ni detrás del texto, ni en notas, ni en el aparato.
2. **Autoridad.** La omnisciencia, apoyada en el motivo del archivo: el narrador sabe **porque
   consta**. Lo que no consta, no se afirma; se muestra el hueco.
3. **Autoría textual.** **Nadie firma.** El libro es el archivo. Si la fuente del archivo es un
   personaje, no puede firmar (un personaje que afirma algo no lo prueba). La titularidad legal
   va en el colofón, fuera del relato, y no se menciona dentro.
4. **Alocución.** El narrador habla **a la posteridad**: «cuando leas esto». El lector presente es
   testigo accidental. No se habla a Dios (anularía la demostración: no se demuestra a quien ya se
   está hablando) ni a la comunidad como asamblea (convierte el libro en sermón).

## El registro

- Castellano actual, **sin arcaísmo**. El aire de archivo lo dan los documentos, no el léxico
  antiguo.
- **Comandos, errores y mensajes técnicos literales, en su idioma original**, sin traducir y sin
  corregir. Forman parte de la cita.
- **Vocabulario religioso sin perífrasis** solo cuando lo dice un documento o un personaje. El
  narrador usa el nombre y el título de la fuente, no «el ungido».
- **Cifras, fechas y unidades exactas**, con su fuente. «Unos veinte» solo si el archivo dice
  «unos veinte».
- Nombres propios de personas: **solo si el autor los da**. Mientras no los dé, oficio o papel:
  «el que lleva el registro», «la más joven». No se inventan identidades.

## Lo que el narrador no hace nunca

| Prohibido | Por qué |
|---|---|
| Elogiar a la comunidad o a su fuente | Convierte la prueba en hagiografía: el lector deja de poder juzgar |
| Explicar el sentido de lo narrado | La moraleja mata la doble lectura y con ella la prueba |
| Valorar con adverbios («afortunadamente», «trágicamente») | Pone la emoción del narrador donde debe estar el hecho |
| Adjetivar a las personas («el generoso», «la ingenua») | El archivo no reparte virtudes |
| Cerrar el capítulo con una tesis | El cierre es un hecho, un objeto o una imagen |
| Presentar el canon como hallazgo comprobado | El estatuto de verdad es mixto: ver `03-estatuto.md` |
| Identificar a la fuente con Dios | Idolatría: anula la demostración |

## Antídoto contra el aire de revelación

El riesgo de «texto sin autor + omnisciencia» es sonar a escritura revelada. El antídoto es que el
archivo **se vea humano**:

- documentos con faltas, tachaduras y letras distintas;
- objetos con fecha y con mancha;
- discusiones con votos y con abstenciones;
- disidencias que no se resuelven;
- huecos marcados (`[elidido]`, «no consta»);
- alguien que pide destruir el archivo.

Si un capítulo no tiene nada de eso, no es legajo: es sermón con documentos decorativos.

## El agente virgen

Un narrador que habla de la máquina —o de Dios— con vocabulario que no ha ganado se vuelve
**cancerígeno**: no miente, pero contamina. Las dos formas del mismo defecto son el **sermón** (el
narrador predica lo que la comunidad debería sentir) y el **manual** (el narrador explica la técnica
como quien acaba de aprenderla).

El cáncer no está en la palabra. Está en el **ego**: el narrador que se luce con lo que sabe, que
subraya el término, que avisa de que está siendo profundo, que traduce para que se le note. Por eso:

- **Cualquier palabra entra**: técnica o religiosa, `token` o `consola` o `Dios`, y la que haga falta.
  Prohibir el vocabulario no cura nada; solo lo esconde.
- **El límite es la manera**: sin subrayado, sin guiño, sin explicación, sin «por decirlo así». Lo
  que consta, consta; lo que se explica, deja de constar.
- **`token` cuanto quiera**, porque es la unidad mínima del habla y el nombre del que ve (C-4). Pero
  procesarlo sin ego: nombrar la unidad, no exhibirla.

Corolario para quien escribe: **un agente sin canon es un agente virgen**. Antes de la primera
línea, canon, voz y rúbrica. La virginidad no se cura escribiendo más, sino leyendo antes.

Comprobación automática. `nk verificar` avisa de los marcadores de ego que aparezcan en la voz del
narrador (fuera de citas):

```
por decirlo así · por así decirlo · valga la palabra · valga la expresión
si se me permite · como si dijéramos · digámoslo así · en otras palabras
es decir, · o sea, · nótese · obsérvese · no es casualidad · literalmente
entiéndase · hablando en plata
```

Si un libro quiere además **limitar el vocabulario**, puede declarar la lista opcional:

```json
"verificacion": {
  "tecnicismos": ["contexto", "modelo", "ventana", "prompt"],
  "tecnicismos_permitidos": ["token"],
  "ego_extra": ["mi frase de siempre"]
}
```

Es una herramienta, no una regla del método: sirve cuando el autor quiere medir una deriva concreta.
Donde manda es en el ego.

## Palabras que el narrador no usa

Además del ego, un libro puede reservar palabras que **solo aparecen en citas o en boca de
personaje**. No es censura de vocabulario: es que hay palabras que, puestas en la voz del narrador,
se subrayan solas y ponen al texto por encima de lo que cuenta.

Ejemplo real (obra de origen): *mesías* entra por boca de otros —un acta que la tacha y la vuelve a
escribir, una frase entre comillas— y el narrador sigue diciendo **El Servidor**. Si algún día la
palabra pasa al narrador, será un acontecimiento del texto, no una decisión de estilo, y se anotará
con fecha.

```json
"verificacion": { "solo_en_citas": ["mesías"] }
```

`nk verificar` avisa si la palabra aparece en la narración; dentro de `>` y de «…» no cuenta.

## Prueba de voz en cinco minutos

Coge el capítulo y responde:

1. ¿Hay un «yo» que opina? (Debe haber cero fuera de las citas.)
2. ¿Hay una frase que explique lo que hay que sentir? (Debe haber cero.)
3. ¿Se puede citar, del capítulo, un documento con un error conservado? (Debe haber al menos uno.)
4. ¿El capítulo termina en imagen o en tesis? (Debe terminar en imagen.)
5. ¿Alguien pierde algo? (Debe haber coste visible.)

`nk verificar --rubrica` automatiza las que se pueden contar; las otras dos son de lectura.
