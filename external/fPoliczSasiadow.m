%% funkcja zlicza sasiadow komorki (x,y) wg sasiedztwa Moore'a
% czyli maksymalnie osmiu sasiadow

function sasiedzi = fPoliczSasiadow(plansza,x,y)
    suma = 0;
    % chcemy wiedziec, jakie sa ograniczenia planszy, zeby za nia nie "wyjechac"
    [w,k] = size(plansza);
    
    if x>1 % w przeciwnym razie nie ma co zliczac, bo nie ma nikogo u gory
        if plansza(x-1,y)==2
            suma = suma+1;
        end
    end
    if y>1 % w przeciwnym razie nie ma co zliczac, bo nie ma nikogo po lewej
        if plansza(x,y-1)==2
            suma = suma+1;
        end
    end
    if x<w  % w przeciwnym razie nie ma co zliczac, bo nie ma nikogo na dole
        if plansza(x+1,y)==2
            suma = suma+1;
        end
    end
    if y<k % w przeciwnym razie nie ma co zliczac, bo nie ma nikogo po prawej
        if plansza(x,y+1)==2
            suma = suma+1;
        end
    end
    if x>1 && y>1 % w przeciwnym razie nie ma co zliczac, bo nie ma nikogo u gory po lewej
        if plansza(x-1,y-1)==2
            suma = suma+1;
        end
    end
    if x>1 && y<k % w przeciwnym razie nie ma co zliczac, bo nie ma nikogo u gory po prawej
        if plansza(x-1,y+1)==2
            suma = suma+1;
        end
    end
    if x<w && y>1 % w przeciwnym razie nie ma co zliczac, bo nie ma nikogo na dole po lewej
        if plansza(x+1,y-1)==2
            suma = suma+1;
        end
    end
    if x<w && y<k % w przeciwnym razie nie ma co zliczac, bo nie ma nikogo na dole po prawej
        if plansza(x+1,y+1)==2
            suma = suma+1;
        end
    end
    
sasiedzi = suma;    
   
end
  