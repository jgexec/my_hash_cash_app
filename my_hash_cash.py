import hashlib

#input: challenge should be a string, zero_bits should be an integer, proof should be an integer  
def verify_pow(challenge, zero_bits, proof):
    return hashlib.sha256((challenge + proof).encode('utf-8')).hexdigest().startswith('0' * int(zero_bits / 4))

#challenge should be a string, zero_bits should be an integer, proof should be an integer  
def find_pow(challenge, zero_bits):
    proof=1;
    
    while(1):
        input = challenge + str(proof)
                
        if hashlib.sha256((input).encode('utf-8')).hexdigest().startswith('0' * int(zero_bits / 4)):
            break;
        
        proof+=1
        
    return proof; 
