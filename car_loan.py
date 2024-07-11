# ราคารถ
price = int(input('ราคารถ: '))

# เงินดาวน์
deposit = int(input('เงินดาวน์: '))

# ดอกเบี้ย
rate = float(input('ดอกเบี้ย: '))


# ระยะเวลา
duration = int(input('ระยะเวลา: '))


rate = rate/100
loan = price - deposit
monthly_paid = ((loan*rate)+loan)//duration
print(f'จ่ายงวดละ {monthly_paid}')