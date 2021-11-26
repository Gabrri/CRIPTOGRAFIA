%Valentina Lopez
%Jessenia Piza
%David Martinez


%Dictionary to pass from numbers to Letters
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

%Some Examples, just discomment to use someone
A = 'REIAUBLZXYQOKHMRNTEZHFLVIABHDMJMSJOGIRETPHBVVFTQHEXTARVIXSNQRIQPEJOLMDDEJORGVFECUTQVHIIKVMUKHVQPARPIVBIVGQIUFHIWZSTMBTHOSLXDNDFLFYIBPMRPOHCUOLJFEMSXIJBITHPSEQUXRZEEATPHDAFGLLQAXIQAKKRVFYTPHSVFGNLEQRVMTPWAXYQSCURETQONWTINMTMUMFFHEBKQVVPWMOXXYQSMDWMESAVGTMJEUJMQGKEWMPGWKZOBLYEXUNMWTEKFHMUQMJZOBKURXMTBKQFFFTWPAJKTEAHMFLFBIUQCVXLWZEEEP';

% Set a maximun j, number rows to get key length, big limit could be bad
% for IC calculation
max_j = 9;

%get j
j = get_j(A,max_j)

%once got j, get key
wkey = get_key(A,j)

%Custom Output for Homework encoded message
if A(1:3) == 'IEH'
    %Note that there is an error on second position guessing, by knowing j,
    %then the error occurs each j position starting by 2. k_2 is wrong

    % 'MENY' could be 'MANY', and 'IX' could be 'IT' it covert the text coherent

    %There are the same distance from ('X','T') and ('E','A')
    dist = distancia('X','T');
    dist1 = distancia('E','A');
    
    %distance is 4, so, substitute again k_2 by k_2+4.
    ckey = wkey;
    ckey(2) = mod(ckey(2) + dist,26);
    
    %Output
    fprintf('\n');
    disp('Cipher Message:');
    disp(A);
    fprintf('\n');
    disp('Plaintext:');
    disp(decode(A,j,ckey,Alphabet))
    fprintf('\n');
    Names = {'j';'NWrong_Key';'SWrong_Key';'Correct_Key';'SCorrect_Key';'k2_Error_Distance'};
    T = table(j,wkey,convertCharsToStrings(Alphabet(wkey+1)),ckey,convertCharsToStrings(Alphabet(ckey+1)),dist,'VariableNames',Names);
    disp(T)
else
    fprintf('\n');
    disp('Cipher Message:');
    disp(A);
    fprintf('\n');
    disp('Plaintext:');
    disp(decode(A,j,wkey,Alphabet))
    fprintf('\n');
end
%% Returns Key word for Str decoding -----> Phase 2
function [key] = get_key(A,j)

    %P_i ---> Frequencies of letters on English language
    idiom = [.082,.015,.028,.043,.127,.022,.020,.061,.070,.002,.008,.040,.024,.067,.075,.019,.001,.060,.063,.091,.028,.010,.023,.001,.020,.001];
    %Prealocate space for j-length key,
    key = zeros(1,j);

    %Pass the string to a j rows matrix.
    A_mat = str_to_mat(A,j)+1;
    
    %If there are blank spaces on Matrix, discard last column
    if A_mat(j,size(A_mat,2)) == 0
        A_mat= A_mat(:,1:end-1);
    end
    
    %row by row, find k_i
    for i=1:j
        fila = A_mat(i,:);
        m_g = zeros(1,26);
        
        %Get each M_g of row i
        for q = 1:26
            
            %Calculate p_i*f_{i+g}/total_letters_in_row
            m_g_i = zeros(1,26);
            for u=1:26
                p_r = idiom(u);
                dist = distrib(mod(fila,26));
                dist = dist(mod(u+q-1,26)+1)*p_r;
                m_g_i(u) = dist;
            end     
            m_g(q) = sum(m_g_i)/length(fila);
        end
        
        % If g = k_i, then M_g ~= English_IC
        %Cuadratic error (M_g,IC)
        m_g = (m_g-0.065).^2;
        
        %smallest cuadratic error means M_i nearest to english_IC
        fn = find(m_g==min(m_g));
        
        %Nearest M_g, means K_i = g
        key(i) = fn(1)-1;
        fn(1);
    end
end
%% Returns recommended j for Vigenre attack ----> Phase 1
% In String A, limit max j to get the best
% Out recommendend j
function [j] = get_j(A,limit_j)
    
    %Iterate over each j and get IC
    all_IC = ones(1,limit_j);
    
    for j=1:limit_j
        
        %Set Matrix of j rows
        Matrix = str_to_mat(A,j);
        
        %If there are blank spaces on Matrix, discard last column
        if Matrix(j,size(Matrix,2)) == -1
            Matrix = Matrix(:,1:end-1);
        end
    
        IC_j = zeros(1,j);
        for k=1:j
            IC = ind_c(Matrix(k,:));
            IC_j(k) = IC;
        end
        all_IC(j) = (mean(IC_j)-0.065)^2;
    end
    
    %Choose j which got smallest Cuadratic error
    j = find(all_IC==min(all_IC));
end
%% Receives any string and reshape it to a j rows Matrix
function [w] = str_to_mat(B,j)
    B = double(B)-65;
    cols = ceil(length(B)/j);
    B = [B ones(1,(j*cols)-length(B))*-1];
    w = reshape(B,[j,cols]);
end
%% Returns coincidence index of a vector (Matrix rows)
function [ic,f] = ind_c(x)
    ic = 0;
    f = zeros(1,26);
    for i=1:length(x)
        if x(i)>=0
            f(x(i)+1)= f(x(i)+1)+1;
        end
    end
    for i=1:26
        ic = ic + (f(i)*(f(i)-1))/(length(x)*(length(x)-1));
    end
end
%% Vigenere decode Algorithm
% In = c -> coded message, j, k --> word key, Alphabet --> vector with
% Alphabet letters
%Out decoded message
function [r] = decode(c,j,k,Alphabet)
    m = str_to_mat(c,j);
    m_f = m(:,end);
    for i=1:size(m,1)
        m(i,:) = mod(m(i,:)- k(i),26);
        if m_f(i) ~= -1
            m_f(i) = mod(m_f(i)- k(i),26);
        end
    end
    r = reshape(m(:,1:end-1),[1,size(m,1)*size(m,2)-j])+1;
    r = Alphabet([r m_f(m_f~=-1)'+1]);
end
%% Returns frequence distribution of a vector
function [ds] = distrib(x)
    ds = zeros(1,26);
    for i=1:length(x)
        ds(x(i)+1) = ds(x(i)+1) + 1;
    end
end
%% Measure distance between two Letters
function [ds] = distancia(l,l2)
    ds = (double(l)-65) - (double(l2)-65);
end
