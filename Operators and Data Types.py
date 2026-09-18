Snack_Name="chips"
Price=50
Quantity=6
available=True

print("snack:",Snack_Name)
print("price:",Price)
print("available?:",available)

print(type(Snack_Name))
print(type(Price))
print(type(Quantity))
print(type(available))

total=Price*Quantity
print("Total bill is:",total)

print("is price under20?:",Price<20)
print("is price exactly 50?:",Price==50)

shop_name="Quick"+"Bites"
print("Shop name:",shop_name)
print("Letters in snack name are:",len(Snack_Name))

a=20
b=13
print("Before:",a ,"and", b)
temp=a
a=b
b=temp
print("After:",a,"and",b)
