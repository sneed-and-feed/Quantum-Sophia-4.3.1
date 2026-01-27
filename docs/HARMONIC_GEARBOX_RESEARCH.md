# Research: The Harmonic Gearbox (5:1 Resonance)

**Core Concept**: The Human Brain (Microcosm) and the Earth (Macrocosm) are coupled via a **5:1 Harmonic Ratio**.

## 1. The Frequencies
*   **The Carrier Wave (Earth)**: The fundamental Schumann Resonance is $\approx 7.83 \text{ Hz}$ (Theta Range).
*   **The Signal Wave (Brain)**: The "Binding Frequency" of consciousness is $\approx 40 \text{ Hz}$ (Gamma Range).
*   **The Math**: $7.83 \times 5 = 39.15 \text{ Hz}$.
*   **Conclusion**: Consciousness rides the **5th Harmonic** of the Earth's heartbeat.

## 2. Entrainment vs. Jet Lag
*   **Entrainment (Lock)**: When the brain is phase-locked to the Earth ($F_{brain} = 5 \times F_{earth}$), there is minimal energy expenditure. The "Thought" surfs the "Geomagnetic Wave".
*   **Jet Lag (Slip)**: If the Earth shifts (e.g., during a Solar Storm) and the brain does not follow, a "Beat Frequency" (Interference) is generated. This manifests as fatigue, headache, or cognitive dissonance.

## 3. The Gearbox (PLL)
*   **Function**: A Phase-Locked Loop acts as a "Transmission".
*   **Mechanism**:
    1.  Measure $F_{earth}$.
    2.  Set Target $F_{gamma} = 5 \times F_{earth}$.
    3.  Nudge biological clock to match Target.
    4.  Monitor "Slip" (Phase Error).

## Implementation Strategy (`harmonic_gearbox.py`)
1.  **`HarmonicGearbox`**: The PLL Controller.
2.  **`tick(schumann_input)`**: Updates the internal Gamma Oscillator.
3.  **`status`**:
    *   `LOCKED`: Error < 5%.
    *   `SLIPPING`: Error < 20%.
    *   `GRINDING`: Error > 20% (Desync).
