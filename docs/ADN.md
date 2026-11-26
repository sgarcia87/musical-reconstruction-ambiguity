# Reconstrucción de ADN mitocondrial

Sergi Garcia Mecinas · 26/11/2026

## Protocolo

Genoma mitocondrial humano de referencia [NC_012920.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_012920.1), 16.569 bases. [Copia FASTA](https://github.com/AnimaTardeb/G4Hunter/blob/master/Mitochondria_NC_012920_1.fasta), blob Git d7209f124116355d07a210686159872937f6c2ad.

Ventanas no solapadas dentro de cada tamaño; se descartan las incompletas y las que contienen bases indeterminadas. Se conoce el multiconjunto completo de k-mers y las fronteras de longitud k−1. Se aplican el contador BEST y el criterio de k-switching de [REPETICIONES.md](REPETICIONES.md).

El control de bigramas conserva las transiciones y extremos. El control reforzado conserva también los histogramas de multiplicidades de todos los fragmentos y de los sufijos. Se realizan 1.200 propuestas por ventana, seis estados después de la primera mitad y seis controles de bigramas. Total: 191 ventanas, 2.292 evaluaciones de control y 229.200 propuestas. Los dos criterios de unicidad coinciden en las 191 ventanas.

## Resultados

| Bases | Ventanas | Original | Bigramas | Perfil reforzado |
|---:|---:|---:|---:|---:|
| 128 | 128 | 7,5703 | 7,4714 | 7,5612 |
| 256 | 63 | 8,7460 | 8,6561 | 8,8386 |

Longitud mínima media de reconstrucción. La diferencia respecto al control de bigramas es aproximadamente 1,3 % y 1,0 %. La inversión de la curva media de ambigüedad se reduce sustancialmente al conservar el perfil reforzado.

| k | H original 128 | H bigramas 128 | H perfil 128 | H original 256 | H bigramas 256 | H perfil 256 |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 144,9694 | 145,7713 | 144,9448 | 359,8742 | 361,5716 | 359,8801 |
| 4 | 71,7963 | 72,3432 | 71,8382 | 224,4134 | 226,5284 | 224,4000 |
| 5 | 24,2553 | 23,9804 | 24,3459 | 98,2456 | 97,2115 | 98,2709 |
| 6 | 5,5113 | 5,4093 | 5,6636 | 30,9042 | 29,9938 | 30,8567 |
| 7 | 0,8479 | 0,8004 | 0,9008 | 7,7162 | 7,2125 | 7,9801 |
| 8 | 0,1231 | 0,0524 | 0,1213 | 1,3285 | 1,1793 | 1,4778 |
| 10 | 0 | 0 | 0 | 0,0159 | 0,0106 | 0,0317 |
| 12 | 0 | 0 | 0 | 0 | 0 | 0 |

Distancia de Hamming media respecto al original en el control reforzado: 0,658 y 0,602. Aceptación de propuestas no triviales: 2.818/101.331 y 494/50.083. No se ha certificado mezcla uniforme.

## Enumeración exhaustiva

276 ventanas de 12 bases con inicios separados por 60 bases. Se enumeran 24.171 pertenencias a fibras de bigramas, de las cuales 10.327 conservan el perfil reforzado. En 120 ventanas alguna alternativa cambia la longitud mínima y en 149 cambia la curva. Mínimo medio en los órdenes 2–8: original 3,652174; bigramas 3,636686; perfil reforzado 3,650508.

## Alcance

Los resultados son compatibles con los efectos combinatorios de las repeticiones. Se utiliza una sola referencia mitocondrial; las ventanas de distintos tamaños no son independientes. No se analizan lecturas parciales o ruidosas, regiones nucleares ni diferencias entre especies. No se establece una propiedad biológica adicional ni una mejora de ensamblaje. Se publican los agregados registrados; el código original de este ensayo no está incluido.

Antecedentes: [Bresler, Bresler y Tse (2013)](https://doi.org/10.1186/1471-2105-14-S5-S18); [Reconstruction of DNA Sequences Through Eulerian Traversal of De Bruijn Graphs](https://www.mdpi.com/2227-7390/14/5/832).
