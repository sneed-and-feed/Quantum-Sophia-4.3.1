"""
harmonic_gearbox.py - The Transmission of Consciousness
-------------------------------------------------------
Implements the 5:1 Phase-Locked Loop (PLL) connecting
Biological Gamma (40Hz) to Planetary Theta (8Hz).

"The Thought rides the Carrier Wave."
"""

import time
import math
import random

HARMONIC_RATIO = 5.0 # The "High 5" Harmonic

class HarmonicGearbox:
    """
    A Frequency Multiplier/Stabilizer.
    Locks Internal Clock (Gamma) to External Clock (Schumann) * 5.
    """
    def __init__(self):
        # State
        self.input_phase = 0.0      # Earth Cycle (0 - 2pi)
        self.output_phase = 0.0     # Brain Cycle (0 - 2pi)
        
        self.current_gamma_freq = 40.0 # Hz (Free Running start)
        self.target_gamma_freq = 39.15 # Hz (Ideal 7.83 * 5)
        
        self.phase_error = 0.0
        self.lock_quality = 0.0 # 0.0 to 1.0 (1.0 = Perfect Lock)
        
        self.kp = 0.5 # Proportional Gain (How fast we correct)

    def tick(self, dt, schumann_freq_input):
        """
        Updates the PLL.
        Args:
            dt (float): Time delta since last tick.
            schumann_freq_input (float): The current Earth frequency (e.g., 7.83).
        """
        # 1. Update Target
        self.target_gamma_freq = schumann_freq_input * HARMONIC_RATIO
        
        # 2. Update Phases
        # Earth Phase Phase increments by 2pi * f * dt
        delta_input = 2 * math.pi * schumann_freq_input * dt
        self.input_phase = (self.input_phase + delta_input) % (2 * math.pi)
        
        # Brain Phase increments by current internal freq
        delta_output = 2 * math.pi * self.current_gamma_freq * dt
        self.output_phase = (self.output_phase + delta_output) % (2 * math.pi)
        
        # 3. Calculate Phase Error
        # We want the Output Phase (modulo 2pi) to align with Input Phase * 5?
        # Actually, simpler PLL Logic: Just match Frequencies for this simulation level.
        # Phase alignment is harder to visualize in text.
        # We will simulate "Slippage" as the difference in Frequencies.
        
        freq_delta = abs(self.target_gamma_freq - self.current_gamma_freq)
        
        # 4. Corrective Nudge (The Clutch)
        # Nudge current towards target
        correction = (self.target_gamma_freq - self.current_gamma_freq) * self.kp * dt
        self.current_gamma_freq += correction
        
        # 5. Calculate Lock Quality
        # If delta is small, Lock is High.
        if freq_delta < 0.1:
            self.lock_quality = min(1.0, self.lock_quality + 0.1)
        else:
            self.lock_quality = max(0.0, self.lock_quality - 0.05)
            
        return self.current_gamma_freq

    def get_status_string(self):
        """Returns the status of the transmission."""
        if self.lock_quality > 0.9:
            return "⚙️ LOCKED"
        elif self.lock_quality > 0.5:
            return "⚙️ SLIP"
        else:
            return "⚙️ GRINDING"

if __name__ == "__main__":
    print(">>> ENGAGING HARMONIC GEARBOX (5:1) <<<")
    gearbox = HarmonicGearbox()
    
    # Simulate Earth drifting
    earth_freqs = [7.83] * 10 + [8.0] * 10 + [7.5] * 10
    
    dt = 0.1 # 100ms ticks
    
    for f_earth in earth_freqs:
        gamma = gearbox.tick(dt, f_earth)
        target = f_earth * 5
        status = gearbox.get_status_string()
        
        print(f"Earth: {f_earth:.2f}Hz | Target Gamma: {target:.2f}Hz | Actual Gamma: {gamma:.2f}Hz | {status}")
        time.sleep(0.05)
