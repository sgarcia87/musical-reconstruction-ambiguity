# Agenda de investigación · RGO v0.5.1

La prioridad es identificar estructuras bajo observaciones parciales, simetrías, priors y errores. Cada nueva hipótesis debe especificar el objeto, objetivo, espacio de candidatos, transformaciones irrelevantes, protocolo de medición, coste, referencia y criterio de rechazo.

## Estado de la investigación tras XVII

[Marco general](MARCO_GENERAL.md) · [Fase XVII](rgo_fase17_nota.md) · [Contraste semántico](SEMANTICA.md).

El fundamento matemático I–XI se conserva. XII muestra el riesgo de la coherencia circular; XIII–XVI delimitan el uso de asociaciones para inferir pertenencia y orden. XVII proporciona un observador ordinal exacto, una proposición de distancia mínima y censos de mínimos fijos hasta seis elementos y adaptativos hasta ocho. Los primeros dos pilotos no dieron cobertura útil; JJGraph aporta cobertura parcial, pero el filtro ordinal simple produce contradicciones y errores. No se ha resuelto el descubrimiento fiable de la dimensión ni su orden semántico. [Ampliación XVII](rgo_fase17_extension.md).

### Siguiente paso empírico: evidencia ordinal suficiente

Obtener observaciones comparativas contextualizadas y mediciones por atributo (por ejemplo, DoQ). JJGraph ya se ha evaluado mediante una regla simple; falta comparar contra el método entrenado de Cocos et al. y la inferencia de de Melo/Bansal, sin convertir juicios de evaluación en observaciones. Separar sentidos, atributos y escalas antes de fijar reglas de extracción; permitir empates, conflictos y abstenciones. Separar desarrollo y prueba por escala y vocabulario; medir cobertura, precisión condicionada, falsos certificados, coste y comparación con baselines de intensidad, similitud y frecuencia. No simular etiquetas como sustituto de observaciones externas.

### Siguiente paso matemático

Extender los mínimos fijos de XVII a tamaños mayores, contrastar el límite adaptativo más allá de n=8 y estudiar certificados parciales, empates, órdenes parciales, consultas binarias vs ternarias, costes y oráculos ruidosos. Contrastar prioridad bibliográfica antes de reivindicar novedad. Comparar selección de máxima entropía con minimax, auditorías directas de restricciones y protocolos resistentes a errores. No transferir la garantía n−2 a un modelo distinto sin demostrarla.

## Prioridad 1 — Fragilidad del conocimiento previo

Hasta ahora los protocolos principales conocen el espectro inicial y admiten el objeto verdadero dentro de su espacio de candidatos. Probar qué sucede cuando alguna de esas hipótesis es incorrecta.

- Definir compatibilidad exacta y aproximada con la imagen del modelo observado.
- Distinguir una fibra vacía, una fibra ambigua y una solución única dentro de un modelo equivocado.
- Introducir candidatos no binarios, errores de magnitudes y soporte espectral incorrecto; medir rechazo correcto de modelos inválidos y falsas certezas.
- Contrastar identificación posterior con certificados de distancia al modelo. Una distancia pequeña a algún candidato no es prueba de identidad.
- Diseñar observaciones de validación no utilizadas en la reconstrucción; evaluar con casos independientes.
- Comparar rechazo, cobertura, precisión y coste de consultas con referencias fijas sencillas y sin prior restrictivo.

No se declara ninguna garantía general frente a priors erróneos. XII muestra un caso interno circular; XVII verifica rechazo bajo un universo correcto y un oráculo exacto. Falta validación con observaciones independientes suficientemente cubiertas.

## Prioridad 2 — Selección robusta y observabilidad condicionada

Generalizar el problema de cobertura de pares a otros tamaños, otros diccionarios y costes por consulta. Buscar testigos de minimalidad, casos donde la repetición sea ineficiente, protocolos con borrados y errores simultáneos y contraejemplos a la selección voraz. Comparar adaptación con una referencia fija diversa y evaluar incertidumbre estadística, no solo aciertos medios.

En grafos semánticos: definir el objetivo mediante etiquetas externas; verificar que las perturbaciones conservan el significado. Comparar PPR convencional, centralidad y otros métodos pertinentes con el mismo presupuesto. Medir información sobre el objetivo, estabilidad ante perturbaciones irrelevantes y capacidad de detectar cambios reales. Separar selección y evaluación. Si no hay ventaja robusta, reformular o descartar el método. Las fases XIII–XVII aportan pruebas externas exploratorias, no una validación general de la difracción, de la seriación geométrica ni de un oráculo lingüístico.

## Prioridad 3 — Teoremas y revisión de antecedentes

Estudiar el cociente de retículos y las cotas de orden con ceros espectrales, priors discretos y mediciones parciales. Contrastar con Jaming–Kolountzakis, Keleti–Kolountzakis, Bandeira et al., Agulnick–Busick-Warner y Casper–Orozco. Determinar si los mínimos 8h y los recuentos de Z₁₂ se conocen. Publicar como reproducción cuando corresponda; no inferir novedad por falta de coincidencias de terminología.

## Prioridad 4 — Tiempo y aplicaciones independientes

Extender el criterio temporal a medidas de correlación incompletas y ruidosas, órbitas locales desconocidas y costes no uniformes. Buscar contraejemplos a optimalidad de la selección voraz de aristas. En música, comparar reconocimiento de versiones con métodos establecidos, manteniendo separadas la identificación condicionada y la reconstrucción desde audio.

## Secundario

Q48, Cubo64, funciones bent y predicciones cuánticas son ejemplos que permiten comprobar la teoría, no objetivos de unificación por sí solos. No ampliar la interpretación física ni simbólica sin una predicción verificable. Una prueba de hardware solo tendría sentido con protocolo, presupuesto y comparación claros.

[Correcciones](CORRECCIONES.md) · [Informe matemático I–XI](INVESTIGACION.md) · [Marco general](MARCO_GENERAL.md).
