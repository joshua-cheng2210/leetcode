import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # students["grade"] = int(students["grade"]) # this is wrong
    return students.astype({'grade': int})