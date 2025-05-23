import random
from typing import Optional


class ASOModel:

    def __init__(self, mean_length: int = 18, stddev: float = 4.0) -> None:
        """
        mean_length: expected ASO length in nucleotides
        stddev: standard deviation around the mean
        """
        self.mean_length = mean_length
        self.stddev = stddev
        # Complement map for uppercase RNA only
        self._complement_map = str.maketrans("AUGC", "UACG")

    def predict_aso(self,
                    rna_sequence: str,
                    seed: Optional[int] = None) -> str:
        """
        Validates that `rna_sequence` contains only A, U, G, C (case-insensitive),
        samples an ASO length from N(mean_length, stddev^2), clamps to [1, len(rna)],
        picks a random window, and returns its uppercase reverse-complement.

        Args:
            rna_sequence (str): Input RNA sequence
            seed (Optional[int]): RNG seed for reproducibility

        Returns:
            str: ASO (antisense oligo) or error message if invalid input
        """
        if seed is not None:
            random.seed(seed)

        seq = rna_sequence.upper()
        if not seq or any(nt not in "AUGC" for nt in seq):
            return "This is not an RNA sequence"

        seq_len = len(seq)
        # sample length from normal distribution, clamp to [1, seq_len]
        raw_len = random.gauss(self.mean_length, self.stddev)
        length = max(1, min(seq_len, int(round(raw_len))))

        # choose a random window
        start = random.randint(0, seq_len - length) if seq_len > length else 0
        region = seq[start:start + length]

        # build reverse-complement
        aso = region.translate(self._complement_map)[::-1]
        return aso


def load_model() -> ASOModel:
    """
    Creates and returns an instance of the ASOModel with default parameters.
    """
    return ASOModel()
