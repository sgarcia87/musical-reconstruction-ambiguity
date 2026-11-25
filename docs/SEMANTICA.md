# Observabilidad semántica: priors, pertenencia y orden (XII–XVII)

**RGO v0.5.1 · Sergi Garcia Mecinas · 26 de noviembre de 2026**

[Informe matemático](INVESTIGACION.md) · [Correcciones](CORRECCIONES.md) · [Agenda](ROADMAP.md)

La reconstrucción matemática de señales y la identificación de relaciones semánticas comparten una pregunta formal: ¿qué alternativas son compatibles con la evidencia observada y con el conocimiento previo? La analogía no traslada automáticamente las garantías de un dominio a otro. Los resultados siguientes son experimentos exploratorios; los resultados matemáticos de las fases anteriores conservan sus hipótesis específicas.

## XII. Fragilidad del conocimiento previo: corrección de circularidad

Se empleó una muestra del grafo IA_m (27 casos de equilibrio anotados), con aristas reservadas para validar la reconstrucción. En el conjunto, 18 priors erróneos eran estables; el validador rechazó 17 de ellos. Sin embargo, el rechazo de un prior erróneo coincidió exactamente con que el validador reprodujera la referencia (24/27). El prior erróneo excluye la referencia por diseño y tanto esta referencia como las aristas de validación fueron producidas por el mismo sistema de anotación. **No es una demostración de detección de errores semánticos externos.** La restricción a los 11 casos no automáticos no elimina necesariamente el origen compartido de las anotaciones. El contraejemplo de sesgo compartido, simulado en el grafo, muestra una corroboración errónea con validación alterada.

La auditoría XII se ejecutó de nuevo y su JSON coincide por igualdad de objetos con el original. La [nota histórica corregida](rgo_fase12_nota.md), [demostración](../demos/rgo_fase12.html), [auditoría](../audits/rgo_fase12_audit.py) y [resultados](../results/rgo_fase12_results.json) se conservan.

## XIII. Asociación libre externa: una hipótesis que no supera el baseline

El grafo USF tiene 10.617 palabras y 72.176 relaciones dirigidas. La referencia de Wilkinson y Oates (2016) aporta escalas ordenadas por humanos. En 46 consultas con pertenencia a escala dada, difracción obtiene 60,87% de top-1 con grafo intacto y 58,70% tras retirar las 138 aristas internas a escalas anotadas. PPR mínimo: 63,04% y 65,22%, respectivamente. En el vocabulario completo tras ablación, solo 1/56 primeros candidatos de difracción y 5/56 de PPR mínimo coinciden con la referencia conocida. No se califican como inválidas las palabras sin anotaciones. No se ha probado ventaja de la difracción ni descubrimiento abierto. La ablación usa pertenencia conocida y la vista reversa no es una fuente independiente.

[Auditoría](../audits/rgo_fase13_audit.py) · [Resultados](../results/rgo_fase13_resultados.json).

## XIV. Proyección sobre extremos conocidos

Se representan las palabras por perfiles de asociación entrante/saliente normalizados y se calcula la coordenada de X sobre el segmento A–B: t(X)=((X−A)·(B−A))/||B−A||². En el banco de Wilkinson, con extremos conocidos, los perfiles entrantes aciertan 20/28 pares internos antes de retirar aristas de la misma escala y 26/28 después. Con 56 consultas y un vocabulario restringido a los términos anotados disponibles, el punto medio entrante obtiene 42/56 tras ablación, frente a 27/56 de PPR mínimo y 20/56 de difracción. Con 4.870 candidatos obtiene 28/56 coincidencias conocidas. Bajo cambio de anclajes, se obtienen 80/87 comparaciones correctas tras ablación (70 de las 87 comparaciones vienen de una única escala). La estabilidad de coordenadas puede coexistir con errores. No es una evaluación confirmatoria ni libre de anclajes.

[Demostración](../demos/rgo_fase14.html) · [Auditoría](../audits/rgo_fase14_audit.py) · [Resultados](../results/rgo_fase14_resultados.json).

## XV. Ejes sin anclajes: pertenencia y orden no son lo mismo

