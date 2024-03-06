import time


start = time.perf_counter()

def calc_sqr():

    print ("calc sqr numbers")
    for n in range(1,10001):
        time.sleep(0.0001)
        n* n
        print ("sqr of ", n, " is ", n * n)

calc_sqr()
end = time.perf_counter()
print ("Time taken is : ", end - start, " seconds")