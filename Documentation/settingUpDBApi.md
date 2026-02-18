# Setting Up API for PostgreSQL Database

## Step 1: Set up schema for API

```sql
CREATE SCHEMA IF NOT EXISTS api;
```

## Step 2: Set up Views for API

```sql
CREATE OR REPLACE VIEW view_name.api AS
SELECT
    atts
FROM
    tables;
```