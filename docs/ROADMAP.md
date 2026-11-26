# RGO — Agenda de investigación · v0.6.1

[Inicio](../README.md) · [Investigación musical](MUSICA.md) · [Archivo de líneas anteriores](ARCHIVO.md)

## Prioridad 1: invariantes frente a alineación musical

**Pregunta:** ¿cuándo una representación relacional temporal ofrece una ventaja medible sobre la alineación de secuencias, ya sea en precisión, robustez o coste?

El resultado XIX de 79,92% para recuperar otra transcripción del mismo ID no se debe comparar directamente con el 48,04% de alineación para recuperar melodías de otro ID en el subconjunto de 51 representantes: son tareas diferentes. La comparación directa de este último control es 33,33% de trigramas frente a 48,04% de alineación. El próximo experimento debe usar los mismos candidatos, consultas y etiquetas para todos los métodos.

- Separar identificación de otra versión de la misma obra y parentesco entre obras distintas.
- Comparar trigramas invariantes, relaciones multilag, alineación cromática y un método híbrido con igual entrada y protocolos de evaluación comunes. Registrar también tiempo, memoria y tamaño de firma.
- Aplicar niveles controlados de transposición global, cambios de duración, ornamentación, inserción/borrado de notas, fragmentación y ruido; separar controles simbólicos de grabaciones reales.
- Reservar obras o familias para prueba, escoger parámetros únicamente en desarrollo, contabilizar empates y comparar por obra, no tratar versiones de una misma obra como muestras independientes.
- Obtener un corpus de audio con versiones verificadas y permiso de uso; medir la extracción de cromas, timbre y tempo. Si no se consigue, declarar el límite y no sustituir grabaciones por partituras.

El criterio de éxito debe fijarse antes de evaluar y no presupone que los invariantes ganen. Si no hay ventaja, se conserva la conclusión y se estudia cuándo una firma compacta permite un filtro previo útil sin perjudicar la recuperación.

## Prioridad 2: fundamento matemático

Extender el criterio temporal a relaciones incompletas o ruidosas, órbitas locales desconocidas y costes desiguales. Estudiar ambigüedad residual, mínimos de consultas, corrección de errores, selección adaptativa y verificación de modelos. No confundir un acierto dentro de un catálogo con la identificación exacta de una estructura.

Contrastar con literatura de fase y homometría (Jaming, Kolountzakis, Keleti, Mandereau, Amiot, Yust), recuperación de órbitas, códigos y sincronización. La originalidad de los resultados concretos no está establecida.

## Líneas secundarias

El estudio matemático de intermediación XVII se conserva como problema combinatorio independiente. Revisar los antecedentes de betweenness, seriación y ordenación por mediana de tres antes de darle peso como contribución original. Los experimentos semánticos XII–XVII quedan en pausa: las pruebas no han establecido descubrimiento fiable. La topología musical queda como referencia comparativa y fuente de contraejemplos, no como hipótesis principal. Q48, Cubo64 y cuántica se conservan como casos particulares. No se elimina ningún registro previo; véase el [archivo científico](ARCHIVO.md).
