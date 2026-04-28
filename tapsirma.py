san = input("zat jazin: ")
a = list(san)

print("1_Sortlaw")
print("2_Teris aylandiriw")
print("3_1-haripti bas harip qiliw")
print("4_Barin bas harip qiliw")
print("5_Oshiriw yaki listti toliqtazalaw")
input = input("Qaysin isleyik? (1-5): ")

if input == "1":
    a.sort()
    print(a)
elif input == "2":
    a.reverse()
    print(a)
elif input == "3":
    print("".join(a).capitalize())
elif input == "4":
    print("".join(a).upper())
elif input == "5":
    a.remove()
    print(a)












