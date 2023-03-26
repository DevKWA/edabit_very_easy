def broken_bridge(hashes):
    return False if " " in hashes else True


print(broken_bridge('####'))
print(broken_bridge('## ####'))
print(broken_bridge('#'))
