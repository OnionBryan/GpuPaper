"""
build_circular_flow_db.py
Build, seed, and test the GPU circular capital flows SQLite database.
Usage: python build_circular_flow_db.py
"""

import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), "circular_flow.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "circular_flow_schema.sql")


# =============================================================================
# ENTITY DATA
# =============================================================================

ENTITIES = [
    # (id, name, category_id, ticker, hq, founded, notes)
    # --- chipmakers ---
    ("nvidia",          "NVIDIA Corporation",           "chipmaker",       "NVDA",  "Santa Clara, CA",    1993, None),
    ("amd",             "Advanced Micro Devices",       "chipmaker",       "AMD",   "Santa Clara, CA",    1969, None),

    # --- neoclouds ---
    ("coreweave",       "CoreWeave",                    "neocloud",        "CRWV",  "Roseland, NJ",       2017, "IPO Mar 28 2025 at $40/share"),
    ("lambda_labs",     "Lambda Labs",                  "neocloud",        None,    "San Jose, CA",       2012, "IPO preparation ongoing late 2025"),
    ("crusoe",          "Crusoe Energy Systems",        "neocloud",        None,    "San Francisco, CA",  2018, "Also known as Crusoe Cloud post-pivot"),
    ("nscale",          "Nscale",                       "neocloud",        None,    "London, UK",         2022, "Largest European Series B ($1.1B Sep 2025)"),
    ("fluidstack",      "FluidStack",                   "neocloud",        None,    "London, UK",         2019, None),
    ("nebius",          "Nebius Group",                 "neocloud",        "NBIS",  "Amsterdam, NL",      2024, "Formerly Yandex Cloud international; NASDAQ listed"),
    ("sharon_ai",       "Sharon AI",                    "neocloud",        "SHAZ",  "Australia",          2023, "ASX listed; USD.AI $500M facility"),

    # --- ai companies ---
    ("openai",          "OpenAI",                       "ai_company",      None,    "San Francisco, CA",  2015, "$300B valuation (Mar 2025 round)"),
    ("mistral",         "Mistral AI",                   "ai_company",      None,    "Paris, France",      2023, "€11.7B valuation (Sep 2025 Series C)"),
    ("xai",             "xAI",                          "ai_company",      None,    "Memphis, TN",        2023, "Elon Musk; Colossus ~555k GPUs"),

    # --- hyperscalers ---
    ("microsoft",       "Microsoft Corporation",        "hyperscaler",     "MSFT",  "Redmond, WA",        1975, None),
    ("meta",            "Meta Platforms",               "hyperscaler",     "META",  "Menlo Park, CA",     2004, None),
    ("google",          "Alphabet / Google",            "hyperscaler",     "GOOGL", "Mountain View, CA",  1998, None),

    # --- financial institutions ---
    ("blackstone",      "Blackstone",                   "fin_institution", "BX",    "New York, NY",       1985, "CoreWeave debt via Blackstone Tactical Opportunities"),
    ("magnetar",        "Magnetar Capital",             "fin_institution", None,    "Evanston, IL",       1996, "Dual role: lender + largest CoreWeave equity holder (~23-30%)"),
    ("digitalbridge",   "DigitalBridge",                "fin_institution", "DBRG",  "Boca Raton, FL",     1994, None),
    ("carlyle",         "Carlyle Group",                "fin_institution", "CG",    "Washington, DC",     1987, None),
    ("pimco",           "PIMCO",                        "fin_institution", None,    "Newport Beach, CA",  1971, None),
    ("blackrock",       "BlackRock",                    "fin_institution", "BLK",   "New York, NY",       1988, None),
    ("blue_owl",        "Blue Owl Capital",             "fin_institution", "OWL",   "New York, NY",       2016, None),
    ("goldman_sachs",   "Goldman Sachs",                "fin_institution", "GS",    "New York, NY",       1869, None),
    ("jpmorgan",        "JPMorgan Chase",               "fin_institution", "JPM",   "New York, NY",       1799, None),
    ("morgan_stanley",  "Morgan Stanley",               "fin_institution", "MS",    "New York, NY",       1935, None),
    ("mufg",            "MUFG Bank",                    "fin_institution", None,    "Tokyo, Japan",       1919, None),
    ("macquarie",       "Macquarie Group",              "fin_institution", "MQG",   "Sydney, Australia",  1969, None),
    ("luminArx",        "LuminArx Capital Management",  "fin_institution", None,    "New York, NY",       2021, None),
    ("cdpq",            "CDPQ",                         "fin_institution", None,    "Montreal, Canada",   1965, "Caisse de dépôt et placement du Québec"),
    ("usdai",           "USD.AI",                       "fin_institution", None,    "Decentralized",      2024, "On-chain GPU-collateral lending protocol"),
    ("terawulf",        "TeraWulf",                     "fin_institution", "WULF",  "Easton, MD",         2021, "Former Bitcoin miner; pivoted to AI hosting"),

    # --- investment funds ---
    ("coatue",          "Coatue Management",            "inv_fund",        None,    "New York, NY",       1999, "Philippe Laffont; led CoreWeave Series C"),
    ("jane_street",     "Jane Street Capital",          "inv_fund",        None,    "New York, NY",       2000, None),
    ("fidelity",        "Fidelity Management & Research","inv_fund",       None,    "Boston, MA",         1946, None),
    ("softbank",        "SoftBank Group",               "inv_fund",        "9984",  "Tokyo, Japan",       1981, "Sold entire Nvidia stake Nov 2025 ($5.83B)"),
    ("founders_fund",   "Founders Fund",                "inv_fund",        None,    "San Francisco, CA",  2005, None),
    ("a16z",            "Andreessen Horowitz",          "inv_fund",        None,    "Menlo Park, CA",     2009, "Passed on CoreWeave; regrets noted"),
    ("tiger_global",    "Tiger Global Management",      "inv_fund",        None,    "New York, NY",       2001, None),
    ("thrive_capital",  "Thrive Capital",               "inv_fund",        None,    "New York, NY",       2009, "Led OpenAI Oct 2024 round; OpenAI later invested in Thrive Holdings"),
    ("accel",           "Accel",                        "inv_fund",        None,    "Palo Alto, CA",      1983, None),
    ("valor",           "Valor Equity Partners",        "inv_fund",        None,    "Chicago, IL",        2001, None),
    ("mubadala",        "Mubadala Capital",             "inv_fund",        None,    "Abu Dhabi, UAE",     2002, None),
    ("twg_global",      "TWG Global",                   "inv_fund",        None,    "Los Angeles, CA",    2023, "Thomas Tull + Mark Walter; led Lambda Series E"),
    ("aker",            "Aker ASA",                     "inv_fund",        "AKER",  "Oslo, Norway",       1996, "Led Nscale $1.1B Series B"),
    ("nokia",           "Nokia Corporation",            "inv_fund",        "NOK",   "Espoo, Finland",     1865, None),
    ("core_scientific", "Core Scientific",              "neocloud",        "CORZ",  "Austin, TX",         2017, "Bitcoin miner → AI hosting/colocation; CoreWeave acquisition abandoned; AMD capacity+warrants Jul 2026"),

    # --- regulators ---
    ("doj",             "US Department of Justice",     "regulator",       None,    "Washington, DC",     1870, None),
    ("ec",              "European Commission",          "regulator",       None,    "Brussels, Belgium",  1958, None),
    ("france_adlc",     "Autorité de la concurrence",  "regulator",       None,    "Paris, France",      2009, "First to formally charge Nvidia (Jul 2024)"),
    ("china_samr",      "China SAMR",                  "regulator",       None,    "Beijing, China",     2018, "State Administration for Market Regulation"),

    # --- special purpose / unnamed ---
    ("fleet1_tract",    "Fleet I / Tract Capital",      "fin_institution", None,    "New York, NY",       2024, "SV RNO Property Owner 1; $3.8B junk bonds; 200MW Nevada DC"),
    ("thrive_holdings", "Thrive Holdings",              "ai_company",      None,    "New York, NY",       2024, "Enterprise AI deployment arm of Thrive Capital"),
    ("undisclosed_dc",  "Undisclosed Partner DC",       "neocloud",        None,    "Unknown",            None, "Nvidia 10-Q: $860M lease guarantee; identity not disclosed"),
]


