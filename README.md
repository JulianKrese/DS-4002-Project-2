# DS-4002-Project-2
## We Hate Tickets - A ticket prediction model for Charlottesville VA
This project analyzes the Charlottesville Open Data Portal to train various models based on different time frames of tickets within the city. In the end, we arrived at one final model that had the greatest accuracy at **96.6%**, which was trained on the **2009-2013** time frame.

## Contents
* **`/SCRIPTS`**: Reusable code for data pulls, cleaning, modeling, plotting.
* **`/DATA`**: All data states, including intial and final.
* **`/OUTPUT`**: Final figures and metrics used in the write-up, as well as figures from MI2.
* **`LICENSE`**: An MIT license for our project
* **`requirements.txt`**: Necessary package installations
* **`.gitignore`**: Ignore local python virtual environment

## Software and Platform
**Software stack**

* **Language:** Python 3.10+ (tested on 3.11)
* **Environment:** VS Code
* **Package manager:** `pip` (Conda optional)

**Key Python packages**

* Standard Library: `datetime`, `os`, `joblib`, `shutil`
* External: `pandas`, `sklearn.preprocessing (StandardScaler)`, `sklearn.ensemble (IsolationForest)`, `sklearn.metrics (accuracy_score)`, `matplotlib.pyplot (plt)`

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
│   │   └── cleaned_parking_tickets.csv             : processed parking ticket file, dropping unecessary columns and encoding catgeorical variables
│   ├── Initial/                                : initial data
│   │   └── Parking_Tickets.csv                     : un-processed parking ticket file
|   └── README                                  : Metadata explanation
├── OUTPUT/                                 : includes final outputs from "analyze.py"
│   ├── Final/                                  : -
│   │   └── models/                                 : all generated models and their corresponding scalers
│   └── M12/                                    : EDA for MI2 shown in DATA/README.md
│       ├── tickets_by_day_of_week_and_street.png   : EDA chart that counts grouped occurences of parking tickets by day and week
│       └── tickets_by_day_of_week.png              : EDA chart that counts grouped occurences of parking tickets by day
├── SCRIPTS/                                : folder holding all scripts
│   ├── clean_parking_data.py                   : a script for processing the intial data
│   ├── create_models.py                        : a script for training models on the time split
│   └── score_models.py                         : a script for scoring trained models on accuracy
├── LICENSE.md                              : general file - MIT licensing
├── requirements.txt                        : general file - contains necessary packages
└── .venv                                   : general file - private environment specific to a user
```

## Replication Instructions
1) Base Installations
    - Install Python 3.10+ and Git
        - more information can be found at https://www.python.org/downloads/ and https://git-scm.com/downloads
    - clone this repository (use the link https://github.com/JulianKrese/DS-4002-Project-2)
        - clone --> `git clone https://github.com/JulianKrese/DS-4002-Project-2`
        - enter the folder --> `cd DS-4002-Project-2`
2) Project Installations
    - Create python environment
        - macOS/Linux --> `python -m venv .venv && source .venv/bin/activate`
        - Windows --> `python -m venv .venv && .venv\Scripts\activate`
            - Note, if you are user a newer python it may be `python3 ...` for all commands
    - Install required packages
        - within the terminal, `pip install -r requirements.txt`
    - Register the Jupyter kernel (if using notebooks outside VS Code):
        - `pip install ipykernel`
        - `python -m ipykernel install --user --name=.venv`
        - alternatively, in VS code you may have to define your interpreter as the one located in your venv. 
3) Run
    - If you want to recreate all final files, within the base directory, run in order...
        1) `clean_parking_data.py` to re-create the cleaned data
        2) `create_models.py` to re-create the models on the train split
        3) `score_models.py` to re-score the models
    - View the output in `/OUTPUT/Final`, which includes the models as well as the performance in `model_performance.csv`.

### References
- [1] “Parking Tickets.” City of Charlottesville, 2017. https://opendata.charlottesville.org/datasets/0ae373f4c2884abbb296500125bb9d8a_7/explore. 
- [2] GeeksforGeeks. 2025. “Evaluation Metrics in Machine Learning.” GeeksforGeeks. July 15, 2025. https://www.geeksforgeeks.org/machine-learning/metrics-for-machine-learning-model/.
- [3]“6.3. Preprocessing data — scikit-learn 0.22.2 documentation,” scikit-learn.org. https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features
- [4] Anon. IsolationForest. Scikit-learn. https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html.
