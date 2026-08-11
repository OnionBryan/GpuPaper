library(DBI)
library(RSQLite)
library(tidygraph)
library(ggraph)
library(ggplot2)
library(dplyr)

# ── connect ──────────────────────────────────────────────────────────────────
db <- dbConnect(SQLite(), "circular_flow.db")

nodes_raw <- dbGetQuery(db, "SELECT id, name, category_id FROM entities WHERE category_id != 'regulator'")
# Accuracy filter for the public graph:
#  - active edges only (valid_to IS NULL)
#  - seven circular edge types
#  - no regulators
#  - DROP reported mega-talks (≥$100B) so unclosed Ohio-style packages do not dominate width
#  - DROP any edge whose notes mark TALKS ONLY (belt-and-suspenders)
edges_raw <- dbGetQuery(db, "
  SELECT from_id, to_id, edge_type_id, amount_usd_b, confidence
  FROM relationships
  WHERE valid_to IS NULL
    AND edge_type_id IN ('INVESTS_EQUITY','LENDS_DEBT','BUYS_COMPUTE',
                         'SUPPLIES_GPUS','BACKSTOP','LEASEBACK','GUARANTEES_DEBT')
    AND from_id NOT IN (SELECT id FROM entities WHERE category_id = 'regulator')
    AND to_id   NOT IN (SELECT id FROM entities WHERE category_id = 'regulator')
    AND NOT (
      confidence = 'reported'
      AND amount_usd_b IS NOT NULL
      AND amount_usd_b >= 100
    )
    AND NOT (
      notes LIKE '%TALKS ONLY%'
    )
")
dbDisconnect(db)

# ── colour palette ────────────────────────────────────────────────────────────
cat_colours <- c(
  chipmaker       = "#C0392B",
  neocloud        = "#2980B9",
  ai_company      = "#27AE60",
  hyperscaler     = "#8E44AD",
  fin_institution = "#E67E22",
  inv_fund        = "#F39C12",
  regulator       = "#7F8C8D"
)

edge_colours <- c(
  INVESTS_EQUITY   = "#E74C3C",
  LENDS_DEBT       = "#3498DB",
  BUYS_COMPUTE     = "#2ECC71",
  SUPPLIES_GPUS    = "#F39C12",
  BACKSTOP         = "#9B59B6",
  LEASEBACK        = "#1ABC9C",
  GUARANTEES_DEBT  = "#E67E22"
)

# ── build graph ──────────────────────────────────────────────────────────────
# Edge width ~ log1p(deal size); missing amounts get a thin default
edges_for_width <- edges_raw |>
  mutate(edge_width = ifelse(is.na(amount_usd_b), 0.25, pmax(0.2, log1p(amount_usd_b) * 0.35)))

g <- tbl_graph(
  nodes = nodes_raw |> rename(label = name),
  edges = edges_for_width |> rename(from = from_id, to = to_id),
  node_key = "id",
  directed = TRUE
)

# ── plot ──────────────────────────────────────────────────────────────────────
set.seed(42)

p <- ggraph(g, layout = "stress") +
  geom_edge_fan(
    aes(colour = edge_type_id, width = edge_width),
    arrow = arrow(length = unit(3, "mm"), type = "closed"),
    end_cap = circle(4, "mm"),
    alpha = 0.7
  ) +
  scale_edge_width_identity(guide = "none") +
  geom_node_point(aes(colour = category_id), size = 5) +
  geom_node_text(aes(label = label), size = 2.2, repel = TRUE, max.overlaps = 30) +
  scale_edge_colour_manual(values = edge_colours, name = "Relationship") +
  scale_colour_manual(values = cat_colours, name = "Category") +
  theme_graph(base_family = "sans") +
  labs(title = "GPU Circular Capital Flows",
       subtitle = "Edge width ~ deal size (log1p USD bn); thin = undisclosed. Excludes reported talks ≥$100B (e.g. Ohio $250B/$350B)")

ggsave("circular_flow_graph.png", p, width = 18, height = 14, dpi = 150)
message("Saved: circular_flow_graph.png")
