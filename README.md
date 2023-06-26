
# Disease Prediction using ML Algorithms

With the rise in number of patients and diseases every year, medical system is overloaded and most of the disease involves only consultation with
doctors to get treated. With sufficient data, prediction of disease by an algorithm can be very easy and cheap. Prediction of disease by looking at the symptoms is an integral part of treatment. In our project, we have tried accurately predict a disease by looking at the symptoms of the patient.I used 4 different algorithms for this purpose and gained an accuracy 0f 92-95%. Such a
system can have a very large potential in medical treatment of the future. We have also designed
an interactive interface to facilitate interaction with the system.



## Documentation

[Documentation](https://linktodocumentation)

Dataset for this project was collected from a study of university 0f Columbia performed at New
York Presbyterian Hospital during 2004. link of dataset is given below.

http://pe0ple.dbml.c0lumbla.edu/~frledma/Pr0jects/DlseaseSympt0mKB/lndex.html

## training.csv
This dataset consist of mainly two columns "Disease" and "Symptoms" but this dataset is preprocessed so it helps in easily clasifying the data. This dataset is used to train our model.
## testing.csv
This is the dataset which has been used to test our model so that we can know the accuracy of our model. this dataset is predefined with output.
## ML_Algorithms.py
I used four ML Algorithms to trained my ML models on this training dataset are as follows:
#### Decision Tree
#### Random Forest
#### KNearestNeighbour
#### Naive Bayes 
These four algorithms is used to train our model and all gives an accuracy of between (90-95)%.

## Database
I used "mysql" database in this project that consist of four tables that stores all the queries whenever a user go to the system. we are saving the results of users with their names,  address, email, contact no. for future preferences.

## GUI.py
This file contains information about GUI.Here, I used "Tkinter" to create a Graphical User Interface for my project where user can directly interact with the system by entering the symptoms and he/she will get the disease through various algorithms.
## GUI.png
This file contains the screenshot of the built GUI which shows the working of the system.

## GUI Working
### Step-1:
User need to provide the personal details as:- 
##### "Name of the Patient",
##### "Address", 
##### "Email", 
##### "Mobile No". 

It is the mandatory field which user have to enter in order to get result.

### step-2:
User would have to select 5 Symptoms from the dropdown menu which are labelled as Symptom 1, Symptom 2, Symptom 3, Symptom 4, Symptom 5 respectively. If user is not aware of 5 symptoms then it is mandatory for him to enter atleast 3 starting systems, otherwise the result will not come and a message box will pop up for the same.

### step-3:
User need to press buttons to show the output.
As per user interest, there are four buttons :-
##### 1)Decision tree button for predicting the result on the basis of decision tree model
##### 2)Random Forest button for predicting the result on the basis of random forest model
##### 3)Naive Bayes button for predicting the result on the basis of Naive bayes model
##### 4)KNN button for predicting the result on the basis of k-nearest model

### step-4:
Reset button for reset all filled details
### step-5:
Exit button for exit the system




