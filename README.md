# 🌊 Coral Health & Species Analyzer

## 🎯 Aligning with Sustainable Development Goals

This project directly supports **SDG 14: Life Below Water** - Conserve and sustainably use the oceans, seas and marine resources.

**How we're making an impact:**
- 🔬 **Monitoring Marine Ecosystems** - Automated coral health assessment
- 🌱 **Biodiversity Protection** - Species identification for conservation tracking
- 📊 **Scientific Research** - Accessible tools for marine biologists and researchers
- 🚨 **Early Warning System** - Detecting coral stress and bleaching events

## 🚀 Live Demo

Experience the Coral Analyzer in action:  
**[🌐 Try the Live App](https://huggingface.co/spaces/KennethAlbert/Coral-classification-models)**

## 🛠️ Technology Stack

| Category | Technologies Used |
|----------|-------------------|
| **🤖 Machine Learning** | TensorFlow, Keras, Deep Learning |
| **🌐 Web Framework** | Gradio (for interactive UI) |
| **🖼️ Image Processing** | OpenCV, PIL, NumPy |
| **🔬 Model Types** | Convolutional Neural Networks (CNNs) |
| **☁️ Deployment** | Hugging Face Spaces |
| **🐍 Programming** | Python 3 |

## 🎪 How It Works: The Magic Behind the Scenes

### 🔍 Two-Stage Analysis Pipeline

1. **🧬 Species Identification**
   - Identifies coral genus from uploaded images
   - Classifies into specific coral species
   - Provides confidence scores for accuracy

2. **💚 Health Assessment** 
   - Analyzes coral health status
   - Detects signs of bleaching or stress
   - Binary classification: Healthy vs. Unhealthy

### ⚡ User Journey

```
📸 Upload Coral Image 
    ↓
🔄 AI Preprocessing (Resize & Normalize)
    ↓
🧠 Dual Model Analysis
    ↓
📊 Comprehensive Results
    ↓
🌊 Conservation Insights
```

### 🎨 Interactive Features

- **Drag & Drop** image uploads
- **Real-time Analysis** with progress indicators
- **Confidence Scoring** for transparent results
- **Example Gallery** for testing (expandable)
- **Mobile-Responsive** design

## 🎯 Key Features

| Feature | Impact |
|---------|---------|
| **Instant Analysis** | Get results in seconds, not days |
| **Dual Classification** | Species + Health in one scan |
| **High Accuracy** | Deep learning models trained on reef imagery |
| **Accessible** | No marine biology degree required |
| **Conservation-Focused** | Directly supports coral protection efforts |

## 🌟 Why This Matters

Coral reefs are the **rainforests of the sea**, supporting 25% of all marine life. With climate change threatening these vital ecosystems, our tool provides:

- **🦠 Early bleaching detection**
- **📈 Population monitoring capabilities**  
- **🔬 Research acceleration**
- **🌍 Global accessibility** for conservation groups

## 🏗️ Technical Architecture

```
User Interface (Gradio)
        ↓
Image Preprocessing Pipeline
        ↓
Dual Model Inference
├── Genus Classification Model
└── Health Assessment Model  
        ↓
Result Aggregation & Display
```

## 🚀 Getting Started

### For Users:
1. Visit our **[Live Demo](https://huggingface.co/spaces/KennethAlbert/Coral-classification-models)**
2. Upload a coral image
3. Click "Analyze Coral"
4. Receive instant species and health analysis!

### For Developers:
The code is structured for easy extension:
```python
# Add new coral species
GENUS_CLASS_NAMES = np.load('genus_class_names.npy')

# Extend health metrics
HEALTH_CLASS_NAMES = np.load('health_class_names.npy')
```

## 📈 Future Enhancements

- [ ] Regional coral database expansion
- [ ] Time-series analysis for reef monitoring
- [ ] Mobile app development
- [ ] API for research institutions
- [ ] Satellite imagery integration

## 🤝 Contributing to Ocean Conservation

This project demonstrates how **technology can amplify conservation efforts**. By making coral analysis accessible, we're empowering:

- **Marine Biologists** with rapid assessment tools
- **Conservation Organizations** with scalable monitoring
- **Citizen Scientists** to contribute to reef protection
- **Policy Makers** with data-driven insights

---

**💙 Together, we're using AI to protect our planet's most vibrant underwater ecosystems. Every coral analyzed is a step toward healthier oceans!**

---
*Built with ❤️ for SDG 14 • Protecting life below water through innovation*
