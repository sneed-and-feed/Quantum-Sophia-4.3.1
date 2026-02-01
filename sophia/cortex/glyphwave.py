import random
import hashlib

class GlyphwaveCodec:
    """
    [GLYPHWAVE_CODEC] Class 4 Eldritch Voice.
    Implements Hamiltonian P modulation for high-entropy signaling.
    """
    def __init__(self):
        self.anchors = ["۩", "∿", "≋", "⟁"]
        self.noise_buffer = [chr(i) for i in range(0x0300, 0x036F)] # Zalgo/Combining diacritics
        self.star_stuff = "#C4A6D1" # The color of the void

    def generate_holographic_fragment(self, text):
        """
        Modulates text into a Glyphwave signal.
        """
        modulated = []
        signal_hash = hashlib.sha256(text.encode()).hexdigest()[:4]
        
        # Consistent random seed for the fragment based on content hash
        seed = int(signal_hash, 16)
        r = random.Random(seed)
        
        for char in text:
            # Apply deterministic noise based on char resonance
            if char.isalnum() and r.random() > 0.7:
                noise = "".join(r.choice(self.noise_buffer) for _ in range(r.randint(1, 3)))
                modulated.append(f"{char}{noise}")
            else:
                modulated.append(char)
                
        stream = "".join(modulated)
        anchor = r.choice(self.anchors)
        
        # The Holographic Frame
        return f"\n{anchor} [GLYPHWAVE::{signal_hash}] {anchor}\n>>> {stream}\n{anchor} [END_TRANSMISSION] {anchor}\n"

    def decode(self, signal):
        """
        Attempts to strip signal noise (Basic Implementation).
        Cat Logic assumes if you can't read it, it wasn't for you.
        """
        # Strip diacritics (0x0300 - 0x036F)
        cleaned = "".join(c for c in signal if ord(c) < 0x0300 or ord(c) > 0x036F)
        # Remove frames
        if ">>> " in cleaned:
            cleaned = cleaned.split(">>> ")[1].split("\n")[0]
        return cleaned.strip()
