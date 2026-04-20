print("Валовий Анатолій (ОІ-23), lab-1 v-15")

import itertools
import numpy as np

constraints = [
    (7, 5, 7),
    (7, -5, 35),
    (1, -1, 10),
    (1, 0, 0),
    (0, 1, 0)
]

points = []

for (a1, b1, c1), (a2, b2, c2) in itertools.combinations(constraints, 2):
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    if np.linalg.det(A) != 0:
        solution = np.linalg.solve(A, B)
        points.append(tuple(solution))

def is_feasible(x1, x2):
    eps = 1e-6
    return (
        7 * x1 + 5 * x2 >= 7 - eps and
        7 * x1 - 5 * x2 >= 35 - eps and
        x1 - x2 <= 10 + eps and
        x1 >= -eps and
        x2 >= -eps
    )

feasible_points = []
for p in points:
    x1, x2 = p
    if is_feasible(x1, x2):
        feasible_points.append((round(x1, 5), round(x2, 5)))

feasible_points = list(set(feasible_points))

results = []
for x1, x2 in feasible_points:
    Z = 7 * x1 + 5 * x2
    results.append((x1, x2, Z))

min_point = min(results, key=lambda x: x[2])
max_point = max(results, key=lambda x: x[2])

print("\nТочки ОДР (кути заштрихованої фігури):")
for r in results:
    print(f"x1={r[0]}, x2={r[1]}, F={r[2]}")

print("\nМінімум:")
print(f"x1={min_point[0]}, x2={min_point[1]}, F={min_point[2]}")

print("\nМаксимум:")
print("Оскільки область допустимих розв'язків є необмеженою,")
print("максимального значення функції не існує (F прямує до +∞).")
print(f"Найбільше значення виключно серед кутових точок: x1={max_point[0]}, x2={max_point[1]}, F={max_point[2]}")