#3) Use $100 to buy 100 chicken, hens or cocks, one cock spend $5, one hen
# spend $3 and one chick spend $1/3. Try to write code to find all
# combinations satisfied with this requirements.

combinations = []

for cocks in range(21):
    for hens in range(34): 
        chickens = 100 - cocks - hens 
        if chickens >= 0:
            cost = 5 * cocks + 3 * hens + (1 / 3) * chickens 
            if cost == 100:
                combinations.append((cocks, hens, chickens)) 

for i in combinations:
    print(f"Chickens: {i[2]},Hens: {i[1]}, Cocks: {i[0]} ")
