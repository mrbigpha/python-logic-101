import importlib
import os
import sys

def run_test(ex_name, func_name, cases):
    if not os.path.exists(f"{ex_name}.py"):
        return "NOT_FOUND"
    
    try:
        # ล้าง cache เพื่อโหลดโค้ดใหม่
        if ex_name in sys.modules:
            importlib.reload(sys.modules[ex_name])
        module = importlib.import_module(ex_name)
        func = getattr(module, func_name)
        
        # ตรวจสอบก่อนว่ามีการเริ่มทำหรือยัง (ลองรันเคสแรก)
        try:
            func(*cases[0][0])
        except NotImplementedError:
            return "SKIPPED" # ไม่ต้องพูดถึงเลย
            
        print(f"📌 {ex_name}:")
        passed_count = 0
        total_cases = len(cases)
        
        for args, expected in cases:
            try:
                result = func(*args)
                if result == expected:
                    print(f"    ✅ ทดสอบ {args} -> ผ่าน")
                    passed_count += 1
                else:
                    print(f"    ❌ ทดสอบ {args} -> ไม่ผ่าน (ได้: {repr(result)}, คาดหวัง: {repr(expected)})")
            except Exception as e:
                print(f"    ❌ ทดสอบ {args} -> เกิดข้อผิดพลาด ({e})")
        
        percentage = (passed_count / total_cases) * 100
        print(f"--- {ex_name} ผ่าน {percentage:.0f}% ---\n")
        return passed_count == total_cases
        
    except Exception as e:
        print(f"📌 {ex_name}: ⚠️ ไม่สามารถโหลดไฟล์ได้ ({e})\n")
        return False

# รายการโจทย์
all_tests = [
    ("ex01_is_even", "is_even", [((2,), True), ((3,), False), ((0,), True), ((-4,), True), ((-5,), False)]),
    ("ex02_is_positive", "is_positive", [((5,), True), ((-2,), False), ((0,), False), ((100,), True), ((-0.5,), False)]),
    ("ex03_check_grade", "check_grade", [((75,), "Pass"), ((45,), "Fail"), ((50,), "Pass"), ((0,), "Fail"), ((100,), "Pass")]),
    ("ex04_can_vote", "can_vote", [((18,), True), ((17,), False), ((25,), True), ((0,), False), ((150,), True)]),
    ("ex05_absolute_value", "absolute_value", [((10,), 10), ((-5,), 5), ((0,), 0), ((-100,), 100), ((3.14,), 3.14)]),
    ("ex06_find_max", "find_max", [((10, 20), 20), ((50, 10), 50), ((30, 30), 30), ((-5, -10), -5), ((0, 0), 0)]),
    ("ex07_is_teenager", "is_teenager", [((15,), True), ((12,), False), ((13,), True), ((19,), True), ((20,), False)]),
    ("ex08_get_ticket_price", "get_ticket_price", [((10,), 50), ((15,), 100), ((12,), 100), ((5,), 50), ((60,), 100)]),
    ("ex09_is_vowel", "is_vowel", [(('a',), True), (('b',), False), (('E',), True), (('z',), False), (('u',), True)]),
    ("ex10_get_sign", "get_sign", [((10,), "positive"), ((-5,), "negative"), ((0,), "zero"), ((0.1,), "positive"), ((-99,), "negative")]),
    ("ex11_is_leap_year", "is_leap_year", [((2000,), True), ((1900,), False), ((2024,), True), ((2023,), False), ((2100,), False)]),
    ("ex12_atm_withdrawal", "atm_withdrawal", [((2600,), "1000: 2, 500: 1, 100: 1"), ((1000,), "1000: 1, 500: 0, 100: 0"), ((255,), "Invalid"), ((700,), "1000: 0, 500: 1, 100: 2"), ((150,), "Invalid")]),
]

if __name__ == "__main__":
    started = 0
    passed = 0
    failed = 0
    
    for ex, func, cases in all_tests:
        status = run_test(ex, func, cases)
        if status == "SKIPPED" or status == "NOT_FOUND":
            continue
            
        started += 1
        if status == True:
            passed += 1
        else:
            failed += 1

    if started == 0:
        print("💡 ยังไม่ได้เริ่มทำโจทย์ข้อไหนเลย เริ่มทำได้ที่ไฟล์ ex01_is_even.py!")
    elif failed == 0 and passed == len(all_tests):
        print("🎉 ยินดีด้วย! คุณผ่านโจทย์ครบทุกข้อแล้ว! (100%)")
    else:
        print(f"📊 สรุปผลการทำ: เริ่มทำแล้ว {started}/{len(all_tests)} ข้อ")
        print(f"   - ผ่านแล้ว: {passed} ข้อ")
        if failed > 0:
            print(f"   - ยังต้องแก้ไข: {failed} ข้อ")
