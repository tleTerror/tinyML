# Gesture Recognition using TensorFlow Lite & OpenCV

## 📌 Project Overview
This project is a **real-time gesture recognition system** using **TensorFlow Lite (TFLite)** and **OpenCV**. It utilizes the **MobileNetV1** model for efficient and lightweight classification, making it ideal for **edge devices** like Raspberry Pi, NVIDIA Jetson, or any AI-powered IoT device.

## ✨ Why This Project?
Unlike traditional object classifiers, this project is designed for:
- **Edge Computing:** Runs efficiently on low-power devices using **TinyML** and **Edge Impulse**.
- **Optimized Performance:** Uses **TensorFlow Lite** for faster and optimized inference.
- **Real-time Gesture Recognition:** Captures live video feed, processes frames, and predicts gestures instantly.
- **Scalability:** Can be easily adapted for **IoT applications, robotics, smart home controls**, and more.

## 🚀 Features
✅ Uses a **pre-trained MobileNetV1 model** optimized for low-latency inference.
✅ Supports real-time inference from **webcam or external cameras**.
✅ Displays predictions live on screen with an easy-to-use **fullscreen UI**.
✅ Works efficiently on **edge devices** without requiring heavy computational resources.
✅ Uses **TensorFlow Lite**, reducing **model size and inference time**.

---

## 📂 Project Structure
```
📁 Gesture_Recognition
│── 📄 main.py                 # Main script to run gesture recognition
│── 📄 labels.txt              # Class labels for MobileNetV1 model
│── 📄 mobilenet_v1_1.0_224_quant.tflite # TFLite model file
│── 📄 README.md               # Project Documentation
```

---

## ⚡ Installation
Ensure you have Python installed. Then, install the required dependencies:
```bash
pip install opencv-python numpy tensorflow
```

---

## 🎯 How to Run
1️⃣ Clone this repository:
```bash
git clone https://github.com/your-username/gesture-recognition-tflite.git
cd gesture-recognition-tflite
```
2️⃣ Run the script:
```bash
python main.py
```
3️⃣ The **webcam** will open, and predictions will appear on the screen.
4️⃣ Press **'q'** to quit the application.

---


## 🔥 Why is This Different from Other Object Classifiers?
### **1️⃣ Edge AI Compatibility** 🏆
- Designed for **TinyML**-based microcontrollers.
- Runs on **Raspberry Pi, Jetson Nano, and low-power IoT devices**.

### **2️⃣ Lightweight Model** ⚡
- Uses **MobileNetV1 Quantized TFLite**, optimized for low-latency inference.
- Runs seamlessly on **Edge Impulse** for easy deployment.

### **3️⃣ Real-Time Processing** 📷
- Uses **OpenCV** for **frame-by-frame analysis**.
- Detects gestures within **milliseconds**.

### **4️⃣ Customization & Expandability** 🔄
- Can be **re-trained with custom gestures** using **Edge Impulse**.
- Supports **new models** by replacing `mobilenet_v1_1.0_224_quant.tflite`.

---

## 📌 Future Enhancements
🔹 Integrate with **Edge Impulse** for real-time model training.
🔹 Add **gesture-controlled automation** (e.g., control IoT devices, smart home, etc.).
🔹 Deploy on **Raspberry Pi** for a truly **portable edge AI device**.

---

## 📢 Contributing
Feel free to contribute! Fork this repo, make improvements, and submit a PR. 🚀

💡 **Let's push the boundaries of AI on edge devices!** 💡

