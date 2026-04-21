def is_teenager(age):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อตรวจสอบว่าบุคคลนั้นอยู่ในวัยรุ่นหรือไม่ (อายุระหว่าง 13 ถึง 19 ปี)
    
    Input:
    - age: int (อายุของบุคคล เช่น 15, 12, 19, 20)
    
    Output:
    - คืนค่าเป็น boolean (True หรือ False)
    - True: เมื่ออายุอยู่ในช่วง 13 ถึง 19 ปี (รวม 13 และ 19)
    - False: เมื่ออายุไม่อยู่ในช่วงดังกล่าว
    
    ตัวอย่าง Input/Output:
    - is_teenager(15) -> True
    - is_teenager(12) -> False
    - is_teenager(13) -> True
    - is_teenager(19) -> True
    
    เงื่อนไข:
    - ถ้าอายุตั้งแต่ 13 ถึง 19 ปี (รวมทั้งสองค่า) ให้ส่งค่ากลับเป็น True
    - ถ้าไม่อยู่ในช่วงนี้ ให้ส่งค่ากลับเป็น False
    
    คำใบ้:
    ใช้ตัวเชื่อม logic `and` ในการตรวจสอบช่วงอายุ
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    

    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    test_age = 15
    print(f"Is {test_age} a teenager? : {is_teenager(test_age)}")