ENTITY_ROLES = [
    # (entity_id, role, since, notes)
    ("nvidia",        "supplier",         "1993-01-01", None),
    ("nvidia",        "investor",         "2023-04-18", "equity investor in multiple neoclouds and AI cos"),
    ("nvidia",        "customer",         "2025-09-08", "customer of Lambda via $1.5B leaseback"),
    ("nvidia",        "guarantor",        "2023-04-13", "CoreWeave $6.3B backstop + $860M unnamed partner"),
    ("amd",           "supplier",         "1969-01-01", None),
    ("amd",           "guarantor",        "2026-02-19", "AMD backstops Crusoe $300M Goldman loan"),
    ("coreweave",     "compute_provider", "2017-01-01", None),
    ("coreweave",     "borrower",         "2023-08-01", "DDTL 1.0 onwards"),
    ("coreweave",     "issuer",           "2025-05-01", "Senior notes and convertibles"),
    ("coreweave",     "customer",         "2017-01-01", "purchases Nvidia GPUs"),
    ("lambda_labs",   "compute_provider", "2012-01-01", None),
    ("lambda_labs",   "borrower",         "2023-01-01", None),
    ("crusoe",        "compute_provider", "2018-01-01", None),
    ("crusoe",        "borrower",         "2026-02-19", "AMD-backed Goldman $300M loan"),
    ("nscale",        "compute_provider", "2022-01-01", None),
    ("nscale",        "borrower",         "2026-02-12", "DDTL $1.4B"),
    ("fluidstack",    "compute_provider", "2019-01-01", None),
    ("fluidstack",    "borrower",         "2025-04-01", "Macquarie $10B facility"),
    ("nebius",        "compute_provider", "2024-01-01", None),
    ("openai",        "customer",         "2022-01-01", "CoreWeave compute buyer"),
    ("openai",        "investor",         "2025-03-10", "holds CoreWeave equity from compute deal"),
    ("microsoft",     "customer",         "2022-01-01", "CoreWeave + Lambda compute buyer"),
    ("microsoft",     "investor",         "2019-01-01", "OpenAI 27% stake"),
    ("meta",          "customer",         "2024-01-01", "Nvidia GPU buyer"),
    ("magnetar",      "lender",           "2023-08-01", "CoreWeave DDTL lead"),
    ("magnetar",      "investor",         "2021-01-01", "CoreWeave equity ~23-30%; largest shareholder"),
    ("blackstone",    "lender",           "2023-08-01", "CoreWeave DDTL lead"),
    ("coatue",        "investor",         "2024-05-01", "led CoreWeave Series C"),
    ("coatue",        "lender",           "2023-08-01", "CoreWeave DDTL participant"),
    ("thrive_capital","investor",         "2024-10-02", "led OpenAI Oct 2024 round"),
    ("softbank",      "investor",         "2025-03-31", "OpenAI ~11% stake; sold Nvidia stake"),
    ("goldman_sachs", "lender",           "2025-07-31", None),
    ("goldman_sachs", "arranger",         "2025-07-31", None),
    ("jpmorgan",      "lender",           "2024-10-01", None),
    ("jpmorgan",      "investor",         "2023-12-01", "JPM Asset Mgmt CoreWeave secondary"),
    ("morgan_stanley","lender",           "2025-07-31", None),
    ("blue_owl",      "lender",           "2025-01-01", None),
    ("blue_owl",      "investor",         "2025-09-25", "Nscale equity"),
    ("google",        "investor",         "2025-08-01", "~14% TeraWulf equity via warrants"),
    ("google",        "guarantor",        "2025-08-01", "~$4.5B FluidStack/TeraWulf backstop"),
]


