## 5. adapt.harpia (owner: mocap-adapt/P4)

- **Depends on:** 4
- **Contract:**
  - In: —
  - Requires: joints named as in FreeMoCap; units in meters; Z-up coordinate system
  - Delivers: `MocapFrame` (frame_id, timestamp, body_joints, left_hand, right_hand, face_blendshapes, gaze_vector, emotion, foot_contact) and `MocapTake` (header + frames)
- **Pre-work:** none
- **Out of scope:** Filling in face/emotion (phase 2)
- **Tests:** JSON round-trip; a frame with empty face fields is valid
