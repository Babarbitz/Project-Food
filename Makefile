PY=python3
TEST=pytest

.PHONY: run test

run:
	$(PY) src

test:
	$(TEST) src
