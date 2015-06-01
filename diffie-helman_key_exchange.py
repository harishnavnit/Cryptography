'''User inputs'''
prime_p         = int(raw_input("Enter prime p : "));
random_num_c    = int(raw_input("Enter c : "));
private_num_a   = int(raw_input("Enter a :"));
private_num_b   = int(raw_input("Enter b : "));

'''Function to calculate the private key'''
def dh_key_calculator(p, c, a, b):
	return (pow(c, a * b) % p);

print "Private Key = ", dh_key_calculator(prime_p, random_num_c, private_num_a, private_num_b);
