def calculate_discount(total_amount):
    """
    โจทย์:
    ให้น้องๆ เขียนฟังก์ชันเพื่อคำนวณราคาสุทธิหลังหักส่วนลด
    เงื่อนไข: ถ้าซื้อสินค้าเกิน 1000 บาท จะได้รับส่วนลด 10%
    
    Input:
    - total_amount: float (ราคาสินค้ารวมทั้งหมด)
    
    Output:
    - คืนค่าเป็น float (ราคาสุทธิที่ต้องจ่าย)
    
    ตัวอย่าง Input/Output:
    - calculate_discount(1500) -> 1350.0 (ได้รับส่วนลด 150 บาท)
    - calculate_discount(1000) -> 1000.0 (ไม่ได้รับส่วนลดเพราะไม่เกิน 1000)
    - calculate_discount(500) -> 500.0 (ไม่ได้รับส่วนลด)
    - calculate_discount(2000) -> 1800.0 (ได้รับส่วนลด 200 บาท)
    """
    
    # --- เริ่มเขียนโค้ดด้านล่างนี้ ---
    raise NotImplementedError
    # --- สิ้นสุดการเขียนโค้ด ---

if __name__ == "__main__":
    try:
        print(f"Price for 1500: {calculate_discount(1500)}")
    except NotImplementedError:
        print("ยังไม่ได้เริ่มทำโจทย์ข้อ 14")
