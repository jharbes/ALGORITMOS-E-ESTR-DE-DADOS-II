def hanoi(n, orig, dest, aux):
if n == 1:
print("Mover de",orig,"para",dest)
else:
hanoi(n-1, orig, aux, dest)
print("Mover de",orig,"para",dest)
hanoi(n-1, aux, dest, orig)
def main():
n = int(input("Digite a quantidade de discos: "))
hanoi(n, "A", "B", "C")
main()