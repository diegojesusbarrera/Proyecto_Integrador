%HECHOS PARA LA PROBABILIDAD DE APROBAR PROGRAMACION LOGICA/

%HECHOS PUNTACION TEMA 1/
%% % tiene(A,B): A puntuacionT1 B

puntuacionT1(carlos,60 ).
puntuacionT1(bryan, 77).
puntuacionT1(raul, 80).
puntuacionT1(david, 90).
puntuacionT1(diego, 90).
puntuacionT1(johan, 50).
puntuacionT1(juanito, 100).
puntuacionT1(argenis, 55).
puntuacionT1(libenzi, 70).
puntuacionT1(katia, 88).

%HECHOS PUNTACION TEMA 2/
%% % tiene(A,B): A puntuacionT2 B

puntuacionT2(adrian, 80).
puntuacionT2(miguel, 82).
puntuacionT2(Washin, 80).
puntuacionT2(omar, 95).
puntuacionT2(medina, 55).
puntuacionT2(karina, 65).
puntuacionT2(pedro, 81).
puntuacionT2(leonel, 90).
puntuacionT2(jorge, 50).
puntuacionT2(rusel, 91).

%REGLAS PARA LAS PROBABILIDADES del T1

aprobadoT1(X,logica):- puntuacionT1(X,t77),puntuacionT1(X,80);puntuacionT1(X,90);puntuacionT1(X,100),puntuacionT1(X,70);puntuacionT1(x,88).
noaprobadoT1(X,logica):- puntuacionT1(X,60);puntuacionT1(X,50);puntuacionT1(X,55).

%REGLAS PARA LAS PROBABILIDADES del T2

proba(X,logica):- puntuacionT2(X,80);puntuacionT2(X, 82);puntuacionT2(X, 95);puntuacionT2(X,90);puntuacionT2(X,91).
probnoaprobar(X,logica):-puntuacionT2(X,55),puntuacionT2(X,65);puntuacionT2(X,50).
probaprobar(X,logica):- puntuacionT2(X,80);puntuacionT2(X,81);puntuacionT2(X,82);puntuacionT2(x,90);puntuacionT2(x,91);puntuacionT2(x,95).