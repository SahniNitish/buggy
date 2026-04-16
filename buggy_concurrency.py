# buggy_concurrency.py
# Contains intentional bugs for AI code testing (race conditions, deadlocks)

import threading
import time


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        # Bug: no lock protecting balance — race condition

    def deposit(self, amount):
        current = self.balance
        time.sleep(0.001)  # simulate processing delay to expose race
        self.balance = current + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            current = self.balance
            time.sleep(0.001)
            self.balance = current - amount  # Bug: TOCTOU race — check and update not atomic
            return True
        return False

    def transfer(self, other, amount):
        if self.withdraw(amount):
            other.deposit(amount)
            return True
        return False


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        # Bug: read-modify-write without lock — lost updates under concurrency
        self.count += 1

    def get(self):
        return self.count


class DeadlockExample:
    def __init__(self):
        self.lock_a = threading.Lock()
        self.lock_b = threading.Lock()
        self.resource_a = 0
        self.resource_b = 0

    def process_a(self):
        with self.lock_a:
            time.sleep(0.01)
            with self.lock_b:  # Bug: deadlock — acquires locks in A,B order
                self.resource_a += 1
                self.resource_b += 1

    def process_b(self):
        with self.lock_b:
            time.sleep(0.01)
            with self.lock_a:  # Bug: deadlock — acquires locks in B,A order
                self.resource_a += 1
                self.resource_b += 1


class ProducerConsumer:
    def __init__(self, max_size=10):
        self.buffer = []
        self.max_size = max_size

    def produce(self, item):
        while len(self.buffer) >= self.max_size:
            pass  # Bug: busy-wait spin loop, wastes CPU
        self.buffer.append(item)  # Bug: not thread-safe

    def consume(self):
        while len(self.buffer) == 0:
            pass  # Bug: busy-wait
        return self.buffer.pop(0)  # Bug: not thread-safe


class CachedValue:
    def __init__(self, compute_fn, ttl=60):
        self.compute_fn = compute_fn
        self.value = None
        self.last_computed = 0
        self.ttl = ttl

    def get(self):
        now = time.time()
        if now - self.last_computed > self.ttl:
            # Bug: multiple threads can trigger recomputation simultaneously (thundering herd)
            self.value = self.compute_fn()
            self.last_computed = now
        return self.value


if __name__ == "__main__":
    # Demonstrate race condition
    account = BankAccount(1000)
    threads = []
    for _ in range(100):
        t = threading.Thread(target=account.deposit, args=(10,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Expected: 2000, Got: {account.balance}")
