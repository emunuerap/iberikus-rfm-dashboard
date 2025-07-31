# Iberikus RFM Dashboard

Este proyecto simula el trabajo de un **Data Scientist profesional contratado por Iberikus** para realizar un análisis RFM (Recencia, Frecuencia, Valor Monetario) y ayudar a tomar **decisiones estratégicas de negocio** basadas en datos.

---

## 🎯 Objetivo

Segmentar la base de clientes de Iberikus según sus hábitos de compra y generar un dashboard interactivo para interpretar visualmente los distintos perfiles de clientes.

---

## 📁 Estructura del Proyecto

```
iberikus_rfm_data_product/
│
├── data/              # Dataset RFM segmentado (rfm_clustered_customers.csv)
├── notebooks/         # Notebooks exploratorios (opcional)
├── dashboard/         # Script de Dash: iberikus_rfm_dashboard.py
├── docs/              # README y futuras documentaciones estratégicas
└── outputs/           # Visualizaciones, exportaciones o reportes
```

---

## 📊 Segmentos Identificados

Los clientes han sido agrupados usando **KMeans** en 4 segmentos, visualizados en el dashboard mediante gráficos interactivos que permiten analizar:

- Recency
- Frequency
- Monetary
- Distribución por segmento

---

## 🚀 Ejecutar el Dashboard

1. Instala dependencias:
```bash
pip install dash dash-bootstrap-components plotly pandas
```

2. Ejecuta desde `dashboard/`:
```bash
python iberikus_rfm_dashboard.py
```

3. Abre en tu navegador: [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## ✨ Autor
Este proyecto fue desarrollado como un ejemplo profesional de análisis RFM estratégico, visual y accionable para una empresa de retail gastronómico.

