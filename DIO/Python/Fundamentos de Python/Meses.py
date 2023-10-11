# Desafio de codigo imprimir o mes correspondente, em ingles, ao numero inserido

mes = int(input ()) # Entrada do numero do mes

dicionario_mes = {1:"January",2:"February",3:"March",
                  4:"April",5:"May",6:"June",
                  7:"July",8:"August",9:"September",
                  10:"October",11:"November",12:"December"}

if mes > 0 and mes <=12:
    print (dicionario_mes[mes])
else:
    print ("número inválido")
