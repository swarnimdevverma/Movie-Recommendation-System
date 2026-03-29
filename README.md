#  Movie Recommendation System

## Overview

This project is a simple Movie Recommendation System built using Python and basic Machine Learning concepts.
It suggests movies based on similarity and also allows users to explore movies by genre and mood/tags (like Netflix-style categories).

The goal of this project is to apply concepts like text processing, feature combination, and similarity measures to solve a real-world problem.

---

## Problem Statement

With so many movies available, users often struggle to decide what to watch.
Most platforms use recommendation systems, but understanding how they work is important.

This project aims to build a basic recommendation system that:

* Suggests similar movies
* Allows filtering by genre
* Allows browsing based on mood or keywords

---

## Objectives

What's interesting is * to implement a content-based recommendation system
* To understand how similarity between items works
* To create an interactive system using Python
* To make recommendations based on user input

---

## ⚙️ Features

### 1.Movie Recommendation

* Enter a movie name
* System suggests top 5 similar movies

### 2. Genre-Based Search

* Search movies by genre (e.g., Action, Comedy)
* Displays a list of movies from that category

### 3. Mood/Tag-Based Search

* Search using tags like:

  * nostalgic
  * inspiring
  * dark
  * swoon-worthy
* Mimics Netflix-style browsing

### 4.Show Available Options

* View all genres
* View all available tags

---

## Methodology

### 1. Data Preparation

* Dataset contains:

  * title
  * genre
  * overview
  * keywords
  * year

* Missing values handled using:

```python
df.fillna('', inplace=True)
```

---

### 2. Feature Engineering

All important text features are combined:

```
genre + overview + keywords
```

This creates a single text column used for analysis.

---

### 3. Text Vectorization

Used:

* **CountVectorizer**

This converts text into numerical vectors.

### 4. Similarity Calculation

Used:

* **Cosine Similarity**

This measures how similar two movies are based on their features.

### 5. Recommendation Logic

* Find selected movie index
* Compare with all other movies
* Sort based on similarity
* Return top 5 results

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* CountVectorizer
* Cosine Similarity

---

## Project Structure

```
project-folder/
│── main.py
│── data/
│     └── movies.csv
│── README.md
```

---

## How to Run

1. Install required libraries:

```
pip install pandas scikit-learn
```

2. Run the program:

```
python main.py
```

3. Use menu options to interact with the system

---

## Example Usage

* Enter movie → `Inception`

* Get recommendations like:

  * Interstellar
  * The Matrix

* Search genre → `Action`

* Browse tag → `nostalgic`

---

## Challenges Faced

* Handling text data properly
* Choosing meaningful keywords
* Making output readable
* Fixing file path and module issues

---

## Future Improvements

* Add a GUI (web app or app interface)
* Use larger real-world dataset
* Improve recommendations using TF-IDF
* Add user-based recommendation system

---

## Conclusion

Actually, this project helped in understanding how recommendation systems work at a basic level.
It shows how simple machine learning techniques can be used to build useful applications.

---

## Author

Swarnim Verma
