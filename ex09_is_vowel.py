def is_vowel(char):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อตรวจสอบว่าตัวอักษรที่รับเข้ามาเป็น สระ (a, e, i, o, u) หรือไม่
    
    Input:
    - char: str (ตัวอักษร 1 ตัว เช่น 'a', 'B', 'E', 'z')
    
    Output:
    - คืนค่าเป็น boolean (True หรือ False)
    - True: เมื่อ char เป็นสระ (a, e, i, o, u) ไม่ว่าจะตัวเล็กหรือตัวใหญ่
    - False: เมื่อ char ไม่ใช่สระ
    
    ตัวอย่าง Input/Output:
    - is_vowel('a') -> True
    - is_vowel('b') -> False
    - is_vowel('E') -> True
    
    เงื่อนไข:
    - ถ้าเป็นสระ (ทั้งตัวเล็กและตัวใหญ่) ให้ส่งค่ากลับเป็น True
    - ถ้าไม่ใช่สระ ให้ส่งค่ากลับเป็น False
    
    คำใบ้:
    ใช้ตัวเชื่อม logic `or` หรือใช้ `in` เพื่อตรวจสอบในลิสต์
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    

    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    test_char = 'A'
    print(f"Is '{test_char}' a vowel? : {is_vowel(test_char)}")
