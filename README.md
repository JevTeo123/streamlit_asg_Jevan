# Project Title
The purpose of this project is to query data from the snowflake database and create a customer segmentation model using the data to classify whether the customers are high or low spenders using a machine learning model. A streamlit app is then created, revolving around the machine learning model that allows users to enter specific customer behaviors to see if the customer is a high or low spender.

# Table of Contents

- [Project Title](#project-title)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)

# Installation
To run the ipynb notebook, users can pip install all the required dependencies from the ```requirements.txt``` file.
```py
conda env create <project_name>
pip install -r requirements.txt
```

Credentials have to be replaced in the ipynb file to retreive contents from the database.
```py
accountname = getpass.getpass("Enter account name")
username = getpass.getpass("Enter Username")
password = getpass.getpass("Enter Password")
connection_parameters = {
  "account": accountname,
  "user": username,
  "password": password,
  "role": "SYSADMIN",
  "database": "FROSTBYTE_TASTY_BYTES",
  "warehouse": "COMPUTE_WH",
  "schema": "RAW_POS"
}
session = Session.builder.configs(connection_parameters).create()
```

# Usage
[(Back to top)](#table-of-contents)

The model has already been pickled and readily available in the github. To see how customer behaviour affects how they are a high or low spender, this [streamlit](https://appasgjevan-m6wynvdt6f62d3xd2x28em.streamlit.app/) app can be used to accomplish this task. 
![image](https://github.com/JevTeo123/streamlit_asg_Jevan/assets/123255675/59ce2195-9019-44d4-8990-78ca09ead525)
The first page of the streamlit app shows the purpose of the streamlit app as well as a sidebar to toggle between the different pages.
![image](https://github.com/JevTeo123/streamlit_asg_Jevan/assets/123255675/af16a723-3212-49cb-adfe-29b8f76bd1be)
The second page contains the input boxes where users can enter in different values to mimic different customer behaviours and see how they affect whether a customer would be a high or low spender. This page also gives users a retrospective view as to the possible areas where these types of customers can be found to maximize on profits.
![image](https://github.com/JevTeo123/streamlit_asg_Jevan/assets/123255675/8c558946-36c3-441b-bfd5-a4c9a6d4a7ba)
The third page contains some distinct insights that can be derived from the data about how the different inputs might cause a customer to be a high or low spender.

