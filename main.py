from time import perf_counter, perf_counter_ns
from mpmath import riemannr,log
from math import comb
from decimal import Decimal
import cypari,requests
cond=1
def pifunc(n):
  global cond
  if n<=30000000000000:
    r=requests.get('https://primes.utm.edu/nthprime/index.php#piofx',params={'x':'%s'%n,})
    ans=r.text[6120:6160]
    for i in [',','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',""]:
      ans=ans.replace(i,'')
    pcount=""
    for k in ans:
      if k.isdigit():
        pcount=pcount+k
      if " " in k:
        break
    return int(pcount)
  else:
    cond=0
    return int(riemannr(n))
print(
    "To find the total natural numbers present with the given no.of digits and bitlength"
)
dig = int(input("Enter the number of digits :"))
bit_len = int(input("Enter the bitlength :"))
st = perf_counter()
stn = perf_counter_ns()
a=10**dig
b=2**bit_len
c=10**(dig-1)
d=2**(bit_len - 1)

if a < b:
    ans = a - d
    pia=pifunc(a)
    pid=pifunc(d)
    j=pia-pifunc(Decimal(a).sqrt())
    l=pid-pifunc(Decimal(d).sqrt())
    pcount=pia-pid
    #spcount=comb(pia,2)-comb(j,2)-comb(pid,2)+comb(l,2)
    sp=(a*log(log(a))/log(a))-(d*log(log(d))/log(d))
elif c > d:
    ans = b - c
    pib=pifunc(b)
    pic=pifunc(c)
    j=pib-pifunc(Decimal(b).sqrt())
    l=pic-pifunc(Decimal(c).sqrt())
    pcount=pib-pic
    #spcount=comb(pib,2)-comb(j,2)-comb(pic,2)+comb(l,2)
    sp=(b*log(log(b))/log(b))-(c*log(log(c))/log(c))

elif c < d and a > b:
    ans = b - d
    pib=pifunc(b)
    pid=pifunc(d)
    j=pib-pifunc(Decimal(b).sqrt())
    l=pid-pifunc(Decimal(d).sqrt())
    pcount=pib-pid
    #spcount=comb(pib,2)-comb(j,2)-comb(pid,2)+comb(l,2)
    sp=(b*log(log(b))/log(b))-(d*log(log(d))/log(d))

if ans > 0:
    print("There are %s" % ans + " %s-digit numbers" % dig +
          " with bitlength-%s" % bit_len)
    print("There are approximately %s %s-digit semi-prime numbers with bitlength-%s"%(int(sp),dig,bit_len))
    if cond==1:
      print("There are %s %s-digit prime numbers with bitlength-%s"%(pcount,dig,bit_len))
    elif cond==0:
      print("There are approximately %s %s-digit prime numbers with bitlength-%s"%(pcount,dig,bit_len))
else:
    print("There are NO %s-digit numbers" % dig +
          " with bitlength-%s" % bit_len)
etn = perf_counter_ns()
et = perf_counter()
print("Execution time : ", etn - stn, "nano seconds")
print("Execution time : ", (etn - stn) / 10**6, "milli seconds")
print("Execution time : ", et - st, "seconds")
