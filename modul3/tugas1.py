size = int(input("masukkan size : "))
rumus = int(size/2)

# angka
print("*" * size)
for i in range(1,rumus):
    print("*" + " "* (size - 2) + "*")
for i in range(1,rumus):
    print("*" + " "* (size - 2) + "*")
print("*"*size)

print()

print("*" * size)
for i in range(1,rumus):
    print("*" + " "* (size - 2) + "")
print("*" * size)
for i in range(1,rumus):
    print("*" + " "* (size - 2) + "*")
print("*"*size)

print()

print("*" * size)
for i in range(1,rumus):
    print("*" + " "* (size - 2) + "*")
print("*" * size)
for i in range(1,rumus):
    print("*" + " "* (size - 2) + "*")
print("*"*size)

print()