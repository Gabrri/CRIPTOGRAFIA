%Convierte palabra a numero
function out = word2num(word)
    Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y", "Z"];
    aux = split(word, "");
    aux = aux(2:length(aux) - 1);
    out = zeros(1, length(aux));
    for i = 1:length(aux)
        word_i = aux(i);
        for j = 1:26
            if(Alphabet(j) == word_i)
                out(i) = j - 1;
                break;
            end
        end
    end
 end