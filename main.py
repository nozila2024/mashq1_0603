#1-misol
def qabul(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return "Hammasi musbat"
    else:
        return "Manfiy mavjud"

res = qabul(-2, -7, -3)
print(res)

#2-misol
def son_qabuli(son):
    if son >= 1 and son <= 9:
        return "Bir xonali"
    elif son >= 10 and son <= 99:
        return "Ikki xonali"
    else:
        return "Boshqa"

res = son_qabuli(555)
print(res)

#3-misol
def son_qabuli(a, b):
    if a % 2 == 0 and b % 2 != 0:
        return "Turli turdagi"
    else:
        return "Bir xil turdagi"

res = son_qabuli(5, 8)
print(res)

#4-misol
def matn_qabuli(matn):
    if len(matn) % 2 == 0 and len(matn) >= 6:
        return "mos keladi"
    else:
        return "Mos emas"

res = matn_qabuli("Nozila")
print(res)

#5-misol
def yosh_qabuli(yosh):
    if yosh < 18:
        return "Voyaga yetmagan"
    elif yosh >= 18:
        return "Talaba"
    else:
        return "Oddiy fuqoro"

res = yosh_qabuli(18)
print(res)
