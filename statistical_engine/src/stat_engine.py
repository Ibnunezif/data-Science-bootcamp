import math

class StatEngine:
    def __init__(self, data):
        if not data:
            raise ValueError("Data cannot be empty.")

        self.data = self._clean_data(data)

        if len(self.data) == 0:
            raise ValueError("No valid numeric data found.")

    def _clean_data(self, data):
        """Validate and clean input data."""
        cleaned = []
        for x in data:
            if isinstance(x, (int, float)):
                cleaned.append(x)
            else:
                raise TypeError(f"Invalid data type detected: {x} ({type(x)})")
        return cleaned

    # ---------- Central Tendency ----------

    def get_mean(self):
        """Return mean."""
        return sum(self.data) / len(self.data)

    def get_median(self):
        """Return median."""
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def get_mode(self):
        """Return mode (supports multimodal)."""
        freq = {}

        for x in self.data:
            freq[x] = freq.get(x, 0) + 1

        max_count = max(freq.values())

        if max_count == 1:
            return "No mode (all values are unique)"

        return [k for k, v in freq.items() if v == max_count]

    # ---------- Measure of Dispersion ----------

    def get_variance(self, is_sample=True):
        """Return variance (sample or population)."""
        n = len(self.data)
        mean = self.get_mean()

        if is_sample and n < 2:
            raise ValueError("Sample variance requires at least 2 data points.")

        denominator = n - 1 if is_sample else n

        return sum((x - mean) ** 2 for x in self.data) / denominator

    def get_standard_deviation(self, is_sample=True):
        """Return standard deviation."""
        return math.sqrt(self.get_variance(is_sample))

    def get_outliers(self, threshold=2):
        """Return outliers beyond threshold * std deviation."""
        mean = self.get_mean()
        std = self.get_standard_deviation()

        if std == 0:
            return []

        return [
            x for x in self.data
            if abs(x - mean) > threshold * std
        ]