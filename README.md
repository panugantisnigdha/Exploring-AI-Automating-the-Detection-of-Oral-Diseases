# Exploring-AI-Automating-the-Detection-of-Oral-Diseases


This project uses a Convolutional Neural Network (CNN) with **MobileNetV2** and **transfer learning** to classify **six common oral diseases** from dental images. It is trained on a dataset of **15,000+ labeled images** sourced via **KaggleHub**, and runs end-to-end on **Google Colab**.

## 🧠 Diseases Detected
- **Caries** – tooth decay/cavities
- **Calculus** – hardened plaque deposits
- **Gingivitis** – gum inflammation
- **Tooth Discoloration** – staining or color changes
- **Ulcers** – open sores in the mouth
- **Hypodontia** – missing teeth due to developmental issues

## 🚀 Features
- Trained using **transfer learning** with MobileNetV2
- Accepts user-uploaded images for **real-time prediction**
- Achieves high validation accuracy on a diverse dataset
- Optional: Save trained model and visualize predictions using Grad-CAM

## 📂 Dataset
- Source: [Kaggle - Oral Diseases Dataset](https://www.kaggle.com/datasets/salmansajid05/oral-diseases)
- Accessed via [kagglehub](https://pypi.org/project/kagglehub/)
- Total images: **15,000+**, organized in subfolders for each condition

## 🛠 Tech Stack
- **TensorFlow / Keras**
- **MobileNetV2**
- **KaggleHub**
- **Google Colab**
- **Python**

## 📷 How to Use
1. Open the `oral_disease_detection.ipynb` notebook in Google Colab
2. Run the setup cells to install and load the dataset
3. Train the model or load a saved version
4. Upload a dental image
5. Get predicted condition output in real-time

## 📊 Model Architecture
- Base: `MobileNetV2` (pretrained on ImageNet)
- Global Average Pooling
- Dense (256 units + ReLU)
- Dropout (0.3)
- Output Layer (Softmax)

## 👥 Contributors
- [Panuganti Snigdha](https://github.com/panugantisnigdha)
- [Panuganti Mugdha](https://github.com/PanugantiMugdha) 

---

### 📎 License
This project is for educational and research purposes only. Attribution required if reused.

