import afstand

print(dir(afstand))

print(afstand.mile)

from afstand import mile_to_km as miljs_km

def mph_naar_ms(mph):

    ms = miljs_km(mph) / 3.6
    return ms

result1 = round(mph_naar_ms(50),2)
print(result1)
