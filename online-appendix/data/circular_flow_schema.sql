-- =============================================================================
-- GPU CIRCULAR CAPITAL FLOWS — SQLite Schema
-- Paper: "GPU-Collateralized Debt Facilities: The Rise of Chip Loans"
-- Purpose: Map directed relationships between chipmakers, neoclouds, AI companies,
--          hyperscalers, financial institutions, and investment funds to formally
--          demonstrate circular capital flows in the AI GPU ecosystem.
-- Patterns: Labeled Property Graph + Party-Role vocabulary + Temporal edges
-- =============================================================================

PRAGMA foreign_keys = ON;
PRAGMA journal_mode  = WAL;

-- =============================================================================
-- LAYER 1: ENTITY CATEGORIES (sub-folder keys)
-- Organizes entities into meaningful groups for traversal and display.
-- =============================================================================

CREATE TABLE IF NOT EXISTS entity_categories (
    id          TEXT PRIMARY KEY,   -- short key: 'chipmaker', 'neocloud', etc.
    label       TEXT NOT NULL,      -- display label
    description TEXT
);

INSERT OR IGNORE INTO entity_categories VALUES
    ('chipmaker',       'Chip Manufacturer',
     'Semiconductor designers and manufacturers; primary GPU suppliers'),
    ('neocloud',        'Neo-Cloud Provider',
     'GPU-native cloud infrastructure companies; primary GPU debt holders'),
    ('ai_company',      'AI Application Company',
     'Companies building AI products/services; primary neocloud customers'),
    ('hyperscaler',     'Hyperscaler',
     'Major cloud platform providers (AWS, Azure, GCP, Meta); also neocloud customers'),
    ('fin_institution', 'Financial Institution',
     'Banks, debt underwriters, credit facility providers, ABS arrangers'),
    ('inv_fund',        'Investment Fund',
     'Venture capital, private equity, hedge funds; equity investors in neoclouds/AI'),
    ('regulator',       'Regulatory Body',
     'Government antitrust and competition authorities');


-- =============================================================================
-- LAYER 2: ENTITIES / PLAYERS
-- One row per distinct company, fund, or organization.
-- =============================================================================

CREATE TABLE IF NOT EXISTS entities (
    id          TEXT PRIMARY KEY,       -- slug: 'nvidia', 'coreweave', 'blackstone'
    name        TEXT NOT NULL,          -- full display name
    category_id TEXT NOT NULL REFERENCES entity_categories(id),
    ticker      TEXT,                   -- stock ticker if public
    hq          TEXT,                   -- headquarters country/city
    founded     INTEGER,                -- year
    notes       TEXT,
    properties  TEXT DEFAULT '{}'       -- JSON blob for overflow fields
);


-- =============================================================================
-- LAYER 3: ENTITY ROLES (junction table — multi-role support)
-- Same entity can hold multiple roles simultaneously.
-- e.g. Nvidia = 'supplier' + 'investor' + 'guarantor' all at once.
-- =============================================================================

CREATE TABLE IF NOT EXISTS entity_roles (
    entity_id   TEXT NOT NULL REFERENCES entities(id),
    role        TEXT NOT NULL CHECK(role IN (
                    'supplier',         -- sells hardware/chips
                    'investor',         -- holds equity stake
                    'lender',           -- provides debt/credit
                    'customer',         -- purchases compute or services
                    'guarantor',        -- backstops revenue or debt
                    'compute_provider', -- rents GPU capacity
                    'borrower',         -- has outstanding debt
                    'issuer',           -- issues ABS/bonds
                    'arranger',         -- arranges debt facilities
                    'regulator'         -- government oversight role
                )),
    since       TEXT,                   -- ISO-8601 date role first established
    notes       TEXT,
    PRIMARY KEY (entity_id, role)
);


-- =============================================================================
-- LAYER 4: EDGE TYPE VOCABULARY (controlled vocabulary for relationship types)
-- All edge_type_id values in relationships must appear here.
-- =============================================================================

