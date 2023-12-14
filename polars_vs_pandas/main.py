from pokemon_dataset import PokemonDataset
from performance_comparator import PerformanceComparator

# Create an instance of PokemonDataset
pokemon_dataset = PokemonDataset("pokemon.csv")

# Load the dataset
pokemon_dataset.load_dataset()

# Filter by type
pokemon_dataset.filter_by_type("Fire")

# Multiply the "Attack" stat by 2 for Fire Pokemon
pokemon_dataset.multiply_stat_by_type("Attack", 2)

# Create an instance of PerformanceComparator
performance_comparator = PerformanceComparator(pokemon_dataset)

# Compare the performance of calculations using polars and pandas
polars_execution_time, pandas_execution_time = performance_comparator.compare_performance()

print("Polars Execution Time:", polars_execution_time)
print("Pandas Execution Time:", pandas_execution_time)
