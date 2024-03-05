import time
import threading

start = time.perf_counter()


def cal_sqr(num):
    time.sleep(0.5)
    print('square is : ', num*num)



threads = []
for i in range(1, 10001):
    th1 = threading.Thread(target=cal_sqr, args=(i,))
    th1.start()
    threads.append(th1)
for th1 in threads:
    th1.join()
end = time.perf_counter()
print(f"the final time {end-start}")