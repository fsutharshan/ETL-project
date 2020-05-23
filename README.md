# ETL-Project Documentation:

In this project we combined a datasource that quantifies the happiness of a country 
with a datasource that provides metrics that might affect the happiness of a country.
Then we upload this combined dataset to a Heroku remote database.


## Extract:
The data was extracted from the following sources as CSV files

* UN Country Data:
https://www.kaggle.com/sudalairajkumar/undata-country-profiles

* World happiness Report:
https://www.kaggle.com/unsdsn/world-happiness.

* World Happiness Data Set ---> 2019.csv
* Country Profile Data Set ---> country_profile_variables.csv


## Transform:
Loaded the csv files into seperate dataframes in Pandas. Using a jupyter notebook (Transform_jtp.ipynb)
There were mismatches in the country names in both dataframes.This was fixed by using 
 country_converter python library.
The two datasets were merged to form one dataframe, joined by country name.
The merged dataframe were looped through to generate SQL "insert" statement and write to an output files by regions (one .sql file per region). 
These files were placed under regiontables/ subfolder.


## Load:
Created a new remote database to store the data extracted and transformed above.
Creted a schema to match the necessary data that need to be loaded (some unnecessary data columns were not included).
Only one table named world_happiness is created in the target database.

Created a python script  (postgres_remote.py ) to load all the "insert" scripts to the table in the database.
This python script is written in such a way every .sql script is executed against the target database by looping through 
all the files in regiontables subfolder.

