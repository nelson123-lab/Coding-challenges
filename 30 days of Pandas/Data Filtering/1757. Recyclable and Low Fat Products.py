import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products1 = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return products1[['product_id']]

"""
Here we extract the data that satisfies both the condition to the products1 and return the product_id column
"""
