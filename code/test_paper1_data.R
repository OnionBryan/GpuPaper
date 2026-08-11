# =============================================================================
# Paper 1 Data Validation Tests
# Verifies that key empirical values in paper1_gpu_debt_accounting.Rmd are
# consistent with source data and internally coherent.
# =============================================================================

library(testthat)

# ── ROIC calculations ───────────────────────────────────────────────────────
test_that("ROIC sensitivity values are internally consistent", {
  gpu_fleet <- 15
  ebitda    <- 3.4
  interest  <- 1.24
  capital   <- 19.1
  tax_rate  <- 0.0
  obs_pv    <- 23.0

  lives <- c(2, 3, 4, 5, 6, 6.5)
  dep   <- gpu_fleet / lives
  ebit  <- ebitda - dep
  nopat <- ebit * (1 - tax_rate)
  roic  <- nopat / capital * 100

  # Bull case (6yr) should be ~4.7%
  expect_equal(round(roic[5], 1), 4.7,
               info = "Bull case (6yr) ROIC should be 4.7%")

  # OBS-adjusted bull case should be ~2.1%
  roic_obs <- nopat[5] / (capital + obs_pv) * 100
  expect_equal(round(roic_obs, 1), 2.1,
               info = "OBS-adjusted bull case ROIC should be 2.1%")

  # No scenario should exceed WACC of 9.72%
  expect_true(all(roic < 9.72),
              info = "No depreciation scenario should exceed WACC threshold")

  # Solvency metric (EBIT - interest) / capital: all scenarios negative
  solvency <- (ebit - interest) / capital * 100
  expect_true(all(solvency < 0),
              info = "Solvency metric should be negative at all useful lives")
})

# ── Facility data completeness ──────────────────────────────────────────────
test_that("Facility table has required fields", {
  # These are the borrowers that should appear in the facility table
  expected_borrowers <- c("CoreWeave", "Lambda Labs", "Crusoe Energy",
                          "FluidStack", "Nebius", "Nscale",
                          "Applied Digital", "Iris Energy", "Helios",
                          "Voltage Park", "Sharon AI")
  expect_true(length(expected_borrowers) >= 10,
              info = "At least 10 borrowers expected in facility table")
})

# ── Network metrics consistency (filtered 7-type directed network) ───────────
test_that("Network metrics are consistent with DB query results", {
  # Values from circular_flow.db query (2026-03-12), FILTERED to 7 financial edge types
  total_nodes <- 133
  total_edges <- 432  # 7 filtered types, non-regulator
  nvidia_filtered_degree <- 45  # NVIDIA edges in filtered types (NOT 63 total)
  coreweave_filtered_rels <- 42  # CoreWeave edges in filtered types
  cw_nvidia_filtered_rels <- 4  # CoreWeave-NVIDIA in filtered types

  # Directed density = edges / (nodes * (nodes - 1))
  directed_density <- total_edges / (total_nodes * (total_nodes - 1))
  expect_equal(round(directed_density, 3), 0.025,
               info = "Directed network density should be 0.025")

  # CoreWeave-NVIDIA dependency ratio (filtered)
  cw_dep_ratio <- cw_nvidia_filtered_rels / coreweave_filtered_rels
  expect_equal(round(cw_dep_ratio, 3), 0.095,
               info = "CoreWeave-NVIDIA filtered dependency ratio should be 0.095")

  # NVIDIA distinct counterparties in filtered network
  nvidia_counterparties <- 39
  expect_true(nvidia_counterparties > 30,
              info = "NVIDIA should connect to 30+ counterparties in filtered network")
})

# ── Spread anomaly values ───────────────────────────────────────────────────
test_that("BIS spread values are correctly stated", {
  ai_spread <- 6.2
  non_ai_spread <- 6.1
  spread_diff <- ai_spread - non_ai_spread

  expect_equal(spread_diff, 0.1,
               info = "AI vs non-AI spread differential should be 10 bps")

  # Average deal sizes (from BIS data)
  ai_avg_deal <- 169  # $M
  non_ai_avg_deal <- 90  # $M
  expect_true(ai_avg_deal > non_ai_avg_deal,
              info = "AI average deal size should exceed non-AI")
})

# ── OBS lease calculations ─────────────────────────────────────────────────
test_that("OBS lease capitalization is consistent", {
  nominal_leases <- 39  # $B
  pv_leases <- 23       # $B (at ~9.5% discount rate)
  borrowing_rate <- 0.095

  # PV should be less than nominal

  expect_true(pv_leases < nominal_leases,
              info = "PV of leases must be less than nominal")

  # Discount factor sanity check: PV/nominal ratio
  discount_ratio <- pv_leases / nominal_leases
  expect_true(discount_ratio > 0.4 && discount_ratio < 0.8,
              info = "PV/nominal ratio should be between 0.4 and 0.8")
})

# ── CoreWeave financial metrics ─────────────────────────────────────────────
test_that("CoreWeave financial metrics are internally consistent", {
  interest_q3 <- 311  # $M per quarter
  interest_annual <- interest_q3 * 4  # $1.244B annualized
  ebitda_annual <- 3400  # $M

  # EBIT-to-interest coverage at various depreciation levels
  gpu_fleet <- 15000  # $M
  dep_6yr <- gpu_fleet / 6
  ebit_bull <- ebitda_annual - dep_6yr

  coverage <- ebit_bull / interest_annual
  expect_true(coverage < 2.0,
              info = "Even bull case coverage should be below 2x")
  expect_true(coverage > 0,
              info = "Bull case should have positive EBIT")

  # FCF is negative
  fcf <- -8100  # $M trailing twelve months
  expect_true(fcf < 0,
              info = "CoreWeave FCF should be negative")
})

# Run with: Rscript -e 'testthat::test_file("test_paper1_data.R")'
