
# Classification Problem

Its a binary Classification Problem where we need to predict whether an astronaut can reach the desired Destination or not in the outer space.

----------------

**Dataset**: Space Travel.csv

**Features (X)**:
PassengerId, HomePlanet, CryoSleep, Cabin , Destination, Age, Travel company, Name, VIP , RoomService, FoodCourt	

**Target (Y)**:
Travel Outcome

----------------

**Data Info**

RangeIndex: 8693 entries, 0 to 8692

Data columns (total 13 columns):

 | sr. no. | Column |  Non-Null | Count |  Dtype 
 |--|-----------|-------|------|------
 0  | Unnamed: 0   |   8693 | non-null |  int64
 1 |  PassengerId  |   8693 | non-null |  object 
 2 |  HomePlanet  |    8492 | non-null |  object 
 3 |  CryoSleep    |   8476 | non-null |  object 
 4  | Cabin        |   8494 | non-null |  object 
 5  | Destination  |   8511 | non-null |  object 
 6  | Age          |   8514 | non-null |  float64
 7  | Travel company | 8693 | non-null |  object 
 8  | Name          |  8493 | non-null |  object 
 9  | VIP           |  8490 | non-null |  object 
 10 | RoomService   |  8512 | non-null |  float64
 11 | FoodCourt     | 8510 | non-null | float64 
 12 | Travel Outcome | 8693 | non-null |  object 

dtypes: float64(3), int64(1), object(9)

## Features

**space_travel.ipynb**
- Exploratory Data Analysis
- Data Visualization
- Preprocessing
    - Duplicates
    - Null values
    - Categorical values
- Data Standardization 
- Modelling (making model)
        -Logisting Regression
        - Random Forest
        - SVM
        - XGBoost
        - Deep Learning Neural network model 
- Prediction
- Evaluation

**Flask API**:

GET /getpred

returns the prediction based on the given input



## Authors

- [@Abhiheet Ringe](https://github.com/hisenberggg/)

