# Object Dectection Module 

This folder contains Jupyter Notebooks that implements labelling for images in `YOLO` format as well as the Object detection Module which uses `ultralytics` module with pre-trained `yolov8n` model.

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

### 5. Selectr the Kernel
After opening the `odm.ipynb` file in Jupyter Lab, select the correct kernel:
1. Click the "Kernel" menu at the top.
2. Choose the kernel created in **Step 3** (`Python venv_name`).

## Project Overview
### Main Files
- `odm.ipynb`: This is the main notebook containing the object detection module. It uses the YOLOv8 model from Ultralytics.
- `yolov8n.pt`: This is the YOLOv8 model file that will be downloaded automatically the first time the module is run. 
- `yolo_fine_tuned.pt`: This is a pre-trained fine-tuned YOLO model to save time. Users can use this pre-tuned model or opt to fine-tune it themselves.
- `fine-tune-dataset/`: Folder containing training and validation datasets for fine-tuning the YOLO model.

### Fine-Tuning the Model
To fine-tune the model, you can uncomment the `fine_tune_model()` function in the example usage section of the `odm.ipynb` file. Note that fine-tuning the model is computationally intensive and time-consuming, so using the pre-trained `yolo_fine_tuned.pt` model is recommended for quick testing.

### Running Object Detection
1. The object detection module uses test images located in the `test_imgs/` folder.
2. Once an image is processed, the annotated result will be saved in the `detected_imgs/` folder as `annodated_img.jpg`.

## File Directory Structure
``` bash
.
├── detected_imgs
│   └── annotated_img.jpg
├── fine-tune-dataset
│   └── datasets
├── fine-tune-dataset.zip
├── fine-tune.yaml
├── labelling.ipynb
├── odm.ipynb
├── README.md
├── requirements.txt
├── test_imgs
│   ├── gun.jpg
│   ├── guy_w_gun.jpg
│   ├── knife.jpg
│   └── man_w_gun_2.jpg
├── yolo_fine_tuned.pt
└── yolov8n.pt
```