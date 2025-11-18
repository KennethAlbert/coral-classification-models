# app.py
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import gradio as gr
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

# Global variables for models
GENUS_MODEL = None
HEALTH_MODEL = None
GENUS_CLASS_NAMES = None
HEALTH_CLASS_NAMES = None

def load_models():
    """Load all models and class names"""
    global GENUS_MODEL, HEALTH_MODEL, GENUS_CLASS_NAMES, HEALTH_CLASS_NAMES
    
    try:
        # Load models
        GENUS_MODEL = tf.keras.models.load_model('genus_model.h5')
        HEALTH_MODEL = tf.keras.models.load_model('health_model.h5')
        
        # Load class names
        GENUS_CLASS_NAMES = np.load('genus_class_names.npy', allow_pickle=True)
        HEALTH_CLASS_NAMES = np.load('health_class_names.npy', allow_pickle=True)
        
        print("✅ All models loaded successfully!")
        print(f"Genus classes: {list(GENUS_CLASS_NAMES)}")
        print(f"Health classes: {list(HEALTH_CLASS_NAMES)}")
        
        return True
    except Exception as e:
        print(f"❌ Error loading models: {e}")
        return False

def preprocess_image(image):
    """Preprocess image for model prediction"""
    # Convert to numpy array if it's a PIL Image
    if hasattr(image, 'size'):
        image = np.array(image)
    
    # Ensure image is in RGB format
    if len(image.shape) == 3:
        if image.shape[2] == 4:  # RGBA to RGB
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        elif image.shape[2] == 3:  # Ensure RGB
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Resize and normalize
    resize = tf.image.resize(image, (256, 256))
    processed_img = np.expand_dims(resize/255, 0)
    
    return processed_img

def analyze_coral_image(image):
    """Analyze coral image for genus and health"""
    try:
        # Check if models are loaded
        if GENUS_MODEL is None or HEALTH_MODEL is None:
            return "❌ Models not loaded properly. Please check the logs."
        
        # Preprocess image
        processed_img = preprocess_image(image)
        
        # Predict genus
        genus_pred = GENUS_MODEL.predict(processed_img, verbose=0)
        genus_class_idx = np.argmax(genus_pred[0])
        genus_confidence = genus_pred[0][genus_class_idx]
        predicted_genus = GENUS_CLASS_NAMES[genus_class_idx]
        
        # Predict health
        health_pred = HEALTH_MODEL.predict(processed_img, verbose=0)
        health_score = health_pred[0][0]
        
        # Determine health prediction
        health_is_positive = health_score > 0.5
        predicted_health = HEALTH_CLASS_NAMES[1] if health_is_positive else HEALTH_CLASS_NAMES[0]
        health_confidence = health_score if health_is_positive else 1 - health_score
        
        # Format results
        result = f"""
🌊 **CORAL ANALYSIS RESULTS**

🔬 **GENUS IDENTIFICATION**
• **Species**: {predicted_genus}
• **Confidence**: {genus_confidence:.1%}

💚 **HEALTH ASSESSMENT** 
• **Status**: {predicted_health.upper()}
• **Confidence**: {health_confidence:.1%}

---
*Analyzed using deep learning models*
"""
        
        return result
        
    except Exception as e:
        return f"❌ Error during analysis: {str(e)}"

# Initialize models at startup
models_loaded = load_models()

# Create Gradio interface
def create_interface():
    with gr.Blocks(theme=gr.themes.Soft(), title="Coral Analyzer") as demo:
        gr.Markdown(
        """
        # 🌊 Coral Health & Species Analyzer
        *Upload an image of coral to identify its species and health status*
        """)
        
        with gr.Row():
            with gr.Column():
                image_input = gr.Image(
                    type="pil", 
                    label="📷 Upload Coral Image",
                    sources=["upload"],
                    height=300
                )
                analyze_btn = gr.Button("🔍 Analyze Coral", variant="primary")
            
            with gr.Column():
                output_text = gr.Markdown(
                    label="📊 Analysis Results",
                    value="*Results will appear here after analysis...*"
                )
        
        # Examples section
        gr.Markdown("### 📸 Example Images")
        gr.Examples(
            examples=[],  # You can add example images later
            inputs=image_input,
            outputs=output_text,
            fn=analyze_coral_image,
            cache_examples=False
        )
        
        # Footer
        gr.Markdown(
        """
        ---
        *Built with TensorFlow & Gradio • Models trained on coral reef imagery*
        """)
        
        # Connect button to function
        analyze_btn.click(
            fn=analyze_coral_image,
            inputs=image_input,
            outputs=output_text
        )
    
    return demo

# Create and launch interface
if __name__ == "__main__":
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )