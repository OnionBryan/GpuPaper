# GPU Circular Capital Flows — Entity & Relationship Research
Compiled: 2026-02-23 | Last DB/graph fix: 2026-07-28 | Second full web audit: 2026-07-28  
Sources: SEC filings, press releases, tier-1 news  
**Audit receipts (URLs for external challenge):** [`audit_receipts/`](audit_receipts/) — start with `AUDIT_REPORT_2026-07-28.md` and `RECEIPTS_BY_CLAIM.md`

---

## CATEGORY: chipmaker

### Nvidia (NVDA)

#### Equity investments in neoclouds

**CoreWeave — sequential equity (stake ladder)**

| Stage | Date | Amount | Shares / stake | Source | Confidence |
|-------|------|--------|----------------|--------|------------|
| Series B | Apr 2023 | undisclosed | ~1.21% pre-IPO Class A (later S-1 reconstruct) | BusinessWire Apr 18 2023 | confirmed |
| S-1 beneficial ownership | Feb 28 2025 | — | 896,623 Class A = **5.97% of Class A** | S-1 p.197 fn 12 | confirmed |
| IPO + $250M top-up | Mar 2025 | **$0.25B** top-up | **~7% / ~24.2M shares** | 13G; CNBC May 2025 | confirmed |
| Follow-on | Jan 26 2026 | **$2.0B** at $87.20 (~22.9M new shares) | Press often said **~13%** at announcement | Nvidia Newsroom; CNBC; Bloomberg Jan 26 2026 | amount confirmed |
| Post-deal 13G/A | filed around Jan 26 2026 deal | — | **47,213,353 shares = 11.5% Class A** (sole vote/dispositive) | Schedule 13G/A | **confirmed — use this, not ~13%** |
| Later secondary commentary | May 2026 13F recaps | — | Still ~47.2M shares; some outlets say ~11% of company | 13F / press | consistent with 13G/A share count |

- DB rows: three sequential `INVESTS_EQUITY` edges with `valid_to` chain so only the current stake is active for graphing.
- **Authoritative stake after $2B: 11.5% Class A per 13G/A.** Discard unreconciled ~13% and ~8.65% headlines unless a newer 13G supersedes.

**Lambda Labs — Series D (February 19 2025)**
- Round: $480M Series D co-led Andra Capital + SGW, $2.5B valuation; Nvidia participating (amount **undisclosed**)
- Other investors: ARK Invest, In-Q-Tel, Andrej Karpathy, Pegatron, Supermicro, Wistron, Wiwynn, 1517, G Squared, USIT
- Source: Lambda blog Feb 19 2025; CNBC Feb 19 2025
- CONFIDENCE: confirmed; amount undisclosed

**Crusoe Energy — Series D (December 12 2024)**
- Round: $600M led by Founders Fund, $2.8B valuation; Nvidia participating (amount **undisclosed**)
- Other investors: Fidelity, Lowercarbon, Polychain, Winklevoss, DRW, Mubadala, Valor, Ribbit
- Source: Crusoe press release Dec 12 2024; GlobeNewswire
- CONFIDENCE: confirmed; amount undisclosed

**Crusoe Energy — Series E (October 24 2025)**
- Round: $1.375B co-led by Valor Equity Partners + Mubadala Capital, $10B+ valuation; Nvidia participating (amount **undisclosed**); AMD named as strategic partner
- Source: Crusoe press release Oct 24 2025; GlobeNewswire
- CONFIDENCE: confirmed; amount undisclosed

**Nscale — Series B (September 25 2025)**
- Round: $1.1B led by Aker ASA (largest European Series B ever); Nvidia participating (amount **undisclosed**)
- Other investors: Blue Owl, Dell, Fidelity, G Squared, Nokia, Point72, T.Capital, Sandton Capital
- Source: Nscale press release Sep 25 2025; DCD
- CONFIDENCE: confirmed; amount undisclosed

**Nscale — Pre-Series C SAFE (October 1 2025)**
- Round: $433M SAFE; Nvidia participating (amount **undisclosed**) alongside Blue Owl, Dell, Nokia
- Source: Nscale press release Oct 1 2025; Silicon Republic
- CONFIDENCE: confirmed; amount undisclosed

**Nebius Group — December 2 2024**
- Round: $700M private placement (33.3M Class A shares at $21/share); Nvidia **co-led** alongside Accel and Orbis; individual Nvidia tranche **undisclosed**
- Source: TechCrunch Dec 2 2024; Nebius press release; Bloomberg Dec 2 2024
- CONFIDENCE: confirmed; exact Nvidia amount undisclosed

**OpenAI — October 2024 round ($6.6B at $157B valuation)**
- Nvidia invested: reported **~$100M** (first Nvidia equity investment in OpenAI)
- Source: CNBC Oct 2 2024; Bloomberg corroborated
- CONFIDENCE: reported (press); $100M from reporting, not confirmed by Nvidia

**OpenAI — February 2026 (in negotiations)**
- Nvidia in advanced talks to invest **up to $30B** as part of $100B+ round at ~$830B post-money valuation
- Status: **not yet closed** as of Feb 23 2026
- Source: CNBC Feb 19 2026; Bloomberg Jan 31 2026
- CONFIDENCE: reported; deal not closed

**Mistral AI — Series B (June 2024) and Series C (September 2025)**
- Nvidia participated in both; individual amounts **undisclosed**
- Series C: €1.7B led by ASML (11% stake at €1.3B); €11.7B (~$13.6B) total valuation
- Source: CNBC Sep 9 2025; TechStartups Sep 2025
- CONFIDENCE: confirmed (named in both); amounts undisclosed

---

#### Circular / self-dealing transactions

**Lambda Leaseback (September 2025)**
- Direction: Nvidia sells GPUs → Lambda purchases → **Nvidia rents 18,000 GPUs back from Lambda** over 4 years
- Amount: **$1.5B** (4-year contract value); Nvidia becomes Lambda's single largest customer
- Source: DCD Sep 8 2025; Tom's Hardware Sep 2025; RCR Wireless Sep 2025
- CONFIDENCE: confirmed (multiple tier-1 sources; not denied)

