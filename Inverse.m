% Se halla el inverso de el numero a mod 26
function i= Inverse(a)

if(mod(a,2)== 0 | mod(a,13)== 0)
    return
else
    for i=1:26
        if (mod((a.*i),26)==1)
            i
            return
        end
    end
end
end

