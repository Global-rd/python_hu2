
#Bekérem a várost az összehasonlítások egyszerüsítése végett nagy kezdőbetüssé alakítom
city = input("Please enter the city: ").capitalize()
price = int(input("Please enter the price of the flat: "))

#Megnézem először melyik városokról van szó, és az alapján nézem meg az albérletek árait, és adok választ
if city == "New York" or city == "San Fransisco":
    result = "This flat is suitable for Sarah" if price <= 4000 else "This flat is NOT suitable for Sarah"
    print(result)
elif city == "Washington":
    print("No way she is moving there")
elif city == "Chicago":
    print("Money is no issue here, she is moving there")
else:
    result = "This flat is suitable for Sarah" if price <= 3000 else "This flat is NOT suitable for Sarah"
    print(result)