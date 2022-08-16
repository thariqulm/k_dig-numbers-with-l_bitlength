from time import perf_counter, perf_counter_ns

print(
    "To find the total natural numbers present with the given no.of digits and bitlength"
)
dig = int(input("Enter the number of digits :"))
bit_len = int(input("Enter the bitlength :"))
st = perf_counter()
stn = perf_counter_ns()
if 10**dig < 2**bit_len:
    ans = 10**dig - 2**(bit_len - 1)
elif 10**(dig - 1) > 2**(bit_len - 1):
    ans = 2**bit_len - 10**(dig - 1)
elif 10**(dig - 1) < 2**(bit_len - 1) and 10**dig > 2**bit_len:
    ans = 2**bit_len - 2**(bit_len - 1)

if ans > 0:
    print("There are %s" % ans + " %s-digit numbers" % dig +
          " with bitlength-%s" % bit_len)
else:
    print("There are NO %s-digit numbers" % dig +
          " with bitlength-%s" % bit_len)
etn = perf_counter_ns()
et = perf_counter()
print("Execution time : ", etn - stn, "nano seconds")
print("Execution time : ", (etn - stn) / 10**6, "milli seconds")
print("Execution time : ", et - st, "seconds")
