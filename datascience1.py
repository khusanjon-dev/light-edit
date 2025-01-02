"""
10. Berilgan dars jadvali ma'lumotlaridan foydalanib, har bir kun uchun dars jadvalini yaratadigan  dasturni yozing.

Dars jadvali:
```
shedule = {
    'Matematika': ['dush', 'yak'],
    'Fizika': ['dush', 'sesh'],
    'Kimyo': ['chor', 'pay', 'jum'],
    'Biologiya': ['chor', 'jum', 'yak'],
    'Tarix': ['pay'],
    'Geografiya': ['jum', 'yak'],
    'Adabiyot': ['sesh', 'yak'],
}

hafta_kunlari = ['dush', 'sesh', 'chor', 'pay', 'jum', 'shan', 'yak']

```

Kutilayotgan yechim:
```
{
    'dush': ['Matematika', 'Fizika'],
    'sesh': ['Fizika', 'Adabiyot'],
    'chor': ['Kimyo', 'Biologiya'],
    'pay': ['Kimyo', 'Tarix'],
    'jum': ['Kimyo', 'Biologiya', 'Geografiya'],
    'shan': [],
    'yak': ['Matematika', 'Biologiya', 'Geografiya', 'Adabiyot']
}

```
"""
schedule = {
    'Matematika': ['dush', 'yak'],
    'Fizika': ['dush', 'sesh'],
    'Kimyo': ['chor', 'pay', 'jum'],
    'Biologiya': ['chor', 'jum', 'yak'],
    'Tarix': ['pay'],
    'Geografiya': ['jum', 'yak'],
    'Adabiyot': ['sesh', 'yak']
}
hafta_kunlari = ['dush', 'sesh', 'chor', 'pay', 'jum', 'shan', 'yak']
# javobni qaytarish uchun lug'at yaratib olamiz. bu yerda ham list comprehensiondan foydalandim
kunlik_jadval = {kun: [] for kun in hafta_kunlari}
# for operatori orqali kalit va qiymatlarni chiqarib olamiz
for fan, kunlar in schedule.items():
    # bizda har bir qiymat listlardan iborat. endi shu listlardan kunlarni ajratib olamiz.
    for kun in kunlar:
        # mos kunlarga darslarni joylaymiz
        kunlik_jadval[kun].append(fan)
# endi uni chop etamiz
for kun, fanlar in kunlik_jadval.items():
    print(f"{kun.capitalize()}: {', '.join(fanlar) if fanlar else "Dars yo'q"}")
