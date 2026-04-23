print("Валовий Анатолій (ОІ-23), lab-1 v-15")

import itertools
import numpy as np
import matplotlib.pyplot as plt

c1, c2 = 7, 5

constraints = [
    (7, 5, 7, '>='),
    (7, -5, 35, '<='),
    (1, -1, 10, '<='),
    (1, 0, 0, '>='),
    (0, 1, 0, '>=')
]

points = []

for (a1, b1, c1, _), (a2, b2, c2, _) in itertools.combinations(constraints, 2):
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    if np.linalg.det(A) != 0:
        solution = np.linalg.solve(A, B)
        points.append(tuple(solution))

def is_feasible(x1, x2, constraints):
    eps = 1e-6
    for a, b, c, sign in constraints:
        val = a * x1 + b * x2
        if sign == '>=' and val < c - eps: return False
        if sign == '<=' and val > c + eps: return False
        if sign == '==' and abs(val - c) > eps: return False
    return True

feasible_points = []
for p in points:
    x1, x2 = p
    if is_feasible(x1, x2, constraints):
        feasible_points.append((round(x1, 5), round(x2, 5)))

feasible_points = list(set(feasible_points))
results = []
for x1, x2 in feasible_points:
    Z = c1 * x1 + c2 * x2
    results.append((x1, x2, Z))

print("\nТочки ОДР (кути фігури):")
for r in results:
    print(f"x1={r[0]}, x2={r[1]}, F={r[2]}")

if results:
    min_point = min(results, key=lambda x: x[2])
    print(f"\nМінімум F = {min_point[2]}")
else:
    print("\nОДР порожня, розв'язків немає!")

plt.figure(figsize=(10, 8))

x_vals = np.linspace(-2, 15, 400)

for a, b, c, sign in constraints:
    if b != 0:
        y_vals = (c - a * x_vals) / b
        plt.plot(x_vals, y_vals, label=f'{a}x1 + {b}x2 {sign} {c}')
    else:
        plt.axvline(x=c/a, color='gray', linestyle='--', label=f'x1 {sign} {c/a}')

for x1, x2, _ in results:
    plt.plot(x1, x2, 'ko', markersize=6)

if results:
    plt.plot(min_point[0], min_point[1], 'ro', markersize=10, label=f'Мінімум ({min_point[0]}; {min_point[1]})')

plt.xlim(-2, 12)
plt.ylim(-12, 12)
plt.axhline(0, color='black', linewidth=1.2) # Вісь X
plt.axvline(0, color='black', linewidth=1.2) # Вісь Y
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(loc='upper right')
plt.title("Графічний метод (Оновлена умова)")
plt.xlabel("x1")
plt.ylabel("x2")

plt.show()
