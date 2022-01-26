# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from bmi_calculator.pipeline.file_read_module import read_json
from bmi_calculator.pipeline.calculate_bmi import calculate_BMI


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pd = read_json('./data.json')
    df = calculate_BMI(pd)
    print(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
