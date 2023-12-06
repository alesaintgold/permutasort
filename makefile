rmcache:
	rm -frd __pycache__ src/__pycache__ src/algorithms/__pycache__ src/algorithms/devices/__pycache__

rmlog:
	rm -f log/*

clean:
	make rmcache
	make rmlog
