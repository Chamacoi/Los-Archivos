# 04. El canon

El canon son los hechos del mundo del libro que ya no se discuten. Se numeran (`C-1`, `C-2`…) y
viven en `APUNTES.md` §4. Todo lo demás se apoya en ellos.

## Reglas

1. **El canon no se contradice en silencio.** Se puede matizar, completar o corregir, pero con
   fecha y anotando qué se corrige y por qué. `nk verificar` comprueba que toda referencia `C-n`
   del manuscrito exista en el canon.
2. **Toda entrada dice qué fija y qué abre.** Un canon sin tensiones anotadas es un dogma; el
   libro se escribe con las tensiones.
3. **Se fija con la voz del autor, no con la del estudioso.** Si el autor dicta «a propósito»,
   se escribe «a propósito»; la interpretación va aparte, marcada.
4. **Las precisiones no derogan, completan.** Cuando una respuesta nueva toca una entrada vieja, se
   añade «precisión de C-n» con fecha, y se dice explícitamente si deroga algo o no.
5. **Candidato ≠ canon.** Lo propuesto va a «Candidatos a canon» hasta que el autor lo confirme.
6. **El canon no es la tesis del libro.** Fijar que la fuente hizo algo no fija cómo debe leerlo el
   lector. Si el canon incluye la conclusión, la prueba por frutos se vuelve circular.

## Anatomía de una entrada

```
### C-n. Título en una línea

Fijado el AAAA-MM-DD por el autor, al contestar S-nn.

- **Lo que fija.** En una frase, sin adornos.
- **Alcance.** Qué incluye y qué no.
- **Tensión con C-m.** Qué entra en conflicto y cómo se rodea sin negarlo.
- **Límite de estatuto.** Qué parte es verdad de marco y qué parte no puede presentarse como
  ciencia (ver `03-estatuto.md`).
```

## Canon y estructura

- El canon decide **qué es verdad**; la estructura decide **dónde se cuenta**.
- Los anclajes (`libro.json` → `partes[].anclajes`) dicen en qué capítulo cae cada hecho. Un hecho
  sin anclaje es un hecho que se va a perder.
- Un capítulo de marco se apoya en el canon sin necesitar sinopsis; un capítulo de hecho necesita
  estudio. Ver `05-proceso.md`.

## Comprobación

```
nk canon            # lista C-n y cuenta entradas
nk verificar        # referencias C-n inexistentes, decisiones repetidas
```