# =============================================================================
# RELATIONSHIP DATA
# (from_id, to_id, edge_type_id, amount_usd_b, stake_pct, rate_pct, valid_from, source, confidence, notes)
# =============================================================================

RELATIONSHIPS = [
    # ----- NVIDIA → neoclouds (equity investments) -----
    # Sequential stakes: earlier rows get valid_to set in post-seed supersession (see seed notes).
    # Live DB uses valid_to chain: Series B → IPO top-up → Jan 2026 $2B. stake_pct 13% is press headline;
    # reconcile against latest 13F/13G (may be ~8.65–11.5% after dilution).
    ("nvidia", "coreweave",     "INVESTS_EQUITY", None, 1.21,  None, "2023-04-18", "BusinessWire Apr 2023",               "confirmed", "Series B participation; ~1.21% pre-IPO"),
    ("nvidia", "coreweave",     "INVESTS_EQUITY", 0.25, 7.0,   None, "2025-03-28", "Nvidia 13G SEC filing Mar 2025",       "confirmed", "$250M top-up tranche; ~7% / ~24.2M shares at IPO"),
    ("nvidia", "coreweave",     "INVESTS_EQUITY", 2.0,  13.0,  None, "2026-01-26", "Nvidia Newsroom Jan 26 2026",          "confirmed", "$2B at $87.20/share; ~22.9M new shares; headline ~13% — verify vs 13F"),
    ("nvidia", "coreweave",     "BACKSTOP",       6.3,  None,  None, "2023-04-13", "CoreWeave SEC filing Sep 2025",        "confirmed", "Nvidia to purchase unsold CoreWeave capacity through Apr 13 2032"),
    ("nvidia", "lambda_labs",   "INVESTS_EQUITY", None, None,  None, "2025-02-19", "Lambda blog Feb 19 2025",              "confirmed", "Series D participant; amount undisclosed"),
    ("nvidia", "crusoe",        "INVESTS_EQUITY", None, None,  None, "2024-12-12", "Crusoe press release Dec 2024",        "confirmed", "Series D participant; amount undisclosed"),
    ("nvidia", "crusoe",        "INVESTS_EQUITY", None, None,  None, "2025-10-24", "Crusoe press release Oct 2025",        "confirmed", "Series E participant; AMD named strategic partner in same round"),
    ("nvidia", "nscale",        "INVESTS_EQUITY", None, None,  None, "2025-09-25", "Nscale press release Sep 25 2025",     "confirmed", "Series B participant; amount undisclosed"),
    ("nvidia", "nscale",        "INVESTS_EQUITY", None, None,  None, "2025-10-01", "Nscale SAFE press release Oct 2025",   "confirmed", "Pre-Series C SAFE participant; amount undisclosed"),
    ("nvidia", "nebius",        "INVESTS_EQUITY", None, None,  None, "2024-12-02", "TechCrunch Dec 2 2024; Nebius PR",     "confirmed", "Co-led $700M round alongside Accel and Orbis; exact amount undisclosed"),
    ("nvidia", "openai",        "INVESTS_EQUITY", 0.1,  None,  None, "2024-10-02", "CNBC Oct 2 2024",                      "reported",  "$100M in $6.6B round at $157B valuation; first Nvidia OpenAI investment"),
    ("nvidia", "openai",        "INVESTS_EQUITY", 30.0, None,  None, "2026-02-19", "CNBC Feb 19 2026",                     "reported",  "Up to $30B in ~$830B valuation round; NOT YET CLOSED as of Feb 23 2026"),
    ("nvidia", "mistral",       "INVESTS_EQUITY", None, None,  None, "2024-06-01", "CNBC Sep 9 2025",                      "confirmed", "Series B (Jun 2024 €600M round); amount undisclosed"),
    ("nvidia", "mistral",       "INVESTS_EQUITY", None, None,  None, "2025-09-09", "CNBC Sep 9 2025",                      "confirmed", "Series C (€1.7B led by ASML at 11%); Nvidia amount undisclosed"),
    ("nvidia", "undisclosed_dc","GUARANTEES_DEBT",0.86, None,  None, "2025-10-01", "Nvidia Q3 FY2026 10-Q",                "confirmed", "5yr facility lease guarantee; partner placed $470M escrow; Nvidia received warrants; partner identity undisclosed"),
    ("nvidia", "fleet1_tract",  "BUYS_COMPUTE",   None, None,  None, "2026-02-12", "Bloomberg Feb 12 2026",                "confirmed", "~16yr anchor lease at $3.8B junk-bond-financed 200MW Nevada DC; Storey County"),

    # ----- NVIDIA ↔ LAMBDA (circular leaseback) -----
    # Nvidia sells GPUs to Lambda (recognized as Nvidia revenue)
    ("nvidia", "lambda_labs",   "SUPPLIES_GPUS",  None, None,  None, "2020-01-01", "inferred from Lambda infrastructure",  "confirmed", "Lambda fleet is 100% Nvidia hardware"),
    # Lambda owns GPUs then Nvidia rents them back
    ("lambda_labs", "nvidia",   "LEASEBACK",      1.5,  None,  None, "2025-09-08", "DCD Sep 8 2025; Tom's Hardware",       "confirmed", "Lambda sells capacity to Nvidia: 18,000 H100-gen GPUs over 4 years; Nvidia = Lambda's single largest customer"),

    # ----- AMD -----
    ("amd",   "crusoe",         "GUARANTEES_DEBT",0.3,  None,  None, "2026-02-19", "The Information Feb 19 2026; DCD",     "reported",  "AMD backstops Goldman Sachs $300M loan; Crusoe buys AMD chips for Ohio DC; AMD leases back if needed; ~6% rate"),
    ("goldman_sachs", "crusoe", "LENDS_DEBT",     0.3,  None,  None, "2026-02-19", "Tom's Hardware Feb 2026",              "reported",  "AMD-backstopped loan; arranged by Goldman; first AMD-chip loan collateralization"),

    # ----- CoreWeave suppliers / customers -----
    ("nvidia",     "coreweave", "SUPPLIES_GPUS",  None, None,  None, "2021-01-01", "CoreWeave S-1",                        "confirmed", "Sole GPU supplier; H100/H200/GB200/NVL72/GB300 fleet"),
    ("coreweave",  "microsoft", "BUYS_COMPUTE",   1.2,  None,  None, "2022-01-01", "CoreWeave S-1 (62% of FY2024 revenue)","confirmed", "Customer A in S-1; ~$1.2B FY2024 based on 62% of $1.92B revenue; ~$10B total commitment"),
    ("coreweave",  "openai",    "BUYS_COMPUTE",   22.4, None,  None, "2025-03-10", "CoreWeave IR Mar/May/Sep 2025",         "confirmed", "$11.9B (Mar) + $4B (May) + $6.5B (Sep) = up to $22.4B contracted over 5 years"),
    ("coreweave",  "mistral",   "BUYS_COMPUTE",   None, None,  None, "2023-01-01", "DCD; CoreWeave blog",                  "confirmed", "Customer since 2023; H100/H200/GB200 NVL72; trained on GB200 NVL72 2.5x faster"),
    # Customer C (~15% 2024 revenue) = inferred as Nvidia via $6.3B backstop
    ("coreweave",  "nvidia",    "BUYS_COMPUTE",   None, None,  None, "2023-04-13", "inferred: S-1 Customer C + $6.3B backstop","inferred","~15% of 2024 revenue (~$288M); consistent with Nvidia as compute purchaser under backstop"),

    # ----- OpenAI ↔ CoreWeave (circular: customer + shareholder) -----
    ("openai",  "coreweave",    "INVESTS_EQUITY", 0.35, 2.0,   None, "2025-03-10", "CoreWeave PR Mar 10 2025",              "confirmed", "OpenAI received 8.75M CoreWeave shares ($350M at $40 IPO price) as equity component of compute deal"),

    # ----- CoreWeave → Core Scientific (lease obligations) -----
    ("coreweave", "core_scientific", "LENDS_DEBT",10.2, None,  None, "2024-01-01", "Core Scientific IR; CoreWeave Q3 2025 10-Q","confirmed","~$10.2B in 12-year lease payments for ~590MW hosting across 6 sites. CoreWeave all-stock acquisition later abandoned; CORZ remains independent neocloud/hosting platform."),

    # ----- CoreWeave DEBT facilities -----
    ("magnetar",      "coreweave", "LENDS_DEBT",  0.05, None,  None, "2021-01-01", "PitchBook; Benzinga",                  "confirmed", "$50M convertible notes (2021); earliest investment; grew to ~$12.5B position by late 2025"),
    ("magnetar",      "coreweave", "LENDS_DEBT",  None, None,  None, "2023-08-01", "Blackstone PR Aug 2023",               "confirmed", "DDTL 1.0 co-lead with Blackstone ($2.3B total facility); allocation undisclosed"),
    ("blackstone",    "coreweave", "LENDS_DEBT",  None, None,  None, "2023-08-01", "Blackstone PR Aug 2023",               "confirmed", "DDTL 1.0 co-lead with Magnetar ($2.3B total facility); allocation undisclosed"),
    ("magnetar",      "coreweave", "LENDS_DEBT",  None, None,  None, "2024-05-17", "Blackstone PR May 2024",               "confirmed", "DDTL 2.0 co-lead with Blackstone ($7.5B facility); allocation undisclosed"),
    ("blackstone",    "coreweave", "LENDS_DEBT",  4.5,  None,  None, "2024-05-17", "IFR Awards (Blackstone Tac Ops ~$4.5B of $7.5B)", "reported", "DDTL 2.0; ~$4.5B of $7.5B facility via Blackstone Tactical Opportunities"),
    ("pimco",         "coreweave", "LENDS_DEBT",  None, None,  None, "2023-08-01", "Blackstone PR Aug 2023",               "confirmed", "DDTL 1.0 participant; allocation undisclosed"),
    ("blackrock",     "coreweave", "LENDS_DEBT",  None, None,  None, "2023-08-01", "Blackstone PR Aug 2023",               "confirmed", "DDTL 1.0 participant; allocation undisclosed"),
    ("carlyle",       "coreweave", "LENDS_DEBT",  None, None,  None, "2023-08-01", "Blackstone PR Aug 2023",               "confirmed", "DDTL 1.0 participant; allocation undisclosed"),
    ("digitalbridge", "coreweave", "LENDS_DEBT",  None, None,  None, "2023-08-01", "DigitalBridge PR Aug 2023",            "confirmed", "DDTL 1.0 participant via DigitalBridge Credit; allocation undisclosed"),
    ("blackrock",     "coreweave", "LENDS_DEBT",  None, None,  None, "2024-05-17", "Blackstone PR May 2024",               "confirmed", "DDTL 2.0 participant; allocation undisclosed"),
    ("carlyle",       "coreweave", "LENDS_DEBT",  None, None,  None, "2024-05-17", "Blackstone PR May 2024",               "confirmed", "DDTL 2.0 participant; allocation undisclosed"),
    ("digitalbridge", "coreweave", "LENDS_DEBT",  None, None,  None, "2024-05-17", "Blackstone PR May 2024",               "confirmed", "DDTL 2.0 participant; allocation undisclosed"),
    ("cdpq",          "coreweave", "LENDS_DEBT",  None, None,  None, "2024-05-17", "Blackstone PR May 2024",               "confirmed", "DDTL 2.0 participant; allocation undisclosed"),
    ("goldman_sachs", "coreweave", "LENDS_DEBT",  None, None,  None, "2025-07-31", "CoreWeave IR Jul 2025",                "confirmed", "DDTL 3.0 joint lead arranger ($2.6B total)"),
    ("morgan_stanley","coreweave", "LENDS_DEBT",  None, None,  None, "2025-07-31", "CoreWeave IR Jul 2025",                "confirmed", "DDTL 3.0 joint lead (via Morgan Stanley Asset Funding)"),
    ("mufg",          "coreweave", "LENDS_DEBT",  None, None,  None, "2025-07-31", "CoreWeave IR Jul 2025",                "confirmed", "DDTL 3.0 admin agent + joint lead"),
    ("jpmorgan",      "coreweave", "LENDS_DEBT",  None, None,  None, "2024-10-01", "CoreWeave IR Oct 2024",                "confirmed", "Revolving credit joint lead ($650M→$2.5B)"),
    ("goldman_sachs", "coreweave", "LENDS_DEBT",  None, None,  None, "2024-10-01", "CoreWeave IR Oct 2024",                "confirmed", "Revolving credit joint lead"),
    ("morgan_stanley","coreweave", "LENDS_DEBT",  None, None,  None, "2024-10-01", "CoreWeave IR Oct 2024",                "confirmed", "Revolving credit joint lead"),
    ("goldman_sachs", "coreweave", "LENDS_DEBT",  None, None,  None, "2025-12-01", "BusinessWire Dec 2025",                "confirmed", "Convertible notes joint bookrunner ($2.25B, 1.75%, 2031)"),
    ("morgan_stanley","coreweave", "LENDS_DEBT",  None, None,  None, "2025-12-01", "BusinessWire Dec 2025",                "confirmed", "Convertible notes joint bookrunner"),
    ("jpmorgan",      "coreweave", "LENDS_DEBT",  None, None,  None, "2025-12-01", "BusinessWire Dec 2025",                "confirmed", "Convertible notes joint bookrunner"),
    ("blue_owl",      "coreweave", "LENDS_DEBT",  0.5,  None,  None, "2025-01-01", "Bisnow; DNYUZ Feb 2026",               "confirmed", "$500M bridge commitment for PA datacenter project; full $4B arrangement failed Feb 20 2026"),

    # ----- CoreWeave EQUITY investors -----
    ("magnetar",     "coreweave", "INVESTS_EQUITY",0.111,23.0,  None, "2023-04-18", "MarketScreener; BusinessWire Apr 2023","confirmed", "Led Series B; ~$111M of $221M round; ultimately ~23-30% largest shareholder"),
    ("coatue",       "coreweave", "INVESTS_EQUITY",None, None,  None, "2023-08-01", "Blackstone PR Aug 2023",               "confirmed", "DDTL 1.0 participant (debt role); also equity later"),
    ("coatue",       "coreweave", "INVESTS_EQUITY",1.1,  None,  None, "2024-05-01", "PRNewswire May 2024",                  "confirmed", "Led $1.1B Series C at $19B valuation"),
    ("fidelity",     "coreweave", "INVESTS_EQUITY",None, 6.75, None, "2023-12-01", "Fortune Dec 2023",                     "confirmed", "Led $642M secondary; ~6.75% total stake"),
    ("jane_street",  "coreweave", "INVESTS_EQUITY",None, 5.4,  None, "2023-12-01", "Bloomberg Dec 2023",                   "confirmed", "Co-investor in $642M secondary at $7B valuation"),
    ("jpmorgan",     "coreweave", "INVESTS_EQUITY",None, None,  None, "2023-12-01", "Fortune Dec 2023",                     "confirmed", "JPMorgan Asset Mgmt; $642M secondary"),
    ("macquarie",    "coreweave", "INVESTS_EQUITY",None, None,  None, "2024-11-13", "CoreWeave IR Nov 2024",                "confirmed", "$650M secondary participant"),
    ("jane_street",  "coreweave", "INVESTS_EQUITY",None, 5.4,  None, "2024-11-13", "CoreWeave IR Nov 2024",                "confirmed", "Led $650M secondary alongside Magnetar and Fidelity"),
    ("fidelity",     "coreweave", "INVESTS_EQUITY",None, 6.75, None, "2024-11-13", "CoreWeave IR Nov 2024",                "confirmed", "$650M secondary; total stake ~6.75%"),

    # ----- Nscale debt -----
    ("pimco",         "nscale",   "LENDS_DEBT",    None, None,  None, "2026-02-12", "Nscale PR Feb 12 2026",                "confirmed", "DDTL co-lead ($1.4B total); GPU clusters Norway/Portugal/Iceland/UK"),
    ("blue_owl",      "nscale",   "LENDS_DEBT",    None, None,  None, "2026-02-12", "Bloomberg Feb 12 2026",                "confirmed", "DDTL co-lead ($1.4B total)"),
    ("luminArx",      "nscale",   "LENDS_DEBT",    None, None,  None, "2026-02-12", "Nscale PR Feb 12 2026",                "confirmed", "DDTL co-lead ($1.4B total)"),
    ("goldman_sachs", "nscale",   "ARRANGES_DEBT", 1.4,  None,  None, "2026-02-12", "Nscale PR Feb 12 2026",                "confirmed", "Sole structuring agent and sole placement agent"),

    # ----- Nscale equity -----
    ("aker",          "nscale",   "INVESTS_EQUITY",None, None,  None, "2025-09-25", "Nscale PR Sep 2025",                   "confirmed", "Led $1.1B Series B"),
    ("nokia",         "nscale",   "INVESTS_EQUITY",None, None,  None, "2025-09-25", "Nscale PR Sep 2025",                   "confirmed", "Series B + SAFE participant"),
    ("blue_owl",      "nscale",   "INVESTS_EQUITY",None, None,  None, "2025-09-25", "Nscale PR Sep 2025",                   "confirmed", "Series B + SAFE equity participant"),
    ("fidelity",      "nscale",   "INVESTS_EQUITY",None, None,  None, "2025-09-25", "Nscale PR Sep 2025",                   "confirmed", "Series B participant"),

    # ----- Crusoe equity -----
    ("founders_fund", "crusoe",   "INVESTS_EQUITY",None, None,  None, "2024-12-12", "Crusoe PR Dec 2024",                   "confirmed", "Led $600M Series D at $2.8B valuation"),
    ("fidelity",      "crusoe",   "INVESTS_EQUITY",None, None,  None, "2024-12-12", "Crusoe PR Dec 2024",                   "confirmed", "Series D participant"),
    ("valor",         "crusoe",   "INVESTS_EQUITY",None, None,  None, "2025-10-24", "Crusoe PR Oct 2025",                   "confirmed", "Co-led $1.375B Series E at $10B+ valuation"),
    ("mubadala",      "crusoe",   "INVESTS_EQUITY",None, None,  None, "2025-10-24", "Crusoe PR Oct 2025",                   "confirmed", "Co-led $1.375B Series E"),
    ("tiger_global",  "crusoe",   "INVESTS_EQUITY",None, None,  None, "2025-10-24", "Crusoe PR Oct 2025",                   "confirmed", "Series E participant"),

    # ----- Lambda equity -----
    ("twg_global",   "lambda_labs","INVESTS_EQUITY",None, None,  None, "2025-11-18", "Lambda blog Nov 18 2025",              "confirmed", "Led $1.5B+ Series E"),
    ("microsoft",    "lambda_labs","BUYS_COMPUTE",  None, None,  None, "2025-11-03", "Lambda blog Nov 3 2025",               "confirmed", "Multibillion-dollar multi-year deal; tens of thousands of GB300 NVL72 GPUs"),

    # ----- Nebius equity -----
    ("accel",         "nebius",   "INVESTS_EQUITY",None, None,  None, "2024-12-02", "TechCrunch Dec 2 2024",                "confirmed", "Co-led $700M round with Nvidia; 33.3M Class A shares at $21"),

    # ----- FluidStack -----
    ("macquarie",   "fluidstack", "LENDS_DEBT",     10.0, None,  None, "2025-04-01", "BusinessWire Apr 1 2025; DCD",         "confirmed", "Up to $10B GPU-collateralized senior debt facility for European GPU buildout"),
    ("google",      "fluidstack", "BACKSTOP",       4.5,  None,  None, "2025-08-01", "DCD Aug 2025; CNBC Aug 18 2025",       "confirmed", "Google backstops FluidStack/TeraWulf lease obligations; ~$4.5B across tranches; Google holds ~14% TeraWulf equity (warrants)"),
    ("google",      "terawulf",   "INVESTS_EQUITY", None, 14.0,  None, "2025-08-01", "CNBC Aug 18 2025; TeraWulf SEC filings","confirmed","~14% equity stake via warrants from FluidStack backstop arrangement"),

    # ----- FleetI / Tract Capital (Nvidia DC bond) -----
    ("jpmorgan",    "fleet1_tract","ARRANGES_DEBT",  3.8, None,  None, "2026-02-12", "Bloomberg Feb 12 2026",                "confirmed", "JP Morgan led $3.8B junk bond sale for SV RNO Property Owner 1 (Tract Capital Fleet I)"),
    ("morgan_stanley","fleet1_tract","LENDS_DEBT",   None, None, None, "2026-02-12", "Bloomberg Feb 12 2026",                "confirmed", "Co-managed Nvidia $3.8B DC junk bond"),

    # ----- OpenAI ecosystem -----
    ("microsoft",    "openai",    "INVESTS_EQUITY", 13.0, 27.0,  None, "2019-01-01", "Microsoft 10-K Oct 2025",              "confirmed", "$13B cumulative; 27% on as-converted basis post-PBC restructure Oct 2025"),
    ("softbank",     "openai",    "INVESTS_EQUITY", 30.0, 11.0,  None, "2025-03-31", "CNBC Mar 31 2025; CNBC Dec 30 2025",   "confirmed", "Led $40B round; $30B SoftBank commitment fully funded Dec 2025; ~11% stake"),
    ("thrive_capital","openai",   "INVESTS_EQUITY", 1.2,  None,  None, "2024-10-02", "TechCrunch / BusinessToday Oct 2024",  "confirmed", "Led $6.6B round at $157B valuation; ~$1.2B check; option for additional $1B"),
    ("coatue",       "openai",    "INVESTS_EQUITY", None, None,  None, "2025-03-31", "CNBC Mar 31 2025",                     "confirmed", "Co-investor in SoftBank-led $40B round"),
    ("tiger_global", "openai",    "INVESTS_EQUITY", None, None,  None, "2024-10-02", "CNBC Oct 2024",                        "confirmed", "Oct 2024 $6.6B round participant"),
    # CIRCULAR: OpenAI invests in Thrive Holdings (after Thrive invested in OpenAI)
    ("openai",      "thrive_holdings","INVESTS_EQUITY",None,None, None,"2025-12-01", "TechCrunch Dec 1 2025",                "confirmed", "CIRCULAR: OpenAI took equity in Thrive Holdings after Thrive led $6.6B OpenAI round"),

    # ----- Meta -----
    ("meta",         "nvidia",    "BUYS_COMPUTE",   50.0, None,  None, "2026-02-17", "CNBC Feb 17 2026; Nvidia Newsroom",    "confirmed", "Multi-year deal: Blackwell + Vera Rubin + Grace CPUs; up to $50B"),

    # ----- SoftBank / Nvidia -----
    ("softbank",     "nvidia",    "INVESTS_EQUITY", 3.0,  None,  None, "2025-03-01", "DCD Mar 2025",                         "confirmed", "Built Nvidia stake to ~$3B by Mar 2025"),
    # SoftBank sold entire Nvidia stake — closing the edge with valid_to handled separately

    # ----- Regulators -----
    ("doj",          "nvidia",    "INVESTIGATES",   None, None,  None, "2024-09-03", "Bloomberg Sep 3 2024",                 "confirmed", "DOJ subpoenas to Nvidia; scope: GPU bundling, InfiniBand tying, Run:AI acquisition"),
    ("ec",           "nvidia",    "INVESTIGATES",   None, None,  None, "2024-12-06", "Reuters Dec 6 2024",                   "confirmed", "EC questionnaires; GPU + InfiniBand bundling; pre-formal investigation"),
    ("france_adlc",  "nvidia",    "INVESTIGATES",   None, None,  None, "2024-07-01", "Bloomberg/Reuters Jul 1 2024",         "confirmed", "First jurisdiction to prepare formal Statement of Objections; CUDA lock-in; circular investment concern"),
    ("china_samr",   "nvidia",    "INVESTIGATES",   None, None,  None, "2025-09-15", "CNBC Sep 15 2025",                     "confirmed", "Preliminary finding: violated Anti-Monopoly Law re: Mellanox acquisition behavioral conditions"),

    # ----- USD.AI / Sharon AI -----
    ("usdai",        "sharon_ai", "LENDS_DEBT",     0.5,  None,  None, "2026-01-22", "BusinessWire/Nasdaq Jan 22 2026",      "confirmed", "Up to $500M non-recourse; $65M initially drawn; tokenized GPU collateral; on-chain protocol"),
]


