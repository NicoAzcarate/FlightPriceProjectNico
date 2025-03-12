# FlightPriceProjectNico

Flight Pricing Project - Nicolás Azcárate

Dataset: https://www.kaggle.com/datasets/dilwong/flightprices/data

My project is focused on Flight Booking Optimization, helping users find the best flights to book.

The main idea is to suggest the best flights based on user preferences (e.g., cheapest, fastest, best deal). To do so, I will:
    - Compare flights from different airlines and routes.
    - Identify trends in pricing based on historical data.
    - Provide users with insights on the best flights to book.

Workflow:

1. Data Exploration and Preprocessing:
    - Load and explore data
    - Handel/convert/clean data...
2. Splitting data into training and testing sets.
    - Training set (80%) → Used to train the model.
    - Testing set (20%) → Used to evaluate accuracy.
3. Use Machine Learning models such as:
    - Supervised learning to predict flight prices and recommend best times to buy.
    - Unsupervised learning to cluster flights into groups.
4. Create a Recommendation System for the users:
    - Implement sorting-based recommendations such as Cheapest flights, Fastest flights, Best deal flights using weighted scores...
    - Implement clustering-based recommendations using different clustering methods to group flights into Budget-friendly, Premium (fast, non-stop, best airline), Balanced...
5. Optimize model performance
