"""
    Comentario multilinha
"""

x = 'bom dia'
y = "M5"
z = """
Um texto
multinha
qualquer
"""

# print(x)
# print(y)
# print(z)

# Tipagem dinamica
z = 5

# ``` $$

# Tipo imutável
template_str = f"Boa tarde M{z}"
# print(template_str)

# print(template_str[0])
# # template_str[0] = 'L'
# # print(template_str)

# str_len = len(template_str)
# print(str_len)

# print(len(template_str))


# print(template_str[len(template_str) - 1])
# print(template_str[-1])


# Slicing
template_str = f"Boa tarde M{z}"

# print(template_str[1:5])
# print(template_str)

# print(template_str[2:7:2])
# # print(template_str)

# print(template_str[:5])

# Split
str_split = template_str.split()

print(str_split)
print(type(str_split))


# Join
str_join = "_".join(str_split)

print(str_join)
print(type(str_join))
