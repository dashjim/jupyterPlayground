fn = 'ivr_rec_sankey.svg'
f = open(fn, encoding="utf-8")
output = []
need_remove = False
# for ind, p in enumerate(p_list)
for line in f:
    if "order [" in line:
        need_remove = True
    if "<?xml version" in line:
        need_remove = False
    if not need_remove:
        output.append(line)
f.close()
f = open(fn, 'w', encoding="utf-8")
f.writelines(output)
f.close()
