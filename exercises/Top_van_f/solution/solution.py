a = float(input("Voer de coëfficiënt van x^2 in."))
b = float(input("Voer de coëfficiënt van x in."))
c = float(input("Voer de term zonder x in."))

alpha = (-b)/(2*a)
beta = (-b**2+4*a*c)/(4*a)

print("De coördinaat van de top van de grafiek van f is: T(",alpha,";",beta,")")
