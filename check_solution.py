import importlib
import os
import sys

def run_test(ex_name, func_name, cases):
    if not os.path.exists(f"{ex_name}.py"):
        return True # ยังไม่ทำ ไม่นับเป็น Error แต่ไม่ขึ้นเขียว
    
    try:
        module = importlib.import_module(ex_name)
        func = getattr(module, func_name)
        for args, expected in cases:
            if func(*args) != expected:
                print(f"❌ {ex_name}: ทดสอบ {args} ผิดพลาด!")
                return False
        print(f"✅ {ex_name}: ผ่าน!")
        return True
    except Exception as e:
        print(f"⚠️ {ex_name}: โค้ดมีปัญหา ({e})")
        return False

# รายการโจทย์และ Test Cases
all_tests = [
    ("ex01_is_even", "is_even", [((2,), True), ((3,), False)]),
    # ... เพิ่มให้ครบ 10 ข้อ
]

errors = 0
for ex, func, cases in all_tests:
    if not run_test(ex, func, cases):
        errors += 1

if errors > 0:
    sys.exit(1)
