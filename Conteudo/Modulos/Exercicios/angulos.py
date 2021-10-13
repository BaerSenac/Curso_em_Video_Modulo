from math import radians,sin,cos,tan
angulo = float(input("Insira um ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("o angulo de {} tem o seno de {:.2f}".format(angulo,seno))
print("O angulo de {} tem o cosseno de {:.2f}".format(angulo,cosseno))
print("O angulo de {} tem o tangente de {:.2f}".format(angulo,tangente))