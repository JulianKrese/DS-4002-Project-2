# DS-4002-Project-2
## We Hate Tickets - A ticket prediction model for Charlottesville VA
This project analyzes the Charlottesville Open Data Portal to train various models based on different time frames of tickets within the city. In the end, we arrived at one final model that had the greatest accuracy at ----**TBD**----%, which was trained on the ----****TBD**----** time frame.

## Contents
* **`/SCRIPTS`**: Reusable code for data pulls, cleaning, modeling, plotting.
* **`/DATA`**: All data states, including intial and final.
* **`/OUTPUT`**: Final figures and metrics used in the write-up, as well as figures from MI2.

## Software and Platform
**Software stack**

* **Language:** Python 3.10+ (tested on 3.11)
* **Environment:** VS Code
* **Package manager:** `pip` (Conda optional)

**Key Python packages**

* Standard Library: `EXAMPLE`, ----**TBD**----
* External: `EXAMPLE`, ----**TBD**----

> Install all via `pip install -r requirements.txt`.

**Platform used for development**

* **macOS** (Apple Silicon/Intel)
  The project also works on Windows with the same Python packages.

## Documentation Map
Below is the project's folder structure.

```
DS-4002-Project1-GPT-6.0
├── DATA/                                   : includes all data
│   ├── Final/                                  : final data
│   │   └── ____                                    : ----**TBD**----
│   ├── Initial/                                : initial data
│   │   └── ____                                    : ----**TBD**----
|   └── README                                  : Metadata explanation
├── OUTPUT/                                 : includes final outputs from "Analyze.py"
│   ├── Final/                                  : final scores for each user
│   │   └── ____                                    : ----**TBD**----
│   └── M12/                                    : EDA for MI2 shown in DATA/README.md
│       ├── tickets_by_day_of_week_and_street.png   : EDA chart that counts grouped occurences of parking tickets by day and week
│       └── tickets_by_day_of_week.png              : EDA chart that counts grouped occurences of parking tickets by day
├── SCRIPTS/                                : folder holding all scripts
│   ├── Analyze.py                              : final script that combines all others into a "one shot" script
│   └── ____                                    : ----**TBD**---- 
├── LICENSE.md                              : general file - MIT licensing
├── requirements.txt                        : general file - contains necessary packages
└── venv/                                   : general file - private environment specific to a user
```


## Replication Instructions


### References
[1] “Parking Tickets.” City of Charlottesville, 2017. https://opendata.charlottesville.org/datasets/0ae373f4c2884abbb296500125bb9d8a_7/explore. 
[2] GeeksforGeeks. 2025. “Evaluation Metrics in Machine Learning.” GeeksforGeeks. July 15, 2025. https://www.geeksforgeeks.org/machine-learning/metrics-for-machine-learning-model/.
[3]“6.3. Preprocessing data — scikit-learn 0.22.2 documentation,” scikit-learn.org. https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features
[4]GeeksforGeeks, “Advantages and Disadvantages of Logistic Regression,” GeeksforGeeks, Aug. 25, 2020. https://www.geeksforgeeks.org/data-science/advantages-and-disadvantages-of-logistic-regression/