CREATE TABLE IF NOT EXISTS edge_types (
    id          TEXT PRIMARY KEY,
    label       TEXT NOT NULL,
    flow_type   TEXT NOT NULL CHECK(flow_type IN (
                    'capital',      -- money moving from buyer to seller
                    'compute',      -- GPU capacity / hardware delivery
                    'equity',       -- ownership stake transfer
                    'debt',         -- loan / credit facility
                    'guarantee',    -- contingent obligation
                    'regulatory'    -- oversight / investigation
                )),
    description TEXT
);

INSERT OR IGNORE INTO edge_types VALUES
    ('SUPPLIES_GPUS',   'Supplies GPUs',            'compute',
     'Chipmaker sells GPU hardware to neocloud or hyperscaler'),
    ('INVESTS_EQUITY',  'Equity Investment',         'equity',
     'Entity purchases an equity stake (directional: investor → investee)'),
    ('LENDS_DEBT',      'Debt / Credit Facility',   'debt',
     'Entity provides debt financing (directional: lender → borrower)'),
    ('BUYS_COMPUTE',    'Purchases Compute',         'capital',
     'Customer pays for GPU cloud access (directional: customer → provider)'),
    ('BACKSTOP',        'Demand Backstop',           'guarantee',
     'Guarantor agrees to purchase unsold capacity at floor price'),
    ('LEASEBACK',       'Sale-Leaseback',            'capital',
     'Entity sold asset to counterparty then leased same asset back'),
    ('GUARANTEES_DEBT', 'Debt Guarantee',            'guarantee',
     'Entity guarantees debt obligations of counterparty'),
    ('ISSUES_ABS',      'Issues ABS',                'debt',
     'Entity securitizes assets into ABS tranche'),
    ('ARRANGES_DEBT',   'Arranges Debt Facility',    'debt',
     'Financial institution structures/syndicates debt facility'),
    ('INVESTIGATES',    'Regulatory Investigation',  'regulatory',
     'Regulator opens investigation or files charges against entity');


-- =============================================================================
-- LAYER 5: RELATIONSHIPS (directed, weighted, temporal edges)
-- Each row is one directed relationship with temporal validity window.
-- valid_to IS NULL means currently active.
-- =============================================================================

CREATE TABLE IF NOT EXISTS relationships (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    from_id         TEXT    NOT NULL REFERENCES entities(id),
    to_id           TEXT    NOT NULL REFERENCES entities(id),
    edge_type_id    TEXT    NOT NULL REFERENCES edge_types(id),

    -- Quantitative attributes (both optional — undisclosed is common)
    amount_usd_b    REAL,           -- deal size in USD billions
    stake_pct       REAL,           -- equity stake as percentage (0–100)
    rate_pct        REAL,           -- interest rate for debt relationships

    -- Temporal validity
    valid_from      TEXT    NOT NULL,   -- ISO-8601: '2021-04-13'
    valid_to        TEXT,               -- NULL = currently active

    -- Provenance
    source          TEXT,               -- citation key or URL
    confidence      TEXT DEFAULT 'confirmed' CHECK(confidence IN (
                        'confirmed',    -- directly stated in primary source
                        'inferred',     -- calculated from disclosed figures
                        'reported',     -- from secondary/press sources
                        'estimated'     -- rough estimate with stated basis
                    )),
    notes           TEXT
);

-- Indexes for common traversal patterns
CREATE INDEX IF NOT EXISTS idx_rel_from     ON relationships(from_id);
CREATE INDEX IF NOT EXISTS idx_rel_to       ON relationships(to_id);
CREATE INDEX IF NOT EXISTS idx_rel_type     ON relationships(edge_type_id);
CREATE INDEX IF NOT EXISTS idx_rel_current  ON relationships(from_id, to_id, edge_type_id)
    WHERE valid_to IS NULL;


