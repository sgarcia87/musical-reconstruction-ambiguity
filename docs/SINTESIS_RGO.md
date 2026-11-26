# Geometría relacional y observabilidad (RGO)

**Sergi Garcia Mecinas · 26/11/2026**

## Principios

### 1. Observar es agrupar
Sea U un universo de candidatos, O una observación y y el valor observado. La fibra F_U(y) = {x ∈ U : O(x) = y} contiene todas las estructuras compatibles. Para un universo discreto finito, log₂|F_U(y)| cuantifica la ambigüedad combinatoria; solo es entropía bajo equiprobabilidad dentro de la fibra. Las simetrías consideradas irrelevantes requieren un cociente compatible con la observación.

### 2. El conocimiento previo aporta información
Una restricción P reduce la fibra a F_U(y) ∩ P. La unicidad en P no implica unicidad en U; un prior que excluye la verdad puede producir una solución inequívoca y falsa. En ℤ₁₂, con magnitudes y componente constante exactas, 262 de los 4096 indicadores requieren orden cuatro si se admiten señales reales; 24 si se restringen a indicadores. De los 262 casos difíciles, 238 reducen su orden (90,84 %). [Censo y condiciones](rgo_fase11_nota.md).

### 3. Coherencia no equivale a verdad
La contracción de divergencias bajo un canal común puede aumentar el acuerdo mientras se pierde capacidad de distinguir. No es una equivalencia universal. En el grafo interno IA_m, un prior incorrecto pudo superar criterios de estabilidad; el aparente rechazo posterior era en gran parte circular al compartir origen referencia y evidencia. [Auditoría y correcciones](SEMANTICA.md).

### 4. Cambiar de perspectiva significa distinguir nuevas alternativas
Una observación adicional refina la fibra. La selección de consultas puede minimizar la peor rama o maximizar información esperada con coste y distribución especificados. Con ruido, la distancia entre firmas determina la capacidad de detectar y corregir errores. No se ha probado una ventaja universal de la adaptación. [Robustez](rgo_fase11_nota.md).

### 5. Reconocer no equivale a reconstruir
Una firma puede identificar una obra en un catálogo sin reconstruirla fuera de él. Las relaciones temporales ayudan en música simbólica, pero la alineación sigue siendo competitiva o superior en los protocolos probados. Los cinco tarareos de pilotos no constituyen una evaluación acústica independiente. [Investigación musical anterior](MUSICA.md).

### 6. Registrar asociaciones no basta para descubrir significado
La recuperación de relaciones anotadas debe separarse de la predicción de relaciones desconocidas. En pruebas externas, la difracción semántica no supera consistentemente a PPR mínimo. Sin anclajes ni pertenencia conocida se recuperaron conjuntamente 19/106 ternas. No se ha demostrado descubrimiento semántico fiable. [Resultados](SEMANTICA.md).

## Resultados matemáticos

| Resultado | Alcance | Documento |
|---|---|---|
| Ambigüedad de fase | Magnitudes, soporte y relaciones modulares fijados; módulo traslación | [Nota](AMBIGUEDAD_ESPECTRAL.md) |
| Certificación binaria | Momentos hasta orden 3 en señales no negativas o 4 en reales; no certifica identidad | [Informe](INVESTIGACION.md) |
| Consultas robustas | Mínimos fijos 8/16/24 con espectro/DC exactos y diccionario especificado | [Nota](rgo_fase11_nota.md) |
| Reconstrucción temporal | Órbitas locales conocidas; criterio de conectividad | [Nota](OBSERVABILIDAD_TEMPORAL.md) |
| Orden estricto | Intermediación, orden salvo inversión, distancia mínima n−2 | [Nota](rgo_fase17_nota.md) |
| Fragmentos | Recuento exacto de recorridos eulerianos; equivalencia k-abeliana | [Estudio](REPETICIONES.md) |

## Estudio final

En dos corpus musicales, la ambigüedad residual frente a controles de bigramas se reduce sustancialmente al preservar el perfil de repeticiones. Un contraejemplo binario demuestra que dicho perfil no determina por sí solo la unicidad. La separación local/global se obtiene de BEST. No hay evidencia suficiente de una propiedad adicional específica de la música.

[Estudio de fragmentos](ESTUDIO_FRAGMENTOS.md) · [Estudio final](REPETICIONES.md) · [Archivo científico](ARCHIVO.md).

## Alcance

La homometría, recuperación de fase, equivalencia k-abeliana, geometría musical, grafos y códigos tienen antecedentes establecidos. Q48, funciones bent, Cubo64 y modelos cuánticos son casos algebraicos, no leyes generales de la naturaleza. Los resultados de las líneas anteriores se conservan con sus hipótesis y limitaciones. Investigación exploratoria concluida, sin revisión por pares ni reivindicación de prioridad.
