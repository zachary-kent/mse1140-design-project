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

    def set_properties(self, **kwargs) -> None:
        for name, value in kwargs.items():
            setattr(self, name, value)

    # Vf=(2*k*xi+m*aext)*dt/m
    def get_energy(self) -> float:
        s = 0
        prev_t = 0
        v = 0
        v_sum, v_num = 0, 0
        for t, a_ext in self.acc:
            dt = t - prev_t
            a_net = -2 * self.k * s / self.m + a_ext
            v += a_net * dt
            s += v * dt
            if abs(abs(s) - self.length) < 0.0005:
                v_sum += abs(v)
                v_num += 1
            prev_t = t
        v_at_len = v_sum / v_num
        Ec = self.area ** 2 * self.B_max ** 2 * v_at_len * self.n ** 2 / (self.length * self.R)
        v_at_len = (2 * (0.5 * self.m * v_at_len * 2 - Ec) / self.m) ** 0.5
        Ec1 = self.area ** 2 * self.B_max ** 2 * v_at_len * self.n ** 2 / (self.length * self.R)
        return Ec1
