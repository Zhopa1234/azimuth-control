 gpioblink : gpioblink.o
	cc -g -o gpioblink -g gpioblink.o


gpioblink.o: gpioblink.c
	cc -c -g gpioblink.c  # Runs second

#blah.c:
#	echo "int main() { return 0; }" > blah.c # Runs first
clean:
	rm  gpioblink gpioblink.o