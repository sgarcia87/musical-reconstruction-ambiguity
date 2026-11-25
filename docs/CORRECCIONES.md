# Registro de correcciones y alcance científico

**RGO v0.3 · 25 de noviembre de 2026**

Las notas de trabajo anteriores se conservan íntegras como registro histórico. La referencia vigente es [INVESTIGACION.md](INVESTIGACION.md). Las siguientes precisiones prevalecen sobre formulaciones informales o interpretaciones más amplias de versiones anteriores.

| Tema | Formulación vigente |
|---|---|
| Q48 y Fourier | La caracterización de los hexacordos por F₄=0 y módulo de F₃ al cuadrado igual a 4 es exacta. Es una descripción equivalente de un caso de la teoría DFT de conjuntos musicales, no una prueba de un principio físico nuevo. |
| Correlaciones triples | En Z₁₂ separan las 224 clases por transposición/inversión, pero no todas las 352 clases por traslación. Hay una pareja reflejada que requiere orden 4. |
| El número 262 | Cuenta indicadores iniciales cuya reconstrucción requiere orden 4 si se admiten señales reales arbitrarias con magnitudes dadas. En el espacio binario solo 24 lo requieren. No son 262 pares Z ni 262 órbitas. |
| Q48 y Walsh | La homometría del conjunto Q48 en F₂¹² es diferente de la homometría de cada conjunto de notas sobre Z₁₂. El cociente bent de cuatro bits y las 28 clases están relacionados con formas alternantes no degeneradas. El conteo clásico es GL(4,2)/Sp(4,2)=20160/720. |
| Excepcionalidad de cuatro | q=4 es especial únicamente en la familia que usa la unión de dos subespacios complementarios sin origen. Las construcciones clásicas de Dillon por partial spreads producen funciones bent en otras dimensiones pares. No hay una excepcionalidad universal del cuatro. |
| Cubo64 | Su fórmula lineal concreta lleva las seis etiquetas relacionales a dos rectas sin origen; otras aplicaciones lineales adecuadas también lo hacen. No demuestra equivalencia de las estructuras completas ni un puente exclusivo de Cubo64. |
| Cuántica | Una copia con traslación uniforme desconocida y dos copias que comparten traslación tienen diferente identificabilidad teórica. Estimar signos de esperanzas requiere múltiples preparaciones; no implica discriminación perfecta en dos ejecuciones. La derivación comparte la misma álgebra, no constituye validación empírica independiente entre dominios. |
| Ruido y robustez | 8h es un mínimo para un diccionario y un protocolo determinados, con espectro/DC exactos, lista fija universal y repetición permitida. No corrige sesgos sistemáticos fuera del presupuesto de errores. |
| Certificado binario | Las cotas D₃/D₄ limitan la distancia a algún indicador. No garantizan la identificación de la estructura verdadera ni validan por sí solas un prior incorrecto. |
| Coherencia | La monotonía por procesamiento de datos se aplica bajo un canal común. No toda subida de coherencia destruye información en cualquier sistema. El objetivo y las simetrías deben definirse previamente. |
| Bach | El resultado de frecuencia de Q48 no demuestra privilegio musical independiente de la tonalidad. La reconstrucción temporal presupone órbitas locales conocidas y relaciones completas; no reconstruye grabaciones. |
| Originalidad y física | El problema de fase, homometría, k-decks, funciones bent, sincronización, códigos y aprendizaje activo tiene antecedentes. Falta comprobar la prioridad de los resultados particulares. No se ha demostrado una teoría física o de la consciencia. |

## Verificación de v0.3

Se ejecutaron nuevamente `rgo_fase9_audit.py`, `rgo_fase10_audit.py` y `rgo_fase11_audit.py`, usando NumPy 2.3.5 y SymPy 1.14.0 en el entorno de verificación. Las tres salidas JSON coincidieron byte por byte con los archivos originales.

Además, [verify_robustness.py](../audits/verify_robustness.py) usa un procedimiento independiente de recuento directo de subconjuntos (en vez de correlación de patrones con multiplicidad). Verifica 352 órbitas, 125 familias ambiguas, 189 pares, 62 tipos de consulta, ocho testigos disjuntos, el conjunto de ocho consultas suficiente y la distancia mínima 2 con todas las consultas distintas. Los mínimos de 8h se deducen de esos testigos y de la repetición.

No se repitió el análisis completo del corpus de Bach en esta revisión. Los datos originales permanecen identificados por su procedencia. No se realizó un nuevo experimento cuántico ni semántico. La bibliografía de las fases IX–XI queda como punto de partida para una revisión de prioridad independiente.
