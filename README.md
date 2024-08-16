# Panel Study of Income Dynamics (PSID) Dataset

## Overview

The Panel Study of Income Dynamics (PSID) is a longitudinal dataset that tracks the economic, social, and health-related characteristics of individuals and families over time. This dataset spans from 1987 to 1996 and includes information from individuals who have consistently been the head of their family unit throughout this period.

## Time Period

- **Start Year:** 1987
- **End Year:** 1996

## Inclusion Criteria

- The dataset includes only individuals who were consistently the head of their family unit during the entire time period from 1987 to 1996.

## Data Formats

### Long Format

In the long format, the dataset is structured as follows:

- **Feature Columns:** Include various characteristics and attributes of the individuals.
- **Year Column:** A column representing the year of observation.
- **Number of Rows:** The total number of rows is equal to the number of unique individuals multiplied by the number of years (10 years).

**Example of Long Format:**

| ID_indiv | Year | Age | Income | Employment_Status |
|----------|------|-----|--------|-------------------|
| 001      | 1987 | 45  | 50000  | Employed          |
| 001      | 1988 | 46  | 52000  | Employed          |
| ...      | ...  | ... | ...    | ...               |
| 001      | 1996 | 54  | 60000  | Retired           |

### Wide Format

In the wide format, the dataset is structured as follows:

- **Feature Columns:** Each feature column from the long format is appended with the year (e.g., `Income_87`, `Income_88`, ..., `Income_96`).
- **Number of Rows:** The number of rows is equal to the number of unique individuals (one row per individual).

**Example of Wide Format:**

| ID_indiv | Age_1987 | Age_1988 | ... | Age_1996 | Income_1987 | Income_1988 | ... | Income_1996 |
|----------|----------|----------|-----|----------|-------------|-------------|-----|-------------|
| 001      | 45       | 46       | ... | 54       | 50000       | 52000       | ... | 60000       |
| 002      | 38       | 39       | ... | 48       | 45000       | 47000       | ... | 55000       |

## Data Access

The dataset can be accessed in both long and wide formats depending on the analysis requirements. 

## Usage

- **Long Format:** The long format is suitable for obtaining the utility metrics report

- **Wide Format:** the wide format is used to run the synthesizers.

The python scripts to convert long to wide format and wide to long format is provided.

For more information on the dataset and detailed descriptions of the features, please refer to the accompanying data dictionary.
