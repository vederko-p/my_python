menu = dict(
    Пепперони = dict(
            consist='Пепперони, моцарелла, томатный соус',
            size_price=dict(S=395,M=545)
    ),
    Маргарита = dict(
            consist='Томаты, моцарелла, томатный соус',
            size_price=dict(S=395,M=545)
    ),
    Гавайская = dict(
            consist='Курица, ветччина,ананас, моцарелла, томатный соус',
            size_price=dict(S=395,M=545)
    )
)

print(menu['Пепперони']['size_price']['S'])
print(menu['Маргарита']['consist'])
print(menu['Гавайская']['size_price']['M'])
