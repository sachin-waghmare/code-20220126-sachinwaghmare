import numpy as np
from bmi_calculator.reference import BMI_Health_dict as BMI
from bmi_calculator.reference import values

"""Method to calculate Health risk and BMI Category
input: dataframe[Gender, HeightCm, WeightKg]
output: dataframe[Gender, Heightcm, WeightKg, BMI Range, Health risk, BMI Category]
"""
def calculate_BMI(dataframe):
    dataframe['BMI Range'] = dataframe['WeightKg'] / ((dataframe['HeightCm'] /100)*(dataframe['HeightCm']/100))
    conditions = [
        (dataframe['BMI Range'] < 18.4),
        (dataframe['BMI Range'] >= 18.5) & (dataframe['BMI Range'] < 24.9),
        (dataframe['BMI Range'] >= 25) & (dataframe['BMI Range'] < 29.9),
        (dataframe['BMI Range'] >= 30) & (dataframe['BMI Range'] < 34.9),
        (dataframe['BMI Range'] >= 35) & (dataframe['BMI Range'] < 39.9),
        (dataframe['BMI Range'] >= 40)
    ]

    dataframe['Health risk'] = np.select(conditions, values)

    dataframe['BMI Category']= dataframe['Health risk'].map(BMI)
    return dataframe