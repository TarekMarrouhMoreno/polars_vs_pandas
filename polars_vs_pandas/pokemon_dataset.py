import polars as pl
import pandas as pd

class PokemonDataset:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dataset = None

    def load_dataset(self):
        self.dataset = pl.read_csv(self.file_path)

    def filter_by_type(self, pokemon_type):
        self.dataset = self.dataset.filter(pl.col("Type 1") == pokemon_type)

    def multiply_stat_by_type(self, stat, multiplier):
        self.dataset = self.dataset.with_column(
            pl.col(stat) * multiplier
        )

    def to_pandas(self):
        return self.dataset.to_pandas()

    def to_polars(self):
        return self.dataset

