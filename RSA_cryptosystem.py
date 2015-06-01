'''Accept user inputs'''
def get_values() :
	''' User inputs '''
	p = int (raw_input("Enter p : "));
	q = int(raw_input("Enter q : "));
	e = int(raw_input("Enter public key 'e' : "));
	m = int(raw_input("Enter message : "));

	return {p, q, e, m};

'''Function to decrypt the plain text'''
def encrypt_text(n, pi_n, m, e) :
	d = pow(e, pi_n - 2) % pi_n;	# Public Key, de = 1 (mod(pi_n))
	c = pow(m, e) % n;				# Encrypted text
	print "Private key : ".format(d);
	print "Encrypted text : ".format(c);
	return {d, c};

'''Function to decrypt the encrypted text'''
def decrypt_text(c, d, n) :
	plain_text = pow(c, d) % n;		# Decrypted plain text
	return plain_text;

'''Check if the decrypted text and the original plain text match'''
def check_sanity(plain_text, m) :
	return (plain_text == m);

def main() :
	(p, q, e, m) = get_values();
	n		= p * q;				print "N = ".format(n);
	pi_n	= (p-1) * (q-1);		# Euler totient function

	(encryptedText, private_key)= encrypt_text(n, pi_n, m, e);
	decryptedText				= decrypt_text(encryptedText, private_key, n);

	print ( "Passed" if (check_sanity(decryptedText, m)) else "Failed");

if __name__ == "__main__" : main();
