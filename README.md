# **Pokemon Dataset Analysis**

Overview

This Python project is designed to analyze a dataset of Pokemon, providing functionalities for loading, filtering, and manipulating the data. The project showcases the use of Pandas and Polars for data processing, with a focus on comparing their performance in specific operations.
Core Components
PokemonDataset Class

The PokemonDataset class serves as the core component for handling the Pokemon dataset.
Methods

    load_dataset()
        Loads the Pokemon dataset from a file.

    filter_by_type(type: str)
        Filters the dataset to include only Pokemon of a specific type.

    multiply_stat_by_type(stat: str, multiplier: int)
        Multiplies a specific stat by a multiplier for Pokemon of a specific type.

PerformanceComparator Class

The PerformanceComparator class is responsible for benchmarking the performance of calculations using both Pandas and Polars.
Methods

    compare_performance()
        Performs the calculations using both Pandas and Polars and measures the execution time.

Getting Started

    git clone https://github.com/TarekMarrouhMoreno/polars_vs_pandas.git

Install the required dependencies.

    pip install -r requirements.txt

Run the main script.

    python main.py

Usage

Adjust the parameters and operations in the main.py script to tailor the analysis according to your needs. Feel free to explore additional functionalities or extend the capabilities of the project.
Dependencies

    Pandas
    Polars

Contributing

Contributions are welcome! Fork the repository, make your improvements, and submit a pull request.
License


Based on the requirements, here are the core classes, functions, and methods that will be necessary:

1. `PokemonDataset` class: This class will be responsible for loading and manipulating the Pokemon dataset.
   - `load_dataset()` method: Loads the Pokemon dataset from a file.
   - `filter_by_type(type: str)` method: Filters the dataset to include only Pokemon of a specific type.
   - `multiply_stat_by_type(stat: str, multiplier: int)` method: Multiplies a specific stat by a multiplier for Pokemon of a specific type.

2. `PerformanceComparator` class: This class will be responsible for comparing the performance of calculations using polars and pandas.
   - `compare_performance()` method: Performs the calculations using both polars and pandas and measures the execution time.
