def calculate_bmi(weight, height):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อคำนวณค่า BMI และแปรผลตามเกณฑ์
    สูตร: BMI = weight / (height * height) โดยที่ height คือส่วนสูงหน่วยเป็นเมตร
    
    Input:
    - weight: float (น้ำหนักหน่วยเป็นกิโลกรัม)
    - height: float (ส่วนสูงหน่วยเป็นเมตร)
    
    Output:
    - คืนค่าเป็น string ตามเกณฑ์ดังนี้:
      - BMI < 18.5: "Underweight"
      - 18.5 <= BMI < 25.0: "Normal"
      - 25.0 <= BMI < 30.0: "Overweight"
      - BMI >= 30.0: "Obese"
    
    ตัวอย่าง Input/Output:
    - calculate_bmi(50, 1.70) -> "Underweight"
    - calculate_bmi(65, 1.70) -> "Normal"
    - calculate_bmi(80, 1.70) -> "Overweight"
    - calculate_bmi(90, 1.60) -> "Obese"
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    try:
        print(f"BMI (65kg, 1.70m): {calculate_bmi(65, 1.70)}")
    except NotImplementedError:
        print("ยังไม่ได้เริ่มทำโจทย์ข้อ 13")
