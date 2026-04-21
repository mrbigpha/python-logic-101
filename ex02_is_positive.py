def is_positive(number):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อตรวจสอบว่าตัวเลขที่รับเข้ามา (number) เป็น "จำนวนบวก" หรือไม่
    
    Input:
    - number: int หรือ float (ตัวเลขใดๆ เช่น 5, -2, 0, 3.5)
    
    Output:
    - คืนค่าเป็น boolean (True หรือ False)
    - True: เมื่อ number มีค่ามากกว่า 0
    - False: เมื่อ number มีค่าน้อยกว่าหรือเท่ากับ 0
    
    ตัวอย่าง Input/Output:
    - is_positive(5) -> True
    - is_positive(-2) -> False
    - is_positive(0) -> False
    
    เงื่อนไข:
    - ถ้าตัวเลขมากกว่า 0 ให้ส่งค่ากลับ (return) เป็น True
    - ถ้าตัวเลขน้อยกว่าหรือเท่ากับ 0 ให้ส่งค่ากลับ (return) เป็น False
    
    คำใบ้:
    ใช้เครื่องหมาย > ในการเปรียบเทียบ
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError       

    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    test_num = 5
    print(f"Is {test_num} positive? : {is_positive(test_num)}")
