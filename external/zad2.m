% Probabilistyczny automat asynchroniczny

clear all
close all
n = 50; % rozmiar sieci n na n
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

alpha = 0.5;
beta = 0.3;
counter = 0;
% 4. Punkty 1–3 powtarzaj dopóki są komórki w stanie S
while (any(D(:) == 0))
    % 1. Wybierz losowa komórkę. Jeśli jest w stanie I to wylosuj liczbę przypadkowa x ∈ (0, 1).
    rand_cell = [randi([1, n]) randi([1, n])];
    rand_cell_state = D(rand_cell(1), rand_cell(2));
    if (0 < rand_cell_state && rand_cell_state < a + b)
        x = randi([0, 1]);
        % 2. Jeśli x < α wówczas zmień stan komórki z I na R.
        if (x < alpha)
            D(rand_cell(1), rand_cell(2)) = a;
        else
            % 3. W przeciwnym wypadku wybierz losowo najbliższego sąsiada.
            neig_x = 0;
            neig_y = 0;
            % while loop until we chose valid neighbour (not same point and meets the boundary conditions)
            while ((~neig_x && ~neig_y) || (1 > rand_cell(1) + neig_x) || (rand_cell(1) + neig_x > n) || ...
                                           (1 > rand_cell(2) + neig_y) || (rand_cell(2) + neig_y > n))
                neig_x = randi([-1 1]);
                neig_y = randi([-1 1]);
            end
            % Jeśli jest on w stanie S to zaraź go z prawdopodobieństwem 𝛽.
            if (~D(rand_cell(1) + neig_x, rand_cell(2) + neig_y))
                probability = randi([0 1]);
                if (probability <= beta)
                    D(rand_cell(1) + neig_x, rand_cell(2) + neig_y) = 1;
                end
            end
        end
    end
%     for row = 1:n
%        for col = 1:n
%            D(row, col) = D(row, col) + 1;
%        end
%     end
    if (counter >= 100)
        image(D); colormap(X); colorbar ; % stan poczatkowy
    %     title(strcat("iteration ", int2str(counter)))
        axis square;
        pause(0.00001)
        counter = 0;
    end
    counter = counter + 1;
end
  



