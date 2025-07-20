from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
import pandas as pd

# โหลดโมเดล
model = tf.keras.models.load_model("my_stock_prediction_cnn_model.keras")

# label ของ pattern ที่เราสนใจ
label_names = ['CDLDOJI', 'CDLSPINNINGTOP', 'CDLMARUBOZU', 'CDLENGULFING',
               'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLDRAGONFLYDOJI']

app = FastAPI()

# Define input schema
class OHLCRequest(BaseModel):
    ohlc: list  # [ [open, high, low, close], [open, high, low, close], ..., ]

@app.post("/predict")
def predict_pattern(data: OHLCRequest):
    # แปลงข้อมูล input ให้เป็น numpy array [batch, seq_len, 4]
    input_data = np.array(data.ohlc, dtype=np.float32).reshape(1, -1, 4)

    # ทำ prediction
    prediction = model.predict(input_data)[0]

    # หาคำตอบที่มีค่ามากสุด
    pred_index = np.argmax(prediction)
    pred_label = label_names[pred_index]
    confidence = float(prediction[pred_index])

    return {
        "predicted_pattern": pred_label,
        "confidence": confidence,
        "all_confidences": dict(zip(label_names, map(float, prediction)))
    }
