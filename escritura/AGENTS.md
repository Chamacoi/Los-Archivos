# AGENTS.md — protocolo de escritura

Instrucciones para cualquier agente (o persona) que trabaje en este repositorio. El repositorio es
una obra literaria que se escribe **como archivo**: no es un proyecto de software, aunque tenga
scripts.

## Perfil del agente que puede continuar

El repositorio no se escribe con un modelo concreto. Se escribe con un agente que pueda hacer lo
que sigue; **la marca, el proveedor y la versión no se fijan a propósito**, porque caducan y este
texto no.

**Capacidades mínimas.**

- Leer y escribir ficheros de texto del árbol de trabajo y **editar por bloques exactos**, sin
  reescribir lo que no se toca.
- Ejecutar comandos de consola (`git`, `tar` y los scripts de `bin/nk`) sobre los ficheros de la
  obra, sin privilegios de administrador.
- **Contexto amplio:** tener a la vez el capítulo en curso (≈3.000 palabras), `APUNTES.md` §0, §3 y
  §4, el dossier del capítulo y `libro.json` — del orden de **15.000-20.000 tokens**.
- Castellano de España para el texto y para hablar con el autor.

**Lo que no hace falta.** Conexión permanente, GPU, visión, claves de API ni ninguna herramienta
propietaria: todo lo que manda está en ficheros de texto y el control de versiones es `git`.

**Credenciales.** Nunca en un fichero versionado. Si alguna vez hicieran falta (hoy no hacen falta
para nada de lo que pide este protocolo), van por **variable de entorno** o por un fichero local
**ignorado por git** (`.env` está en `.gitignore`). `bin/nk verificar` busca los patrones habituales
—correos, claves tipo `sk-…`/`ghp_…`, IPv4, teléfonos, base64 largo, URLs con credenciales— y avisa.
Un dato personal que no se pueda omitir se **elide y se marca**: `[elidido]`, `[corte]`.

**Variante legible por máquina.** El manifiesto `libro.json` lleva un bloque `"agente"` con estas
capacidades, para que un agente que clone la obra sepa qué se le pide sin interpretar prosa:

```json
"agente": {
  "modelo": null,
  "proveedor": null,
  "capacidades": ["leer_ficheros", "escribir_ficheros", "editar_por_bloques",
                  "ejecutar_comandos", "contexto_amplio", "castellano_es_ES"],
  "contexto_minimo_tokens": 15000,
  "requiere": {"red": false, "gpu": false, "vision": false, "claves_api": false},
  "credenciales": {"en_repositorio": false,
                    "via": ["variable_de_entorno", "fichero_local_ignorado"],
                    "detector": "bin/nk verificar"}
}
```

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
