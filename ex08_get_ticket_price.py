def get_ticket_price(age):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อคำนวณราคาตั๋วสวนสนุกตามอายุ
    
    Input:
    - age: int (อายุของผู้ซื้อตั๋ว เช่น 10, 15, 12)
    
    Output:
    - คืนค่าเป็น int (ราคาตั๋ว)
    - 50: เมื่ออายุน้อยกว่า 12 ปี
    - 100: เมื่ออายุตั้งแต่ 12 ปีขึ้นไป
    
    ตัวอย่าง Input/Output:
    - get_ticket_price(10) -> 50
    - get_ticket_price(15) -> 100
    - get_ticket_price(12) -> 100
    
    เงื่อนไข:
    - ถ้าอายุน้อยกว่า 12 ปี ราคาตั๋วคือ 50 บาท
    - ถ้าอายุตั้งแต่ 12 ปีขึ้นไป ราคาตั๋วคือ 100 บาท
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    

    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    test_age = 10
    print(f"Ticket price for age {test_age} is: {get_ticket_price(test_age)}")
