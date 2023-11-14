class DivisibleBySeven:
    def __init__(self, n):
        self.count = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.n:
            raise StopIteration
        else:
            self.count += 1
            return self.count if self.count % 7 == 0 else None

    def __len__(self):
        return self.n // 7


# Usage example
range_limit = 50
divisible_by_seven = DivisibleBySeven(range_limit)

for num in divisible_by_seven:
    print(num)
