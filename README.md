# Musical Reconstruction Ambiguity

**Sergi Garcia Mecinas · 2026**

Análisis combinatorio exacto de la reconstrucción melódica a partir de fragmentos de intervalos y estructuras de repetición.

[Web interactiva](https://sgarcia87.github.io/musical-reconstruction-ambiguity/) · [Manuscrito (EN)](study/MANUSCRIPT.md) · [English](README.en.md) · [Reproducción](study/README.md)

¿Cuántos fragmentos de una melodía hacen falta para determinarla de forma única?

Se estudia la ambigüedad de reconstrucción a partir del multiconjunto completo de fragmentos consecutivos de intervalos de clase de altura, con fronteras conocidas. El recuento exacto emplea equivalencia k-abeliana, grafos de De Bruijn y recorridos eulerianos.

**Estado:** investigación exploratoria cerrada; manuscrito pendiente de reproducción independiente y revisión académica.

## Resultados

| Corpus | Secuencias | Original | Control de bigramas | Perfil completo |
|---|---:|---:|---:|---:|
| Bach | 382 | 6,586 | 5,629 | 6,644 |
| The Session | 51 | 11,098 | 6,711 | 11,431 |
| Essen | 740 | 5,984 | 5,228 | 6,068 |

Longitud mínima media de reconstrucción, en intervalos. La ambigüedad media de los originales es menor en órdenes cortos y mayor en órdenes posteriores respecto al control de bigramas. El control que conserva las multiplicidades de las repeticiones atenúa la diferencia.

En Essen, conservar el perfil hasta tres intervalos reduce un 94,6 % la diferencia de longitud mínima en un ensayo graduado, pero aumenta un 13,7 % la discrepancia absoluta de ambigüedad en los órdenes 6 y 8. Conservar perfiles hasta seis u ocho intervalos aproxima también la ambigüedad tardía.

La auditoría independiente con abcjs 6.7.3 coincide en los 33.748 eventos de las 740 melodías de Essen. No hay palabras de intervalos idénticas entre los tres corpus; Bach contiene 38 registros duplicados en esta representación.

## Contraste exacto

La hipótesis exploratoria de menor entrelazamiento de las repeticiones no se confirma al enumerar todas las alternativas en 36 melodías computacionalmente tratables. Las diferencias original–control exacto en los órdenes 4 y 5 son +1,52 y +0,93 puntos porcentuales, frente a las diferencias negativas observadas en el muestreo del corpus completo. La selección del subconjunto impide atribuir la inversión exclusivamente al muestreo. No se sostiene una regularidad musical de entrelazamiento.

## Documentación

- [Manuscrito científico](study/MANUSCRIPT.md)
- [Prueba exacta y resultado negativo](study/EXACT_INTERLEAVING.md)
- [Metodología y reproducción](study/README.md)
- [Código](study/) y [resultados agregados](study/results/)
- [Archivo de la investigación anterior](https://github.com/sgarcia87/musical-reconstruction-ambiguity/tree/f0905323a98448229ff5504763987db97648f40b)

## Alcance

Se consideran intervalos módulo 12, sin ritmo, registro ni polifonía. Los controles por perfil no tienen convergencia certificada. Los intervalos de confianza agrupados de Essen corresponden al primer ensayo; los controles graduados aún requieren reproducción completa con resultados por melodía. Manuscrito de investigación no revisado por pares; originalidad bibliográfica no establecida.
