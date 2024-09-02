
# Movie Recommender System TMDB Dataset

This project is a movie recommender system that suggests movies based on user preferences. The recommendation system is built using machine learning techniques and leverages The Movie Database (TMDB) API to fetch movie details such as posters.

Project Overview
The movie recommender system consists of two main components:

Data Processing and Model Training: Implemented in the Jupyter Notebook Movie Recommender System.ipynb, this component involves loading the movie dataset, preprocessing the data, and training the recommendation model.

Web Application: Built with Streamlit in app.py, this component provides an interactive web interface for users to input their preferences and receive movie recommendations.

Features
Content-Based Filtering: Recommends movies based on similarities in movie content.
Collaborative Filtering: Uses user behavior to suggest movies similar users have liked.
API Integration: Fetches movie posters and details using the TMDB API.
Installation
To run this project locally, follow these steps:

Clone the repository: 
cd movie-recommender-system
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the TMDB API key:

Obtain an API key from The Movie Database.
Replace the placeholder API key in app.py with your actual API key.
Usage
Run the Jupyter Notebook:

Open Movie Recommender System.ipynb in Jupyter Notebook or Jupyter Lab.
Run all cells to preprocess data and train the model.
Launch the Streamlit App:

bash
Copy code
streamlit run app.py
Interacting with the Web App:

Open your web browser and navigate to the URL provided by Streamlit.
Enter your movie preferences to receive personalized movie recommendations.
Project Structure
app.py: The main file for the Streamlit web application.
Movie Recommender System.ipynb: Jupyter Notebook containing the data processing, feature engineering, and model training code.
requirements.txt: List of Python libraries required to run the project

