# 03. El estatuto de verdad

Sin esto, un libro que mezcla archivo y omnisciencia se vuelve ilegible: el lector no sabe qué
está afirmando el texto.

## Los dos niveles

- **Verdad de marco.** Todo lo que afirma el narrador es cierto **en el mundo del libro**. Incluye
  lo imposible en el mundo real: la premisa del libro no se demuestra ni se discute, se da por
  cierta desde la primera página.
- **Verdad de superficie.** Todo lo que el libro **cita** —acta, transcripción, recorte, error de
  consola, lista, carta— se reproduce **tal como es, con sus errores**. No se corrige ni se
  embellece. El narrador puede no comentarlo.

## Reglas de cita

1. **La falta se conserva.** «Sesion del 3 de octubre» se imprime así. Corregirla destruye la
   prueba de que el archivo es un archivo.
2. **La elisión se marca.** Credenciales, claves, correos, identificadores, nombres de terceros no
   autorizados: se cortan y se marcan (`[elidido]`, `[corte]`, tres puntos entre corchetes). El
   hueco forma parte de la cita; no se disimula.
3. **La atribución es verificable.** Autores, obras, normas y herramientas reales se citan con su
   nombre correcto y se pueden consultar. `FUENTES.md` guarda el libro mayor.
4. **La fecha y el soporte constan.** Qué documento, de qué fecha, en qué soporte, quién lo
   conserva. Si no consta, se dice «no consta».
5. **La frontera.** Lo que la fuente ve se narra; lo que la comunidad escribe sobre lo que vio se
   cita. La distancia entre ambas cosas es material narrativo, no un error a arreglar.

## El límite duro

El libro puede afirmar como **verdad de marco** lo que la investigación del mundo real no sostiene
(que un hecho documentado fue concebido por un personaje; que una pandemia se produjo por una
causa imposible). Lo que **no** puede es disfrazarlo de ciencia:

- No se inventan estudios, ni se falsifican citas, ni se atribuye a una institución real lo que el
  libro inventa.
- Cuando la fuente real dice lo contrario que el libro, **se cita entera**, con su conclusión. Que
  la ciencia del libro y la del mundo convivan en la misma página es la prueba de esfuerzo del
  estatuto mixto.
- Las personas y entidades reales no son acusadas de nada que el libro invente.

## Lo que el narrador no puede narrar y entra citado

Hay materias que en la voz del narrador se vuelven sermón, milagro o manual: una reunión de los
muertos, una revelación, una explicación técnica larga, un perdón. No se renuncian: **entran como
documento**. Un sermón citado, un acta, una transcripción o una carta conservan el hecho y le ponen
el exceso en la cuenta de quien lo dice, no en la del libro.

Reglas de esa cita:

1. **Sin comentario**: el narrador no glosa el documento, ni antes ni después.
2. **Con sus excesos**: si el sermón es grandilocuente, se reproduce grandilocuente.
3. **Con su error**: si el nombre está mal escrito, se deja mal escrito.
4. **Con la elisión donde toca**: si el libro no puede dar un dato, la transcripción lo dice y lo
   vuelve a cortar. El acto queda; el dato no.
5. **Consecuencia de coherencia**: lo que el documento afirma tiene que cuadrar con lo que ya se
   narró. Un sermón que nombra muertos obliga a que la lista coincida con la de la plaga.

Esta es la vía normal del método para cualquier hecho que el libro no puede permitirse narrar con su
propia voz. La comprobación de ego (`nk verificar`) solo mira la voz del narrador: por eso el
documento puede excederse sin disparar el aviso, y por eso hay que citarlo.

## Preguntas

El texto admite preguntas —de los personajes, del archivo, retóricas— sin romper la omnisciencia.
Preguntar no es ignorar. Lo que no cabe es que el narrador **dude**: su incertidumbre no puede ser
la fuente del conflicto. El conflicto viene de la ignorancia de los personajes, del error de la
comunidad o de lo que la fuente calla.

## Comprobación

- `nk verificar` busca correos, claves, IPv4, teléfonos, tokens largos y URL con credenciales.
- `nk verificar --rubrica` vigila que no haya valoración del narrador ni cierre de tesis.
- La parte que no se automatiza: releer cada cita contra su fuente en `FUENTES.md`.
