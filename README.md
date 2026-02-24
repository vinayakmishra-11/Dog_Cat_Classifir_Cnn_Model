# Dog Cat Classifier CNN Model 🐱🐶

A Flask web application that uses a Convolutional Neural Network (CNN) to classify images as either a cat or a dog.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Flask](https://img.shields.io/badge/Flask-3.x-green)

## 🎯 Features

- **Image Classification**: Upload any image and get instant cat/dog prediction
- **Drag & Drop Upload**: Modern drag and drop interface for easy image uploading
- **Real-time Prediction**: Fast classification using pre-trained CNN model
- **Responsive UI**: Beautiful gradient design that works on all devices

## 📸 Screenshots

*Add screenshots of your application here*

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web framework |
| TensorFlow/Keras | Deep learning model |
| HTML/CSS/JS | Frontend interface |
| NumPy | Numerical operations |

## 📂 Project Structure

```
Cat_vs_Dog/
├── app.py                        # Flask application
├── cat_dog_classifier_model.h5   # Trained CNN model
├── requirements.txt              # Python dependencies
├── static/
│   └── uploads/                  # Uploaded images storage
└── templates/
    └── index.html                # Web interface
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Dog_Cat_Classifir_Cnn_Model.git
   cd Dog_Cat_Classifir_Cnn_Model
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add the trained model**
   
   Place your `cat_dog_classifier_model.h5` file in the project root directory.

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🧠 Model Information

- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 256x256 RGB images
- **Output**: Binary classification (Cat: 0, Dog: 1)
- **Framework**: TensorFlow/Keras

[Kaggle](https://www.kaggle.com/)

## 📋 Requirements

```
flask
tensorflow
numpy
pillow
h5py
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact



Project Link: [https://github.com/vinayakmishra-11/Dog_Cat_Classifir_Cnn_Model.git](https://github.com/YOUR_USERNAME/Dog_Cat_Classifir_Cnn_Model)

---

⭐ Star this repository if you found it helpful!
