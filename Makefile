all::	cpulimit

cpulimit:	cpulimit.c
	gcc -o cpulimit cpulimit.c -lrt -Wall -O2

clean:
	rm -f *~ cpulimit
