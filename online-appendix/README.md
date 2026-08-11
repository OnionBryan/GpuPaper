# Online Appendix

Companion to Gibson, Hall, and Demerjian (2026), *Accounting for GPU-Collateralized Debt*.

| File | Description |
|------|-------------|
| **[online_appendix.pdf](online_appendix.pdf)** | Knitted online appendix (10 pp.) |
| [online_appendix.Rmd](online_appendix.Rmd) | Source |
| [chip_loan.bib](chip_loan.bib) | Bibliography |
| [figures/](figures/) | Circular-flow and related figures |
| [data/](data/) | Network build scripts, schema, fire-sale framework notes |

## Contents

1. **Market chronology and accumulation** — deal history + waterfall figure  
2. **Circular-flow network** — simplified chain + full network map  
3. **Extended facility-level detail** — sector facility table beyond main-paper Table 1  
4. **Warrant technical notes** — liability vs equity, intrinsic vs option value, measurement date  
5. **Fire-sale recovery and short-life pricing** — aircraft comparison + reduced-form $\Delta s = p \times L$

Main-paper **Appendix A** (ROIC / WACC / lease PV) stays in the main manuscript and is not duplicated here.

## Knit

```bash
cd online-appendix
Rscript -e 'rmarkdown::render("online_appendix.Rmd")'
```
