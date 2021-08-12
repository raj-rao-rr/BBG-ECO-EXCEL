### Bloomberg Economic Release Parser

## 1	Introduction
We provide a script and accompanying excel file to pull U.S. economic release information from Bloomberg.

## 2	Software Dependencies
* Python 3.6 with the following libraries (Pandas, Numpy, Time)
*	Bloomberg Professional Services for historical data

## 3	Code Structure

### 3.1 	`Input`
* `ECO_RELEASES.xslx` which contains Bloomberg formulas designed to automatically pull economic release information (e.g. US Nonfarm Payrolls). This spreadsheet is updated if and only if a Bloomberg Terminal is active.      

### 3.2 	`Output`
* `bloomberg_economic_releases.csv` which contains the cleaned series of economic variables organized from oldest to most recent.

## 4	Running Code

Our code file runs exclusive from our single python script `bbg_eco.py`. This script can be run via IDE or terminal, provided correct Python compiler location is provided from the header.  

1. Open the `ECO_RELEASES.xslx`, go to the Bloomberg tab on Excel and click the Refresh Worksheets icon to update the Bloomberg formulas, populating the data fields. 
2. Run the `bbg_eco.py` to produce the cleaned series stored under the `Output` folder. Refer to the table below for a sample output. 

| RELEASE_DATE   | TICKER         | NAME                                                                        | ACTUAL_RELEASE | ECO_RELEASE_DT | BN_SURVEY_MEDIAN | BN_SURVEY_AVERAGE | BN_SURVEY_HIGH | BN_SURVEY_LOW | FORECAST_STANDARD_DEVIATION | BN_SURVEY_NUMBER_OBSERVATIONS | RELEVANCE_VALUE | SURPRISES | ZSCORE       |
|----------------|----------------|-----------------------------------------------------------------------------|----------------|----------------|------------------|-------------------|----------------|---------------|-----------------------------|-------------------------------|-----------------|-----------|--------------|
| 1/20/2000 0:00 | INJCJC Index   | US Initial Jobless Claims SA                                                | 272            | 20000120       | 295              | 293.6             | 310            | 284           | 6                           | 23                            | 97.6378         | -23       | -3.833333333 |
| 1/20/2000 0:00 | OUTFGAF Index  | Philadelphia Fed Business Outlook Survey Diffusion Index General Conditions | 9.1            | 20000120       | 12               | 11.73             | 18             | 4.2           | 3.2                         | 28                            | 77.4803         | -2.9      | -0.90625     |
| 1/25/2000 0:00 | CONCCONF Index | Conference Board Consumer Confidence SA 1985=100                            | 144.7          | 20000125       | 142.5            | 142.13            | 147            | 138           | 1.8                         | 35                            | 93.7008         | 2.2       | 1.222222222  |

## 5	Possible Extensions
* Extend the number of economic variables being examined
* Expand on the number of countries being examined/retrieved 

## 6	Contributors
* [Rajesh Rao](https://github.com/Raj9898) (Sr. Research Analyst)  
