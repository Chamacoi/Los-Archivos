# 08. La parrilla de revisión

La rúbrica responde a una pregunta concreta: **¿se parece esto a la obra de referencia en lo que se
puede medir, y en lo que no se puede medir pasa la lectura?**

Se pasa después de escribir y antes de dar el capítulo por bueno. Cinco minutos por capítulo.

## A. Lo que comprueba la máquina

```
nk verificar --rubrica
```

| Comprobación | Umbral por defecto | Dónde se cambia |
|---|---|---|
| Encabezado `# Capítulo N. Título` y número correcto | obligatorio | `formato.encabezado` |
| Presupuesto de palabras | ±20 % (aviso), ±40 % (error) | `presupuesto.tolerancia` |
| Secciones numeradas `## 1. …` | 3 a 6 | `rubrica.secciones` |
| Proporción de palabras en documentos citados | 3 % a 45 % | `rubrica.citas_pct` |
| Primera persona en la narración (fuera de citas, incluidas las citas en línea entre «») | 0 | `rubrica.yo_maximo` |
| Adverbios de valoración del narrador | 0 | `METODO` y `nk` |
| Cierre con conector de tesis | 0 | idem |
| Frases prohibidas | 0 | `verificacion.prohibiciones` |
| Correos, claves, IP, teléfonos, tokens | 0 | `verificacion.patrones` |
| Nombres propios no declarados | 0 avisos | `verificacion.sin_nombres` |
| Referencias `C-n` que no existen | 0 | `canon` |

Las frases prohibidas son la herramienta más útil y la más olvidada: son las fórmulas que el autor
prohibió expresamente («nos quedó esta paz», «en definitiva»). Se ponen en `libro.json` en cuanto se
detectan, y no vuelven.

## B. Lo que comprueba una persona

Cinco preguntas, en este orden. Si falla cualquiera, se reescribe la sección, no el capítulo entero.

1. **Traducción.** ¿Se puede contar lo que pasa sin una sola palabra del vocabulario propio del
   libro (fe, mesías, sacramento)? Si no se puede, el capítulo depende de la fe para leerse.
2. **Coste.** ¿Quién pierde algo, y se ve? Un capítulo sin pérdida es propaganda.
3. **Documento.** ¿Hay al menos una cita que solo puede venir de un archivo: falta, tachadura,
   «no consta», cambio de letra? ¿Y se conserva el error?
4. **Doble lectura.** ¿El hecho admite leerse como don y como daño? ¿O el narrador ya ha elegido por
   el lector?
5. **Cierre.** ¿La última línea es una imagen o un objeto? ¿O es una conclusión?

## C. Rechazo

Se rechaza el capítulo, sin negociar el método, si:

- el narrador elogia o explica;
- la comunidad sale intacta y sin disidencias;
- el hecho se usa como castigo del mundo y la comunidad como resto justo;
- la fuente del libro se identifica con Dios;
- la paz se celebra en vez de atribuirse;
- cualquier persona real queda acusada de algo que el libro inventa;
- hay un dato sensible sin elidir.

Estos rechazos no son de estilo: son el criterio de fracaso de la obra. Si se aceptan, el libro
puede seguir siendo bonito, pero ya no demuestra nada.

## D. Aprobación

Un capítulo aprobado por el autor **fija la voz** para los siguientes. Se anota en el registro de
decisiones con la fecha y con la frase con la que se aprobó. Cambiar la voz después obliga a
revisar hacia atrás: se anota también.