# =============================================================================
# BUILD DB
# =============================================================================

def build_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Removed existing database: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.executescript("PRAGMA foreign_keys = ON; PRAGMA journal_mode = WAL;")

    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()
    conn.executescript(schema_sql)
    print("Schema created.")

    # Insert entities
    for row in ENTITIES:
        cur.execute("""
            INSERT OR IGNORE INTO entities (id, name, category_id, ticker, hq, founded, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, row)
    print(f"Inserted {len(ENTITIES)} entities.")

    # Insert entity roles
    for row in ENTITY_ROLES:
        cur.execute("""
            INSERT OR IGNORE INTO entity_roles (entity_id, role, since, notes)
            VALUES (?, ?, ?, ?)
        """, row)
    print(f"Inserted {len(ENTITY_ROLES)} entity roles.")

    # Insert relationships — temporarily disable trigger to allow seeding
    cur.execute("DROP TRIGGER IF EXISTS enforce_one_open_relationship")

    for row in RELATIONSHIPS:
        (from_id, to_id, edge_type_id, amount, stake, rate,
         valid_from, source, confidence, notes) = row
        cur.execute("""
            INSERT INTO relationships
              (from_id, to_id, edge_type_id, amount_usd_b, stake_pct, rate_pct,
               valid_from, valid_to, source, confidence, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, NULL, ?, ?, ?)
        """, (from_id, to_id, edge_type_id, amount, stake, rate,
              valid_from, source, confidence, notes))
    print(f"Inserted {len(RELATIONSHIPS)} relationships.")

    # Rebuild the trigger after seeding
    cur.executescript("""
        CREATE TRIGGER IF NOT EXISTS enforce_one_open_relationship
        BEFORE INSERT ON relationships
        WHEN NEW.valid_to IS NULL
        BEGIN
            SELECT RAISE(ABORT,
                'Active relationship already exists for this from/to/edge_type. '
                || 'Close existing record (set valid_to) before inserting new version.')
            WHERE EXISTS (
                SELECT 1 FROM relationships
                WHERE from_id      = NEW.from_id
                  AND to_id        = NEW.to_id
                  AND edge_type_id = NEW.edge_type_id
                  AND valid_to IS NULL
                  AND rowid != NEW.rowid
            );
        END;
    """)

    conn.commit()
    conn.close()
    print(f"\nDatabase built: {DB_PATH}")


# =============================================================================
# GRAPH TESTS
# =============================================================================

def run_tests():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")

    sep = "─" * 70

    # ── Test 1: All Nvidia relationships ──────────────────────────────────────
    print(f"\n{sep}")
    print("TEST 1: All Nvidia outgoing relationships")
    print(sep)
    cur.execute("""
        SELECT from_name, edge_label, to_name,
               COALESCE('$' || ROUND(amount_usd_b,2) || 'B', '—') AS amount,
               COALESCE(ROUND(stake_pct,1) || '%', '—')           AS stake,
               confidence
        FROM relationships_current
        WHERE from_id = 'nvidia'
        ORDER BY edge_label, to_name
    """)
    for r in cur.fetchall():
        print(f"  {r['from_name']} → [{r['edge_label']}] → {r['to_name']}  "
              f"amt={r['amount']}  stake={r['stake']}  ({r['confidence']})")

    # ── Test 2: The "incest check" — all edges between Nvidia and CoreWeave ───
    print(f"\n{sep}")
    print("TEST 2: All edges between Nvidia and CoreWeave (incest check)")
    print(sep)
    cur.execute("""
        SELECT from_name, edge_label, to_name,
               COALESCE('$' || ROUND(amount_usd_b,2) || 'B', '—') AS amount,
               COALESCE(ROUND(stake_pct,1) || '%', '—')           AS stake,
               valid_from, confidence
        FROM relationships_current
        WHERE (from_id = 'nvidia'    AND to_id = 'coreweave')
           OR (from_id = 'coreweave' AND to_id = 'nvidia')
        ORDER BY valid_from
    """)
    for r in cur.fetchall():
        print(f"  [{r['valid_from']}] {r['from_name']} → [{r['edge_label']}] → {r['to_name']}  "
              f"amt={r['amount']}  stake={r['stake']}")

    # ── Test 3: Documented circular loops ─────────────────────────────────────
    print(f"\n{sep}")
    print("TEST 3: Documented circular ownership (entity appears as both investor and investee)")
    print(sep)
    cur.execute("""
        SELECT a.from_name || ' → ' || a.to_name AS leg_1,
               b.from_name || ' → ' || b.to_name AS leg_2,
               a.edge_label AS type_1,
               b.edge_label AS type_2
        FROM relationships_current a
        JOIN relationships_current b
          ON a.to_id = b.from_id AND b.to_id = a.from_id
        WHERE a.edge_type_id IN ('INVESTS_EQUITY','BACKSTOP','LEASEBACK','BUYS_COMPUTE')
          AND b.edge_type_id IN ('INVESTS_EQUITY','BACKSTOP','LEASEBACK','BUYS_COMPUTE','SUPPLIES_GPUS')
        ORDER BY a.from_name, b.from_name
    """)
    seen = set()
    for r in cur.fetchall():
        key = tuple(sorted([r['leg_1'], r['leg_2']]))
        if key not in seen:
            seen.add(key)
            print(f"  CYCLE: {r['leg_1']} [{r['type_1']}]  ↔  {r['leg_2']} [{r['type_2']}]")

    # ── Test 4: Recursive cycle detection — who can Nvidia reach via investment? ──
    print(f"\n{sep}")
    print("TEST 4: Recursive reachability — who can Nvidia reach via INVESTS_EQUITY? (cycle-safe)")
    print(sep)
    cur.execute("""
        WITH RECURSIVE reach(node_id, node_name, path, depth) AS (
            SELECT 'nvidia', 'NVIDIA Corporation', json_array('nvidia'), 0
            UNION ALL
            SELECT r.to_id,
                   e.name,
                   json_insert(rc.path, '$[#]', r.to_id),
                   rc.depth + 1
            FROM   relationships r
            JOIN   entities e     ON r.to_id = e.id
            JOIN   reach rc       ON r.from_id = rc.node_id
            WHERE  r.edge_type_id = 'INVESTS_EQUITY'
              AND  r.valid_to IS NULL
              AND  NOT EXISTS (
                       SELECT 1 FROM json_each(rc.path) WHERE value = r.to_id
                   )
              AND  rc.depth < 6
        )
        SELECT node_name, depth, path
        FROM   reach
        WHERE  depth > 0
        ORDER  BY depth, node_name
    """)
    for r in cur.fetchall():
        path = " → ".join(json.loads(r['path']))
        print(f"  depth={r['depth']}  {r['node_name']}")
        print(f"         path: {path}")

    # ── Test 5: Who lends to CoreWeave and also invests in CoreWeave? ─────────
    print(f"\n{sep}")
    print("TEST 5: Entities that are BOTH lenders AND equity investors in CoreWeave")
    print(sep)
    cur.execute("""
        SELECT l.from_name AS entity, l.amount_usd_b AS debt_amt, i.stake_pct AS equity_stake
        FROM relationships_current l
        JOIN relationships_current i
          ON l.from_id = i.from_id AND l.to_id = i.to_id
        WHERE l.to_id       = 'coreweave'
          AND l.edge_type_id = 'LENDS_DEBT'
          AND i.edge_type_id = 'INVESTS_EQUITY'
        GROUP BY l.from_name
        ORDER BY l.from_name
    """)
    rows = cur.fetchall()
    if rows:
        for r in rows:
            print(f"  {r['entity']}  debt_amt={r['debt_amt']}  equity_stake={r['equity_stake']}")
    else:
        print("  (none with both explicit rows — check Magnetar and Coatue)")

    # ── Test 6: Summary stats ─────────────────────────────────────────────────
    print(f"\n{sep}")
    print("TEST 6: Summary statistics")
    print(sep)
    cur.execute("SELECT COUNT(*) FROM entities")
    print(f"  Entities:      {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM relationships WHERE valid_to IS NULL")
    print(f"  Active rels:   {cur.fetchone()[0]}")
    cur.execute("SELECT edge_type_id, COUNT(*) AS n FROM relationships WHERE valid_to IS NULL GROUP BY edge_type_id ORDER BY n DESC")
    print("  By edge type:")
    for r in cur.fetchall():
        print(f"    {r['edge_type_id']:<20} {r['n']}")
    cur.execute("SELECT category_id, COUNT(*) AS n FROM entities GROUP BY category_id ORDER BY n DESC")
    print("  By category:")
    for r in cur.fetchall():
        print(f"    {r['category_id']:<20} {r['n']}")

    # ── Test 7: The core circular chain for the paper ─────────────────────────
    print(f"\n{sep}")
    print("TEST 7: The paper's core circular chain — Nvidia → CoreWeave → [customers] → Nvidia")
    print(sep)
    cur.execute("""
        SELECT rc.from_name AS neocloud,
               rc.edge_label AS rel_type,
               rc.to_name   AS customer,
               nr.from_name AS customer_also,
               nr.edge_label AS back_to_nvidia,
               nr.to_name   AS back_to
        FROM relationships_current rc
        JOIN relationships_current nr ON rc.to_id = nr.from_id
        WHERE rc.from_id = 'coreweave'
          AND rc.edge_type_id = 'BUYS_COMPUTE'
          AND nr.to_id IN ('nvidia', 'coreweave')
        ORDER BY rc.to_name
    """)
    for r in cur.fetchall():
        print(f"  Nvidia → CoreWeave → [{r['rel_type']}] → {r['customer']}"
              f" → [{r['back_to_nvidia']}] → {r['back_to']}")

    conn.close()
    print(f"\n{sep}")
    print("All tests complete.")
    print(sep)


if __name__ == "__main__":
    build_db()
    run_tests()
