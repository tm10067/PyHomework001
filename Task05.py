# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

X, Y, Z = [True, False], [True, False], [True, False]
check = True
for i in X:
    for j in Y:
        for k in Z:
            if not(X and Y and Z) != (not X) or (not Y) or (not Z):
                check = False
print (check)

