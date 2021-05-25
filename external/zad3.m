% Probabilistyczny automat asynchroniczny

clear all
close all
n = 100; % rozmiar sieci n na n
a = 1; % ilosc stanow infekcyjnych: 1,...,a
b = 0; % ilosc stanow z odpornoscia: a+1,...,a+b
T=300;
p = 0.1; % poczatkowa czestosc wystepowania stanow infekcyjnych i opornych
%Przygotowanie COLORMAP
X0 = [0 1 0]; % podatni sa zieloni
Xa = [1 0 0]; % zarazeni sa zolto-czerwoni
X= cat(1,X0,cat(1,Xa)); % cala colormap

% Stan poczatkowy
D1 = 2; % macierz wypełniona liczbami z rozkładu płaskiego od 1 do a+b
D2 = rand(n,n) < p; %wybieramy wezly zarazeni i odporni
D = D1.*D2;

alpha = 0.2;
beta = 0.3;
counter = 0;
k = 9;
% 4. Punkty 1–3 powtarzaj dopóki są komórki w stanie S
while (any(D(:) == 0))
%     1. Wybierz losowa komórkę. Jeśli jest w stanie 𝐼, wówczas wylosuj x ∈ (0, 1)
    rand_cell = [randi([1, n]) randi([1, n])];
    rand_cell_state = D(rand_cell(1), rand_cell(2));
    x = randi([0, 1]);
%         2. Jeśli 𝑥 < 𝑐 = 1/(1 + 𝜆), wówczas 𝐼 → S
    n_ = fPoliczSasiadow(D, rand_cell(1), rand_cell(2));

    lambda = n_/k;
    c = 1/(1 + lambda);
    if (x < c)
        D(rand_cell(1), rand_cell(2)) = 0;
    else
%             3. W przeciwnym wypadku wybierz losowo najbliższego sąsiada.
        neig_x = 0;
        neig_y = 0;
%             while loop until we chose valid neighbour (not same point and meets the boundary conditions)
        while ((~neig_x && ~neig_y) || (1 > rand_cell(1) + neig_x) || (rand_cell(1) + neig_x > n) || ...
                                       (1 > rand_cell(2) + neig_y) || (rand_cell(2) + neig_y > n))
            neig_x = randi([-1 1]);
            neig_y = randi([-1 1]);
        end
%             jeśli jest on w stanie S to zmień ten stan na 𝐼.
        if (~D(rand_cell(1) + neig_x, rand_cell(2) + neig_y))
            D(rand_cell(1) + neig_x, rand_cell(2) + neig_y) = 2;
        end
    end

    
    if (counter >= 100)
        image(D); colormap(X); % stan poczatkowy
        axis square;
        pause(0.00001)
        counter = 0;
    end
    counter = counter + 1;
end
  



