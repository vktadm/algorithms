def hanoi(from_peg, to_peg, temp_peg, disks):
    # Рекурсивно перемещаем n - 1 дисков из from_peg на temp_peg.
    if disks > 1:
        hanoi(from_peg, temp_peg, to_peg, disks - 1)

    # Перемещаем последний диск from_peg to to_peg.
    print(from_peg, "->",  to_peg)

    # Рекурсивно перемещаем верхние n - 1 disks обратно из temp_peg на to_peg.
    if disks > 1:
        hanoi(temp_peg, to_peg, from_peg, disks - 1)


hanoi("A", "C", "B", 4)