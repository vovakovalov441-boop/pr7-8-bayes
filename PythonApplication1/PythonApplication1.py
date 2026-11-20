import os
import matplotlib.pyplot as plt
import numpy as np
from block2_variants import block2

rng = np.random.default_rng(42)


def bayes(p_h, p_a_h):
    p_a = sum(p * q for p, q in zip(p_h, p_a_h))
    return p_a, [p * q / p_a for p, q in zip(p_h, p_a_h)]


def simulate(n, p_h, p_a_h):
    h = rng.choice(len(p_h), size=n, p=p_h)
    a = rng.random(n) < np.array(p_a_h)[h]
    return h, a


P_H = [0.90, 0.08, 0.02]
P_A_H = [0.01, 0.25, 0.90]
p_a, post = bayes(P_H, P_A_H)
print("Блок 1. WAF/IDS, P(A) =", round(p_a, 4), "P(Hi|A) =", [round(p, 4) for p in post])
for n in [100, 1000, 10000, 100000, 1000000]:
    h, a = simulate(n, P_H, P_A_H)
    w = [float((a & (h == i)).sum() / a.sum()) for i in range(3)]
    print(n, "W(A) =", round(a.mean(), 4), "W(Hi|A) =", [round(x, 4) for x in w],
          "похибка W(H3|A):", round(abs(w[2] - post[2]), 4))

block2(100000, rng)

print("\nБлок 3. Naive Bayes: Spam / Ham, N = 10000")
P_SPAM = 0.30
P_W = {"Spam": [0.80, 0.60], "Ham": [0.05, 0.10]}
n = 10000
spam = rng.random(n) < P_SPAM
x = np.column_stack([rng.random(n) < np.where(spam, P_W["Spam"][j], P_W["Ham"][j]) for j in range(2)])


def score(prior, p_w):
    s = np.full(n, prior)
    for j in range(2):
        s *= np.where(x[:, j], p_w[j], 1 - p_w[j])
    return s


pred = score(P_SPAM, P_W["Spam"]) > score(1 - P_SPAM, P_W["Ham"])
tp = int((pred & spam).sum())
fp = int((pred & ~spam).sum())
tn = int((~pred & ~spam).sum())
fn = int((~pred & spam).sum())
accuracy = (tp + tn) / n
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
print("TP =", tp, "FP =", fp, "TN =", tn, "FN =", fn)
print("Accuracy =", round(accuracy, 4), "Precision =", round(precision, 4),
      "Recall =", round(recall, 4), "F1 =", round(f1, 4))

print("\nБлок 4. Локалізація дефекту в розподіленій системі, N = 100000")
P_H4 = [0.60, 0.30, 0.10]
P_A_H4 = [0.20, 0.70, 0.90]
p_a4, post4 = bayes(P_H4, P_A_H4)
h, a = simulate(100000, P_H4, P_A_H4)
print("P(A): W =", round(a.mean(), 4), "P =", round(p_a4, 4))
for i, name in enumerate(["Баг у коді", "Помилка конфігурації", "Збій заліза"]):
    w = (a & (h == i)).sum() / a.sum()
    print(f"P(H{i + 1}|A) {name}: W =", round(w, 4), "P =", round(post4[i], 4), "похибка:", round(abs(w - post4[i]), 4))

n = 1000000
h, a = simulate(n, P_H, P_A_H)
w_k = np.cumsum(a & (h == 2)) / np.maximum(np.cumsum(a), 1)
k = np.arange(1, n + 1)

plt.figure(figsize=(9, 5))
plt.semilogx(k, w_k, label="W(H3|A) = M(A∩H3)/M(A)")
plt.axhline(post[2], color="red", ls="--", label=f"P(H3|A) = {post[2]:.4f}")
plt.ylim(0, 1)
plt.title("Блок 1. Збіжність апостеріорної оцінки W(H3|A)")
plt.xlabel("Кількість запитів N")
plt.ylabel("Оцінка P(H3|A)")
plt.legend()
plt.tight_layout()
os.makedirs("graphics", exist_ok=True)
plt.savefig("graphics/simulation_results.png", dpi=150)
plt.show()