import numpy as np

P_H = [0.05, 0.95]
P_A_H = [0.90, 0.02]
P_A = P_H[0] * P_A_H[0] + P_H[1] * P_A_H[1]
P_H1_A = P_H[0] * P_A_H[0] / P_A


def block2(n, rng):
    defect = rng.random(n) < P_H[0]
    alarm = rng.random(n) < np.where(defect, P_A_H[0], P_A_H[1])
    w_a = alarm.mean()
    w_h1_a = (defect & alarm).sum() / alarm.sum()
    w_tp = alarm[defect].mean()
    w_fp = alarm[~defect].mean()
    print("\nБлок 2. Аналізатор коду SAST, N =", n)
    print("P(A): W =", round(w_a, 4), "P =", round(P_A, 4), "похибка:", round(abs(w_a - P_A), 4))
    print("P(H1|A): W =", round(w_h1_a, 4), "P =", round(P_H1_A, 4), "похибка:", round(abs(w_h1_a - P_H1_A), 4))
    print("Помилка I роду P(A|H2): W =", round(w_fp, 4), "P =", P_A_H[1])
    print("Помилка II роду P(не A|H1): W =", round(1 - w_tp, 4), "P =", round(1 - P_A_H[0], 2))
    return w_a, w_h1_a