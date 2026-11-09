"""Tower of Hanoi"""

def towerOfHanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towerOfHanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towerOfHanoi(n-1, auxiliary, target, source)

num=3
towerOfHanoi(num, "A","C","B")