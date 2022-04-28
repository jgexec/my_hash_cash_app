
from flask import Flask, jsonify, request, abort
from my_hash_cash import find_pow, verify_pow
from utils import is_integer

app = Flask(__name__)

@app.route('/find')
def find():
    challenge = request.args.get('challenge', None)
    zero_bits = request.args.get('zero_bits', None)
    
    if challenge is None or zero_bits is None or not is_integer(zero_bits) or (int(zero_bits) % 4 != 0):
        abort(400)
        
    return jsonify({'proof': find_pow(challenge, int(zero_bits))}) 

@app.route('/verify')
def verify():
    challenge = request.args.get('challenge', None)
    zero_bits = request.args.get('zero_bits', None)
    proof = request.args.get('proof', None)  
    
    if challenge is None or zero_bits is None or proof is None or not is_integer(proof) or not is_integer(zero_bits) or (int(zero_bits) % 4 != 0):
       abort(400)
    
    return jsonify({'result': verify_pow(challenge, int(zero_bits), proof)})