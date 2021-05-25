clear all
close all
n = 100; % rozmiar sieci n na n
a = 4; % ilosc stanow infekcyjnych: 1,...,a
b = 10; % ilosc stanow z odpornoscia: a+1,...,a+b
T=300;
p = 0.2; % poczatkowa czestosc wystepowania stanow infekcyjnych i opornych
%Przygotowanie COLORMAP
X0 = [0 1 0]; % podatni sa zieloni
Xa = colormap(autumn(a)); % zarazeni sa zolto-czerwoni
Xb = colormap(winter(b)); % odporni sa niebiesko-zieloni
X= cat(1,X0,cat(1,Xa,Xb)); % cala colormap
% Stan poczatkowy
D1 = ceil((a+b)*rand(n,n)); % macierz wypełniona liczbami z rozkładu płaskiego od 1 do a+b
D2 = rand(n,n) < p; %wybieramy wezly zarazeni i odporni
D = D1.*D2;

for iter = 1:T
    temp_D = D;
%     rand_cell = D(rand)
    for row = 1:n
       for col = 1:n
          if (D(row, col) == 0)
              for i = -1 : 1
                 for j = -1 : 1
                     if (0 < i + row && i + row < n)
                          if (0 < j + col && j + col < n)
                              if (0 < D(row + i , col + j) && D(row + i , col + j) <= a)
                                   temp_D(row, col) = 1;
                              end
                          end
                     end
                 end
              end
          elseif(D(row, col) < a + b)
              temp_D(row, col) = D(row, col) + 1;
          else
              temp_D(row, col) = 0;
          end
       end
    end
    D = temp_D;
    image(D); colormap(X); colorbar ; % stan poczatkowy
    title(strcat("iteration ", int2str(iter)))
    axis square;
    pause(0.05)
end
