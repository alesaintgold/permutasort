rmcache:
	rm -rd src/__pycache__ src/algorithms/__pycache__ src/algorithms/devices/__pycache__

clean:
	make rmcache
	rm log/*