# inflation_prediction_model

## Objective	

To build upon our knowledge and interest of world inflation this team has used data modeling and machine learning to predict future inflation trends globally. This model can use the year, GDP, interest rate, and unemployment rate to predict whether a country will experience inflation at 85% accuracy. This model is useful in a civic capacity where it can prepare a country for economic flux. 

## Requirements

* Python, Anaconda Prompt, Jupyter Notebook, pgAdmin4, Visual Studio Code, Tableau
* Packages: pandas, numpy, sklearn, matplotlib, pickle, sqlalchemy, config, 
* Algorithms: Random Forest Classifier

### How the code works:
1.	Run the initial imports required in the jupyter notebook. 
2. 	Import the csv file in jupyter notebook
3.	Use ETL to clean the data and load into the SQL database using pgAdmin4.
4.	Run the random forest classifier model in the jupyter notebook and use Pickle to save the model.
5.	Run the app.py file in anaconda prompt and use the link to open the webpage.
6.	Enter the data required for prediction and click on predict. 

## Random Forest Classifier Model 

Using the supervised learning model Random Forests, our data was analyzed through a method of creating various decision trees and having the models learn off themselves to create optimum accuracy. In the case of this model and demonstration, 500 n_estimators or decision trees were generated with our learning model. The more decision trees trained and learned the higher the probability the accuracy score can be dependable. Once the classification model was established, a Confusion Matrix is used to test the accuracy of predictions against the original dataset. Again, this model was executed at an 85% accuracy rate.

## Why use this product?

The model was created with economists, policy makers, citizens, and data developers in mind so they can leverage historical data to make the best forecast on economic wellbeing. The data used in the model is plentiful, trained, and tested. With educated input and foresight on the users end they can utilize the product to make a useful prediction which will impact livelihoods globally. Will there be inflation in Vietnam in the year 2070 with an employment rate of 7%? And how about those same inputs in Tanzania? The inflation prediction model is individualized with the categorical data of all 141 countries giving the most personalized predictions per trained data. 

## Resources 

Dataset Source: https://www.kaggle.com/code/kimmik123/inflation-interest-rate-and-unemployment/input?select=inflation+interest+unemployment.csv

### The Team
* Kim, Olivia
* Loprimo, Katherine
* Montalva, Romy
* Owens, Amber
* Patel, Avani
* Rose, Amanda
