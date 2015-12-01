.PHONY: clean run

run:
	python app.py

clean:
	find . -name '*.pyc' -delete
	find . -name '*.swp' -delete
