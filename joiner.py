import os
import numpy as np
import pandas as pd

"""This function joins several csv files which contain time series of the
same lenght into a unique csv file."""

# NEEDSWORK: this function is too dependent on the file names. This can be improved I think

def joiner():
    
    # Set the names of the files which contain the data
    amonio = "ammonium_nor.csv"
    conductividad = "conductivity_nor.csv"
    nivel = "water level_nor.csv"
    oxigeno = "dissolved oxygen_nor.csv"
    ph = "pH_nor.csv"
    temperatura = "water temperature_nor.csv"
    turbidez = "turbidity_nor.csv"

    # Read the files and store them as a pandas database
    df = pd.read_csv(f'data/{amonio}', delimiter=';', parse_dates=['date'], index_col=['date'])
    dfConductividad = pd.read_csv(f'data/{conductividad}', delimiter=';', parse_dates=['date'], index_col=['date'])
    dfNivel = pd.read_csv(f'data/{nivel}', delimiter=';', parse_dates=['date'], index_col=['date'])
    dfOxigeno = pd.read_csv(f'data/{oxigeno}', delimiter=';', parse_dates=['date'], index_col=['date'])
    dfph = pd.read_csv(f'data/{ph}', delimiter=';', parse_dates=['date'], index_col=['date'])
    dfTemperatura = pd.read_csv(f'data/{temperatura}', delimiter=';', parse_dates=['date'], index_col=['date'])
    dfTurbidez = pd.read_csv(f'data/{turbidez}', delimiter=';', parse_dates=['date'], index_col=['date'])


    # Extract the desired columns
    conductividad = dfConductividad['value']
    nitratos = dfNivel['value']
    oxigeno = dfOxigeno['value']
    ph = dfph['value']
    temperatura = dfTemperatura['value']
    turbidez = dfTurbidez['value']

    # Insert the new columns in the database
    df.insert(1, "conductivity", conductividad, True)
    df.insert(3, "oxygen", oxigeno, True)
    df.insert(4, "pH", ph, True)
    df.insert(6, "turbidity", turbidez, True)
    df.insert(2, "water level", nitratos, True)
    df.insert(5, "water temperature", temperatura, True)

    cols = list(df.columns.values.tolist())
    cols = [i.replace("value", "ammonium") for i in cols]
    df.to_csv(f'data/joined.csv', sep=';', encoding='utf-8', index=True, header=cols)
