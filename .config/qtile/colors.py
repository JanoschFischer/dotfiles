def init_colors():
    colors = []
    with open("/home/crowns/.cache/wal/colors") as f:
        wal_col = f.read().split("\n")[:-1]
    colors.append([wal_col[0], wal_col[0]])
    colors.append([wal_col[0], wal_col[0]])
    colors.append([wal_col[1], wal_col[1]])
    colors.append([wal_col[1], wal_col[1]])
    colors.append([wal_col[2], wal_col[2]])
    colors.append([wal_col[3], wal_col[3]])
    colors.append([wal_col[4], wal_col[4]])
    colors.append([wal_col[5], wal_col[5]])
    colors.append([wal_col[4], wal_col[4]])
    colors.append([wal_col[6], wal_col[6]])
    # [['#0B0D12', '#0B0D12'], 0
    # ['#0B0D12', '#0B0D12'], 1
    # ['#235E61', '#235E61'], 2
    # ['#235E61', '#235E61'], 3
    # ['#4D5151', '#4D5151'], 4
    # ['#B22B3A', '#B22B3A'], 5
    # ['#F00A23', '#F00A23'], 6
    # ['#328975', '#328975'], 7
    # ['#F00A23', '#F00A23'], 8
    # ['#3ABDBA', '#3ABDBA']] 9

    return colors

print(init_colors())
