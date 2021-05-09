from time import perf_counter

t0 = perf_counter()
for i in range(10):
    print(i)
print(perf_counter() - t0)
