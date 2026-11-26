# Selección implícita de una observación binaria

Universo: palabras binarias lineales, multiconjunto de k-gramas y fronteras de longitud k−1 conocidos, prior uniforme. Se elige únicamente la **primera consulta** (posición o XOR entre dos posiciones), coste unitario, sin ruido. Una consulta determinista binaria aporta h₂(p) bits en esperanza. No se calcula un árbol adaptativo completo.

Estado dinámico: vértice actual v y vector r de multiplicidades restantes. C(v,r) suma C de los sucesores legales (restando una arista de cada tipo), con C(v,0)=1 si v es la raíz final y 0 si no. No se multiplican las aristas repetidas, puesto que se cuentan palabras, no etiquetados. Los prefijos que comparten estado se agregan mediante su número y los primeros momentos por posición. Multiplicar esos momentos por el número de sufijos legales permite recuperar exactamente los conteos de unos y de pares de unos; P(X_i XOR X_j)=P(X_i)+P(X_j)−2P(X_i=X_j=1). Todas las cuentas son enteras arbitrarias. Solo la entropía se evalúa en coma flotante. Se escoge el conteo más cercano a N/2 (equivalentemente, máxima entropía).

Cota de estados: a lo sumo |V| ∏_e (m_e+1), polinómica en longitud si alfabeto y k permanecen fijos, pero crece rápidamente con el número de tipos de aristas. El cálculo de momentos añade coste por longitud. No es una garantía de escalabilidad general.

Comparaciones: puente de Markov (frecuencias de transición normalizadas, extremo final condicionado, sin imponer agotamiento exacto de multiplicidades), 64 muestras uniformes de recorridos por arborescencia de últimas salidas, y consulta aleatoria uniforme entre posiciones y pares con al menos una posición fuera de las fronteras conocidas. Se evalúan todas frente a probabilidades exactas, no a sus propias estimaciones. En clases pequeñas también se contrasta cada conteo por enumeración explícita. El puente y el muestreo son referencias conocidas; la programación dinámica es una técnica clásica, sin reivindicación de prioridad.

Resultados: 1.160 clases de longitud 8,10,12 y k=2,3, con 2–32 candidatos. Todos los conteos coinciden con enumeración; bits medios óptimo 0,97812, puente 0,82177, muestreo 0,97534, aleatorio 0,67096. El puente selecciona una consulta constante en 153 clases. 48 casos adicionales de longitud 24–128, k=2,3, generados con bits equiprobables, sin alcanzar el límite de 300.000 estados; máximo 790618044114917387149095158232829440 candidatos. En n=128,k=2 (6 casos), óptimo 0,999998, aleatorio 0,999746, puente 0,999954. En 72 casos adicionales (sesgo 0,85; persistencia 0,94; alternancia 0,92; n=64,128), el método exacto supera la referencia aleatoria; también se verifica el total por la fórmula independiente de composiciones de carreras para k=2. No se demuestra ventaja general respecto a muestreo o inferencia existente.

Los comandos de reproducción generan results.json y stress.json. Los tiempos dependen de la máquina; no constituyen benchmark universal. No hay datos reales ni consultas posteriores condicionadas por respuestas.

## Reproducción
Python 3 y NumPy. Desde este directorio:

    OPENBLAS_NUM_THREADS=1 python audit.py
    OPENBLAS_NUM_THREADS=1 python stress.py

Antecedentes: Jacquet, Knessl y Szpankowski, Counting Markov Types; Exact Goodness-of-Fit Tests for Markov Chains (2013), https://academic.oup.com/biometrics/article/69/2/488/7492302; programación dinámica y forward-backward para inferencia en cadenas de Markov.
