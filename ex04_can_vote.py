def can_vote(age):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อตรวจสอบว่าบุคคลนั้นมีสิทธิ์เลือกตั้งหรือไม่ตามอายุ (age)
    
    Input:
    - age: int (อายุของบุคคล เช่น 18, 17, 25)
    
    Output:
    - คืนค่าเป็น boolean (True หรือ False)
    - True: เมื่ออายุตั้งแต่ 18 ปีขึ้นไป
    - False: เมื่ออายุน้อยกว่า 18 ปี
    
    ตัวอย่าง Input/Output:
    - can_vote(18) -> True
    - can_vote(17) -> False
    - can_vote(25) -> True
    
    เงื่อนไข:
    - ถ้าอายุตั้งแต่ 18 ปีขึ้นไป ให้ส่งค่ากลับ (return) เป็น True
    - ถ้าอายุน้อยกว่า 18 ปี ให้ส่งค่ากลับ (return) เป็น False
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    

    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    test_age = 20
    print(f"Age {test_age} can vote? : {can_vote(test_age)}")
