import time

class PerformanceComparator:
    def __init__(self, pokemon_dataset):
        self.pokemon_dataset = pokemon_dataset

    def compare_performance(self):
        start_time = time.time()
        # Perform calculations using polars
        polars_dataset = self.pokemon_dataset.to_polars()
        polars_dataset = polars_dataset.with_column(
            pl.col("Attack") * 2
        )
        polars_execution_time = time.time() - start_time

        start_time = time.time()
        # Perform calculations using pandas
        pandas_dataset = self.pokemon_dataset.to_pandas()
        pandas_dataset["Attack"] = pandas_dataset["Attack"] * 2
        pandas_execution_time = time.time() - start_time

        return polars_execution_time, pandas_execution_time