-- =============================================================================
-- LAYER 6: CURRENT-STATE VIEW
-- Most queries should use this view, not the base table directly.
-- =============================================================================

CREATE VIEW IF NOT EXISTS relationships_current AS
    SELECT
        r.id,
        f.name          AS from_name,
        f.category_id   AS from_category,
        r.from_id,
        r.to_id,
        t.name          AS to_name,
        t.category_id   AS to_category,
        r.edge_type_id,
        et.label        AS edge_label,
        et.flow_type,
        r.amount_usd_b,
        r.stake_pct,
        r.rate_pct,
        r.valid_from,
        r.source,
        r.confidence,
        r.notes
    FROM  relationships  r
    JOIN  entities       f   ON r.from_id      = f.id
    JOIN  entities       t   ON r.to_id        = t.id
    JOIN  edge_types     et  ON r.edge_type_id = et.id
    WHERE r.valid_to IS NULL;


-- =============================================================================
-- LAYER 7: CLOSURE TABLE (precomputed reachability — rebuilt on batch ingest)
-- Stores all (ancestor → descendant) pairs reachable via directed edges.
-- Depth 0 = self. Rebuilt via populate_closure.sql after each data load.
-- =============================================================================

CREATE TABLE IF NOT EXISTS closure (
    ancestor_id     TEXT    NOT NULL REFERENCES entities(id),
    descendant_id   TEXT    NOT NULL REFERENCES entities(id),
    depth           INTEGER NOT NULL DEFAULT 0,
    via_edge_type   TEXT    REFERENCES edge_types(id),  -- NULL = any/mixed path
    PRIMARY KEY (ancestor_id, descendant_id, via_edge_type)
);


-- =============================================================================
-- LAYER 8: SAFETY TRIGGER
-- Prevents duplicate open-ended records for the same (from, to, edge_type).
-- NOTE: SQLite UNIQUE(a, b, NULL) allows multiple NULLs — trigger is required.
-- =============================================================================

CREATE TRIGGER IF NOT EXISTS enforce_one_open_relationship
BEFORE INSERT ON relationships
WHEN NEW.valid_to IS NULL
BEGIN
    SELECT RAISE(ABORT,
        'An active relationship already exists for this from/to/edge_type. '
        || 'Close the existing record (set valid_to) before inserting a new version.')
    WHERE EXISTS (
        SELECT 1 FROM relationships
        WHERE from_id      = NEW.from_id
          AND to_id        = NEW.to_id
          AND edge_type_id = NEW.edge_type_id
          AND valid_to IS NULL
    );
END;


-- =============================================================================
-- UTILITY QUERIES (saved as comments for reference)
-- =============================================================================

-- All roles Nvidia plays across the network:
-- SELECT from_name, edge_label, to_name, amount_usd_b, stake_pct
-- FROM relationships_current WHERE from_id = 'nvidia' OR to_id = 'nvidia';

-- All relationships between two specific entities (the "incest check"):
-- SELECT edge_label, amount_usd_b, stake_pct, valid_from, source
-- FROM relationships_current
-- WHERE (from_id = 'nvidia' AND to_id = 'coreweave')
--    OR (from_id = 'coreweave' AND to_id = 'nvidia');

-- Cycle detection — all nodes reachable from Nvidia via investment edges:
-- WITH RECURSIVE reach(node, path, depth) AS (
--     SELECT 'nvidia', json_array('nvidia'), 0
--     UNION ALL
--     SELECT r.to_id,
--            json_insert(rc.path, '$[#]', r.to_id),
--            rc.depth + 1
--     FROM   relationships r
--     JOIN   reach rc ON r.from_id = rc.node
--     WHERE  r.edge_type_id = 'INVESTS_EQUITY'
--       AND  r.valid_to IS NULL
--       AND  NOT EXISTS (SELECT 1 FROM json_each(rc.path) WHERE value = r.to_id)
--       AND  rc.depth < 8
-- )
-- SELECT node, path, depth FROM reach ORDER BY depth;
