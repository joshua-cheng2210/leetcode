import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # products = products[products['name'].isnull()] = 0
    products['quantity'].fillna(0, inplace=True)
    return products