# Handling Imbalanced Dataset

This folder contains Jupyter Notebook that implements data balancing techniques for the `abalone` dataset from ucirepo. A `RandomForestClassifier` model is used to access the impact of balancing the dataset on the model's performance.

## Getting Started
To get started with the project, follow these steps: 

### Prerequisites
- Python 3.11 or later
- Pip 24.0 or later

### 1. Set Up a Virtual Environment 
It is recommended to use a virtual environment to manage dependencies.
</br>
**Create a Virutal Environment**
It is recomemded to use a virtual environment to manage dependencies. 
</br>
```bash 
python -m venv venv_name
```
Replace `venv_name` with the desired name of your virtual environment.
</br>
**Activate the Virtual Environment:**
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
pip install -r requirments.txt
```

### 3. Create Jupyter Kernel for the Virtual Environment 
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
This will open Jupyter Lab in your browser at `http://localhost:8080`. You can then open the `odm.ipynb` file.

### 5. Select the Kernel
After opening the `odm.ipynb` file in Jupyter Lab, select the correct kernel:
1. Click the "Kernel" menu at the top.
2. Choose the kernel created in **Step 3** (`Python venv_name`).

### 6. Run the Notebook 
Once the kernel is selected, you can run the cells in the notebook to explore various techniques for handling imbalanced datasets. 

### Project Structure 
- `imbalance-ml.ipynb`: Jupyter Notebook containing the data balancing implementation.
- `requirements.txt`: List of required Python packages for the project.
.
├── imbalance-ml.ipynb
├── README.md
└── requirements.txt