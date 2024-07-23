
# Water Quality and Well Construction Feasibility Prediction

This project aims to predict water quality and the feasibility of well construction based on latitude and longitude inputs using a pre-trained multioutput XGBoost model. The web application is built using Flask and provides two main functionalities: predicting water quality and assessing the feasibility of well construction.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This web application allows users to predict the quality of water and the feasibility of constructing a well at a given geographical location. By entering the latitude and longitude, the model provides insights into various water quality parameters and determines whether constructing a well is feasible based on specific chemical thresholds.

## Features

- Predict water quality parameters such as pH level, electrical conductivity, and TDS content.
- Assess the feasibility of constructing a well based on CO3 and SO4 content.
- User-friendly interface with separate routes for each functionality.
- Results are displayed directly on the web page.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/water-quality-prediction.git
   cd water-quality-prediction
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the `multioutput_xgboost_model.pkl` file in the project directory.

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Use the forms on the home page to navigate to the water quality prediction or well construction feasibility pages.

## Project Structure

```
water-quality-prediction/
├── templates/
│   ├── index.html
│   ├── predict.html
│   └── feasible.html
├── app.py
├── multioutput_xgboost_model.pkl
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgements

- [XGBoost](https://xgboost.readthedocs.io/)
- [Flask](https://flask.palletsprojects.com/)
- [Joblib](https://joblib.readthedocs.io/)

---

