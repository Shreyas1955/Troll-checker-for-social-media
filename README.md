# Troll-checker-for-social-media

This project is a hate speech detection and rephrasing tool. It classifies comments as either "Hate Speech," "Offensive Language," or "Neither" using a fine-tuned Twitter RoBERTa model, and rephrases hate speech comments into positive comments using a Generative AI model.
Features
•	Detects hate speech and offensive language in user comments.
•	Rephrases hate speech into positive comments using a generative model.
•	Logs user comments and their classifications into a MySQL database.
•	Supports real-time comment moderation and logging.
Project structure
•	Final.ipynb: For analysis, classification, evaluation, model training
•	main.py: Entry point for the Streamlit application.
•	Login_page.py: Login page using credentials from sql database
•	User_page.py: Contains UI to input comment, check for classification and rephrasing task
•	Admin_page.py: To view logs of comments
•	model/: Contains the RoBERTa classification model.
•	labeled_data.csv: dataset used for training/testing the model.
•	social_media_platform.sql: SQL Database file 
•	README.md: Documentation and setup instructions.

Prerequisites
•	Python 3.7 or higher (if perform the training locally)
•	Memory 50gb or more
•	Google colab pro (for A100 GPU for faster model training) 
•	Xampp/MySQL for local database management
•	Google Cloud API Key for rephrasing using the Generative AI model (Paid service)






Instructions to run
Final.ipynb (Model training and evaluation)
1.	Colab setup (if running online)
•	Load the dataset into colab files 
•	Place your Google API key in secret key section of colab and name it as “GOOGLE_API_KEY”
•	Run all cells in notebook
•	The trained model will be saved locally. Download the model for further use.
2.	Local setup (if running locally)
•	Ensure that all required files (dataset, model, etc.) are in the same folder.
•	Place your Google API key in the appropriate cell.
•	Run the notebook to train and evaluate the model.

To run Front-end System on localhost
1.	Install XAMPP and MySQL:
•	Download and install XAMPP
•	Download and install MySQL
2.	Start XAMPP services:
•	Open XAMPP control panel and run:
•	Apache 
•	MySQL
3.	Import database file:
•	Click on "Admin" next to the MySQL field in XAMPP.
•	Import the provided .sql file into your database in MyPHP localhost
4.	Set up the project:
•	Open the project folder in VS Code or any IDE.
•	Update MySQL credentials in main_page.py and login_page.py to match your local setup.
5.	Run the Streamlit App:
•	Execute the following command in terminal: Streamlit run main_page.py
6.	Login:
•	Use the credentials from the database (you can check phpMyAdmin for user credentials).
•	Test the system by posting comments for classification and rephrasing.
7.	View Comment Logs (Admin Access):
•	Click the three dots in the top-right corner of the Streamlit page.
•	Choose "Clear Cache" -> "Rerun".
•	Log in with admin credentials to view the comment logs.

Important Links
To download Python: https://www.python.org/downloads/
To get API key: https://ai.google.dev/gemini-api/docs/api-key (Paid)
To download Xampp: https://www.apachefriends.org/download.html 
To download MySQL: https://www.mysql.com/downloads/ 

Notes
•	You will need a Google Cloud API Key to use the rephrasing model. Obtain the key from the Google Cloud Console and insert it where required in the code.
•	Ensure that the XAMPP Apache and MySQL services are running before attempting to launch the app.

