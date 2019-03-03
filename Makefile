PY=python3
FLAGS=-B
TEST=pytest

.PHONY: run test

run:
	$(PY) $(FLAGS) Food/src

test:
	$(TEST) Food/src
