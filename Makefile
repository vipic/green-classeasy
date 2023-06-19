all: start

.PHONY: start
start:
	python3 run.py

.PHONY: build
build:
	cd web && npm run build