**CoreWeave $6.3B Backstop (signed 2023, disclosed September 2025)**
- Structure: Nvidia agreed to purchase any unsold CoreWeave compute capacity through **April 13 2032**, up to cumulative **$6.3B**; Nvidia receives the compute it pays for
- Agreement signed: 2023 (coincides with Nvidia's Series B investment)
- First publicly disclosed: September 2025 (CoreWeave quarterly SEC filing)
- Source: DCD; Motley Fool Sep 19 2025; CoreWeave SEC filing Sep 2025
- CONFIDENCE: confirmed

**Nvidia $860M Lease Guarantee (unnamed partner, Nvidia 10-Q Q3 FY2026)**
- Nvidia guaranteed up to **$860M** in a 5-year facility lease for an unnamed neocloud/datacenter partner
- Partner placed $470M in escrow; Nvidia received **warrants** in exchange; Nvidia has rights to assume or sublease if partner defaults
- Partner identity: **undisclosed**
- Source: DCD ("Nvidia backs $860m lease obligations"); Nvidia Q3 FY2026 10-Q
- CONFIDENCE: confirmed (Nvidia 10-Q); counterparty undisclosed

**Nvidia $3.8B junk-bond datacenter lease (February 12 2026)**
- Vehicle: SV RNO Property Owner 1, backed by Tract Capital's Fleet I fund
- Deal: Fleet I sold $3.8B junk bonds to finance 200MW datacenter (Storey County, NV)
- Nvidia signed **~16-year anchor lease** with two 10-year extensions
- Fleet I contributed ~$620M equity; JP Morgan led bond transaction; Morgan Stanley co-managed
- Source: Bloomberg Feb 12 2026; Business Standard Feb 13 2026
- CONFIDENCE: confirmed (Bloomberg; bond offering documents)

---

### AMD (AMD)

**AMD → Crusoe $300M Goldman Sachs Loan Backstop (February 2026)**
- Structure: Goldman Sachs issues $300M loan to Crusoe; AMD guarantees/backstops; Crusoe buys AMD chips for Ohio datacenter
- Interest rate: ~6%; AMD can book $300M in chip sales upfront; AMD leases back if Crusoe cannot place capacity
- First AMD-chip loan collateralization on record; explicitly described as "mirrors Nvidia strategy"
- Reported: The Information Feb 19 2026; corroborated by DCD, Tom's Hardware, Benzinga
- CONFIDENCE: reported (not yet confirmed via press release from either party)

---

## CATEGORY: neocloud

### CoreWeave (CRWV — IPO March 28 2025 at $40/share)

#### GPU Suppliers
- **Nvidia exclusively.** Full fleet runs Nvidia hardware (H100, H200, GB200/NVL72, GB300). No AMD supply relationship disclosed.

#### Customers (from S-1/10-Q disclosures)
| Customer | Revenue % | Notes | Source |
|----------|-----------|-------|--------|
| Microsoft (Customer A) | 62% of 2024 revenue (~$1.2B); rose to 71% Q2 2025 | Total commitment ~$10B by end of decade | CoreWeave S-1; DCD |
| OpenAI | grew to largest by dollar commitment | $11.9B initial (Mar 2025) + $4B (May 2025) + $6.5B (Sep 2025) = up to **$22.4B** contracted. OpenAI also received **8.75M CoreWeave shares ($350M at IPO price)** as equity component. | CoreWeave IR; CNBC Mar 10 2025 |
| Customer C (unnamed, ~15% 2024 rev) | ~15% | Prevailing analyst view: **Nvidia itself** (consistent with $6.3B backstop / capacity purchase agreement signed 2023) | inferred from S-1 + backstop |
| Mistral AI | undisclosed | confirmed CoreWeave customer since 2023; trained on H100/H200/GB200 NVL72; 2.5× faster with GB200 NVL72 | DCD; CoreWeave blog |
| Other named (no rev amount) | — | Meta, IBM, Cohere, Poolside | various |

#### CoreWeave acquisition of Core Scientific
- CoreWeave announced acquisition of **Core Scientific** (CORZ) in all-stock deal: 0.1235 CRWV shares per CORZ share
- Core Scientific provides ~590MW of datacenter hosting across 6 sites; **~$10.2B in 12-year lease payments** = CoreWeave's largest off-balance-sheet obligation
- Source: Core Scientific press releases 2025
- CONFIDENCE: confirmed

#### Debt facilities — complete inventory
| Facility | Amount | Lead Lender(s) | Participants (named) | Rate | Maturity | Date |
|----------|--------|----------------|---------------------|------|----------|------|
| DDTL 1.0 | $2.3B | Magnetar + Blackstone Tac Ops | Coatue, DigitalBridge Credit, BlackRock, PIMCO, Carlyle | ~15% floating | Mar 2028 | Aug 2023 |
| DDTL 2.0 | $7.5B→$10.6B (via amendments) | Blackstone Tac Ops + Magnetar | Carlyle, CDPQ, DigitalBridge Credit, BlackRock, Eldridge, Great Elm; Blackstone Tac Ops ~$4.5B of the $7.5B | ~11% floating | 5yr per draw | May 2024 |
| DDTL 2.0 5th Amendment | +$3.0B incremental | Same syndicate | — | lower spread | — | Sep 2025 |
| DDTL 3.0 | $2.6B | MUFG (admin agent); Morgan Stanley Asset Funding + MUFG + Goldman Sachs (joint leads) | — | SOFR+400bps | Aug 2030 | Jul 2025 |
| Revolving Credit | $650M→$1.5B→$2.5B | JPMorgan, Goldman Sachs, Morgan Stanley, MUFG | Barclays, Citi, Credit Agricole, Deutsche Bank, Jefferies, Mizuho, SocGen, SMBC, Wells Fargo | — | Nov 2029 | Oct 2024→May 2025→Nov 2025 |
| 9.250% Senior Notes | $2.0B | — | — | 9.25% fixed | Jun 2030 | May 2025 |
| 9.000% Senior Notes | $1.75B | — | — | 9.0% fixed | Feb 2031 | Jul 2025 |
| 1.75% Convertible Notes | $2.25B | Goldman Sachs, Morgan Stanley, JPMorgan, Wells Fargo | — | 1.75% + 25% conv. premium | 2031 | Dec 2025 |
| Blue Owl bridge | $0.5B committed | Blue Owl | — | — | — | 2025 |

Sources: Blackstone PR Aug 2023; Blackstone PR May 2024; CoreWeave IR Oct 2024; Jul 2025; May 2025; Dec 2025

#### Equity investors — complete roster
| Investor | Amount | Stake | Round/Date | Source |
|----------|--------|-------|-----------|--------|
| Magnetar Capital | $0.05B converts (2021) → led $0.111B of $221M (Apr 2023) | **~23–30%** (largest single shareholder, ~91.4M shares as of Q3 2025) | 2021–2025 | PitchBook; Benzinga; MarketScreener |
| Nvidia | undisclosed (Apr 2023) + $0.25B top-up + $2.0B (Jan 2026) | headline **~13%** post Jan 2026; **reconcile vs 13F (~8.65%?)** | Apr 2023; Mar 2025; Jan 2026 | S-1; 13G; Nvidia Newsroom; 13F pending |
| Nat Friedman / Daniel Gross | undisclosed | small | Apr 2023 | TechCrunch |
| Fidelity | led $0.642B secondary (Dec 2023) | **~6.75%** total | Dec 2023; May 2024; Nov 2024 | Fortune Dec 2023 |
| Jane Street | undisclosed | **~5.4%** | Dec 2023; Nov 2024 | Bloomberg Dec 2023; CoreWeave IR |
| JPMorgan Asset Mgmt | undisclosed | — | Dec 2023 | Fortune Dec 2023 |
| OMERS | undisclosed | — | Dec 2023 | Crunchbase |
| Coatue Management | led $1.1B Series C (May 2024) | undisclosed | May 2024; Nov 2024 | PRNewswire May 2024 |
| Altimeter Capital | undisclosed | — | May 2024 | PRNewswire |
| Lykos Global | undisclosed | — | May 2024 | PRNewswire |
| Magnetar Capital | led $0.65B secondary (Nov 2024) | — | Nov 2024 | CoreWeave IR Nov 2024 |
| Macquarie Capital | part of $0.65B secondary | — | Nov 2024 | PR Newswire Nov 2024 |
| Cisco Investments | undisclosed | — | Nov 2024 | CNBC Nov 2024 |
| Pure Storage | undisclosed | — | Nov 2024 | CNBC Nov 2024 |
| BlackRock | undisclosed | — | Nov 2024 | CNBC Nov 2024 |
| Neuberger Berman | undisclosed | — | Nov 2024 | CNBC Nov 2024 |
| OpenAI | $0.35B in stock (received, not cash) | **~2%** est. | Mar 2025 (compute deal) | CoreWeave PR Mar 10 2025 |

Note: OpenAI is simultaneously CoreWeave's largest-dollar customer **and** a CoreWeave equity holder — documented circular ownership.

---

### Lambda Labs (private; hiring investment banks for IPO as of late 2025)

**GPU supplier:** Nvidia exclusively (all infrastructure disclosed; Microsoft deal specifies GB300 NVL72)

**Funding rounds:**
- Series D: $480M, Feb 19 2025, Andra Capital + SGW co-lead, $2.5B valuation. Nvidia, ARK Invest, Andrej Karpathy, In-Q-Tel, Pegatron, Supermicro, Wistron, Wiwynn participated.
- Series E: $1.5B+, Nov 18 2025, TWG Global (Thomas Tull + Mark Walter) + USIT co-lead. Total funding ~$2.3B post-round.

**Lambda leaseback (September 2025):**
Lambda owns 18,000 GPUs → Nvidia rents them back for $1.5B over 4 years. Nvidia = Lambda's **single largest customer**.
Circular: Nvidia manufactures → Lambda purchases (Nvidia recognizes as revenue) → Nvidia rents back.
- Source: DCD Sep 8 2025; Tom's Hardware; RCR Wireless

**Customers:**
- Microsoft: multibillion-dollar multi-year deal (Nov 3 2025); "tens of thousands of Nvidia GB300 NVL72 GPUs"; dollar amount undisclosed
- Nvidia: $1.5B leaseback

---

### Crusoe Energy / Crusoe Cloud

**Funding:**
- Series D: $600M, Dec 12 2024, Founders Fund lead, $2.8B valuation. Nvidia, Fidelity, Lowercarbon, Polychain, Winklevoss, DRW, Mubadala, Valor, Ribbit.
- Series E: $1.375B, Oct 24 2025, Valor Equity Partners + Mubadala Capital co-lead, $10B+ valuation. Nvidia and **AMD named as strategic partner**.

**AMD $300M backstop (February 2026):**
Goldman Sachs arranges $300M loan; AMD backstops it; Crusoe buys AMD chips for Ohio datacenter. AMD leases back if Crusoe cannot place capacity with third parties. ~6% interest rate. First AMD-chip loan collateralization on record.
- Source: The Information Feb 19 2026; DCD; Tom's Hardware

---

### Nscale (private — European)

**Funding:**
- Seed: $30M (Dec 2023)
- Series A: $155M (Dec 2024)
- Series B: $1.1B, Sep 25 2025. Lead: Aker ASA. Participants: Nvidia, Nokia, Blue Owl, Dell, Fidelity, G Squared, Point72, T.Capital, Sandton.
- Pre-Series C SAFE: $433M, Oct 1 2025. Participants: Nvidia, Nokia, Dell, Blue Owl.
- DDTL: $1.4B, Feb 12 2026. Lenders: PIMCO (lead), Blue Owl (lead), LuminArx Capital (lead). Goldman Sachs sole structuring and placement agent. Use: GPU clusters in Norway, Portugal, Iceland, UK. Oversubscribed.

**Customers:** OpenAI Stargate Project (UK and Norway infrastructure). Microsoft (partnership announced).

---

### FluidStack (private — European)

**Note:** No direct Nvidia equity investment confirmed. Nvidia Inception program partnership only (joint announcement on Borealis/Dell GPU cluster, Mar 25 2025).

**Funding:**
- SAFE: $24.7M (2024)
- Series A: $200M, Feb 2025, Cacti PE led
- Equity: $450M, Jan 2026
- Series D talks: ~$700M at $7B valuation, Situational Awareness (Leopold Aschenbrenner fund), late 2025 (not confirmed closed)

**Macquarie GPU debt facility:** Up to **$10B** GPU-collateralized senior debt for European GPU cluster buildout (announced April 2025).
- Source: BusinessWire Apr 1 2025; DCD

**Google → TeraWulf → FluidStack backstop:**
Google backstops FluidStack's lease obligations to TeraWulf (Lake Mariner, NY). Google's total backstop commitment grown to **~$4.5B** across multiple tranches; Google holds **~14% equity** in TeraWulf (received warrants). Contracted revenue to JV ~$9.5B (25-year). TeraWulf/FluidStack JV also issued $1.275B secured notes.
- Source: DCD Aug 2025; CNBC Aug 18 2025; SEC filings from TeraWulf
- CONFIDENCE: confirmed (SEC filings)

---

### Nebius Group (NBIS — NASDAQ)

**Nvidia investment:** co-led $700M round Dec 2024 alongside Accel and Orbis; exact Nvidia tranche undisclosed.

**Business model:** Full-stack AI cloud (Nvidia GPU clusters, developer tools, inference platform). Uses Nvidia hardware exclusively.

**Customers (disclosed):**
- Microsoft: five-year $17.4B AI infrastructure supply agreement (Vineland, NJ datacenter)
- Meta: disclosed customer

**Revenue:** FY2024: $117.5M (+462% YoY); Q2 2025: $105.1M (+625% YoY); Dec 2024 ARR: ~$90M; projected Dec 2025 ARR: $750M–$1B

---

### USD.AI / Sharon AI (ASX: SHAZ)

- $500M non-recourse credit facility from USD.AI (blockchain-based GPU collateral lending protocol)
- $65M initially drawn; announced Jan 22 2026
- No Nvidia equity connection to USD.AI documented
- Source: BusinessWire/Nasdaq PR Jan 22 2026; CoinDesk; The Block
- CONFIDENCE: confirmed

---

## CATEGORY: ai_company

### Microsoft (MSFT)

| Relationship | Amount | Notes | Source |
|-------------|--------|-------|--------|
| CoreWeave customer | ~$1.2B+ annualized (62% of 2024 rev); ~$10B total commitment | Customer A in S-1 | CoreWeave S-1; DCD |
| Lambda customer | multibillion-dollar, multi-year | GB300 NVL72 GPUs | CNBC Nov 3 2025 |
| OpenAI investor | $13B cumulative (11.6B funded as of Sep 2025) | **27% stake** on as-converted basis (post-restructure, Oct 2025) | Microsoft 10-K Oct 2025 |
| Azure GPU buyer | massive; capex $80B+ 2025 | no itemized Nvidia figure | Microsoft guidance |

### OpenAI

| Relationship | Amount | Notes | Source |
|-------------|--------|-------|--------|
| CoreWeave customer | up to $22.4B contracted (3 tranches) | also holds **~2% CoreWeave equity** (8.75M shares / $350M) | CoreWeave IR |
| Microsoft investment (received) | $13B cumulative | 27% stake on as-converted | Microsoft 10-K |
| SoftBank investment (received) | $30B (SoftBank led; ~11% stake) | $40B total round Mar 2025 | CNBC |
| Nvidia investment (received) | ~$0.1B reported (Oct 2024) | $30B talks ongoing (Feb 2026) | CNBC |
| Thrive Holdings investment (made) | undisclosed | OpenAI took equity stake in Thrive Holdings Dec 2025 — circular | TechCrunch Dec 1 2025 |

### Meta (META)

| Relationship | Amount | Notes | Source |
|-------------|--------|-------|--------|
| Nvidia GPU purchases | up to **$50B** multi-year deal | Blackwell + Vera Rubin + Grace CPUs; announced Feb 17 2026 | CNBC Feb 17 2026; Nvidia Newsroom |
| AI capex | $38-40B (2024); $70-72B (2025 actual); $115-135B (2026 guide) | building 2GW datacenter with 1.3M+ Nvidia GPUs | Tom's Hardware |
| CoreWeave customer | not publicly disclosed | — | — |
| Google TPU discussions | ~$1B+/yr potential | Meta + Google in talks; not finalized | The Information |

### Google / Alphabet

| Relationship | Amount | Notes | Source |
|-------------|--------|-------|--------|
| CoreWeave (preliminary talks) | undisclosed | Google in talks to rent CoreWeave datacenter space for its own TPUs | DCD |
| FluidStack backstop | ~$4.5B | via TeraWulf warrants (~14% TeraWulf equity) | DCD; CNBC Aug 2025 |
| TPU external sales | — | Google now sells TPUs to third parties; placed outside Google campuses | multiple |

### Mistral AI

| Relationship | Amount | Notes | Source |
|-------------|--------|-------|--------|
| CoreWeave customer | undisclosed | since 2023; trained on H100/H200/GB200 NVL72; 2.5× speed on GB200 | DCD; CoreWeave blog |
| Nvidia investor (received) | undisclosed | Nvidia in both Series B (Jun 2024) and Series C (Sep 2025) | CNBC |

### xAI (Elon Musk)

| Relationship | Amount | Notes | Source |
|-------------|--------|-------|--------|
| Nvidia GPU purchases | undisclosed dollar | Colossus (Memphis): ~555,000 GPUs as of Feb 15 2026 (H100 + H200 + GB200); plans for 1M+ | DCD; Tom's Hardware; BasenorBlog |
| CoreWeave | not disclosed | no relationship confirmed | — |

---

## CATEGORY: fin_institution

### Blackstone
- **DDTL 1.0 co-lead** ($2.3B, Aug 2023): via Blackstone Tactical Opportunities; exact allocation undisclosed
- **DDTL 2.0 co-lead** ($7.5B, May 2024): Blackstone Tac Ops provided **~$4.5B** of the $7.5B (IFR Awards)
- No equity investments in CoreWeave documented
- Source: Blackstone PRs Aug 2023, May 2024; IFR Awards

### Magnetar Capital
- **2021**: $50M convertible notes → transformed into **~$12.5B position** by late 2025 (~23–30% stake, ~91.4M shares = largest single CoreWeave shareholder)
- **Apr 2023**: led Series B, ~$111M tranche within $221M
- **May 2023**: led Series B extension (+$200M)
- **Aug 2023**: co-led DDTL 1.0 with Blackstone
- **May 2024**: co-led DDTL 2.0 with Blackstone; also participated in Series C
- **Nov 2024**: led $650M secondary
- Source: PitchBook; Benzinga; Yahoo Finance; MarketScreener

### DigitalBridge
- **DDTL 1.0 participant** (Aug 2023): via DigitalBridge Credit; amount undisclosed
- **DDTL 2.0 participant** (May 2024): via DigitalBridge Credit; amount undisclosed
- Source: DigitalBridge PR Aug 2023; Blackstone PR May 2024

### Carlyle
- **DDTL 1.0 participant** (Aug 2023): amount undisclosed
- **DDTL 2.0 participant** (May 2024): amount undisclosed

### PIMCO
- **DDTL 1.0 participant** (Aug 2023)
- **Nscale DDTL co-lead** ($1.4B, Feb 2026)

### Blue Owl
- **CoreWeave bridge**: $500M committed for PA datacenter project (failed to arrange full ~$4B third-party debt, reported Feb 20 2026)
- **Nscale Series B + SAFE equity participant** (Sep/Oct 2025; amounts undisclosed)
- **Nscale DDTL co-lead** ($1.4B, Feb 2026)
- Source: Bloomberg Feb 12 2026; Bisnow; DNYUZ Feb 20 2026

### Goldman Sachs
- **DDTL 3.0 joint lead** ($2.6B, Jul 2025); **Revolving credit joint lead** ($2.5B, Oct 2024+); **Convertible notes joint bookrunner** ($2.25B, Dec 2025); **IPO joint lead bookrunner** (Mar 2025) — all CoreWeave
- **Nscale DDTL sole structuring and placement agent** ($1.4B, Feb 2026)
- **AMD/Crusoe $300M loan arranger** (Feb 2026)
- Source: CoreWeave IR; Nscale PR; Tom's Hardware

### JPMorgan
- **CoreWeave revolving credit joint lead** ($2.5B, Oct 2024+)
- **CoreWeave convertible notes joint bookrunner** ($2.25B, Dec 2025)
- **CoreWeave $642M secondary equity investor** (Dec 2023; JPMorgan Asset Mgmt)
- **CoreWeave IPO joint lead bookrunner** (Mar 2025)
- **Nvidia $3.8B junk bond lead manager** (Feb 2026)
- Source: ABL Advisor; CoreWeave IR; Bloomberg Feb 2026

### Morgan Stanley
- **CoreWeave DDTL 3.0 joint lead** (via Morgan Stanley Asset Funding, $2.6B, Jul 2025)
- **CoreWeave revolving credit joint lead** ($2.5B)
- **CoreWeave convertible notes joint bookrunner** ($2.25B, Dec 2025)
- **CoreWeave IPO joint lead bookrunner** (Mar 2025)
- **Nvidia $3.8B junk bond co-manager** (Feb 2026)
- Source: CoreWeave IRs; Bloomberg Feb 2026

### MUFG
- **CoreWeave DDTL 3.0 admin agent and joint lead** ($2.6B, Jul 2025)
- **CoreWeave revolving credit joint lead** ($2.5B)
- Source: CoreWeave IR Jul 2025

### LuminArx Capital Management
- **Nscale DDTL co-lead** ($1.4B, Feb 2026)
- Source: Nscale PR Feb 2026; Bloomberg Feb 12 2026

### Macquarie Group
- **CoreWeave $650M secondary participant** (Nov 2024)
- **FluidStack European GPU debt facility** up to $10B (Apr 2025)
- Source: CoreWeave IR Nov 2024; BusinessWire Apr 1 2025

---

## CATEGORY: inv_fund

### Coatue Management (Philippe Laffont)
- **CoreWeave Series C lead** ($1.1B, May 2024, $19B valuation)
- **CoreWeave DDTL 1.0 participant** (debt, Aug 2023)
- **CoreWeave DDTL 2.0 participant** (debt, May 2024)
- **CoreWeave $650M secondary participant** (Nov 2024)
- **OpenAI $40B round co-investor** (Mar 2025; amount undisclosed)

### Jane Street
- **CoreWeave $642M secondary** (Dec 2023, $7B valuation): ~5.4% stake; co-investor with Fidelity
- **CoreWeave $650M secondary lead** (Nov 2024, $23B valuation): co-lead with Magnetar and Fidelity

### Fidelity Management & Research
- **CoreWeave $642M secondary lead** (Dec 2023): ~6.75% total stake
- **CoreWeave Series C participant** (May 2024)
- **CoreWeave $650M secondary lead** (Nov 2024)
- **Crusoe Series D participant** (Dec 2024)
- **Nscale Series B participant** (Sep 2025)

### SoftBank
- **OpenAI $40B round** (Mar 31 2025, $300B valuation): led with **$30B**; fully funded by Dec 30 2025; **~11% stake in OpenAI**
- **Nvidia equity**: built stake to ~$3B (Mar 2025); **sold entire position for $5.83B** (Nov 2025; SoftBank Vision Fund full exit)
- **Stargate JV**: SoftBank + OpenAI + Oracle; $500B AI infra JV (Jan 2025); SoftBank leads financing
- Source: CNBC Mar 31 2025; CNBC Nov 11 2025; DCD

### Founders Fund
- **Crusoe Series D lead** ($600M, Dec 2024, $2.8B valuation)

### TWG Global (Thomas Tull + Mark Walter)
- **Lambda Series E lead** ($1.5B+, Nov 2025)

### a16z (Andreessen Horowitz)
- **No direct CoreWeave investment** (partner Casado publicly stated regret at passing)
- **Mistral Series C participant** (Sep 2025; amount undisclosed)
- $1.25B AI infrastructure fund (2024) + $1.7B additional (Jan 2026) = $2.95B dedicated AI infrastructure
- Source: Mercury News Jan 2026

### Thrive Capital
- **OpenAI $6.6B round lead** (Oct 2024): ~$1.2B check; secured option for additional $1B at same valuation (best terms in round)
- **OpenAI $40B round co-investor** (Mar 2025)
- **OpenAI took equity stake in Thrive Holdings** (Dec 1 2025): OpenAI → Thrive → OpenAI circular ownership documented
- Source: BusinessToday Oct 2024; TechCrunch Dec 1 2025

### Tiger Global
- **OpenAI $6.6B round participant** (Oct 2024; amount undisclosed)
- **Crusoe Series E participant** (Oct 2025; amount undisclosed)

### Valor Equity Partners
- **Crusoe Series E co-lead** ($1.375B, Oct 2025)

### Mubadala Capital
- **Crusoe Series D participant** (Dec 2024)
- **Crusoe Series E co-lead** ($1.375B, Oct 2025)

---

## CATEGORY: regulator

| Authority | Action | Date | Scope | Current Status | Source |
|-----------|--------|------|-------|----------------|--------|
| DOJ (US) | Questionnaires → **subpoenas** | Jun 2024 (questionnaires); Sep 3 2024 (subpoenas) | GPU market dominance; bundling GPUs + InfiniBand networking; Run:AI acquisition | Active investigation | Bloomberg Sep 3 2024 |
| EC (EU) | Questionnaires | Dec 6 2024 | Commercial/technical tying of GPUs + InfiniBand; bundling practices | Pre-formal investigation | Reuters Dec 6 2024 |
| France ADLC | **Statement of Objections prepared** | Sep 2023 (raid); Jul 1 2024 (charges) | Anticompetitive GPU market practices; CUDA lock-in; investments in neoclouds as circular concern | First jurisdiction to formally charge Nvidia | Bloomberg/Reuters Jul 1 2024 |
| China SAMR | **Preliminary finding of violation** | Sep 15 2025 | Failure to comply with behavioral conditions from Mellanox $6.9B acquisition (2020); Articles 30–36 Anti-Monopoly Law | Investigation ongoing; no penalty announced | CNBC Sep 15 2025 |

---

## COMPLETE RELATIONSHIP TABLE (machine-readable, for SQL insert)

```
FROM               | TO                 | EDGE_TYPE        | AMOUNT_USD_B       | STAKE_PCT     | DATE              | SOURCE                                    | CONFIDENCE
nvidia             | coreweave          | SUPPLIES_GPUS    | NULL               | NULL          | 2021-01-01        | CoreWeave S-1                             | confirmed
nvidia             | coreweave          | INVESTS_EQUITY   | NULL               | 1.21          | 2023-04-18        | BusinessWire Apr 2023                     | confirmed
nvidia             | coreweave          | INVESTS_EQUITY   | 0.25               | 7.0           | 2025-03-01        | Nvidia 13G SEC filing Mar 2025            | confirmed
nvidia             | coreweave          | INVESTS_EQUITY   | 2.0                | 11.5          | 2026-01-26        | Nvidia Newsroom; Schedule 13G/A 11.5%     | confirmed
nvidia             | coreweave          | BACKSTOP         | 6.3                | NULL          | 2023-04-13        | CoreWeave SEC filing Sep 2025             | confirmed
nvidia             | lambda_labs        | INVESTS_EQUITY   | NULL               | NULL          | 2025-02-19        | Lambda blog Feb 2025                      | confirmed
lambda_labs        | nvidia             | LEASEBACK        | 1.5                | NULL          | 2025-09-08        | DCD Sep 2025; Tom's Hardware              | confirmed
nvidia             | lambda_labs        | BUYS_COMPUTE     | 1.5                | NULL          | 2025-09-08        | DCD Sep 2025 (leaseback = compute rental) | confirmed
nvidia             | crusoe             | INVESTS_EQUITY   | NULL               | NULL          | 2024-12-12        | Crusoe PR Dec 2024                        | confirmed
nvidia             | crusoe             | INVESTS_EQUITY   | NULL               | NULL          | 2025-10-24        | Crusoe PR Oct 2025                        | confirmed
nvidia             | nscale             | INVESTS_EQUITY   | NULL               | NULL          | 2025-09-25        | Nscale PR Sep 2025                        | confirmed
nvidia             | nscale             | INVESTS_EQUITY   | NULL               | NULL          | 2025-10-01        | Nscale SAFE PR Oct 2025                   | confirmed
nvidia             | nscale             | INVESTS_EQUITY   | NULL               | NULL          | 2026-03-09        | Nscale Series C PR ($2B @ $14.6B val)     | confirmed
nvidia             | nebius             | INVESTS_EQUITY   | NULL               | NULL          | 2024-12-02        | Nebius PR Dec 2024                        | confirmed
nvidia             | nebius             | INVESTS_EQUITY   | 2.0                | 9.3           | 2026-03-11        | Nvidia PR; 13G Jul 2026                   | confirmed
nvidia             | openai             | INVESTS_EQUITY   | 0.1                | NULL          | 2024-10-02        | CNBC Oct 2024 (reported; not Nvidia-confirmed) | reported
nvidia             | openai             | INVESTS_EQUITY   | 30.0               | NULL          | 2026-02-27        | OpenAI PR; round closed 2026-03-31        | confirmed
nvidia             | openai             | SUPPLIES_GPUS    | NULL               | NULL          | 2026-02-27        | OpenAI PR (3+2 GW Vera Rubin)             | confirmed
nvidia             | openai             | BACKSTOP         | 250.0              | NULL          | 2026-07-26        | WSJ/Reuters Ohio talks only               | reported
nvidia             | openai             | LENDS_DEBT       | 350.0              | NULL          | 2026-07-26        | WSJ/Reuters chip financing talks          | reported
nvidia             | hut8               | BUYS_COMPUTE     | 19.6               | NULL          | 2026-05-06        | Hut 8 PR economics; FT names Nvidia       | reported
nvidia             | naver              | INVESTS_EQUITY   | 1.0                | 4.5           | 2026-07-24        | Nvidia PR; Naver filing                   | confirmed
amd                | anthropic          | INVESTS_EQUITY   | 5.0                | NULL          | 2026-07-22        | AMD IR (up to $5B ceiling)                | confirmed
amd                | anthropic          | SUPPLIES_GPUS    | NULL               | NULL          | 2026-07-22        | AMD IR (up to 2 GW MI450)                 | confirmed
amd                | core_scientific    | BUYS_COMPUTE     | 14.0               | NULL          | 2026-07-27        | CORZ 8-K (~530 MW firm)                   | confirmed
amd                | core_scientific    | INVESTS_EQUITY   | NULL               | 1.3           | 2026-07-27        | CORZ warrants ~6.5M vested                | confirmed
nvidia             | mistral            | INVESTS_EQUITY   | NULL               | NULL          | 2024-06-01        | CNBC Sep 2025                             | confirmed
nvidia             | mistral            | INVESTS_EQUITY   | NULL               | NULL          | 2025-09-09        | CNBC Sep 9 2025                           | confirmed
nvidia             | undisclosed_dc     | GUARANTEES_DEBT  | 0.86               | NULL          | 2025-10-01        | Nvidia Q3 FY2026 10-Q                     | confirmed
nvidia             | fleet1_tract       | BUYS_COMPUTE     | NULL               | NULL          | 2026-02-12        | Bloomberg Feb 12 2026 (16yr lease)        | confirmed
amd                | crusoe             | GUARANTEES_DEBT  | 0.3                | NULL          | 2026-02-19        | The Information Feb 2026; DCD             | reported
goldman_sachs      | crusoe             | LENDS_DEBT       | 0.3                | NULL          | 2026-02-19        | Tom's Hardware Feb 2026                   | reported
coreweave          | nvidia             | BUYS_COMPUTE     | NULL               | NULL          | 2021-01-01        | S-1 (GPU supplier)                        | confirmed
coreweave          | core_scientific    | LENDS_DEBT       | 10.2               | NULL          | 2024-01-01        | Core Scientific IR (12yr lease pmt)       | confirmed
microsoft          | coreweave          | BUYS_COMPUTE     | 1.2                | NULL          | 2022-01-01        | CoreWeave S-1 (62% of FY2024 rev)         | confirmed
openai             | coreweave          | BUYS_COMPUTE     | 22.4               | NULL          | 2025-03-10        | CoreWeave IR Mar/May/Sep 2025             | confirmed
openai             | coreweave          | INVESTS_EQUITY   | 0.35               | 2.0           | 2025-03-10        | CoreWeave PR Mar 10 2025 (shares received)| confirmed
mistral            | coreweave          | BUYS_COMPUTE     | NULL               | NULL          | 2023-01-01        | DCD; CoreWeave blog                       | confirmed
microsoft          | lambda_labs        | BUYS_COMPUTE     | NULL               | NULL          | 2025-11-03        | Lambda blog Nov 3 2025                    | confirmed
microsoft          | openai             | INVESTS_EQUITY   | 13.0               | 27.0          | 2019-01-01        | Microsoft 10-K Oct 2025                   | confirmed
softbank           | openai             | INVESTS_EQUITY   | 30.0               | 11.0          | 2025-03-31        | CNBC Mar 2025; CNBC Dec 2025              | confirmed
openai             | thrive_holdings    | INVESTS_EQUITY   | NULL               | NULL          | 2025-12-01        | TechCrunch Dec 1 2025                     | confirmed
thrive_capital     | openai             | INVESTS_EQUITY   | 1.2                | NULL          | 2024-10-02        | TechCrunch / BusinessToday Oct 2024       | confirmed
meta               | nvidia             | BUYS_COMPUTE     | 50.0               | NULL          | 2026-02-17        | CNBC Feb 17 2026; Nvidia Newsroom         | confirmed
xai                | nvidia             | BUYS_COMPUTE     | NULL               | NULL          | 2024-07-22        | DCD; Tom's Hardware                       | confirmed
magnetar           | coreweave          | LENDS_DEBT       | 0.05               | NULL          | 2021-01-01        | PitchBook; Benzinga (conv notes)          | confirmed
magnetar           | coreweave          | INVESTS_EQUITY   | 0.111              | 23.0          | 2023-04-18        | MarketScreener; BusinessWire              | confirmed
magnetar           | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2023-08-01        | Blackstone PR Aug 2023                    | confirmed
magnetar           | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2024-05-17        | Blackstone PR May 2024                    | confirmed
blackstone         | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2023-08-01        | Blackstone PR Aug 2023                    | confirmed
blackstone         | coreweave          | LENDS_DEBT       | 4.5                | NULL          | 2024-05-17        | IFR Awards (Tac Ops ~$4.5B of $7.5B)     | reported
digitalbridge      | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2023-08-01        | DigitalBridge PR Aug 2023                 | confirmed
digitalbridge      | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2024-05-17        | Blackstone PR May 2024                    | confirmed
carlyle            | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2023-08-01        | Blackstone PR Aug 2023                    | confirmed
carlyle            | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2024-05-17        | Blackstone PR May 2024                    | confirmed
pimco              | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2023-08-01        | Blackstone PR Aug 2023                    | confirmed
blackrock          | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2023-08-01        | Blackstone PR Aug 2023                    | confirmed
blackrock          | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2024-05-17        | Blackstone PR May 2024                    | confirmed
cdpq               | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2024-05-17        | Blackstone PR May 2024                    | confirmed
blue_owl           | coreweave          | LENDS_DEBT       | 0.5                | NULL          | 2025-01-01        | Bisnow; DNYUZ (bridge commitment)         | confirmed
pimco              | nscale             | LENDS_DEBT       | NULL               | NULL          | 2026-02-12        | Nscale PR Feb 12 2026                     | confirmed
blue_owl           | nscale             | LENDS_DEBT       | NULL               | NULL          | 2026-02-12        | Bloomberg Feb 12 2026                     | confirmed
luminArx           | nscale             | LENDS_DEBT       | NULL               | NULL          | 2026-02-12        | Nscale PR Feb 12 2026                     | confirmed
goldman_sachs      | nscale             | ARRANGES_DEBT    | 1.4                | NULL          | 2026-02-12        | Nscale PR Feb 2026                        | confirmed
goldman_sachs      | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2025-07-31        | CoreWeave IR Jul 2025                     | confirmed
goldman_sachs      | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2025-12-01        | BusinessWire Dec 2025 (converts)          | confirmed
morgan_stanley     | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2025-07-31        | CoreWeave IR Jul 2025                     | confirmed
morgan_stanley     | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2025-12-01        | BusinessWire Dec 2025                     | confirmed
jpmorgan           | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2024-10-01        | CoreWeave IR Oct 2024                     | confirmed
jpmorgan           | coreweave          | INVESTS_EQUITY   | NULL               | NULL          | 2023-12-01        | Fortune Dec 2023 (JPM Asset Mgmt)         | confirmed
mufg               | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2025-07-31        | CoreWeave IR Jul 2025                     | confirmed
coatue             | coreweave          | INVESTS_EQUITY   | 1.1                | NULL          | 2024-05-01        | PRNewswire May 2024 (led Series C)        | confirmed
coatue             | coreweave          | LENDS_DEBT       | NULL               | NULL          | 2023-08-01        | Blackstone PR Aug 2023 (participant)      | confirmed
coatue             | openai             | INVESTS_EQUITY   | NULL               | NULL          | 2025-03-31        | CNBC Mar 2025                             | confirmed
jane_street        | coreweave          | INVESTS_EQUITY   | NULL               | 5.4           | 2023-12-01        | Bloomberg Dec 2023                        | confirmed
jane_street        | coreweave          | INVESTS_EQUITY   | NULL               | 5.4           | 2024-11-13        | CoreWeave IR Nov 2024                     | confirmed
fidelity           | coreweave          | INVESTS_EQUITY   | NULL               | 6.75          | 2023-12-01        | Fortune Dec 2023                          | confirmed
fidelity           | coreweave          | INVESTS_EQUITY   | NULL               | 6.75          | 2024-05-01        | PRNewswire Series C                       | confirmed
fidelity           | coreweave          | INVESTS_EQUITY   | NULL               | 6.75          | 2024-11-13        | CoreWeave IR Nov 2024                     | confirmed
fidelity           | crusoe             | INVESTS_EQUITY   | NULL               | NULL          | 2024-12-12        | Crusoe PR Dec 2024                        | confirmed
fidelity           | nscale             | INVESTS_EQUITY   | NULL               | NULL          | 2025-09-25        | Nscale PR Sep 2025                        | confirmed
macquarie          | coreweave          | INVESTS_EQUITY   | NULL               | NULL          | 2024-11-13        | CoreWeave IR Nov 2024                     | confirmed
macquarie          | fluidstack         | LENDS_DEBT       | 10.0               | NULL          | 2025-04-01        | BusinessWire Apr 2025 (up to $10B)        | confirmed
google             | terawulf           | INVESTS_EQUITY   | NULL               | 14.0          | 2025-08-01        | CNBC Aug 18 2025; TeraWulf SEC filings    | confirmed
google             | fluidstack         | BACKSTOP         | 4.5                | NULL          | 2025-08-01        | DCD Aug 2025 (via TeraWulf arrangement)   | confirmed
aker               | nscale             | INVESTS_EQUITY   | NULL               | NULL          | 2025-09-25        | Nscale PR Sep 2025                        | confirmed
nokia              | nscale             | INVESTS_EQUITY   | NULL               | NULL          | 2025-09-25        | Nscale PR Sep 2025                        | confirmed
blue_owl           | nscale             | INVESTS_EQUITY   | NULL               | NULL          | 2025-09-25        | Nscale PR Sep 2025                        | confirmed
founders_fund      | crusoe             | INVESTS_EQUITY   | NULL               | NULL          | 2024-12-12        | Crusoe PR Dec 2024                        | confirmed
valor              | crusoe             | INVESTS_EQUITY   | NULL               | NULL          | 2025-10-24        | Crusoe PR Oct 2025                        | confirmed
mubadala           | crusoe             | INVESTS_EQUITY   | NULL               | NULL          | 2025-10-24        | Crusoe PR Oct 2025                        | confirmed
accel              | nebius             | INVESTS_EQUITY   | NULL               | NULL          | 2024-12-02        | TechCrunch Dec 2024                       | confirmed
softbank           | nvidia             | INVESTS_EQUITY   | 3.0                | NULL          | 2025-03-01        | DCD Mar 2025                              | confirmed
tiger_global       | openai             | INVESTS_EQUITY   | NULL               | NULL          | 2024-10-02        | CNBC Oct 2024                             | confirmed
tiger_global       | crusoe             | INVESTS_EQUITY   | NULL               | NULL          | 2025-10-24        | Crusoe PR Oct 2025                        | confirmed
doj                | nvidia             | INVESTIGATES     | NULL               | NULL          | 2024-09-03        | Bloomberg Sep 3 2024                      | confirmed
ec                 | nvidia             | INVESTIGATES     | NULL               | NULL          | 2024-12-06        | Reuters Dec 6 2024                        | confirmed
france_adlc        | nvidia             | INVESTIGATES     | NULL               | NULL          | 2024-07-01        | Bloomberg/Reuters Jul 1 2024              | confirmed
china_samr         | nvidia             | INVESTIGATES     | NULL               | NULL          | 2025-09-15        | CNBC Sep 15 2025                          | confirmed
```

---

## KEY DATA GAPS

1. **Individual creditor allocations** within syndicated facilities (DDTL 1.0/2.0) not disclosed; only Blackstone Tac Ops ~$4.5B of the $7.5B reported via IFR Awards
2. **Nvidia exact equity tranche** in Lambda, Crusoe, Nscale, Nebius — all undisclosed
3. **CoreWeave Customer C identity** (~15% 2024 revenue) — inferred as Nvidia from backstop structure; not confirmed
4. **Nvidia $860M guarantee counterparty** — unnamed in 10-Q
5. **AMD $300M Crusoe backstop** — reported by The Information; no press release yet
6. **Nvidia $30B OpenAI deal** — **CLOSED** post-cutoff (announced 2026-02-27; round closed 2026-03-31). DB updated.
7. **FluidStack Nvidia equity investment** — Inception program partnership only; no equity check confirmed
8. **Nebius individual investor amounts** within $700M round (including Nvidia's exact tranche) — **$2B Mar 2026 + 9.3% 13G now loaded**
9. **Nvidia–CoreWeave post-$2B stake %** — **resolved: 11.5% Class A per Schedule 13G/A** (47,213,353 sh)
10. **Nvidia Ohio $250B/$350B** — talks only as of Jul 28 2026; loaded as `reported`
11. **Hut 8 Beacon Point tenant** — economics confirmed; Nvidia identity reported only

---

## POST-CUTOFF UPDATE (Feb 23 2026 → Jul 28 2026)

*Parallel agent research completed 2026-07-28. Confirmed rows loaded to DB; talks/ceilings flagged.*

### Materialized fixes (2026-07-28)

1. **DB**: sequential Nvidia–CoreWeave `INVESTS_EQUITY` with `valid_to` chain; current stake **11.5% Class A** (47,213,353 sh, Schedule 13G/A) — not ~13% press or ~8.65% audit guess.
2. **R graph**: edge width `log1p(amount_usd_b)`; subtitle matches code; **excludes reported talks ≥$100B** (Ohio $250B/$350B stay in DB, off graph).
3. **Post-cutoff edges** inserted (see table below).
4. **AMD book completeness**: OpenAI + Meta 6 GW `SUPPLIES_GPUS` and reverse **160M-share warrants** (`INVESTS_EQUITY`, up to ~10%).
5. **Hut 8 Beacon Point**: amounts primary-confirmed; **tenant=Nvidia remains `reported`** (FT/Reuters secondary only; Hut 8 PR still says confidential IG tenant).
6. **Core Scientific** re-categorized **`neocloud`** (AI hosting/colocation); notes no longer claim CoreWeave acquisition.

### Verified post-cutoff edges (loaded)

| Edge | Type | Amount | Stake | Date | Confidence | Notes |
|------|------|--------|-------|------|------------|-------|
| Nvidia → OpenAI | INVESTS_EQUITY | **$30B** | n/d (~3–4% est.) | 2026-02-27 (round close 03-31) | **confirmed** | Part of $110B announce → $122B committed / $852B post. Replaces stalled $100B LOI. |
| Nvidia → OpenAI | SUPPLIES_GPUS | — | — | 2026-02-27 | **confirmed** | 3 GW inference + 2 GW training Vera Rubin |
| SoftBank → OpenAI | INVESTS_EQUITY | **$30B** | ~13% cumulative | 2026-02-27 | **confirmed** | $20B cash by Jul; third $10B planned Oct 2026 |
| SoftBank / OpenAI → SB Energy | INVESTS_EQUITY | $0.5B each | — | 2026-01-09 | **confirmed** | Circular: OpenAI owns equity in landlord |
| OpenAI → SB Energy | BUYS_COMPUTE | — | — | 2026-01-09 | **confirmed** | 1.2 GW Milam County TX lease |
| Nvidia → OpenAI | BACKSTOP | **$250B** | — | 2026-07-26 | **reported** | Ohio ~10 GW lease/debt guarantee **talks only** |
| Nvidia → OpenAI | LENDS_DEBT | **$350B** | — | 2026-07-26 | **reported** | Chip-purchase financing **talks only** (separate) |
| Nvidia → Nebius | INVESTS_EQUITY | **$2.0B** | **9.3%** | 2026-03-11 | **confirmed** | 13G Jul 2026: shares + pre-funded warrant |
| Nvidia → Nscale | INVESTS_EQUITY | undisclosed | — | 2026-03-09 | **confirmed** | Series C $2B @ $14.6B val participant; **not** a DDTL lender |
| Nvidia → Hut 8 | BUYS_COMPUTE | **$19.6B** base (≤$50.2B) | — | 2026-05-06 | **reported** | Economics + DSX **primary** (Hut 8 PR). Tenant=Nvidia: **FT + Reuters (FT) secondary only** — Hut 8 still says confidential IG. Not upgraded to confirmed. |
| AMD → OpenAI | SUPPLIES_GPUS | ≤6 GW | — | 2025-10-06 | **confirmed** | Binding first 1 GW MI450 2H 2026; full 6 GW ceiling |
| OpenAI → AMD | INVESTS_EQUITY | warrant | up to ~10% | 2025-10-05 | **confirmed** | 160M shares @ $0.01; GW + price milestones (AMD 8-K) |
| AMD → Meta | SUPPLIES_GPUS | ≤6 GW | — | 2026-02-24 | **confirmed** | First 1 GW H2 2026; ~$60B TCV is secondary (not in amount field) |
| Meta → AMD | INVESTS_EQUITY | warrant | up to ~10% | 2026-02-23 | **confirmed** | 160M shares @ $0.01; same warrant template (AMD 8-K) |
| Nvidia → Naver | INVESTS_EQUITY | **~$1.0B** | **~4.5%** | 2026-07-24 | **confirmed** | 7.2M shares @ 204,500 KRW; close conditions + Brookfield ≤$9B |
| AMD → Anthropic | INVESTS_EQUITY | **≤$5B** | n/d | 2026-07-22 | **confirmed** | Ceiling, milestone-tied, “in the future” |
| AMD → Anthropic | SUPPLIES_GPUS | ≤2 GW MI450 | — | 2026-07-22 | **confirmed** | First GW H1 2027 |
| AMD → Core Scientific | BUYS_COMPUTE | **~$14B** pot. rev | — | 2026-07-27 | **confirmed** | ~530 MW firm; +1.9 GW reservation → “2.5 GW” headline |
| AMD → Core Scientific | INVESTS_EQUITY | warrants | ~1.3% vested | 2026-07-27 | **confirmed** | Up to 30M CORZ @ $23.47 |
| AMD → Core Scientific | BACKSTOP | n/d | — | 2026-07-27 | **confirmed** | CSA on Neocloud 152 MW |
| SK Hynix → Nvidia | SUPPLIES_CHIPS | LOI umbrella | — | 2026-07-25 | **confirmed** | HBM co-dev + offtake; **not equity**; $500B/$750B are LOI packages not pure HBM NPV |
| Nvidia → SK Telecom | SUPPLIES_GPUS | ≤2 GW LOI | — | 2026-07-25 | **confirmed** | Vera Rubin DSX AI factory |
| Samsung → Broadcom | SUPPLIES_CHIPS | **~$200B** MOU | — | 2026-07-25 | **confirmed** | Memory + foundry MOU estimate through 2030 |

### Rejected / not loaded as closed

| Claim | Verdict |
|-------|---------|
| Nvidia–OpenAI **$100B** equity LOI | Superseded by $30B; never closed |
| Lambda additional Comet-scale rent-backs | **No evidence** Jan–Jul 2026 |
| Nvidia as Nscale **debt** participant | **False** — PIMCO/Blue Owl/LuminArx lend |
| CoreWeave stake **~13%** or **~8.65%** | Use **11.5% Class A** (13G/A) |
| SK Hynix **equity** from Nvidia | Explicitly **not investment** (Seoul briefing) |
| Hut 8 tenant = Nvidia | **Still reported** — Hut 8 PR: confidential high-IG; FT (5 sources) + Reuters 2026-07-28; no Hut 8/Nvidia primary naming |
| Graph display of Ohio $250B/$350B | **Excluded from graph** (still in DB as reported talks) |
### Note on Google multi-tranche BACKSTOPs

DB sum of Google BACKSTOP edges (FluidStack $1.3B + Cipher $1.73B + Hut 8 $7.0B) = **$10.03B**, above older research aggregate ~$4.5B. Prefer tranche-level DB rows over a single headline aggregate.

### Circular pattern extension (post-cutoff)

The same structure scaled: **chipmaker equity + GPU supply (+ optional residual-demand backstop) → AI lab / neocloud capacity → more GPU purchases → revenue and sometimes equity back to chipmaker.** AMD now mirrors Nvidia with Anthropic cash equity + Core Scientific landlord warrants; SoftBank sits on both OpenAI equity and SB Energy landlord sides; upstream HBM offtake LOIs (SK Hynix, Samsung–Broadcom) lock multi-year memory supply without equity stakes.
