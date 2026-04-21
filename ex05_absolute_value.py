def absolute_value(number):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อหาค่าสัมบูรณ์ (Absolute Value) ของตัวเลข
    
    Input:
    - number: int หรือ float (ตัวเลขใดๆ เช่น 10, -5, 0)
    
    Output:
    - คืนค่าเป็น int หรือ float (ค่าที่ไม่มีเครื่องหมายลบ)
    - ถ้า number >= 0 คืนค่าเดิม
    - ถ้า number < 0 คืนค่าที่คูณด้วย -1
    
    ตัวอย่าง Input/Output:
    - absolute_value(10) -> 10
    - absolute_value(-5) -> 5
    - absolute_value(0) -> 0
    
    เงื่อนไข:
    - ถ้าตัวเลขมากกว่าหรือเท่ากับ 0 ให้ส่งค่ากลับเป็นตัวเลขเดิม
    - ถ้าตัวเลขน้อยกว่า 0 ให้ส่งค่ากลับเป็นตัวเลขนั้นที่คูณด้วย -1 (เพื่อให้เป็นบวก)
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    

    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    test_num = -10
    print(f"Absolute value of {test_num} is: {absolute_value(test_num)}")
