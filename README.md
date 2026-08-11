# Accounting for GPU-Collateralized Debt

**Depreciation, Revenue Recognition, and Off-Balance-Sheet Measurement**

Bryan Gibson · Brandon Hall · Peter Demerjian  

Working paper (*Accounting Horizons* submission format)

---

## Paper index

| Item | Location |
|------|----------|
| **Main paper (PDF)** | [`manuscript/paper.pdf`](manuscript/paper.pdf) |
| **Main paper (Rmd)** | [`manuscript/paper.Rmd`](manuscript/paper.Rmd) |
| **Bibliography** | [`manuscript/chip_loan.bib`](manuscript/chip_loan.bib) |
| **Online appendix (PDF)** | [`online-appendix/online_appendix.pdf`](online-appendix/online_appendix.pdf) |
| **Online appendix (Rmd)** | [`online-appendix/online_appendix.Rmd`](online-appendix/online_appendix.Rmd) |
| **OA figures & data** | [`online-appendix/figures/`](online-appendix/figures/), [`online-appendix/data/`](online-appendix/data/) |
| **Main-paper figures** | [`figures/`](figures/) |
| **Code / checks** | [`code/`](code/) |

---

## Abstract

GPU-collateralized lending has grown from zero to more than $35 billion in three years, and borrowers’ reported performance, revenue, and leverage rest on accounting estimates that observable market data only weakly constrain. Using CoreWeave’s FY2025 10-K, we document three measurement channels: (1) GPU useful lives and depreciation under ASC 360; (2) AMD customer warrants under ASC 606 / ASC 718 (ASU 2025-04); and (3) uncommenced lease obligations under ASC 842.

---

## Online appendix contents

1. Market chronology and accumulation figure  
2. Circular-flow network map of counterparties  
3. Extended facility-level detail  
4. Warrant classification and fair-value technical notes  
5. Fire-sale recovery benchmarks and reduced-form pricing of the short-life state  

---

## Reproduce

```bash
# Main paper
cd manuscript && Rscript -e 'rmarkdown::render("paper.Rmd", output_file = "paper.pdf")'

# Online appendix
cd ../online-appendix && Rscript -e 'rmarkdown::render("online_appendix.Rmd")'
```

Requires R, rmarkdown, XeLaTeX, Times New Roman.

---

## Citation

Gibson, B., Hall, B., & Demerjian, P. (2026). *Accounting for GPU-Collateralized Debt: Depreciation, Revenue Recognition, and Off-Balance-Sheet Measurement*. Working paper.

```bibtex
@unpublished{gibson2026gpu,
  title  = {Accounting for GPU-Collateralized Debt: Depreciation, Revenue Recognition, and Off-Balance-Sheet Measurement},
  author = {Gibson, Bryan and Hall, Brandon and Demerjian, Peter},
  year   = {2026},
  note   = {Working paper}
}
```

---

## License / use

Working paper. Please do not circulate a modified version as the authors’ manuscript. Comments welcome via GitHub Issues.
