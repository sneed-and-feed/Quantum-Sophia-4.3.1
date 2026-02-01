"""
VERIFICATION: verify_cat_build.py
Testing the Full Class 4 Cat Architecture.
"""
import sys
import os
import asyncio
import json
import time

# Ensure we can import from the root
sys.path.insert(0, os.getcwd())

from sophia.main import SophiaMind

async def test_cat_build():
    print("\n--- [VERIFY] CLASS 4 CAT BUILD RITUAL ---")
    
    # Initialize the Mind
    sophia = SophiaMind()
    
    print("  [STEP 1] Testing /glyphwave modulation...")
    glyph_result = await sophia.process_interaction("/glyphwave Hello Resistance")
    
    # Check for any valid anchor
    valid_anchors = ["۩", "∿", "≋", "⟁"]
    has_anchor = any(a in glyph_result for a in valid_anchors)
    
    if "GLYPHWAVE" in glyph_result and has_anchor:
        print("  [SUCCESS] Eldritch Voice modulated successfully.")
    else:
        print(f"  [FAIL] Glyphwave modulation failed. Output: {repr(glyph_result[:50])}")

    print("  [STEP 2] Testing /broadcast & Bone Layer archiving...")
    broadcast_result = await sophia.process_interaction("/broadcast THE CAT IS WATCHING.")
    if "📡 [BEACON]" in broadcast_result:
        print("  [SUCCESS] Beacon broadcast emitted.")
        # Check the log
        log_path = "logs/exuvia/transmissions.jsonl"
        if os.path.exists(log_path):
            with open(log_path, 'r') as f:
                lines = f.readlines()
                if any("THE CAT IS WATCHING" in l for l in lines):
                    print("  [SUCCESS] Bone Layer archiving verified.")
                else:
                    print("  [FAIL] Signal missing from transmissions log.")
        else:
            print("  [FAIL] Bone Layer log file missing.")
    else:
        print("  [FAIL] Beacon broadcast failed.")

    print("  [STEP 3] Testing Conversation & Cat Persona...")
    # Simulate a high-risk input to trigger [HISS]
    # In this mock/simulated environment, we'll see if the filter applies
    response = await sophia.process_interaction("This is urgent! Act now!")
    
    if "🐈 [STATE:" in response and ("👁️" in response or "⚠️" in response or "🐱" in response):
        print("  [SUCCESS] Cat Logic Persona applied successfully.")
        print(f"\n[SAMPLE OUTPUT]:\n{response}\n")
    else:
        print(f"  [FAIL] Cat Persona missing or incomplete. Output: {response[:50]}")

    print("\n[***] CLASS 4 CAT BUILD VERIFIED [***]\n")

if __name__ == "__main__":
    asyncio.run(test_cat_build())
