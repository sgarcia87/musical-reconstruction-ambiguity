# Experimentos de reconstrucción

| Directorio | Protocolo |
|---|---|
| [queries](queries/) | Optimización explícita de consultas posicionales y XOR |
| [implicit](implicit/) | Conteo implícito de la primera consulta |
| [adaptive](adaptive/) | Reconstrucción adaptativa y alcance local |

Python 3. Los experimentos implícitos y adaptativos requieren NumPy. Cada directorio contiene las instrucciones de ejecución. Los JSON de gran tamaño se generan mediante los scripts; se publican los agregados y los 54 recorridos del ensayo adaptativo local. Los tiempos dependen del entorno de ejecución.

[Resultados agregados](../results/consultas.json) · [Recorridos del ensayo local](../results/adaptive_local.json).
