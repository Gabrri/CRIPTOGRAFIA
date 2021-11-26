%Convierte numero a palabra
function out = num2word(num)
    Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    out = "";
    for i = 1:length(num)
        num_i = num(i);
        if(isnan(num_i))
            out = out + "";
        else
            out = out + Alphabet(num_i + 1);
        end
    end
end