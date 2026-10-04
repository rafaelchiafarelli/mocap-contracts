## 3. extract.harpia (owner: mocap-extract/P3)

- **Depends on:** 2
- **Contract:**
  - In: —
  - Requires: imports `capture.harpia`
  - Delivers: `ExtractIndex` (paths of synced videos, calibration, body/hands 3D, per-camera 2D), `CameraQuality` (detection_rate body/hands, jitter_px, reproj_err_px), `QualityReport`
- **Pre-work:** none
- **Out of scope:** —
- **Tests:** JSON round-trip
