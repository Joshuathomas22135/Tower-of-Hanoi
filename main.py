"""A Python program that uses recursion to calculate the minimum number of moves needed to shift all disks from one peg to another using the rule hanoi(n) = 2 * hanoi(n-1) + 1."""

def towerOfHanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towerOfHanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towerOfHanoi(n-1, auxiliary, target, source)

num=3
towerOfHanoi(num, "A","C","B")