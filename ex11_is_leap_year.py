def is_leap_year(year):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อตรวจสอบว่าปีที่รับเข้ามาเป็นปีอธิกสุรทิน (Leap Year) หรือไม่ (แบบใช้งานจริง)
    
    Input:
    - year: int (ปี ค.ศ. เช่น 2000, 1900, 2024)
    
    Output:
    - คืนค่าเป็น boolean (True หรือ False)
    - True: เมื่อเป็นปีอธิกสุรทิน (หารด้วย 4 ลงตัว และถ้าหารด้วย 100 ลงตัว ต้องหารด้วย 400 ลงตัวด้วย)
    - False: เมื่อไม่เป็นปีอธิกสุรทิน
    
    ตัวอย่าง Input/Output:
    - is_leap_year(2000) -> True
    - is_leap_year(1900) -> False
    - is_leap_year(2024) -> True
    - is_leap_year(2023) -> False
    
    เงื่อนไขปีอธิกสุรทิน:
    1. ต้องหารด้วย 4 ลงตัว
    2. แต่ถ้าหารด้วย 100 ลงตัว "ต้อง" หารด้วย 400 ลงตัวด้วยถึงจะเป็น Leap Year
    
    คำใบ้:
    ใช้ (year % 4 == 0 and year % 100 != 0) หรือ (year % 400 == 0)
    พยายามเขียนโดยใช้ตัวเชื่อม logic `and`, `or` เพื่อให้โค้ดไม่ซ้อนกัน (non-nested)
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    

    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    test_year = 2000
    print(f"Is {test_year} a leap year? : {is_leap_year(test_year)}")
