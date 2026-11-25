# Agenda de investigación · RGO v0.3

La prioridad es identificar estructuras bajo observaciones parciales, simetrías, priors y errores. Cada nueva hipótesis debe especificar el objeto, objetivo, espacio de candidatos, transformaciones irrelevantes, protocolo de medición, coste, referencia y criterio de rechazo.

## Prioridad 1 — Fragilidad del conocimiento previo

Hasta ahora los protocolos principales conocen el espectro inicial y admiten el objeto verdadero dentro de su espacio de candidatos. Probar qué sucede cuando alguna de esas hipótesis es incorrecta.

- Definir compatibilidad exacta y aproximada con la imagen del modelo observado.
- Distinguir una fibra vacía, una fibra ambigua y una solución única dentro de un modelo equivocado.
- Introducir candidatos no binarios, errores de magnitudes y soporte espectral incorrecto; medir rechazo correcto de modelos inválidos y falsas certezas.
- Contrastar identificación posterior con certificados de distancia al modelo. Una distancia pequeña a algún candidato no es prueba de identidad.
- Diseñar observaciones de validación no utilizadas en la reconstrucción; evaluar con casos independientes.
- Comparar rechazo, cobertura, precisión y coste de consultas con referencias fijas sencillas y sin prior restrictivo.

No se declara aún ninguna garantía frente a priors erróneos. La futura v0.4 dependerá de los resultados.

## Prioridad 2 — Selección robusta y observabilidad condicionada

Generalizar el problema de cobertura de pares a otros tamaños, otros diccionarios y costes por consulta. Buscar testigos de minimalidad, casos donde la repetición sea ineficiente, protocolos con borrados y errores simultáneos y contraejemplos a la selección voraz. Comparar adaptación con una referencia fija diversa y evaluar incertidumbre estadística, no solo aciertos medios.

En grafos semánticos: definir el objetivo mediante etiquetas externas; verificar que las perturbaciones conservan el significado. Comparar PPR convencional, centralidad y otros métodos pertinentes con el mismo presupuesto. Medir información sobre el objetivo, estabilidad ante perturbaciones irrelevantes y capacidad de detectar cambios reales. Separar selección y evaluación. Si no hay ventaja robusta, reformular o descartar el método. No hay validación sobre grafos semánticos en v0.3.

## Prioridad 3 — Teoremas y revisión de antecedentes

Estudiar el cociente de retículos y las cotas de orden con ceros espectrales, priors discretos y mediciones parciales. Contrastar con Jaming–Kolountzakis, Keleti–Kolountzakis, Bandeira et al., Agulnick–Busick-Warner y Casper–Orozco. Determinar si los mínimos 8h y los recuentos de Z₁₂ se conocen. Publicar como reproducción cuando corresponda; no inferir novedad por falta de coincidencias de terminología.

## Prioridad 4 — Tiempo y aplicaciones independientes

Extender el criterio temporal a medidas de correlación incompletas y ruidosas, órbitas locales desconocidas y costes no uniformes. Buscar contraejemplos a optimalidad de la selección voraz de aristas. En música, comparar reconocimiento de versiones con métodos establecidos, manteniendo separadas la identificación condicionada y la reconstrucción desde audio.

## Secundario

Q48, Cubo64, funciones bent y predicciones cuánticas son ejemplos que permiten comprobar la teoría, no objetivos de unificación por sí solos. No ampliar la interpretación física ni simbólica sin una predicción verificable. Una prueba de hardware solo tendría sentido con protocolo, presupuesto y comparación claros.

[Correcciones](CORRECCIONES.md) · [Informe v0.3](INVESTIGACION.md).
