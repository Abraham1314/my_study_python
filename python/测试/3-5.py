name = ['张三','李四','王麻子']
print(f"原来邀请 {name[0:]}来参加聚会")

canot = name.pop(1)
name.append('Abraham')

print(f"{canot}同志有事无法参加聚会")
print(f"{name[0]} 您好，你被请来参加我的聚会")
print(f"{name[1]} 您好，你被请来参加我的聚会")
print(f"{name[-1]} 您好，你被请来参加我的聚会")
