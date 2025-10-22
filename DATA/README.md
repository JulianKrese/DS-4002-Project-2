# Metadata
# Data Summary 
This dataset was created to investigate the research question: Can we predict when and where someone is most likely to receive a ticket in the City of Charlottesville? It captures details and information (date, street name, time, and violation description) about parking tickets that were given out in Charlottesville. 

The dataset enables statistical and machine learning analysis to identify temporal and spatial trends in parking enforcement, such as when and where tickets are most likely to occur. 
- Initial Data: The dataset is stored in a CSV downloaded from the City of Charlottesville Open Data Portal.
- Final Data: The model will be able to predict given a details of someone parking and the probabilities of the prediction will be stored in CSV files for each time period tested. 

# Provenance
The data was collected through an ETL pipeline, where we trained the models and evaluated them.
Beginning with the loading, we must retrieve
our data, which is found at the Charlottesville Open Data Portal [1]. Multiple forms are available, but a CSV file fits our use case the best. Data preprocessing involves removing columns that we are not going to be using (AppealDate, AppealGrantedDate, AppealStatus, Location, LicensePlateAnonymized, LicenseState, TicketNumber, BlockNumber, WaiverGrantedDate, WaiverRequestDate, and WaiverStatus), cleaning inconsistent timestamps, standardizing address formats, and removing incomplete or erroneous entries. The loading stage will involve splitting and storing the cleaned dataset into multiple
groups for training and testing our models. Our data will be split into time frames related to each model we want to train. One will include “all-time” data from 2000-2023, one “recent-time” only
consisting of 2023, and the rest will be chunks of 5 years from 2023 and back (2023-2018,2018-2013, etc.). Additionally, we will need to store our testing data, which will be all of 2024.
After our data is split by time frames into their own sets, we can store each file. The reason for this strange split is that we want a predictive model that is accurate currently, but it's unreasonable within our scope to try and account for unknown factors, like when cars park, when we only have the ticketing data. So, if our model is accurate on the most recent data, it would likely be accurate on any new data, which is why we're saving the 2024 data as our testing data. Once the data is processed, we trained the model once each time frame using isolation forest [4]. 

# License 
Our data license is the Attribution 4.0 International Deed, which allows us to share and adapt our data while giving credit to the City of Charlottesville [1]. This means that our group can utilize, visualize, and publish insights from the dataset for educational and research purposes, as long as the original data source is properly credited

# Ethical Statements 
Our dataset is fully anonymized and publicly available through the City of Charlottesville’s Open Data Portal. It does not include any personally identifiable information, and the license plates are completely anonymized. Because the dataset is published under the
Attribution License, it is both legal and ethical to use it for research and educational purposes as long as attribution is given to the City of Charlottesville [1]. Our analysis intends to promote
awareness and transparency in parking policy– not to encourage rule-breaking. 
# Data Dictionary 
<img width="601" height="436" alt="Screenshot 2025-10-22 at 3 45 33 PM" src="https://github.com/user-attachments/assets/a98ad060-51ea-496e-8c6f-bfc5c5078a54" />


# Explanatory Plots 
<img width="591" height="368" alt="Screenshot 2025-10-22 at 3 46 00 PM" src="https://github.com/user-attachments/assets/8bbeb01d-db0d-4ca8-bd83-60a4e2d9083a" />
<img width="576" height="356" alt="Screenshot 2025-10-22 at 3 46 23 PM" src="https://github.com/user-attachments/assets/6915b451-961b-4004-96c5-35637fa0a32e" />

# References 
[1] “Parking Tickets.” City of Charlottesville, 2017. https://opendata.charlottesville.org/datasets/0ae373f4c2884abbb296500125bb9d8a_7/explore. 

[2] GeeksforGeeks. 2025. “Evaluation Metrics in Machine Learning.” GeeksforGeeks. July 15, 2025. https://www.geeksforgeeks.org/machine-learning/metrics-for-machine-learning-model/.

[3]“6.3. Preprocessing data — scikit-learn 0.22.2 documentation,” scikit-learn.org. https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features

[4] Anon. IsolationForest. Scikit-learn. https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html.
