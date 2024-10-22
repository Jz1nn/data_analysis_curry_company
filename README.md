# 1. Business problem

Cury Company is a technology company that created an app that connects restaurants, delivery people and people.

Through this app, you can order a meal from any registered restaurant and have it delivered to the comfort of your home by a delivery person also registered in the Cury Company app.

The company does business between restaurants, delivery people and people, and generates a lot of data about deliveries, types of orders, weather conditions, delivery people's ratings, etc. Although delivery is growing, in terms of deliveries, the CEO does not have complete visibility of the company's growth KPIs.

You were hired as a Data Scientist to create data solutions for delivery, but before training algorithms, the company needs to have the main strategic KPIs organized in a single tool, so that the CEO can consult and make simple but important decisions.

Cury Company has a business model called Marketplace, which acts as an intermediary between three main customers: Restaurants, delivery people and buyers. To track the growth of these businesses, the CEO would like to see the following growth metrics:

## On the company side:

1. Number of orders per day.
2. Number of orders per week.
3. Distribution of orders by traffic type.
4. Comparison of order volume by city and traffic type.
4. Number of orders per delivery person per week.
5. Central location of each city by traffic type.

## On the delivery person side:

1. Youngest and oldest age of delivery people.
2. Worst and best condition of vehicles.
3. Average rating per delivery person.
4. Average rating and standard deviation by traffic type.
5. Average rating and standard deviation by weather conditions.
6. Top 10 fastest delivery people by city.
7. Top 10 slowest delivery people by city.

## On the restaurant side:

1. Number of unique delivery people.
2. Average distance between restaurants and delivery locations.
3. Average delivery time and standard deviation by city.
4. Average delivery time and standard deviation by city and order type.
5. Average delivery time and standard deviation by city and traffic type.
6. Average delivery time during festivals.

The goal of this project is to create a set of graphs and/or tables that display these metrics in the best possible way for the CEO.

# 2. Assumptions assumed for the analysis

1. The analysis was performed with data between 02/11/2022 and 04/06/2022.
2. Marketplace was the assumed business model.
3. The 3 main business views were: Order transaction view, restaurant view, and delivery person view.

# 3. Solution Strategy

The strategic dashboard was developed using metrics that reflect the 3 main views of the company's business model:

1. Company growth view
2. Restaurant growth view
3. Delivery driver growth view

### Each view is represented by the following set of metrics.

1. Company growth view
- a. Orders per day
- b. Percentage of orders by traffic conditions
- c. Number of orders by type and city.
- d. Orders per week
- e. Number of orders by delivery type
- f. Number of orders by traffic conditions and city type

2. Restaurant growth view
- a. Number of unique orders.
- b. Average distance traveled.
- c. Average delivery time during festival and normal days.
- d. Standard deviation of delivery time during festival and normal days.
- e. Average delivery time by city.
- f. Distribution of average delivery time by city.
- g. Average delivery time by order type.

3. Insight into delivery driver growth
- a. Age of oldest and youngest delivery driver.
- b. Rating of best and worst vehicle.
- c. Average rating per delivery driver.
- d. Average rating by traffic conditions.
- e. Average rating by weather conditions.
- f. Average time of fastest delivery driver.
- g. Average time of fastest delivery driver by city.

# 4. Top 3 Data Insights

1. The seasonality of the order quantity is daily. There is a variation of approximately 10% in the number of orders on consecutive days.
2. Semi-Urban cities do not have low traffic conditions.
3. The greatest variations in delivery time occur during sunny weather.

# 5. The final product of the project

Online dashboard, hosted in a Cloud and available for access on any device connected to the internet.

The dashboard can be accessed through this link: https://johnwln-curry-company.streamlit.app/

# 6. Conclusion

The objective of this project is to create a set of graphs and/or tables that display these metrics in the best possible way for the CEO.

From the Company's perspective, we can conclude that the number of orders grew between week 06 and week 13 of the year 2022.

# 7. Next steps

1. Reduce the number of metrics.
2. Create new filters.
3. Add new business views.
