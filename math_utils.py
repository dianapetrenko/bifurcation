import numpy as np


class Histogram:
    def __init__(self, xmin, xmax, bins) -> None:
        self.xmin = xmin
        self.xmax = xmax
        self.bins = bins
        self.bin_size = (xmax - xmin)/bins
        # initiaze freq bins to 0
        self.freqs = [0 for _ in range(bins)]

    def reset_freqs(self):
        for i, _ in enumerate(self.freqs):
            self.freqs[i] = 0

    def get_i_bin(self, x):
        return int((x - self.xmin) // self.bin_size)
    
    def add(self, x):
        if x <= self.xmin:
            i_bin = 0
        elif x >= self.xmax:
            i_bin = self.bins - 1
        else:
            i_bin = self.get_i_bin(x)
        self.freqs[i_bin] += 1

    def get_x(self, i_bin):
        return (i_bin * self.bin_size) + self.xmin
    
    def get_bins_above_threshold(self, threshold):
        """
        threshold: percentage for the frequencies to be higher than threshold
        """
        max_freq = max(self.freqs) * threshold
        ibins = []
        for i, x in enumerate(self.freqs):
            if x > max_freq:
                ibins.append(i)
        return ibins


if __name__ == "__main__":
        
    # n_bins = 140
    n_bins = 200
    xmin = 0
    xmax = 1.4
    hist = Histogram(xmin, xmax, n_bins)

    data = list(np.arange(0.99, 1.01, 0.0001))
    for x in data:
        hist.add(x)

    print(hist.freqs)
    bins = hist.get_bins_above_threshold(0.28)
    for bin in bins:
        print(hist.get_x(bin))