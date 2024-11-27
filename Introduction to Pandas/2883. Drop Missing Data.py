import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
  # result = students[~pd.isna(students['name'])]
  # result = students[~pd.isnull(students['name'])]
  # result = students[~students['name'].isna()]
  # result = students[~students['name'].isnull()]
  # result = students[students['name'].notna()]
  # result = students[students['name'].notnull()]
  # return result
  return students.dropna(subset=['name'])