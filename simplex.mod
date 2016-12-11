var x1 >=0;
var x2 >=0;
var x3 >=0;

maximize z: x1 + 14*x2 + 6*x3;

s.t. A : x1 + x2 + x3 <=4;
s.t. B : x1           <=2;
s.t. C :           x3 <=3;
s.t. D :    3*x2 + x3 <=6;
