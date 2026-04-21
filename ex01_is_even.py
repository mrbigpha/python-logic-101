def is_even(number):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อตรวจสอบว่าตัวเลขที่รับเข้ามา (number) เป็น "เลขคู่" หรือไม่
    
    Input:
    - number: int (ตัวเลขเต็มใดๆ เช่น 2, 5, -10)
    
    Output:
    - คืนค่าเป็น boolean (True หรือ False)
    - True: เมื่อ number เป็นเลขคู่ (หารด้วย 2 ลงตัว)
    - False: เมื่อ number เป็นเลขคี่ (หารด้วย 2 ไม่ลงตัว)
    
    ตัวอย่าง Input/Output:
    - is_even(2) -> True
    - is_even(3) -> False
    - is_even(0) -> True
    - is_even(-4) -> True
    
    เงื่อนไข:
    - ถ้าเป็นเลขคู่ ให้ส่งค่ากลับ (return) เป็น True
    - ถ้าไม่ใช่เลขคู่ (เลขคี่) ให้ส่งค่ากลับ (return) เป็น False
    
    คำใบ้:
    ใช้เครื่องหมาย % (Modulo) เพื่อหาเศษส่วนจากการหารด้วย 2
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    # --- สิ้นสุดการเขียนโค้ด ---

# สำหรับทดสอบรันในเครื่องตัวเอง (เลือกปิด/เปิดได้)
if __name__ == "__main__":
    test_num = 4
    print(f"Is {test_num} even? : {is_even(test_num)}")