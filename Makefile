PY=python3
TEST=pytest

.PHONY: run test

run:
	$(PY) Food/src

test:
	$(TEST) Food/src
