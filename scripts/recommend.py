def recommend_action(open_price, predicted_close, threshold=1.0):
    diff = predicted_close - open_price
    if diff > threshold:
        return "Buy ✅ (ราคาจะขึ้น)"
    elif diff < -threshold:
        return "Sell ❌ (ราคาจะลง)"
    else:
        return "Hold 🤝 (นิ่ง ๆ ไปก่อน)"

if __name__ == "__main__":
    print(recommend_action(150, 152.5))