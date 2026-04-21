def get_sign(number):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อบอกว่าตัวเลขที่รับเข้ามาเป็น ค่าบวก, ค่าลบ หรือ ศูนย์
    
    Input:
    - number: int หรือ float (ตัวเลขใดๆ เช่น 10, -5, 0)
    
    Output:
    - คืนค่าเป็น string ต่อไปนี้เท่านั้น (สะกดตัวเล็กทั้งหมด):
    - "positive": เมื่อ number > 0
    - "negative": เมื่อ number < 0
    - "zero": เมื่อ number == 0
    
    ตัวอย่าง Input/Output:
    - get_sign(10) -> "positive"
    - get_sign(-5) -> "negative"
    - get_sign(0) -> "zero"
    
    เงื่อนไข:
    - ถ้าตัวเลขมากกว่า 0 ให้ส่งค่ากลับเป็น "positive"
    - ถ้าตัวเลขน้อยกว่า 0 ให้ส่งค่ากลับเป็น "negative"
    - ถ้าตัวเลขเท่ากับ 0 ให้ส่งค่ากลับเป็น "zero"
    
    คำใบ้:
    ใช้โครงสร้าง if - elif - else
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    

    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    test_num = -5
    print(f"The sign of {test_num} is: {get_sign(test_num)}")
