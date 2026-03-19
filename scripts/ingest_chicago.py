-- =====================================================
-- Chicago Crime Data - Table Setup (API Ingestion)
-- =====================================================

DROP TABLE IF EXISTS chicago_crime;

CREATE TABLE chicago_crime (
    id TEXT,
    case_number TEXT,
    date TIMESTAMP,
    block TEXT,
    iucr TEXT,
    primary_type TEXT,
    description TEXT,
    location_description TEXT,
    arrest BOOLEAN,
    domestic BOOLEAN,
    beat INTEGER,
    district INTEGER,
    ward INTEGER,
    community_area INTEGER,
    year INTEGER,
    latitude NUMERIC,
    longitude NUMERIC
    fbi_code TEXT,
    x_coordinate NUMERIC,
    y_coordinate NUMERIC,
    updated_on TIMESTAMP,
    geom GEOMETRY(Point, 4326)
);

-- =====================================================
-- Notes
-- =====================================================

-- Data is ingested via Python using the Chicago Open Data API:
-- https://data.cityofchicago.org/resource/ijzp-q8t2.csv

-- =====================================================
-- Validation
-- =====================================================

SELECT COUNT(*) FROM chicago_crime;

SELECT MIN(date), MAX(date) FROM chicago_crime;

CREATE INDEX idx_crime_date ON chicago_crime (date);
CREATE INDEX idx_crime_district ON chicago_crime (district);
CREATE INDEX idx_crime_beat ON chicago_crime (beat);