En las 4.870 palabras con perfiles entrantes y salientes, el grafo de vecinos recíprocos y la optimización de modularidad no reciben etiquetas de escala. En el banco de 52 palabras anotadas, coseno entrante distingue pares de la misma escala (AUC 0,97475). Con k=20, la agrupación entrante acierta 50 de 96 pares positivos y no mezcla etiquetas en esos 50 pares anotados; no se conoce la pureza de todas las comunidades. PC1 acierta 19 de 33 ternas reunidas (19/106 conjuntamente). Con pertenencia conocida, Fiedler combinado acierta 70/106 ternas, 50 de ellas en la escala de valoración; sin dicha escala, 20/50. La seriación Robinson exacta demuestra que optimizar coherencia geométrica no necesariamente recupera orden humano: dos perspectivas con coste cero pueden escoger intermedios distintos.

[Nota](rgo_fase15_nota.md) · [Demostración](../demos/rgo_fase15.html) · [Auditoría](../audits/rgo_fase15_audit.mjs) · [Resultados](../results/rgo_fase15_resultados.json).

## XVI. Segundo banco: la ventaja no se reproduce

Se cambió la referencia a 87 semiescalas de de Melo y Bansal (2013), usando el mismo grafo USF. Con pertenencia conocida, se excluyen empates de referencia y se evalúan ternas estrictas. De 353 ternas posibles solo 40 están cubiertas (19 semiescalas). PC1 entrante 39,17%; coseno local combinado 35,83%; Fiedler combinado 25,83%; azar 33,33%. Al quitar todos los términos de Wilkinson antes de calcular coordenadas, quedan 20 ternas cubiertas de 257 posibles (12 semiescalas); el mejor resultado descriptivo es coseno local 46,67%, con muestra demasiado pequeña y dependiente para inferir superioridad.

[Nota](rgo_fase16_nota.md) · [Auditoría](../audits/rgo_fase16_audit.mjs) · [Resultados](../results/rgo_fase16_resultados.json).

## XVII. Un observador ordinal exacto y una prueba de cobertura

El modelo ideal de órdenes estrictos salvo inversión permite contar fibras, seleccionar consultas y estudiar ruido. La distancia de la firma ternaria completa es n−2; para seis elementos se obtienen mínimos de 7/10/16 consultas fijas distintas (identificación/detección/corrección de una lectura) y seis adaptativas exactas. La prueba artificial de prior excluyente muestra 218/240 falsas unicidades y 240/240 rechazos al ampliar al universo correcto con un oráculo ideal; consultar directamente la restricción del prior es un control más simple en ese ejemplo. No son resultados sobre datos lingüísticos.

Para acercarse a un oráculo real se buscaron siete patrones de intensidad en 16.622 enunciados (254.820 tokens) del English Web Treebank: tres ocurrencias, ninguna conecta dos términos de una misma escala objetivo. Se intentó también transferir las ternas estrictas anotadas en de Melo/Bansal a las escalas completas de Wilkinson: ninguna de 344 ternas fuente coincide con una terna objetivo. **No hay cobertura útil ni medida de precisión en este piloto.** La fuente de observaciones ordinales suficiente y contextualizada sigue pendiente. Se conserva el fracaso como resultado, no como corroboración.

[Nota y demostraciones](rgo_fase17_nota.md) · [Laboratorio XVII](../demos/rgo_fase17.html) · [Auditoría matemática](../audits/rgo_fase17_audit.mjs) · [Extracción](../audits/rgo_fase17_evidence.mjs) · [Resultados exactos](../results/rgo_fase17_resultados.json) · [Resultados del piloto](../results/rgo_fase17_evidence.json).

### Ampliación XVII: observación ordinal con cobertura real

La ampliación XVII extiende la optimalidad adaptativa exacta hasta ocho elementos (20.160 órdenes, 10 consultas en el peor caso), comprueba un prior de extremo fijo y evalúa JJGraph (Cocos et al., 2018). Con pertenencia dada, 190 comparaciones propuestas, 85 acuerdos estrictos, 62 desacuerdos y 43 empates; 22/87 escalas incompatibles y dos soluciones únicas, una equivocada. No se ha resuelto el descubrimiento de atributos ni la extracción fiable de comparaciones.

