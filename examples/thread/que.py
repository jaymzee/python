import queue
import threading
import time

# producer task
def task(count, queue, delay):
    while True:
        queue.put(count)
        time.sleep(delay)
        count += 1


def main():
    # shared queue
    q = queue.Queue()

    # start 2 producers
    threading.Thread(target=task, args=(1, q, 0.5), daemon=True).start()
    threading.Thread(target=task, args=(10, q, 0.1), daemon=True).start()
    print('started two threads')

    # consumer
    for _ in range(20):
        val = q.get()
        print(val)


if __name__ == "__main__":
    main()
