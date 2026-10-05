"""camera-protocol camera-messages/2-3: the generated Java (gen/java). Slow."""

import pytest
from java_harness import SKIP_REASON, SLOW, docker_ok, gradle, stage_java

pytestmark = pytest.mark.skipif(not (SLOW and docker_ok()), reason=SKIP_REASON)


def test_generated_java_project_builds():
    java = stage_java()
    r = gradle("build")
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert list((java / "build" / "libs").glob("*.jar"))
