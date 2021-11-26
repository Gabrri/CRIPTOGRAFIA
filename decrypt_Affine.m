% Descifrar cifrado Affine
function d_k = decrypt_Affine(c, k)

    a = k(1);
    b = k(2);
    
    a_inv = Inverse(a);
    
    c_n = word2num(c);
    d = mod(a_inv .* (c_n - b), 26);
    d_k = num2word(d);
end