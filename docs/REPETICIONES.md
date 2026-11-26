# Repeticiones, conectividad y observabilidad

26/11/2026 · Estudio exploratorio

## Unicidad

La equivalencia k-abeliana coincide, para palabras lineales de longitud n≥k, con la igualdad de multiplicidades de fragmentos k y de prefijo/sufijo de longitud k−1. La caracterización por k-switchings da un criterio exacto: existen i<j≤l<m con fragmentos (k−1) iguales en i,l y j,m cuyo intercambio de segmentos A B C → C B A (A=x[i:j], B=x[j:l], C=x[l:m]) cambia la palabra. Una clase no unitaria admite un intercambio no trivial desde cada representante. Una repetición por sí sola no basta.

Se comparó el criterio con enumeración directa en 90.112 pares palabra/orden binarios de longitudes 2–12, sin discrepancias, y con BEST en los límites k_min y k_min−1 de los 433 originales (433/433).

## Perfil de repeticiones

R_k(m) es el número de fragmentos distintos de longitud k y multiplicidad m. El perfil completo reúne todas las longitudes. Con n fijo, m=1 se deduce de los m≥2. No conserva los nombres de los fragmentos ni su organización.

Las palabras 0000101 y 0001001 tienen iguales bigramas, extremos y perfil completo, pero cardinalidades [21,4,1,1,1,1,1] y [21,4,2,1,1,1,1]. En el perfil reforzado, que fija también multiplicidades de sufijos, 0101111 y 0111011 presentan las mismas curvas respectivas. No se reclama originalidad bibliográfica.

## Descomposición exacta

Para k≥2, sea d_v el grado de salida, m_uv las multiplicidades y τ_t el número de arborescencias dirigidas hacia la raíz final t, contando aristas paralelas etiquetadas. BEST da

    N = τ_t × ∏_v (d_v − 1 + 1_{v=t})! / ∏_{u,v} m_uv!

Etiquetando temporalmente las aristas, las últimas salidas de los vértices no raíz forman un árbol hacia t. Fijado el árbol, se ordenan libremente las restantes aristas; en t se ordenan todas. Se divide por las permutaciones de aristas idénticas. Los bucles no forman parte del árbol; sí intervienen en los factoriales.

Reescritura:

    N = [∏_v d_v! / ∏_{u,v} m_uv!] × [τ_t / ∏_{v≠t} d_v]
    H = L + G

El primer factor cuenta ordenaciones locales. El segundo es la probabilidad de que una elección independiente y uniforme de una arista etiquetada por vértice no raíz forme una arborescencia hacia t. Es positivo y ≤1, por tanto G≤0. Si F_k=Σ_w log₂(c_k(w)!), entonces L_k=F_{k−1}−F_k−log₂(c_{k−1}(sufijo)). El perfil reforzado fija L_k; las diferencias de H quedan en el término global. Para k=1 se aplica el multinomial.

## Control empírico

Mismos corpus y representación del [estudio de fragmentos](ESTUDIO_FRAGMENTOS.md).

Ensayo inicial: 220 propuestas por pieza, hasta 12 candidatos distintos que conservan bigramas y perfil completo. 419/433 piezas con candidatos; 3.515 evaluados. Bach 6,531 frente a 6,580; The Session 9,932 frente a 10,273. 400 piezas tienen algún cambio de H y 163 algún cambio de k_min.

Ensayo reforzado: propuestas por tripletas de posiciones con el mismo símbolo o pares independientes entrelazados. Se rechazan cambios de perfil o de multiplicidades de sufijos. La propuesta ideal es simétrica, pero no se garantiza irreducibilidad ni mezcla. Xorshift32; 1.800 propuestas, 600 de descarte, estados cada 100; 12 muestras por pieza, incluidas identidades y repeticiones. También 12 controles de bigramas por pieza, con nuevas semillas. Se verifica igualdad del término local en los órdenes medidos.

| Corpus | Original | Transiciones | Perfil reforzado | Distancia de Hamming media |
|---|---:|---:|---:|---:|
| Bach | 6,5864 | 5,6294 | 6,6440 | 0,633 |
| The Session | 11,0980 | 6,7108 | 11,4314 | 0,654 |

10.392 evaluaciones de control. 432 piezas con alguna muestra distinta; 199 con algún cambio de k_min. La inversión de la curva desaparece prácticamente en las medias. [Agregados completos](../results/repeticiones.json).

Las aceptaciones sobre propuestas no triviales son 14,4 % y 3,5 %. En The Session, k medio en las mitades de la cadena es 11,307/11,556: posible mezcla lenta. No son muestras independientes. La cercanía de las curvas no demuestra suficiencia causal del perfil ni ausencia de efectos en otros corpus. No se ha realizado validación externa ni prueba formal de significación.

## Conclusión

El perfil de repeticiones no determina matemáticamente la reconstruibilidad, pero explica descriptivamente gran parte de la diferencia entre música y controles de transiciones en estos corpus bajo el muestreo ensayado. La conectividad determina la compatibilidad global. No hay evidencia suficiente de un efecto adicional específico de la música.

## Reproducción

Node.js 18+:

    node audits/auditoria_repeticiones.mjs --self-test
    node audits/auditoria_repeticiones.mjs --data ./rgo_data --simple > simple.json
    node audits/auditoria_repeticiones.mjs --data ./rgo_data > strict.json

Los corpus se verifican por SHA-1 de blob Git. Los resultados agregados proceden de las ejecuciones sobre los blobs originales; no son filas brutas. El código publicado reúne el protocolo de la auditoría de repeticiones y el parser de la investigación musical anterior. No se ha repetido localmente el ensayo completo.

## Referencias

- Bresler, Bresler y Tse (2013). [Optimal assembly for high throughput shotgun sequencing](https://doi.org/10.1186/1471-2105-14-S5-S18).
- [On cardinalities of k-abelian equivalence classes](https://www.utupub.fi/bitstream/handle/10024/155801/On_cardinalities_of_k-abelian_equivalence_classes.pdf?isAllowed=y&sequence=1).
- [k-Abelian Equivalence and Rationality](https://www.utupub.fi/bitstream/handle/10024/188874/main.pdf?isAllowed=y&sequence=1).
- Ukkonen (1992). [Approximate string-matching with q-grams and maximal matches](https://doi.org/10.1016/0304-3975(92)90143-4).
- Jacquet, Knessl y Szpankowski (2012). [Counting Markov Types, Balanced Matrices, and Eulerian Graphs](https://www.cs.purdue.edu/homes/spa/papers/it12-types.pdf).

La prioridad bibliográfica de los resultados particulares queda abierta.
