build:
	docker build -t diagrams .
run:
	docker run --rm -v `pwd`/app:/app diagrams diagram.py
