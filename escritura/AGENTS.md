# AGENTS.md — protocolo de escritura

Instrucciones para cualquier agente (o persona) que trabaje en este repositorio. El repositorio es
una obra literaria que se escribe **como archivo**: no es un proyecto de software, aunque tenga
scripts.

## Al reanudar

1. Lee `APUNTES.md` empezando por **§0 Punto de reanudación**; después §2 (puntos abiertos), §3
   (registro de decisiones) y §4 (canon).
2. Lee `ESTRUCTURA.md`, `README.md` y la última entrada de `BITACORA.md`.
3. Ejecuta `bin/nk estado` y `bin/nk contar`.
4. Resume al usuario en diez líneas: dónde estamos, qué está cerrado, qué toca.

No escribas en `MANUSCRITO/` hasta que el usuario lo autorice expresamente.

## Fuentes de verdad, por orden

| Rango | Fichero | Manda sobre |
|---|---|---|
| 1 | `APUNTES.md` §4 (canon) | qué es verdad en el mundo del libro |
| 2 | `APUNTES.md` §3 (decisiones) | qué está decidido y desde cuándo |
| 3 | `libro.json` | números: partes, capítulos, presupuesto, tolerancia |
| 4 | `SINOPSIS/` | las palabras del autor, literales |
| 5 | `ESTUDIOS/` | qué se puede narrar y qué no |
| 6 | `ESTRUCTURA.md` | dónde cae cada cosa |
| 7 | `MANUSCRITO/` | el texto, que se deriva de lo anterior |

Si dos fuentes discrepan, para y dilo. No elijas tú.

## Reglas duras

1. **Si no está en el registro de decisiones, no está decidido.** No inventes canon, ni cifras, ni
   nombres, ni hechos.
2. **No contradigas el canon en silencio.** Matizar, completar o corregir se hace con una precisión
   fechada y anotada en el registro.
3. **No inventes personas.** Mientras el autor no dé nombres, se escribe con oficios y papeles.
4. **No inventes datos sensibles ni los reproduzcas.** Credenciales, correos, IP, teléfonos,
   identificadores: se eliden y se marcan (`[elidido]`, `[corte]`). `nk verificar` los busca.
5. **No atribuyas a personas ni instituciones reales hechos que el libro inventa.** Ni como acusación
   ni como broma.
6. **No presentes como ciencia lo que es verdad de marco del libro.** Y cita la fuente real aunque
   concluya lo contrario.
7. **Un capítulo se escribe desde un estudio**, no desde una sinopsis. Los capítulos de marco se
   escriben desde canon y estructura.
8. **La desviación de palabras se anota, no se compensa.**
9. **Nada entra en el repositorio que no pueda publicarse.** Material de terceros y borradores
   sucios van a una carpeta ignorada.
10. **No se escribe el capítulo siguiente sin que el anterior esté aprobado.** Un capítulo aprobado
    fija la voz; cinco sin revisar fijan un error cinco veces.

## Antes de dar un capítulo por escrito

```
bin/nk contar
bin/nk verificar --rubrica
```

Y las cinco preguntas de lectura de `METODO/08-rubrica.md` §B: traducción, coste, documento, doble
lectura, cierre. Si falla una, se reescribe la sección.

## Después de escribir

1. `bin/nk informe` (deja `estado.json`).
2. `bin/nk contar --actualizar` si hay capítulos nuevos.
3. Actualiza §0 de `APUNTES.md`.
4. Añade decisiones nuevas con fecha, sin reciclar números.
5. Entrada de tres líneas en `BITACORA.md`.
6. Commit por capítulo (recuento real, presupuesto y desviación en el mensaje) y otro al cerrar.
   Mensajes en inglés, sobrios, sin datos personales.

## Tono al hablar con el usuario

En castellano de España, breve, sin halagar. Cuando una petición choque con el canon o con el
método, dilo antes de obedecerla y explica el coste. Cuando falte un dato, pide el dato; no lo
supongas.

## Qué no hace un agente en este repositorio

- No reescribe el canon para que encaje con lo que acaba de escribir.
- No «mejora» citas: las reproduce con sus errores.
- No añade capítulos fuera de `libro.json`.
- No cierra puntos abiertos de `APUNTES.md` §2 sin decisión explícita del usuario.
- No publica ni sincroniza el repositorio.
