import unittest
import math
from bmi_calculator.reference import  BMI_Health_dict
from bmi_calculator.pipeline.calculate_bmi import calculate_BMI
import pandas as pd

class TestClass(unittest.TestCase):
    def test_case1(self):
        assert BMI_Health_dict['Malnutrition risk'] == 'Underweight'

    def test_case2(self):
        assert BMI_Health_dict['Low risk'] == 'Normal risk'

    def test_case3(self):
        assert BMI_Health_dict['Enhanced risk'] == 'Overweight'

    def test_case4(self):
        df = pd.DataFrame(columns = ['WeightKg','HeightCm'])
        df['WeightKg'] = [77]
        df['HeightCm'] = [180]
        assert calculate_BMI(df).loc[0]['BMI Category'] == 'Normal risk'



if __name__=="__main__":
    unittest.main()