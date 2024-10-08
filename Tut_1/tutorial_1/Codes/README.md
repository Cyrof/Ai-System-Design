# AI Model for Rice Species Classification

This folder contains a Jupyter Notebook that implements a Support Vector Machine (SVM) model to clssify rice species (`Cammeo` and `Osmancik`) based on specific attributes. The model uses `GridSearchCV` for hyperparameter tuning and `k-fold` cross-validation to find the best parameters.

## Getting Started
To get started with this project, follow these steps: 

### Prerequisites
- Python 3.11 or later
- Pip 24.0 or later

### 1. Set Up a Virtual Environment 
It is recommended to use a virtual environment to manage dependencies.
</br>
**Create a Virtual Environment**
``` bash
python -m venv venv_name
```
Replace `venv_name` with the desired name of your virtual environment.
</br>
**Activate the Virtual Environment**
- **Windows:**
  ```bash 
  .\venv_name\Scripts\activate
  ```
- **MacOS/Linux:**
  ```bash
  source venv_name/bin/activate
  ```

### 2. Install Required Packages
Once the virtual environment is activated, install the required packages from `requirements.txt`.
```bash
pip install -r requirements.txt
```

### 3. Create a Jupyter Kernel for the Virtual Environment
To use the virtual environment in Jupyter Lab, create a new kernel:
```bash 
python -m ipykernel install --user --name=venv_name --display-name "Python venv_name"
```
Replace `venv_name` with the name of your virtual environment.

### 4. Start Jupyter Lab 
Run the following command to start Jupyter Lab: 
```bash 
jupyter-lab
```
This will open Jupyter Lab in your default browser at `http://localhost:8888/`. You can then open the ai.ipynb file.

### 5. Select the Kernel 
After opening the `ai.ipynb` file in Jupyter Lab, select the correct kernel before running any code: 
1. Click on the "Kernel" menu at the top right.
   </br>
   ![change-kernel](images/change-kernel.png)
2. Click on the "select kernel" dropdown menu.
   </br>
   ![select-kernel](images/select-kernel.png)
3. Select the kernel that was created in **Step 3** (named `Python venv_name`).
   </br>
   ![corret-kernel](images/correct-kernel.png)

This ensures the notebook runs with the correct virtual environment.

### Running the Notebook
1. **Data Conversion (if needed)**: Convert the provided Excel dataset to CSV format using the `convert_do_csv()` function in the notebook. Uncomment the line in the notebook to run the conversion function: 
   ```python 
   # convert_do_csv(excelPath)
   ```
2. **Run the SVM Model**: Follow the instructions in the notebook to load the dataset, preprocess the data, and train the SVM model. This process will take some time depending on your system's resources.
3. **Evaluate the Model**: The notebook will provide a detailed classification report and accuracy score of the model.

### Project Structure
- `ai.ipynb`: Jupyter Notebook containing the SVM model implementation.
- `requirements.txt`: List of required Python packages for the project.
- `dataset/Rice_Cammeo_Osmancik.xlsx`: Excel dataset used for model training.
```bash
.
├── ai.ipynb
├── dataset
│   ├── output.csv
│   └── Rice_Cammeo_Osmancik.xlsx
├── ICT304 Tutorial 1.docx
├── images
│   ├── change-kernel.png
│   ├── correct-kernel.png
│   └── select-kernel.png
├── README.md
└── requirements.txt
```