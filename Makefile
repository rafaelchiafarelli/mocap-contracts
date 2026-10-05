PYTHON ?= python3
GENERATED := gen/python gen/java schema/schema_registry mocap_contracts/messages.py mocap_contracts/zmq_endpoints.py

.PHONY: gen check-gen test test-slow

# Regenerate the Python contracts from schema/ with Harpia (needs Docker).
gen:
	$(PYTHON) tools/harpia_gen.py

# Regenerate and fail if anything committed changed.
check-gen: gen
	git diff --exit-code -- $(GENERATED)
	@test -z "$$(git ls-files --others --exclude-standard -- $(GENERATED))" \
		|| { echo "untracked generated files:"; git ls-files --others --exclude-standard -- $(GENERATED); exit 1; }

test:
	.venv/bin/pytest

# Also the slow tests: Gradle builds of the generated Java, Python <-> Java loopback (Docker).
test-slow:
	MOCAP_SLOW_TESTS=1 .venv/bin/pytest
