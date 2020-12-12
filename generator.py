class Generator:

    def __init__(self, acc: tuple):
        self.acc: tuple = acc
        self.k: float = 0
        self.m: float = 0
        self.length: float = 0
        self.area: float = 0
        self.B_max: float = 0
        self.R: float = 0
        self.n: int = 0

    def constants(self, **kwargs) -> None:
        for name, value in kwargs.items():
            setattr(self, name, value)

    def Ec(self) -> float:
        Vsolenoid = self.area * self.length  # m**3
        u0 = 1.2566 * 10 ** -6  # N/A**2
        return self.B_max ** 2 / (2 * u0) * Vsolenoid  # J

    def energy(self) -> float:
        s, v = 0, 0
        v_sum, v_num = 0, 0
        eq = 0
        prev_t, prev_s = 0, 0
        for t, a_ext in self.acc:
            dt = t - prev_t
            a_net = -2 * self.k * s / self.m + a_ext
            v += a_net * dt
            s += v * dt
            if (abs(prev_s) - self.length) * (abs(s) - self.length) < 0:
                v_sum += abs(v)
                v_num += 1
            if s * prev_s < 0:
                eq += 1
            prev_t, prev_s = t, s
        return eq * self.Ec()
