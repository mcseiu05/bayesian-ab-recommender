# Bayesian A/B Testing for Personalized Product Recommendations  

This repository provides a Bayesian A/B testing framework for personalized product recommendations, developed using Python and PyCharm. By leveraging PyMC3, it continuously updates beliefs about the effectiveness of different recommendation strategies based on observed user behavior.  

## Project Goals  
- Enhance the accuracy of personalized recommendations in e-commerce.  
- Improve conversion rates by delivering more relevant product suggestions to users.  
- Develop a data-driven approach for A/B testing recommendation systems using Python.  

## Project Structure  
- **data/**: Contains sample data for the A/B testing experiment (replace with your own data).  
- **src/**: Contains Python scripts for data preparation, model implementation, and analysis.  
- **requirements.txt**: Lists the required Python libraries.  

## Getting Started  

1. **Install dependencies**:  
   Run the following command in your terminal within the project directory:  
   `pip install -r requirements.txt`

2. **Replace sample datas**:
  Update the data/ directory with your own A/B testing data.

3. **Run scripts in PyCharms**:

Open the project in PyCharm.
- Use the Run menu to execute the scripts sequentially:
- Run data_preparation.py to prepare the data.
    - Then run model.py to perform the Bayesian analysis.
    - Then run model.py to perform the Bayesian analysis.


 ## Project Overview

 The scripts in the src/ directory guide you through the following steps:

**1. Data Preparation (data_preparation.py):**
- Loads the A/B testing data from CSV files.
- Cleans and preprocesses the data.
- Prepares the data for model fitting.
**2. Bayesian A/B Testing Model (model.py):**
- Defines the Bayesian model using PyMC3.
- Specifies prior distributions for conversion rates.
- Implements the likelihood function based on a binomial distribution.
- Performs MCMC sampling to obtain posterior distributions.
- Evaluates model performance and optionally generates visualizations (visualizations can be scripted separately).


 ## Expected Outcomes
 
- A Bayesian model that continuously updates beliefs about the effectiveness of different recommendation strategies.
- Insights into user behavior and product preferences.
- Improved conversion rates through more effective personalized recommendations.
