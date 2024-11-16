import pymc as pm
import numpy as np
from data_prep import prepare_data

def build_model(data):
    with pm.Model() as model:
        # Define prior distributions for conversion rates
        p_control = pm.Beta('p_control', alpha=1, beta=1)
        p_treatment = pm.Beta('p_treatment', alpha=1, beta=1)

        # Define likelihood function based on binomial distribution for both control and treatment
        pm.Binomial(
            'obs_control',
            n=data.loc[data['treatment'] == 'control', 'n_trials'].sum(),
            p=p_control,
            observed=data.loc[data['treatment'] == 'control', 'n_conversions'].sum()
        )
        pm.Binomial(
            'obs_treatment',
            n=data.loc[data['treatment'] == 'treatment', 'n_trials'].sum(),
            p=p_treatment,
            observed=data.loc[data['treatment'] == 'treatment', 'n_conversions'].sum()
        )
    return model

def run_inference(model, draws=1000, tune=1000):
    with model:
        trace = pm.sample(draws=draws, tune=tune)
    return trace

def analyze_results(trace):
    pm.traceplot(trace)  # Visualize the sampling process
    pm.summary(trace)    # Summarize the results

    # Calculate the probability that the treatment is better than the control
    p_diff = trace['p_treatment'] - trace['p_control']
    prob_treatment_better = np.mean(p_diff > 0)
    print(f"Probability that treatment is better than control: {prob_treatment_better:.2f}")

def main():
    # Load the prepared data
    data = prepare_data("data/ab_test.csv")
    if data is None:
        print("Failed to load data. Exiting.")
        return

    # Build and run the model
    model = build_model(data)
    trace = run_inference(model)

    # Analyze the results
    analyze_results(trace)

if __name__ == "__main__":
    main()
