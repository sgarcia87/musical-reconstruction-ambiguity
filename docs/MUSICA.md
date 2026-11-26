# RGO — Investigación musical

**v0.6 · Fases XVIII–XIX y relación con I–XI**

[Empezar desde cero](EMPEZAR.md) · [Fundamento matemático](INVESTIGACION.md) · [Marco común](MARCO_GENERAL.md)

## Pregunta original

¿Qué información de una obra musical se conserva bajo transposición, cambio de registro o alteraciones de su interpretación? ¿Qué observaciones permiten distinguir las obras sin borrar diferencias significativas? RGO estudia la identificación en un catálogo y la reconstrucción de una estructura como dos tareas diferentes. Una huella identificadora en un catálogo finito no tiene por qué ser una descripción completa.

## XVIII: relaciones de fase y órbitas conjuntas

En 382 corales de Bach, con 462 consultas sintéticas de las 77 piezas de prueba, las relaciones temporales superan a las bolsas de magnitudes locales. En fragmentos de un cuarto con alteraciones/eliminaciones, fase multilag y órbitas multilag alcanzan 75,32%, frente a 91,56% de alineación cromática. No se demuestra superioridad de fase ni reconocimiento desde audio.

**Resultado exacto condicionado:** con las órbitas de cada ventana conocidas, la órbita conjunta de dos ventanas determina el desplazamiento relativo módulo mcd(pᵢ,pⱼ); las correlaciones cruzadas de Fourier solo módulo del mcm de los órdenes de caracteres compartidos no nulos. El segundo divisor puede ser estrictamente menor. El criterio por conectividad de las potencias primas se extiende a las órbitas conjuntas. En 32 de 18.094 transiciones de acordes colapsados, la órbita conjunta conserva más información. En ventanas de cuatro negras, 377/382 reconstrucciones son únicas mediante correlaciones consecutivas y 378/382 mediante órbitas conjuntas consecutivas; seis o cinco conexiones adicionales respectivamente resuelven los restantes. Es reconstrucción simbólica condicionada, no identificación de versiones.

[Nota XVIII](rgo_fase18_nota.md) · [Auditoría](../audits/rgo_fase18_audit.mjs) · [JSON](../results/rgo_fase18_resultados.json).

## XIX: comparación topológica y variantes independientes

El corpus de Polifonia/The Session incluye 297 transcripciones utilizables, 51 IDs y diez familias. Las relaciones temporales de tres eventos reconocen otras transcripciones del mismo ID con top-1 de 79,92% (288 consultas, azar 3,33%). La topología con coordenada temporal llega al 12,73%. Al buscar otros IDs de la misma familia: 36,03% para trigramas (297 consultas, azar 7,53%). Con un representante por ID, trigramas 33,33%, alineación cromática 48,04%, azar 9,65%. No es evidencia de superioridad sobre alineación.

La homología persistente de ventanas sin coordenada temporal es invariante por reordenación de esas ventanas; el orden puede quedar oculto. Añadir tiempo relativo distingue los 77 controles de permutación estudiados, pero no garantiza identificar toda secuencia ni su orientación absoluta.

[Nota XIX](rgo_fase19_nota.md) · [Auditoría](../audits/rgo_fase19_audit.mjs) · [JSON](../results/rgo_fase19_resultados.json).

## Qué falta

- Audio real: cambio de instrumento, tempo, interpretación y extracción imperfecta de cromas.
- Comparar protocolos de identificación musical con baselines fuertes y presupuestos equivalentes, sin restringir los competidores artificialmente.
- Investigar qué relaciones temporales mínimas conservan una identidad definida y bajo qué errores, y distinguir reconocimiento de reconstrucción.
- Contrastar los resultados matemáticos particulares con la literatura antes de reivindicar prioridad.

Las investigaciones iniciales sobre Fourier, Q48 y el teorema temporal están en [INVESTIGACION.md](INVESTIGACION.md) y [OBSERVABILIDAD_TEMPORAL.md](OBSERVABILIDAD_TEMPORAL.md). La extensión a órdenes y semántica está documentada aparte; no se requiere para entender este trabajo.
