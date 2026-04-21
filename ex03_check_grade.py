def check_grade(score):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อตรวจสอบผลการเรียนจากคะแนน (score)
    
    Input:
    - score: int หรือ float (คะแนนที่ได้รับ เช่น 75, 45, 50)
    
    Output:
    - คืนค่าเป็น string ("Pass" หรือ "Fail")
    - "Pass": เมื่อคะแนนตั้งแต่ 50 ขึ้นไป
    - "Fail": เมื่อคะแนนน้อยกว่า 50
    
    ตัวอย่าง Input/Output:
    - check_grade(75) -> "Pass"
    - check_grade(45) -> "Fail"
    - check_grade(50) -> "Pass"
    
    เงื่อนไข:
    - ถ้าคะแนนตั้งแต่ 50 ขึ้นไป ให้ส่งค่ากลับ (return) เป็น "Pass"
    - ถ้าคะแนนน้อยกว่า 50 ให้ส่งค่ากลับ (return) เป็น "Fail"
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    

    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    test_score = 75
    print(f"Score {test_score} result: {check_grade(test_score)}")
