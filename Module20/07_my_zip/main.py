def shortest_seq_range(string, tpl):
    return min(len(string), len(tpl))

sym_str = 'abcd'
num_tpl = (10, 20, 30, 40)

pairs = ((sym_str[i_elem], num_tpl[i_elem]) for i_elem in range(shortest_seq_range(sym_str, num_tpl)))

print(pairs)
for i_elem in pairs:
    print(i_elem)

print(zip(sym_str, num_tpl))
