# Reconstruction and Classification of Medieval Sinhalese Inscriptions Using Deep Learning

This repository contains the code and setup instructions for reconstructing and classifying degraded medieval Sinhalese letters. The project leverages Pix2Pix GAN for reconstruction and ResNet50 for classification, supported by data augmentation techniques to generate realistic degradation effects.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Model Details](#model-details)
  - [Pix2Pix GAN for Reconstruction](#pix2pix-gan-for-reconstruction)
  - [ResNet50 for Classification](#resnet50-for-classification)
- [Data Augmentation](#data-augmentation)
- [Image Comparison](#image-comparison)
- [Results](#results)
- [License](#license)

## Overview
This project aims to reconstruct and classify images of degraded medieval Sinhalese inscriptions using deep learning. The models were trained and evaluated with both synthetic and real datasets, simulating realistic degradation patterns for robust performance.

## Features
- **Image Reconstruction**: Restores the appearance of degraded inscriptions.
- **Image Classification**: Classifies reconstructed inscriptions accurately to the real datasets image.
- **Data Augmentation**: Simulates degradation with noise, blurring, and erasure.

## Setup

### Prerequisites
- Python 3.8+
- Visual Studio Code with the Jupyter extension
- `pip` package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dhanishfrost/sinhalese-inscriptions-reconstruction-using-deep-learning.git
   cd sinhalese-inscriptions-reconstruction-using-deep-learning
   ```

2. **Install dependencies**
   ```bash
   pip install dependencies (as per required)
   ```

3. **Open in Visual Studio Code with Jupyter Extension**
   - Launch Visual Studio Code and ensure the Jupyter extension is installed.
   - Open the `.ipynb` files in the `src/` folder to run code blocks.

4. **Download Pre-trained Models**
   - Place the trained Pix2Pix and ResNet50 models under the `models/` directory.

### Directory Structure
   ```plaintext
   sinhalese-inscriptions-reconstruction/
   ├── data/                    # Data directory
   │   ├── real_images/         # Original clear images
   │   ├── synthetic_images/    # Generated degraded images
   ├── models/                  # Model files
   │   ├── pix2pix.pth          # Trained Pix2Pix GAN model
   │   ├── resnet50.pth         # Trained ResNet50 model
   ├── src/                     # Source code directory
   │   ├── pix2pix.ipynb           # Pix2Pix GAN model script
   │   ├── resnet50.ipynb          # ResNet50 classification script
   |   ├── Pix2Pix_Reconstruction_GUI.ipynb # GUI using Gradio
   │   ├── augmentation.py      # Data augmentation script (one time use to create the dataset which is readily available in the repo)
   └── README.md
   ```

## Usage

### Running the Pix2Pix GAN Reconstruction
To reconstruct a degraded image, open `pix2pix.ipynb` in Visual Studio Code with the Jupyter extension and run the code block with:
```python
# Run this code block in the pix2pix.ipynb notebook
# Provide paths to input and output as arguments
reconstructed_image = pix2pix_reconstruct(input_path='<path_to_degraded_image>', output_path='<output_path>')
```

### Running the ResNet50 Classification
To classify a reconstructed image, open `resnet50.ipynb` in Visual Studio Code with the Jupyter extension and run the code block with:
```python
# Run this code block in the resnet50.ipynb notebook
# Provide path to input image as an argument
classification_result = resnet50_classify(input_path='<path_to_reconstructed_image>')
```

### Data Augmentation
Generate augmented images by running:
```bash
python src/augmentation.py --input_dir <path_to_real_images> --output_dir <path_to_synthetic_images>
```

**Note:** All code should be run within the `.ipynb` notebook files in the `src/` folder for interactive use. Using Visual Studio Code with the Jupyter extension makes it easy to execute each block individually and view outputs in real time.

## Model Details

### Pix2Pix GAN for Reconstruction
- **Architecture**: U-Net-based generator and PatchGAN discriminator.
- **Loss Functions**: Binary Cross-Entropy (GAN Loss) and L1 Loss.
- **Training**: Trained for 100 epochs with the Adam optimizer.

### ResNet50 for Classification
- **Architecture**: Modified ResNet50 with adjusted input layer for grayscale images.
- **Loss Function**: Cross-Entropy Loss for multi-class classification.
- **Training**: Achieved 99.98% accuracy on the test set.

## Data Augmentation
Data augmentation techniques include:
- **Noise Addition**: Three levels of noise to simulate degradation.
- **Erasure**: Small and medium sections of the image are erased.
- **Blurring**: Three levels of blurring to simulate fading.
- **Combination Transformations**: Mixed augmentations for dataset variability.

See `augmentation.py` for code implementation details.

## Image Comparison

Below is a sample visual comparison between a real image, degraded image, and the reconstructed image.

| Real Image | Degraded Image | Reconstructed Image |
|------------|----------------|---------------------|
| ![Real](images/mdvs1%20.jpg) | ![Degraded](images/mdvs1%20_synthetic_image_14.jpg) | ![Reconstructed](images/mdvs1%20_reconstructed_14.jpg) |
| ![Real](images/mdvs31%20.jpg) | ![Degraded](images/mdvs31%20_synthetic_image_7.jpg) | ![Reconstructed](images/mdvs31%20_reconstructed_7.jpg) |

## Results
The Pix2Pix GAN model achieved an SSIM score of 0.9879 and an MSE of 0.0021 on the reconstruction task, demonstrating strong accuracy. The ResNet50 classification model achieved 99.98% accuracy on reconstructed images.
