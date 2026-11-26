# RGO — Selección de observaciones binarias

Estudio exploratorio. 26/11/2026.

Se enumeran las palabras binarias de longitudes 8, 10 y 12; para cada longitud se agrupan por multiconjunto de fragmentos de longitud k=2,3 y prefijo y sufijo de longitud k−1. Se conservan todas las clases con 2–32 palabras (1.160 clases, 6.866 pertenencias; una palabra puede aparecer en dos censos). Se excluyen 50 clases de tamaño superior a 32, además de las unitarias. Priors uniformes dentro de cada clase y ponderación idéntica por clase. Consultas exactas, sin ruido. No hay corpus musical o biológico en este experimento.

Una consulta posicional devuelve un bit; una consulta relacional devuelve el XOR de dos posiciones. Se eliminan consultas constantes y se identifican particiones complementarias. Se resuelve el mínimo esperado y el mínimo de peor caso por separado: para S con |S|>1, el coste total esperado (sin dividir por |S|) es T(S)=min_q [c(q)|S|+T(S0)+T(S1)], y el peor caso W(S)=min_q [c(q)+max(W(S0),W(S1))]. La estrategia fija optimiza una lista común a todos los candidatos y permite detenerse cuando la respuesta es única. El método voraz maximiza la división equilibrada; rollout elige mediante el coste de completar cada rama con la estrategia voraz y vuelve a planificar tras cada respuesta. El control aleatorio elige uniformemente entre particiones informativas distintas, no entre posiciones físicas.

La cota media binaria exacta sin restricciones de preguntas es d+1−2^d/N, d=ceil(log2(N)), y la cota del peor caso es d. Las consultas posicionales alcanzan la cota media en 930/1160 clases; con XOR de coste unitario, 1134/1160. Óptimo medio posicional 2,293157; óptimo con XOR 2,228927; fijo posicional 2,371741; voraz posicional 2,297021. La estrategia rollout con XOR alcanza el óptimo en los casos estudiados, sin garantía general. Los costes medios con XOR de coste 1;1,25;1,5;2 son 2,228927;2,274141;2,290632;2,293157. Cuando XOR cuesta dos consultas posicionales, puede simularse con ellas, así que no puede mejorar el óptimo.

Contraejemplo a que las consultas posicionales basten para alcanzar la cota: 01011110, 01101110, 01110110, 01111010. Las cuatro palabras comparten bigramas y fronteras. Una consulta posicional informativa separa 1 contra 3; XOR de posiciones 3 y 4 separa 2 contra 2; después basta una consulta posicional. Costes medios 2,25 vs 2, con peores casos 3 vs 2.

No se reivindica novedad matemática: árboles de decisión óptimos y consultas de paridad son problemas conocidos. La evidencia es específica de este censo y de los costes supuestos. No se ha establecido un mecanismo físico para observar XOR a coste unitario, ni se ha comparado con otros métodos de inferencia implícita de grandes fibras. La generación exhaustiva de candidatos no escala necesariamente.

## Reproducción

Python 3, sin dependencias externas. Desde este directorio:

```
python audit.py
python cost_sensitivity.py
python verify_small.py
```

La ejecución genera results.json y costs.json con los resultados por clase. verify_small.py compara 332 resultados con una recursión independiente sobre tuplas explícitas.

Antecedentes: Zhuo y Nagarajan, A simple approximation algorithm for optimal decision tree (2026), DOI 10.1016/j.orl.2025.107370; Decision trees for entity identification, DOI 10.1145/1921659.1921661.
