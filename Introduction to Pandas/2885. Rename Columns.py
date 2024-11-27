import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # students.column["id"] = "student_id"
    # students.column["first"] = "first_name"
    # students.column["last"] = "last_name"
    # students.column["age"] = "age_in_years" # wrong way of diong it and no suce syntaxes
    # return students

    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
    return students