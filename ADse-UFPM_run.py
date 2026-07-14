# -*- coding: utf-8 -*-
"""
ADse-UFPM_run.py
Adaptive Socio-Ecological Urban Forest Management (ADse-UFPM) Framework

Driver / run script. Simulate an urban forest park under one climate
scenario. Each park is a self-contained folder next to this script,
holding its own input data and its own scenarios, for example:

    <SiteFolder>/
        <site-config>.csv      a site configuration (park type, service target,
                               climate zone, simulation settings, social data)
        Baseline.csv           climate scenarios for this park
        RCP45.csv
        RCP85.csv
        Results/               outputs are written here, one folder per scenario

The shared model parameters live in UFPM_SMF_paras.csv. 
"""

import importlib.util
from pathlib import Path

#----------------------------------------------------------------------------
# Import the core model
#----------------------------------------------------------------------------
here = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("adse_ufpm", here / "ADse-UFPM.py")
md = importlib.util.module_from_spec(_spec)

_spec.loader.exec_module(md)
paras_file = here / "UFPM_SMF_paras.csv"

#----------------------------------------------------------------------------
# User Setting
#----------------------------------------------------------------------------
# Name of the site folder to run (e.g. "Beijing").
SITE = "Beijing"

# Site-configuration file inside that folder (park type, service target,
# climate zone, simulation settings, social data).
SITE_CONFIG = "Beijing_NSF.csv"

# Climate-scenario file inside, e.g. "Baseline.csv", "RCP45.csv", "RCP85.csv".
SCENARIO = "Baseline.csv"

# Optional analyses for this run (off by default; both are slow)
RUN_SENSITIVITY = False     # budget x n_managers grid sweep
RUN_SOBOL       = False     # Sobol global sensitivity analysis

SENS_BUDGET_RANGE    = [50, 75, 100, 125, 150]
SENS_NMANAGERS_RANGE = [1, 2, 3, 4, 5]
SENS_N_REPS          = 30
SENS_N_YEARS         = 100
SOBOL_N_BASE  = 64
SOBOL_N_YEARS = 50
SOBOL_N_REPS  = 3

#----------------------------------------------------------------------------
# Resolve the input files directly from the settings above
#----------------------------------------------------------------------------
site_dir      = here / SITE
cfg_file      = site_dir / SITE_CONFIG
scenario_file = site_dir / SCENARIO


#----------------------------------------------------------------------------
# Load parameters, apply the climate scenario, run the site
#----------------------------------------------------------------------------
params = md.load_params(paras_file)
params = md.apply_scenario(params, scenario_file)
cfg    = md.load_site_config(cfg_file)

social_params = {k: cfg[k] for k in ('gdp_per_capita', 'civic_participation',
                                     'park_visitor_density', 'park_area') if k in cfg} or None

scenario    = SCENARIO.replace(".csv", "")
results_out = site_dir / "Results" / scenario   # <SiteFolder>/Results/<scenario>/

print("-" * 60)
print(f"Site folder    : {site_dir.name}  (config: {cfg_file.name})")
print(f"  Site name      : {cfg.get('site_name', cfg_file.stem)}")
print(f"  Park type      : {cfg.get('park_type')}")
print(f"  Service target : {cfg.get('service_target')}")
print(f"  Climate zone   : {cfg.get('climate_zone')}")
print(f"  Scenario       : {SCENARIO}")
print(f"  Results folder : {results_out}")

# --- 1. Case-study simulation -----------------------------------------------
md.run_site(site_cfg=cfg, params=params, output_dir=str(results_out))

# --- 2. Sensitivity grid sweep (optional) -----------------------------------
if RUN_SENSITIVITY:
    print("\n[Sensitivity] grid sweep ...")
    md.sensitivity_analysis(
        park_type        = cfg["park_type"],
        service_target   = cfg["service_target"],
        climate_zone     = cfg["climate_zone"],
        params           = params,
        budget_range     = SENS_BUDGET_RANGE,
        n_managers_range = SENS_NMANAGERS_RANGE,
        n_reps           = SENS_N_REPS,
        n_years          = SENS_N_YEARS,
        seed             = cfg.get("seed", 2024),
        output_dir       = str(results_out),
        social_params    = social_params,
        management_mode  = cfg.get("management_mode", "single"),
        portfolio_method = cfg.get("portfolio_method", "random"),
    )

# --- 3. Sobol global sensitivity (optional) ---------------------------------
if RUN_SOBOL:
    print("\n[Sobol] global sensitivity ...")
    md.sobol_sensitivity(
        site_cfg   = cfg,
        params     = params,
        output_dir = str(results_out),
        n_base     = SOBOL_N_BASE,
        n_years    = SOBOL_N_YEARS,
        n_reps     = SOBOL_N_REPS,
    )

print("\nDone.")
