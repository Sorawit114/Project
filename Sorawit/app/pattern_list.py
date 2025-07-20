import talib

# --------------------------
# Pattern แบบ 1 แท่ง (ชื่ออ่านง่าย)
# --------------------------
one_candle_patterns = {
    "Doji": talib.CDLDOJI,
    "Dragonfly Doji": talib.CDLDRAGONFLYDOJI,
    "Gravestone Doji": talib.CDLGRAVESTONEDOJI,
    "Long Legged Doji": talib.CDLLONGLEGGEDDOJI,
    "Short Line": talib.CDLSHORTLINE,
    "Long Line": talib.CDLLONGLINE,
    "Marubozu": talib.CDLMARUBOZU,
    "Spinning Top": talib.CDLSPINNINGTOP,
    "Hammer": talib.CDLHAMMER,
    "Inverted Hammer": talib.CDLINVERTEDHAMMER,
    "Hanging Man": talib.CDLHANGINGMAN,
    "Shooting Star": talib.CDLSHOOTINGSTAR,
    "Rickshaw Man": talib.CDLRICKSHAWMAN,
    "Takuri": talib.CDLTAKURI,
}

# --------------------------
# Pattern แบบ 2 แท่ง
# --------------------------
two_candle_patterns = {
    "Bullish Engulfing": talib.CDLENGULFING,  # ต้องแยก Bullish/Bearish ในโค้ดหลัก
    "Bearish Engulfing": talib.CDLENGULFING,  # แยกสีได้ในโค้ดหลัก
    "Harami": talib.CDLHARAMI,
    "Harami Cross": talib.CDLHARAMICROSS,
    "Piercing": talib.CDLPIERCING,
    "On Neck": talib.CDLONNECK,
    "In Neck": talib.CDLINNECK,
    "Concealing Baby Swallow": talib.CDLCONCEALBABYSWALL,
    "Homing Pigeon": talib.CDLHOMINGPIGEON,
    "Kicking": talib.CDLKICKING,
    "Kicking by Length": talib.CDLKICKINGBYLENGTH,
    "Separating Lines": talib.CDLSEPARATINGLINES,
    "Counterattack": talib.CDLCOUNTERATTACK,
    "Upside Gap Two Crows": talib.CDLGAPSIDESIDEWHITE,
    "Matching Low": talib.CDLMATCHINGLOW,
    "Belt Hold": talib.CDLBELTHOLD,
}

# --------------------------
# Pattern แบบ 3 แท่ง
# --------------------------
three_candle_patterns = {
    "Three Inside Up/Down": talib.CDL3INSIDE,
    "Three Outside Up/Down": talib.CDL3OUTSIDE,
    "Three Black Crows": talib.CDL3BLACKCROWS,
    "Three White Soldiers": talib.CDL3WHITESOLDIERS,
    "Stick Sandwich": talib.CDLSTICKSANDWICH,
    "Three Line Strike": talib.CDL3LINESTRIKE,
    "Identical Three Crows": talib.CDLIDENTICAL3CROWS,
    "Tristar": talib.CDLTRISTAR,
    "X Side Gap Three Methods": talib.CDLXSIDEGAP3METHODS,
    "Rise Fall Three Methods": talib.CDLRISEFALL3METHODS,
}

# --------------------------
# Pattern แบบ 4 แท่ง
# --------------------------
four_candle_patterns = {
    "Four Price Stars In South": talib.CDL3STARSINSOUTH,  # ฟังก์ชันนี้ชื่อ 3STARSINSOUTH
}

# --------------------------
# Pattern แบบ 5 แท่ง
# --------------------------
five_candle_patterns = {
    "Abandoned Baby": talib.CDLABANDONEDBABY,
    "Breakaway": talib.CDLBREAKAWAY,
    "Morning Star": talib.CDLMORNINGSTAR,
    "Evening Star": talib.CDLEVENINGSTAR,
    "Morning Doji Star": talib.CDLMORNINGDOJISTAR,
    "Evening Doji Star": talib.CDLEVENINGDOJISTAR,
    "Mat Hold": talib.CDLMATHOLD,
    "Advance Block": talib.CDLADVANCEBLOCK,
    "Stalled Pattern": talib.CDLSTALLEDPATTERN,
    "Tasukigap": talib.CDLTASUKIGAP,
}

# รวมทั้งหมด
all_patterns = {}
all_patterns.update(one_candle_patterns)
all_patterns.update(two_candle_patterns)
all_patterns.update(three_candle_patterns)
all_patterns.update(four_candle_patterns)
all_patterns.update(five_candle_patterns)
