import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


##importing covid19 dataset

corona_dataset_csv = pd.read_csv('Covid19_Confirmed_dataset.csv')
print(corona_dataset_csv.head(10))
#We will notice data is from 22 January 2020 to 30 April 2020

##check the shape of the dataframe
print(corona_dataset_csv.shape)    #Tuple with 266 rows and 104 columns
columns = corona_dataset_csv.columns
print(columns)

##Delete the useless columns
#Latitude and Longitude are not important features for us here
corona_dataset_csv.drop(["Lat",
                        "Long"],
                        axis=1,
                        #default value, annotation axis=0 which is equal to rows
                        inplace = True   #will change the corona dataset too )

print(corona_dataset_csv.head(10))


##Aggregating the rows by the country
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()

print(corona_dataset_aggregated.head())
#After aggregation, the index of the df is the column at which we aggregated
print(corona_dataset_aggregated.shape)
#we have 187 countries, 100 dates

##Visualizing data related to a country for example China

print(corona_dataset_aggregated.loc["China"])
#will return pandas series

##Calculating a good measure
corona_dataset_aggregated.loc['China'].plot()
print(corona_dataset_aggregated)
#will plot the values on different date
corona_dataset_aggregated.loc['Egypt'].plot()
plt.legend()
corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc['Italy'].plot()
corona_dataset_aggregated.loc['Spain'].plot()
plt.legend()
#Spread of the virus in China for the first 3 dates only
corona_dataset_aggregated.loc['China'][:3].plot()

##caculating the first derivative of the curve
corona_dataset_aggregated.loc["China"].diff().plot()

##Find max inflection rate for china

corona_dataset_aggregated.loc["China"].diff().max()
#In only 24 hrs, the difference was 15136

corona_dataset_aggregated.loc["Italy"].diff().max()
#In only 24 hrs, the difference was 6557

corona_dataset_aggregated.loc["Spain"].diff().max()
#In only 24 hrs, the difference was 9630

##find maximum infection rate for all of the countries.

countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for c in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
max_infection_rates

corona_dataset_aggregated["max_infection_rates"] = max_infection_rates

corona_dataset_aggregated.head()

## create a new dataframe with only needed column

corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rates"])

corona_data.head()

## importing the dataset

happiness_report_csv = pd.read_csv("worldwide_happiness_report.csv")

happiness_report_csv.head()

## let's drop the useless columns

useless_cols = ["Overall rank", "Score", "Generosity", "Perceptions of corruption"]

happiness_report_csv.drop(useless_cols, axis=1, inplace=True)
happiness_report_csv.head()

## changing the indices of the dataframe

happiness_report_csv.set_index("Country or region", inplace=True)

happiness_report_csv.head()

## now let's join two dataset we have prepared

corona_data.head()

corona_data.shape    #Tuple with 187 countries

## world happiness report dataset

happiness_report_csv.head()

happiness_report_csv.shape    #156 countries, less than corona data

#Inner join
data = corona_data.join(happiness_report_csv,
                how = "inner"    #method/type of join
                )
data.head()

## Correlation matrix

data.corr()

##Visualization of the results

data.head()

##Plotting GDP vs maximum Infection rate

x = data["GDP per capita"]
y = data["max_infection_rates"]
sns.scatterplot(x,y)

#We can see the values need different scaling

#Will apply log scaling to y
x = data["GDP per capita"]
y = data["max_infection_rates"]
sns.scatterplot(x,np.log(y))

#Now we can see +ve correlation

#RegPlot
x = data["GDP per capita"]
y = data["max_infection_rates"]

sns.regplot(x,np.log(y))

#Line fitted, +ve slope seen

## Plotting Social support vs maximum Infection rate

x = data["Social support"]
y = data["max_infection_rates"]

sns.scatterplot(x,np.log(y))

x = data["Social support"]
y = data["max_infection_rates"]

sns.regplot(x,np.log(y))

## Plotting Healthy life expectancy vs maximum Infection rate

x = data["Healthy life expectancy"]
y = data["max_infection_rates"]

sns.scatterplot(x,np.log(y))

x = data["Healthy life expectancy"]
y = data["max_infection_rates"]

sns.regplot(x,np.log(y))

## Plotting Freedom to make life choices vs maximum Infection rate

x = data["Freedom to make life choices"]
y = data["max_infection_rates"]

sns.scatterplot(x,np.log(y))

x = data["Freedom to make life choices"]
y = data["max_infection_rates"]

sns.regplot(x,np.log(y))






