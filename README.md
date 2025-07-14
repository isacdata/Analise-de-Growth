# 📈 Growth Analytics – Análise de Funil e Conversão

Este projeto analisa o comportamento de usuários ao longo do funil de aquisição e conversão, com foco em identificar padrões de engajamento, churn e performance por canal e plano de assinatura.

---

## 🎯 Objetivo

Investigar como os usuários percorrem o funil desde a visita inicial até a conversão paga, segmentando por canal, tempo de conversão, país e tipo de plano.

---

## 🧪 Métodos

- SQL com `CTE`, `JOIN`, `CASE`, `COUNT`, `DISTINCT` e agregações aplicadas a:
  - Conversão direta vs. após 30min (`Free_and_conversions.sql`)
  - Segmentação por canal (`Funnel.sql`)
  - Cohortes (`Waterfall.sql`)
  - Receita por país e período (`Paid_by_country.sql`, `Paid_per_date.sql`)
- Python (`Waterfall.py`) para classificar usuários como novos, convertidos, ressuscitados ou churnados, com base em datas de eventos
- Dashboard final em **Tableau**, com seções para:
  - Funil completo de conversão
  - Distribuição por canal e país
  - Painel de cohortes e receita recorrente

---

## 📊 Resultados

- Identificou-se que **+65% dos usuários pagantes** converteram após 30 minutos
- **Churn mais alto** em canais pagos do que orgânicos
- Tráfego direto apresentou maior LTV e menor abandono
- Framework modular para SaaS e negócios recorrentes

---

## 🗂️ Estrutura

```
Analise-de-Growth/
├── CSV's/
├── Sql Scripts/
│   ├── Free_and_conversions.sql
│   ├── Funnel.sql
│   ├── Paid_by_country.sql
│   ├── Paid_per_date.sql
│   ├── Sessions_by_country.sql
│   ├── Visitors.sql
│   └── Waterfall.sql
├── Python Scripts/
│   └── Waterfall.py
├── Tableau Workbook/
│   ├── Dashboard.twb
│   └── Dashboard.twbx
└── README.md

---

## 👤 Autor

Desenvolvido por **Isac Vieira** com foco em dados aplicados a produtos, growth e retenção de usuários.
