class radar:
    def __init__(self):
        self.count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.gamma = []
        self.epsilon = []

        with open("data", "r") as data:
            self.d = [e.rstrip() for e in data.readlines()]

    def values(self):
        for line in self.d:
            for c in range(0, len(line)):
                if line[c] == "1":
                    self.count[c] += 1

    def calculate_gamma(self):
        z = 0
        for e in range(0, len(self.count)):
            if self.count[e] > 500:
                self.gamma.append(1)
            else:
                self.gamma.append(0)
        for b in self.gamma:
            z = (z << 1) | b
        return z

    def calculate_epsilon(self):
        z = 0
        for e in range(0, len(self.gamma)):
            if self.gamma[e] == 1:
                self.epsilon.append(0)
            else:
                self.epsilon.append(1)
        for b in self.epsilon:
            z = (z << 1) | b
        return z


if __name__ == "__main__":
    r = radar()
    r.values()
    print("Result: ", r.calculate_gamma() * r.calculate_epsilon())
