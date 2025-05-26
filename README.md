# Stock Pattern Detector 📈🧠

ระบบวิเคราะห์รูปแบบราคาหุ้นจากข้อมูลย้อนหลัง พร้อมคำแนะนำแนวโน้มในอนาคต (ขึ้น/ลง) โดยใช้ Machine Learning + Web UI (Streamlit)

---

## 🗂️ โครงสร้างโปรเจกต์
```bash
Project/
│
├── data/
│ ├── raw/ # ข้อมูลดิบที่ดึงมาจาก API
│ └── processed/ # ข้อมูลที่ผ่านการประมวลผลแล้ว
│
├── models/ # ไฟล์โมเดลที่ถูกฝึกแล้ว (pkl)
│
├── scripts/
│ ├── fetch_data.py # ดึงข้อมูลหุ้น
│ ├── preprocess_data.py # ทำความสะอาด/เตรียมข้อมูล
│ ├── train_model.py # ฝึกโมเดลจากข้อมูล
│ ├── evaluate_model.py # ประเมินประสิทธิภาพโมเดล
│ ├── predict.py # พยากรณ์ราคาหุ้นวันถัดไป
│ └── app.py # เว็บแอป Streamlit
│
├── requirements.txt # รายชื่อไลบรารีที่ใช้
└── README.md # คู่มือใช้งาน (ไฟล์นี้)
```
---

## 🛠️ การติดตั้งและใช้งาน
```bash
1. คลอนโปรเจกต์นี้
git clone https://github.com/your-username/stock-pattern-detector.git
cd stock-pattern-detector
📌 หรือดาวน์โหลด ZIP แล้วแตกไฟล์
2. ติดตั้ง Python (ถ้ายังไม่มี)
แนะนำ Python 3.10+
ดาวน์โหลดได้จาก: https://www.python.org/downloads/
3. ติดตั้งไลบรารีที่จำเป็น
python -m pip install -r requirements.txt
4. ดึงข้อมูลหุ้น
python scripts/fetch_data.py
5. เตรียมข้อมูล
python scripts/preprocess_data.py
6. ฝึกโมเดล
python scripts/train_model.py
7. ประเมินโมเดล
python scripts/evaluate_model.py
8. ทำนายราคาหุ้น
python scripts/predict.py
9. เปิดเว็บแอป (Streamlit)
python -m streamlit run scripts/app.py
แล้วเปิดเบราว์เซอร์ที่
👉 http://localhost:8501
```
### ขอให้รวยทุกคนครับ 💸📊