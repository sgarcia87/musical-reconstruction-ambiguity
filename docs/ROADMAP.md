# Agenda de investigación · RGO v0.4

La prioridad es identificar estructuras bajo observaciones parciales, simetrías, priors y errores. Cada nueva hipótesis debe especificar el objeto, objetivo, espacio de candidatos, transformaciones irrelevantes, protocolo de medición, coste, referencia y criterio de rechazo.

## Estado después de las fases XII–XVI

Véase [Observabilidad semántica](SEMANTICA.md). XII mide coherencia interna con referencia y evidencia de origen común. XIII no supera de manera consistente a PPR mínimo. XIV encuentra orden con extremos conocidos, XV muestra el límite de la seriación sin extremos y XVI no reproduce una ventaja robusta en un segundo banco de escalas. Por tanto no se recomienda ampliar la hipótesis geométrica como explicación universal.

**Próximo experimento (pendiente):** usar observaciones ordinales de fuente distinta, por ejemplo patrones comparativos o de gradación en un corpus, sin utilizar los juicios de evaluación como entrada. Definir el espacio de candidatos y la referencia antes de medir; separar desarrollo y prueba por escala y por vocabulario, registrar cobertura y coste, comparar con frecuencia, similitud, PPR y métodos de intensidad establecidos; evaluar resultados por escala y con incertidumbre apropiada. No llamar validación a la concordancia entre dos vistas de la misma fuente. Mantener las prioridades matemáticas y temporales de la versión anterior.

## Prioridad 1 — Fragilidad del conocimiento previo

Hasta ahora los protocolos principales conocen el espectro inicial y admiten el objeto verdadero dentro de su espacio de candidatos. Probar qué sucede cuando alguna de esas hipótesis es incorrecta.

- Definir compatibilidad exacta y aproximada con la imagen del modelo observado.
- Distinguir una fibra vacía, una fibra ambigua y una solución única dentro de un modelo equivocado.
- Introducir candidatos no binarios, errores de magnitudes y soporte espectral incorrecto; medir rechazo correcto de modelos inválidos y falsas certezas.
- Contrastar identificación posterior con certificados de distancia al modelo. Una distancia pequeña a algún candidato no es prueba de identidad.
- Diseñar observaciones de validación no utilizadas en la reconstrucción; evaluar con casos independientes.
- Comparar rechazo, cobertura, precisión y coste de consultas con referencias fijas sencillas y sin prior restrictivo.

No se declara ninguna garantía general frente a priors erróneos. XII muestra un caso interno circular; falta validación con observaciones independientes.

## Prioridad 2 — Selección robusta y observabilidad condicionada

Generalizar el problema de cobertura de pares a otros tamaños, otros diccionarios y costes por consulta. Buscar testigos de minimalidad, casos donde la repetición sea ineficiente, protocolos con borrados y errores simultáneos y contraejemplos a la selección voraz. Comparar adaptación con una referencia fija diversa y evaluar incertidumbre estadística, no solo aciertos medios.

En grafos semánticos: definir el objetivo mediante etiquetas externas; verificar que las perturbaciones conservan el significado. Comparar PPR convencional, centralidad y otros métodos pertinentes con el mismo presupuesto. Medir información sobre el objetivo, estabilidad ante perturbaciones irrelevantes y capacidad de detectar cambios reales. Separar selección y evaluación. Si no hay ventaja robusta, reformular o descartar el método. Las fases XIII–XVI aportan pruebas externas exploratorias, no una validación general de la difracción o de la seriación geométrica.

## Prioridad 3 — Teoremas y revisión de antecedentes

Estudiar el cociente de retículos y las cotas de orden con ceros espectrales, priors discretos y mediciones parciales. Contrastar con Jaming–Kolountzakis, Keleti–Kolountzakis, Bandeira et al., Agulnick–Busick-Warner y Casper–Orozco. Determinar si los mínimos 8h y los recuentos de Z₁₂ se conocen. Publicar como reproducción cuando corresponda; no inferir novedad por falta de coincidencias de terminología.

## Prioridad 4 — Tiempo y aplicaciones independientes

Extender el criterio temporal a medidas de correlación incompletas y ruidosas, órbitas locales desconocidas y costes no uniformes. Buscar contraejemplos a optimalidad de la selección voraz de aristas. En música, comparar reconocimiento de versiones con métodos establecidos, manteniendo separadas la identificación condicionada y la reconstrucción desde audio.

## Secundario

Q48, Cubo64, funciones bent y predicciones cuánticas son ejemplos que permiten comprobar la teoría, no objetivos de unificación por sí solos. No ampliar la interpretación física ni simbólica sin una predicción verificable. Una prueba de hardware solo tendría sentido con protocolo, presupuesto y comparación claros.

[Correcciones](CORRECCIONES.md) · [Informe v0.3](INVESTIGACION.md).
