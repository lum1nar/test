v = [10, 6, 13, 7, 8]      # 物品價值
w = [6, 3, 9, 4, 2]        # 物品重量
capacity = 10              # 背包總容量

# 計算每個物品的單位價值
items = []
for i in range(len(v)):
    items.append((v[i] / w[i], v[i], w[i]))  # (單位價值, 價值, 重量)

# 按單位價值從大到小排序
items.sort(reverse=True)

total_value = 0
remain = capacity

for value_per_weight, value, weight in items:
    if remain >= weight:
        total_value += value
        remain -= weight
    else:
        total_value += value_per_weight * remain
        break

print(f"最大可取得價值: {total_value}")