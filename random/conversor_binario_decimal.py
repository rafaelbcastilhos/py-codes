while True:
    converter = input("Deseja converter [S/N]:")
    if converter == "N" or converter == "n":
        break

    pergunta = input("binario-decimal[B] ou decimal-binario[D]:")
    if pergunta == "B" or pergunta == "b":
        binario = input("binario:")

        str_binario = list(binario)
        decimal = 0
        numero_int = True
        
        for j in range(len(str_binario)):
            if str_binario[j] == ",":
                numeros_quebrados = len(str_binario) - j
                numero_int = False
                break
        
        if numero_int:
            casa = len(str_binario)
        else:
            casa = len(str_binario) - numeros_quebrados
            
        for i in str_binario:
            if i != ",":
                num = int(i)
                somar = num* (2**(casa -1))
                decimal += somar
                casa -= 1

        print(f"({binario})bin = ({decimal})dec")

    elif pergunta == "d" or pergunta == "D":
        str_decimal = input("decimal:")
        str_decimal_int = ""
        str_decimal_quebrado = ""

        numero_int = True
        for j in str_decimal:
            if j == ",":
                numero_int = False
            elif numero_int:
                str_decimal_int += j
            else:
                str_decimal_quebrado += j

        dividir_int = int(str_decimal_int)

        str_binario_int = []

        if not dividir_int:
            str_binario_int.append(0)
        else:
            while dividir_int != 1:
                binario = dividir_int%2
                str_binario_int.append(binario)
                dividir_int = dividir_int//2
                if dividir_int == 1:
                    str_binario_int.append(1)

        if not numero_int:
            str_binario_quebrado = []
            dividir_quebrada = int(str_decimal_quebrado)
            dividir_quebrada = dividir_quebrada/(10**len(str_decimal_quebrado))

            j = 0
            divisao = 1
            while j < 12:
                resultado = divisao/2
                if resultado < dividir_quebrada:
                    str_binario_quebrado.append("1")
                    dividir_quebrada -= resultado

                elif resultado > dividir_quebrada:
                    str_binario_quebrado.append("0")
                else:
                    str_binario_quebrado.append("1")
                    break
                divisao = resultado
                j += 1

        print(f"({str_decimal})dec = (", end="")
        i = 0
        while i < len(str_binario_int):
            print(f"{str_binario_int[len(str_binario_int) - i - 1]}", end="")
            i += 1
        if not numero_int:
            i = 0
            print(",",end="")
            while i < len(str_binario_quebrado):
                print(f"{str_binario_quebrado[i]}", end="")
                i += 1
        print(")bin")

    else:
        print("input invalido")

