# Accounting for GPU-Collateralized Debt

**Depreciation, Revenue Recognition, and Off-Balance-Sheet Measurement**

Bryan Gibson · Brandon Hall · Peter Demerjian  

Working paper (Accounting Horizons submission format)

---

## Paper index

| Item | Location |
|------|----------|
| **PDF (current draft)** | [`manuscript/paper.pdf`](manuscript/paper.pdf) |
| **Source (R Markdown)** | [`manuscript/paper.Rmd`](manuscript/paper.Rmd) |
| **Bibliography** | [`manuscript/chip_loan.bib`](manuscript/chip_loan.bib) |
| **Figures** | [`figures/`](figures/) |
| **Online appendix** | [`online-appendix/`](online-appendix/) |
| **Code / checks** | [`code/`](code/) |

---

## Abstract

GPU-collateralized lending has grown from zero to more than $35 billion in three years, and borrowers’ reported performance, revenue, and leverage rest on accounting estimates that observable market data only weakly constrain. Using CoreWeave’s FY2025 10-K, we document three measurement channels: (1) GPU useful lives and depreciation under ASC 360; (2) AMD customer warrants under ASC 606 / ASC 718 (ASU 2025-04); and (3) uncommenced lease obligations under ASC 842.

---

## Reproduce the PDF

Requires R, rmarkdown, a TeX distribution with XeLaTeX, and Times New Roman.

```bash
cd manuscript
Rscript -e 'rmarkdown::render("paper.Rmd", output_file = "paper.pdf")'
```

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

This is a **working paper**. Please do not circulate a modified version as the authors’ manuscript. Comments welcome via GitHub Issues.

---

## Repository layout

```
GpuPaper/
├── README.md                 ← you are here (index)
├── manuscript/
│   ├── paper.pdf
│   ├── paper.Rmd
│   └── chip_loan.bib
├── figures/
├── online-appendix/
└── code/
```