En las doce escalas bipolares de Wilkinson, la misma regla, restringida a cadenas dirigidas de dos enlaces sin imponer orientación global, certifica condicionalmente 50 de 180 ternas, pero solo 12 coinciden con la referencia. El presupuesto de una violación evita muchas certezas, a costa de la cobertura. Los resultados son exploratorios, con pertenencia conocida y etiquetas no usadas para extraer los enlaces. No reproducen el modelo entrenado de Cocos et al. ni demuestran superioridad sobre métodos existentes.

En el plano combinatorio, la ampliación construye árboles que alcanzan la cota de información para n=7 y n=8 (8 y 10 consultas en el peor caso). Con un prior de extremo fijo, 7.540/15.120 órdenes excluidos producen falsa unicidad en n=8; todos se rechazan al validar con el universo correcto y el oráculo exacto (máximo dos consultas extra para esa política). Es un segundo control sintético, no una garantía empírica.

[Informe ampliado, demostración y fuentes](rgo_fase17_extension.md) · [Laboratorio de hasta ocho elementos](../demos/rgo_fase17_observador.html).

## Conclusión científica y reproducibilidad

La asociación semántica puede informar pertenencia a una dimensión, pero no garantiza su orden. El observador ordinal ideal de XVII está verificado, pero obtener observaciones de una fuente distinta con cobertura y fiabilidad suficientes, y separar desarrollo y prueba por atributo y vocabulario, permanece pendiente. JJGraph ya se ha evaluado mediante una regla explícita y no supera ese obstáculo. Esta línea no demuestra una teoría general del significado ni superioridad de un algoritmo. XII usa datos internos; XIII–XV reutilizan un banco externo y XVI cambia las etiquetas de referencia pero conserva el grafo. No se asume independencia de ternas, parejas ni perspectivas. Se publican también los resultados negativos.

```bash
pip install -r requirements-research.txt
python audits/rgo_fase12_audit.py
python audits/rgo_fase13_audit.py --data ./rgo_data
python audits/rgo_fase14_audit.py --data ./rgo_data
node audits/rgo_fase15_audit.mjs --self-test
node audits/rgo_fase15_audit.mjs --data ./rgo_data
node audits/rgo_fase16_audit.mjs --data ./rgo_data
node audits/rgo_fase17_audit.mjs
node audits/rgo_fase17_evidence.mjs --data ./rgo_data
node audits/rgo_fase17_math.mjs
node audits/rgo_fase17_prior.mjs
node audits/rgo_fase17_semantic.mjs --data ./rgo_data
```

XII se reprodujo localmente. XIII–XVI fueron calculadas sobre los corpus originales mediante JavaScript en el entorno de investigación; los scripts XIII/XIV de Python y XV de Node se comprobaron con datos sintéticos en sesiones anteriores; XV pasó nuevamente su self-test. Los JSON compactos de XIII–XV registran esas ejecuciones, no equivalencias byte a byte con las salidas de scripts locales. XVI comparte la misma función de cálculo con el script local. El acceso de red local no permitió volver a descargar los corpus y repetir los cuatro experimentos enteros localmente. XVII se ejecutó exhaustivamente y sus mínimos principales se comprobaron también por programación entera en Python. El piloto de evidencia se ejecutó sobre los archivos originales recuperados; no se repitió su descarga desde Node local. La ampliación se ejecutó también íntegramente mediante JavaScript, incluida la lectura de JJGraph y las dos referencias originales; no se repitió la descarga desde Node local. Los corpus de terceros no se redistribuyen. Véanse las huellas, fuentes y limitaciones en las notas y resultados.

**Referencias principales:** USF (Nelson et al., 2004, DOI 10.3758/BF03195588); [Wilkinson y Oates, 2016](https://aclanthology.org/L16-1424/); [de Melo y Bansal, 2013](https://aclanthology.org/Q13-1023/); [Cocos et al., 2018](https://aclanthology.org/D18-1202/); [Garí Soler y Apidianaki, 2021](https://aclanthology.org/2021.naacl-main.370/).
