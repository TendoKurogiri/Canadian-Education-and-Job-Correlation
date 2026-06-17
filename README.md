# Canadian Education & Employment Analysis 

## Project Overview
[cite_start]This project provides an estimate of the impact of education on employability, financial returns, and related factors in the Canadian job market using the National Graduates Survey conducted by Statistics Canada[cite: 3]. [cite_start]By analyzing over 13,000 cases [cite: 4][cite_start], this repository highlights the role of education in shaping jobs and opportunities across different fields in Canada, while also examining the influence of immigration status[cite: 12].

## Key Findings
* [cite_start]**Financial ROI:** There is a moderate direct positive correlation (score: 0.34) between the level of study and personal income[cite: 61]. [cite_start]The regression model indicates an average increase in earnings of $12,235 per year for each level of educational attainment[cite: 68].
* [cite_start]**Employability:** The Master's and Doctorate graduates reflected an average employment rate exceeding 90%, with 45% earning over $90,000[cite: 8]. 
* [cite_start]**Labor Market Projections (2024–2033):** University students experience faster growth and 4 times the improvement compared to college students, with the achievement gap increasing by 0.87% points over 10 years[cite: 74].
* [cite_start]**Demographics:** Western Canada has the highest share, with 41.27% individuals[cite: 52]. [cite_start]Quebec represents 22.60% making it the second-largest region group[cite: 53]. 

## Technologies & Methodologies Used
* **Python (`pandas`):** Used for data manipulation, handling null values, and recoding categorical variables into numeric brackets for modeling.
* **R Markdown:** Used for 10-year predictive forecasting of student employment metrics.
* **Tableau / Data Viz:** Used for geographic mapping and visualizing key performance indicators like employment status comparisons and 10-year metrics.
* **Statistical Methods:** Descriptive statistics, Correlation Analysis, and Regression Modeling.

## Repository Contents

| Folder/File | Description |
| :--- | :--- |
| `data/processed/` | Contains the final cleaned dataset (`Education and Employment - Copy.csv`) and the subset used for R modeling (`forecast_ready_sample.csv`). |
| `scripts/data_manipulation_4.py` | Python script detailing the data cleaning and transformation pipeline. |
| `scripts/analysis.py` | Python script for additional exploratory data analysis and statistical testing. |
| `scripts/Employment_Forecasting.Rmd` | R Markdown file containing the predictive analysis and time-series forecasting for 2024–2033. |
| `docs/` | Contains the final written report and the `Graduate Data.html` profile report. |
| `visualizations/` | PNG exports of the 10-year metrics, status comparisons, and university vs. college employment trends. |

## Strategic Recommendations
* [cite_start]**Expand Work-Integrated Learning (WIL) Programs:** Promote co-op placements, internships, and paid practicums in universities and colleges[cite: 148].
* [cite_start]**Create Targeted Support for Immigrant and International Students:** Organize credentials recognition, workplace culture, and networking training, which are specific to Canada[cite: 151].
* [cite_start]**Make Academic Programmes Respond to New Trends in the Labour-Market:** Adjust the program offerings according to the results, depending on the high-growth offerings, such as technology, healthcare, and analytics[cite: 154].
