def calculate_ascii_sum(input_string):
    # ตรวจสอบความยาวของ input
    if not (0 < len(input_string) <= 10):
        return 

    # ตรวจสอบอักขระใน input
    for char in input_string:
        if not (32 <= ord(char) <= 126):  # เช็คว่า ASCII อยู่ในช่วงที่กำหนด
            return

    # คำนวณผลรวมของ ASCII
    ascii_sum = sum(ord(char) for char in input_string)
    return ascii_sum

# รับ input จากผู้ใช้
input_string = input()
result = calculate_ascii_sum(input_string)

# แสดงผลลัพธ์
print(result)
