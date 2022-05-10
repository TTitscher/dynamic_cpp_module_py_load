# no real makefile. just a script to run all of these commands...
all:
	g++ -shared -fPIC -o impl3.so impl3.cpp
	g++ -shared -fPIC -o impl2.so impl2.cpp
	g++ -o main main.cpp -ldl
	# test 
	./main ./impl2.so SayHello
	./main ./impl3.so SayHello


clean:
	rm *.so
	rm main


