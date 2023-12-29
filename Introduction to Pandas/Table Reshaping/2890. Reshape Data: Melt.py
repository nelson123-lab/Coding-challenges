import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report_melted = report.melt(id_vars = ['product'], var_name = 'quarter', value_name = 'sales')
    return report_melted


"""
Here we are using the melt function to convert the data from wide format to long format. In several ways it's opposite of pivot table.

Pivot:
Purpose: Converts data from a "long" format to a "wide" format.
Operation: It takes values from multiple rows and aggregates them into a single row, spreading out a single variable across multiple columns.
Use Case: If you have data where multiple rows contain different measurements for the same entity and you want to consolidate them into a single row per entity, with each measurement in its own column.

Melt:
Purpose: Converts data from a "wide" format to a "long" format.
Operation: It takes values from multiple columns and condenses them into a single column, creating multiple rows from a single row.
Use Case: If you have data where each row contains multiple measurements for an entity across different columns and you want to "unpivot" these measurements into a long format, where each row represents a single measurement.
"""
