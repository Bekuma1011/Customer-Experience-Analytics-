# Bank Customer Reviews Sentiment Analysis

## Overview

This project analyzes customer reviews of multiple banks to uncover sentiment trends and actionable insights using Natural Language Processing (NLP) techniques. The workflow is broken down into multiple tasks, each focused on a specific part of the data pipeline.



##  Task 1: Data Collection & Cleaning

### Description:
- Collected raw customer reviews from bank platforms or provided CSV sources.
- Cleaned the data by removing duplicates, nulls, and irrelevant characters.
- Standardized columns for consistency: `review`, `rating`, `date`, `bank`.

### Outputs:
- `raw_data.csv` (initial version)
- `cleaned_data.csv` (after preprocessing)

##  Task 2: Sentiment Analysis & Labeling

### Description:
- Applied **VADER Sentiment Analysis** to determine sentiment polarity of each review.
- Added new columns:
  - `sentiment_label`: Categorized as "positive", "neutral", or "negative"
  - `sentiment_score`: Compound score from VADER

##  Task 3: Oracle Database Integration

### Description:
- Designed and created an Oracle database schema:
  - `Banks` table (`bank_id`, `bank_name`)
  - `Reviews` table with foreign key to `Banks`
- Loaded sentiment-labeled data into Oracle XE (21c) using `Oracledb`