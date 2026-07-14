# ADse-UFPM
Code and data for the ADse-UFPM model

## Overview

ADse-UFPM is an Adaptive Socio-Ecological Urban Forest Management framework developed for park-scale simulation and assessment.

The model operates at an annual time step and integrates ecological processes, management interventions, visitor dynamics, community engagement, regulatory conflict, climate variability, and climate-extreme disturbances.

This repository contains the model code, parameter files, case-study input data, climate-scenario files, and simulation results for four urban forest park cases in China.

## Case Studies

The repository includes four case-study folders:

- `Beijing/`: Beijing case
- `Chengdu/`: Chengdu case
- `Guangzhou/`: Guangzhou case
- `Harbin/`: Harbin case

Each case folder contains:

- A site-configuration file
- `Baseline.csv`
- `RCP45.csv`
- `RCP85.csv`
- A `Results/` folder containing simulation outputs for each scenario

## Repository Structure

```text
ADse-UFPM/
│
├── ADse-UFPM.py
├── ADse-UFPM_run.py
├── UFPM_SMF_paras.csv
├── Sobol_indices.csv
├── requirements.txt
├── README.md
│
├── Beijing/
│   ├── Beijing_NSF.csv
│   ├── Baseline.csv
│   ├── RCP45.csv
│   ├── RCP85.csv
│   └── Results/
│
├── Chengdu/
│   ├── Chengdu_NRF.csv
│   ├── Baseline.csv
│   ├── RCP45.csv
│   ├── RCP85.csv
│   └── Results/
│
├── Guangzhou/
│   ├── Guangzhou_NISF.csv
│   ├── Baseline.csv
│   ├── RCP45.csv
│   ├── RCP85.csv
│   └── Results/
│
└── Harbin/
    ├── Harbin_PF.csv
    ├── Baseline.csv
    ├── RCP45.csv
    ├── RCP85.csv
    └── Results/
```

## Main Files

- `ADse-UFPM.py`: Core model, simulation modules, sensitivity analysis, Sobol analysis, and early-warning diagnosis
- `ADse-UFPM_run.py`: Main execution script
- `UFPM_SMF_paras.csv`: Shared model parameters
- `Sobol_indices.csv`: Sobol sensitivity-analysis indices
- `requirements.txt`: Required Python packages

## Requirements

Python 3.10 or later is recommended.

Install the required packages with:

```bash
pip install -r requirements.txt
```

The main dependencies are:

- NumPy
- pandas
- SciPy
- SALib

## Running the Model

Open `ADse-UFPM_run.py` and modify the settings in the `User Setting` section.

For example, to run the Beijing case under the baseline scenario:

```python
SITE = "Beijing"
SITE_CONFIG = "Beijing_NSF.csv"
SCENARIO = "Baseline.csv"
```

Available climate scenarios are:

```python
SCENARIO = "Baseline.csv"
SCENARIO = "RCP45.csv"
SCENARIO = "RCP85.csv"
```

Run the model from the repository root directory:

```bash
python ADse-UFPM_run.py
```

## Running Other Case Studies

Use the following settings for the four cases.

### Beijing

```python
SITE = "Beijing"
SITE_CONFIG = "Beijing_NSF.csv"
```

### Chengdu

```python
SITE = "Chengdu"
SITE_CONFIG = "Chengdu_NRF.csv"
```

### Guangzhou

```python
SITE = "Guangzhou"
SITE_CONFIG = "Guangzhou_NISF.csv"
```

### Harbin

```python
SITE = "Harbin"
SITE_CONFIG = "Harbin_PF.csv"
```

Select one of the three climate-scenario files separately for each run.

## Optional Analyses

The sensitivity analyses are disabled by default:

```python
RUN_SENSITIVITY = False
RUN_SOBOL = False
```

To run the budget and manager-number sensitivity analysis:

```python
RUN_SENSITIVITY = True
```

To run the Sobol global sensitivity analysis:

```python
RUN_SOBOL = True
```

These analyses may require considerably more computation time than a standard case-study simulation.

## Model Outputs

Simulation outputs are written automatically to:

```text
<SiteFolder>/Results/<Scenario>/
```

For example:

```text
Beijing/Results/Baseline/
```

The principal output files are:

- `Simulation_results.csv`: Complete annual results for all stochastic replicates
- `Annual_summary.csv`: Annual means and standard deviations
- `Early_warning.csv`: Early-warning level, indicator values, and diagnostic flags

Optional analyses may additionally produce:

- `Sensitivity_analysis.csv`
- `<site_id>_sobol_indices.csv`

Precomputed outputs used in the associated study are included in the corresponding `Results` folders.

## Reproducibility

The repository includes the input data, parameter settings, climate scenarios, model code, and precomputed outputs required to reproduce the principal simulations.

The random seed and the number of simulation years and replicates are specified in each site-configuration file.

Running the model again may overwrite output files with the same names in the selected scenario folder.

## Citation

Citation information for the associated manuscript will be added after publication.

## Contact

Questions about the repository may be submitted through GitHub Issues.
