shorten_ipv6 = input()
split_ipv6 = shorten_ipv6.split(":")
tmp = shorten_ipv6.replace("::", ":").split(":")
if "" in tmp:
    tmp.remove("")
count = len(tmp)

original_ipv6_list = []
shorten = False
for component in split_ipv6:
    if component != "":
        original_ipv6_list.append(component.zfill(4))
    elif not shorten:
        shorten = True
        original_ipv6_list.extend(["0000" for _ in range(8 - count)])
print(":".join(original_ipv6_list))