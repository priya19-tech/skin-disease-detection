AI-Based Skin Disease Detection Using Deep Learning

An AI-powered web application that detects **19 different skin diseases** and identifies **skin type** from uploaded images using **Convolutional Neural Networks (CNNs)**, and provides **personalized skincare recommendations**. This project aims to support **early diagnosis**, improve **dermatological accessibility**, and offer **preliminary care guidance** using deep learning techniques. 

Project Overview

Skin diseases are often misdiagnosed or ignored due to lack of awareness, limited access to dermatologists, and high consultation costs. This project addresses these challenges by providing an **automated, low-cost, AI-based skin disease screening system**.

The system analyzes uploaded skin images and:

* Predicts the **top 5 most probable skin diseases**
* Identifies the user’s **skin type** (Oily / Dry / Normal)
* Provides **personalized care and remedy suggestions**
* Displays prediction confidence using **visual charts**

This tool is intended for **educational and preliminary screening purposes** and does **not replace professional medical diagnosis**. 

Objectives

* To design and train a **CNN model** capable of classifying **19 skin diseases** with high accuracy
* To build a **user-friendly Streamlit web application** for image-based prediction
* To integrate a **personalized skincare recommendation module**
* To improve **early detection** and **skin health awareness**, especially in remote areas


System Architecture

The system follows a **client–server architecture**:

1. **User uploads a skin image** via Streamlit UI
2. Image is **preprocessed** (resizing, normalization)
3. Two deep learning models run in parallel:

   * **Skin Disease Classification Model**
   * **Skin Type Classification Model**
4. Results are combined to generate:

   * Disease prediction probabilities
   * Skin type result
   * Personalized care recommendations
5. Output is displayed with **confidence bar charts**

(Refer to *System Architecture – Chapter 3, Fig 3.1* in the report) 

---

Technologies Used

Programming & Frameworks

* Python 3.8+
* Streamlit (Web Interface)
* TensorFlow & Keras (Deep Learning)

Deep Learning Models

* Convolutional Neural Network (CNN)
* MobileNetV2 (Transfer Learning)
* Optional CNN + XGBoost ensemble (feature-based enhancement)

Libraries

* NumPy
* Pandas
* OpenCV
* Pillow
* Scikit-learn
* Matplotlib



---

## 🗂️ Dataset Details

* Dataset consists of **19 different skin disease classes**
* Images are resized to **192 × 192**
* Data augmentation applied during training:

  * Rotation
  * Zoom
  * Horizontal flipping
  * Shifting
* Dataset split:

  * Training set
  * Validation set
  * Test set



 Model Performance

* **Overall Accuracy:** ~ **95%**
* Predictions displayed as **Top 5 diseases with confidence scores**
* Skin type prediction confidence shown separately
* Bar chart visualization for interpretability



Key Features

✔ Detects **19 skin diseases**
✔ Predicts **skin type** (Oily / Dry / Normal)
✔ Displays **Top 5 disease probabilities**
✔ Provides **personalized skincare suggestions**
✔ Interactive and modern **dark-themed UI**
✔ Uses **Git LFS** for large model handling


 Disclaimer

> This AI-based system is developed **for educational and informational purposes only**.
> It should **not be used as a substitute** for professional medical diagnosis or treatment.
> Always consult a **certified dermatologist** for clinical evaluation.





## 🚀 How to Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
```

Ensure the trained model files (`.keras`) are present in the root directory.



 🔮 Future Enhancements

* CNN–Transformer hybrid architectures
* Integration of **symptom-based inputs**
* Mobile application deployment
* Improved dataset diversity (skin tone inclusiveness)
* Real-time clinical feedback loop


