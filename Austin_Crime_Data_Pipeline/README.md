<h2> This project contains a pipeline using python </h2>

<h4>This was my final project for the Datatalks Bootcamp</h4>

<h5>The data was collected from <a href="https://data.austintexas.gov/Public-Safety/2016-Annual-Crime-Data/8iue-zpf6/about_data">Austin Crime Data </a> </h5>
<p>This pipeline downloads CSV files from the Austin Texas Government public Safety page. The table is then cleaned in Jupyter Notebooks using pandas and then passed to Google Cloud Storage</p>
<p>The cleaned csv files will then be extracted to Mage AI in which it will further undergo more transformations before being loaded to Big Query.</p>
<p>From Big Query, I will use DBT to transform the tables using SQL and then use LOOKER for visualization.</p>
<p></p>
<p>This dataset monitors Part 1 crimes which are murder, rape, robbery, aggravated assault, burglary, larceny, motor vehicle theft, human trafficking and arson in Austin Texas. It monitors the increase and decrease of Part 1 crimes from January 1st 2015 until December 31st 2016. We can compare the information in the dataset to policies that were implemented in Austin and how those policies impacted the community when it comes to Part 1 crimes. The information will be analyzed and used to make suggestions on how to decrease certain Part 1 crimes in Austin Texas.</p>
