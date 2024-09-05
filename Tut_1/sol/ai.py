import pandas as pd 
import os 

def convert_to_csv(filePath):
    # Read the Excel file using pandas
    data = pd.read_excel(filePath)

    # Convert the DataFrame to a CSV file
    data.to_csv('output.csv', index=False)

    print("Conversion successful!")

def main():
    PATH = os.path.join(__file__, os.getcwd())
    filepath = os.path.join(PATH, "Rice_Dataset_Commeo_and_Osmancik/Rice_Cammeo_Osmancik.xlsx")

    # print(filepath)
    # convert_to_csv(filepath)

if __name__ == "__main__":
    main()
    