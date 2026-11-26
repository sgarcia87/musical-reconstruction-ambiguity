# Selección de observaciones y reconstrucción adaptativa

Sergi Garcia Mecinas · 26/11/2026

## Modelo

Palabras binarias de longitud n, multiconjunto completo de k-gramas, fronteras conocidas, prior uniforme. Una consulta exacta devuelve x_i o x_i XOR x_j. Cada respuesta restringe la fibra de palabras compatibles.

## Optimización explícita

Para una fibra S, el coste esperado total sin normalizar es T(S)=min_q[c(q)|S|+T(S₀)+T(S₁)], con T(S)=0 para una fibra unitaria. Se calcula también el mínimo de peor caso. Censo: 1.160 clases de 2–32 candidatos, n=8,10,12, k=2,3; 50 clases mayores excluidas y 6.866 pertenencias a clases.

| Estrategia | Consultas medias |
|---|---:|
| Aleatoria adaptativa posicional | 2,3837 |
| Fija óptima con parada anticipada | 2,3717 |
| Voraz posicional | 2,2970 |
| Adaptativa óptima posicional | 2,2932 |
| Adaptativa óptima con XOR | 2,2289 |
| Cota binaria sin restricciones | 2,2245 |

A coste XOR igual a 2, la consulta puede sustituirse por dos consultas posicionales y no mejora el óptimo. [Protocolo y código](../experiments/queries/README.md).

## Conteo implícito

El estado (v,r) contiene el vértice actual del grafo de De Bruijn y las multiplicidades de aristas restantes. El número C(v,r) de sufijos válidos satisface una recurrencia sobre transiciones legales. Las aristas repetidas son indistinguibles. Los momentos de prefijos agregados y los conteos de sufijos proporcionan los marginales posicionales y de pares sin enumerar las palabras completas.

Si N es la cardinalidad de la fibra y N₁ la de los candidatos con respuesta 1, minimizar |2N₁−N| maximiza la entropía binaria inmediata bajo prior uniforme.

| Método | Información media de la primera consulta (bits) |
|---|---:|
| Aleatorio | 0,67096 |
| Puente de Markov | 0,82177 |
| Muestreo (64 recorridos) | 0,97534 |
| Conteo exacto | 0,97812 |

1.160 clases contrastadas con enumeración; 120 ensayos sintéticos adicionales, hasta n=128. Mayor fibra inicial: 790618044114917387149095158232829440. Cota de estados: |V|·∏(m_e+1). El coste crece con el número de tipos de aristas. [Protocolo y código](../experiments/implicit/README.md).

## Condicionamiento adaptativo

Las respuestas XOR se representan como componentes de paridad sobre GF(2). Se conserva un bit libre por componente abierto no fijado; una posición conocida fija su componente. El contador de sufijos y los momentos de prefijo incorporan estas restricciones. Con relaciones de distancia máxima b, cada componente abierto contiene una arista que cruza el corte. Hay a lo sumo b componentes abiertos y un factor adicional de estados de hasta 2^b.

3.480 recorridos sobre 1.160 clases terminan correctamente; 211.570 comprobaciones de conteos. En otros 22 casos, las consultas posicionales y el muestreo completan todos; XOR sin límite falla en tres al superar 100.000 estados por paso. La implementación local (b=3) supera otras 29.036 comprobaciones.

| Estrategia (18 casos nuevos) | Consultas medias | Tiempo medio (s) |
|---|---:|---:|
| Posicional | 36,1667 | 0,237 |
| XOR local | 35,5000 | 0,514 |
| Muestreo | 35,7778 | 0,445 |

Mayor fibra reconstruida: 68.557.426.042.230.000 candidatos. Los tiempos corresponden a la ejecución registrada; el muestreo utiliza el mismo contador de sufijos. La selección exacta optimiza la ganancia inmediata, no el árbol completo. No se ha demostrado una ventaja general de coste, tiempo o consultas. Ensayos binarios sintéticos, sin ruido.

[Protocolo y código](../experiments/adaptive/README.md) · [54 recorridos del ensayo local](../results/adaptive_local.json).

## Antecedentes

- [Exact Goodness-of-Fit Tests for Markov Chains (2013)](https://academic.oup.com/biometrics/article/69/2/488/7492302): distribución condicionada a transiciones.
- [Statistical Inference in Hidden Markov Models Using k-Segment Constraints (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4867884/): estados aumentados mediante contadores.
- Kschischang, Frey y Loeliger (2001), [Factor Graphs and the Sum-Product Algorithm](https://doi.org/10.1109/18.910572): inferencia y marginales.
- [On the BCJR trellis for linear block codes](https://doi.org/10.1109/18.508834): estados por corte para restricciones lineales.
- Gomes et al. (2007), [From Sampling to Model Counting](https://ijcai.org/proceedings/2007/369): selección de variables y relaciones de paridad para equilibrar conjuntos de soluciones.
- [Performance Bounds for Active Binary Testing with Information Maximization (2024)](https://proceedings.mlr.press/v235/chattopadhyay24a.html): consultas adaptativas por información.
- [Approximate Optimal Active Learning of Decision Trees (2025, preprint)](https://arxiv.org/abs/2512.03971): selección de consultas mediante conteo implícito aproximado.

La especialización combina técnicas establecidas de conteo, programación dinámica, restricciones de paridad y selección de consultas. La prioridad bibliográfica no está establecida. La revisión no es sistemática ni exhaustiva.
