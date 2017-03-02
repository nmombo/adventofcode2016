clear; clc;

%% IMPORT DATA
input = [1 5 10 ; 2 4 4 ; 2 4 6 ; 2 4 5];   % test case, expecting: 2
input = csvread('advent_03.csv', 1,0);      % actual input for submission

%% CALCULATE NUMBER OF POSSIBLE TRIANGLES
input = sort(input,2); % sort
possibleTri = sum(input(:,1) + input(:,2) > input(:,3))

%% RE-IMPORT DATA
input = [101 301 501;102 302 502;103 303 503
         201 401 601;202 402 602;203 403 603];% test case, expecting: 6
input = csvread('advent_03.csv', 1,0);        % actual input for submission
input = [883 357 185 ; input];                % > 1256

%% SORT NEW DATA
i = 1;
mat = input';
while i <= max(size(input))
    input(i:i+2,:) = mat(:,i:i+2);
    i = i + 3;
end
input = sort(input,2);

%% RECALCULATE NUMBER OF POSSIBLE TRIALS
possibleTri = sum(input(:,1) + input(:,2) > input(:,3))