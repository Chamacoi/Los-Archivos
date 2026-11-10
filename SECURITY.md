# Política de seguridad

## Versiones con soporte

Se aceptan informes para la versión más reciente disponible en la rama
`main`. Si publicas versiones o etiquetas, indica aquí cuáles reciben
actualizaciones de seguridad y durante cuánto tiempo.

## Qué se considera un problema de seguridad

Algunos ejemplos relevantes para este repositorio:

- ejecución de comandos o código no prevista en `escritura/bin/nk` o
  `escritura/install.sh`;
- escritura, sobrescritura o lectura de archivos fuera del directorio
  esperado;
- extracción de paquetes o bundles que permita alterar archivos inesperados;
- exposición de credenciales, datos privados o materiales ignorados por Git;
- vulnerabilidades en los workflows de GitHub Actions o en la cadena de
  distribución de los paquetes.

Los errores de estilo, los problemas editoriales y las solicitudes de
funcionalidad no son vulnerabilidades de seguridad.

## Cómo informar de una vulnerabilidad

**No abras un issue público ni publiques detalles explotables antes de que
la persona responsable pueda investigar el problema.**

Envía el informe mediante **Informar de una vulnerabilidad** en la pestaña
**Security** del repositorio, si esa opción está habilitada. Si no está
disponible, contacta con la persona mantenedora por [canal privado de
contacto].

Incluye, si puedes:

- los archivos, comandos o revisiones afectados;
- los pasos para reproducir el problema en un entorno propio;
- el impacto que observaste y sus posibles consecuencias;
- una solución temporal, si conoces alguna.

No incluyas contraseñas, tokens, datos personales ni contenido privado de
`MATERIALES/` o `SINOPSIS/` en un issue público.

## Qué puedes esperar

Confirmaremos la recepción del informe en un plazo de [X días] y te
mantendremos al tanto de la investigación. El plazo para corregir y publicar
una solución dependerá de la gravedad y de la complejidad del problema.
Coordinaremos contigo antes de divulgar detalles públicamente.

## Alcance y límites

Este repositorio no incluye una aplicación web, un servidor ni una base de
datos. Los informes deben referirse a los archivos, scripts, paquetes o
workflows mantenidos aquí.

Realiza las pruebas únicamente en copias y sistemas que tengas autorización
para usar. No accedas a datos ajenos, no interrumpas servicios ni publiques
información sensible.
