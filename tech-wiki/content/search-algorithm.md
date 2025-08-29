---
title: "Search Algorithm"
draft: false
---

# Search Algorithm

CoLD uses PostgreSQL’s built‑in full‑text search to find relevant entries across several parts of the database with a single query.

- You can type normal words (no special operators needed).
- The search understands common word variations (e.g., decision/decisions, arbitrate/arbitration) and ignores very common words.
- Results can be narrowed by content type, jurisdiction, or theme in the interface.

## What is searched
We search multiple content types. For each type, several fields are combined into one searchable text per entry.

- Answers:
  - CoLD ID (e.g., CHE_01.1-P)
  - Answer
  - More information
  - Jurisdictions
  - Legal families
  - Linked questions
  - Themes

- HCCH Answers
  - CoLD ID (e.g., HCCH-01.1-P)
  - Adapted question
  - Position
  - Themes
  - International instruments

- Court Decisions
  - CoLD ID (e.g., CD-CHE-1020)
  - Case citation
  - English translation
  - Jurisdictions
  - Legal families
  - Themes (derived from linked questions)

- Domestic Instruments (laws/statutes)
  - CoLD ID (e.g., DI-CHE-123)
  - Title (English)
  - Official title
  - Relevant provisions
  - Full text of the provisions
  - Text from linked Domestic Legal Provisions (original + English translation)
  - Jurisdictions
  - Abbreviation
  - Linked questions

- Regional Instruments
  - CoLD ID (e.g., RI-ABC-10)
  - Abbreviation
  - Title
  - Specialists
  - Date

- International Instruments
  - CoLD ID (e.g., II-Hag-20)
  - Name
  - Specialists
  - Date

- Literature
  - CoLD ID (e.g., L-501)
  - Title
  - Author
  - Publication title
  - Abstract note
  - Publisher
  - Jurisdictions
  - Themes

Tip: Because the CoLD ID is included in the searchable text, you can paste a code like CD-CHE-1020 to go straight to a specific entry.

## How results are ordered
By default, results are ordered by relevance to your words. You can also sort by date (where a meaningful date exists for a content type).

Additional rules to improve readability:
- Answers that literally contain “No data” are pushed to the end.
- Court Decisions with a low “Case Rank” (value 5 or below) are shown after other results but still before “No data” Answers. Within those, higher rank numbers appear first.

## Filters you can use
- Content type (Answers, HCCH Answers, Court Decisions, Domestic Instruments, Regional Instruments, International Instruments, Literature)
- Jurisdiction (matches the country names shown in results)
- Theme (matches the themes shown in results)

## Why your words may still match
The search uses English stemming. That means word endings are normalized so similar forms match (e.g., “party” ~ “parties”, “decide” ~ “decision/decisions”). Very common words are ignored automatically.

## Freshness of results
Search runs on pre‑built indexes of the data and is refreshed regularly. Recent edits may take a short time to appear in search.