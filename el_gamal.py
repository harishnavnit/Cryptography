def get_values() :
	m = int(raw_input("Enter message : "));		# message
	p = int(raw_input("Enter prime p : "));		# prime 'p'
	g = int(raw_input("Enter G : "));			# generator 'g'
	a = int(raw_input("Enter a : "));			# Client private key 'a'
	k = int(raw_input("Ephemeral key : "));		# Server private key, 'k'

	return {m, p, g, a, k};

def encrypt_message(p, g, a, k, m) :
	A  = pow(g, a) % p;							# Client public key 'A'
	c1 = pow(g, k) % p;							print "C1 = ".format(c1);
	c2 = m * (pow(A, k) % p);					print "C2 = ".format(c2);

	return {c1, c2, A};

def decrypt_message(c1, c2, k, p, a) :
	decrypted_text = pow(c1, a) % c2;
	return decrypted_text;

def main() :
		(m, p, g, a, k) = get_values();
		(c1, c2, A)		= encrypt_message(p, g, a, k, m);
		d_text			= decrypt_message(c1, c2, k, p, a);

		print "Decrypted Message : ".format(d_text);

if __name__ == "__main__" : main();
