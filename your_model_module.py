
class ASOModel:
    def __init__(self):
        pass

    def predict_aso(self, rna_sequence):
        """
        Predicts ASO sequence from input RNA sequence.
        Takes first 20 bases or raises error if sequence is too short.
        
        Args:
            rna_sequence (str): Input RNA sequence
            
        Returns:
            str: First 20 bases of the sequence
            
        Raises:
            ValueError: If sequence is shorter than 20 bases
        """
        if len(rna_sequence) < 20:
            raise ValueError("RNA sequence is too short. Must be at least 20 bases long.")
        
        return rna_sequence[:20]

def load_model():
    """
    Creates and returns an instance of the ASO model.
    
    Returns:
        ASOModel: An instance of the ASO model
    """
    return ASOModel()
