"""Karatsuba em binário - versão 0 (tudo num arquivo só).

Os prints seguem a ordem do quadro do professor:
  1. quem são x, x1, x0, y, y1, y0
  2. quem são A, B e C
  3. resolve A, B e C (aqui entra a recursão)
  4. volta e monta o resultado: 2^n·A + 2^(n/2)·(B - A - C) + C
"""


def karatsuba(x, y, nivel=0):
    pad = "│   " * nivel

    def p(texto=""):
        print(f"{pad}{texto}")

    p(f"┌─ karatsuba(x={x:b}, y={y:b})")

    # ---------- Caso base ----------
    if x < 2 or y < 2:
        r = x * y
        p(f"│  caso base (algum número tem 1 bit): {x:b} · {y:b} = {r:b}")
        p(f"└─ retorna {r:b}")
        return r

    # ---------- 1) Separar x e y ----------
    n = max(x.bit_length(), y.bit_length())
    m = n // 2
    mascara = (1 << m) - 1

    x1, x0 = x >> m, x & mascara
    y1, y0 = y >> m, y & mascara

    p(f"│  n = {n} bits, m = n/2 = {m}")
    p(f"│  x = {x:b} (={x})")
    p(f"│     x1 = {x1:b}   x0 = {x0:b}")
    p(f"│  y = {y:b} (={y})")
    p(f"│     y1 = {y1:b}   y0 = {y0:b}")

    # ---------- 2) Definir A, B e C ----------
    soma_x = x1 + x0
    soma_y = y1 + y0
    p("│")
    p("│  Definindo:")
    p(f"│     A = x1·y1           = {x1:b} · {y1:b}")
    p(f"│     B = (x1+x0)·(y1+y0) = {soma_x:b} · {soma_y:b}")
    p(f"│     C = x0·y0           = {x0:b} · {y0:b}")

    # ---------- 3) Resolver A, B e C (recursão) ----------
    p("│")
    p("│  Resolvendo A, B e C:")

    p(f"│  >> A: chamando recursivamente karatsuba({x1:b}, {y1:b})")
    A = karatsuba(x1, y1, nivel + 1)
    p(f"│  << voltou da recursão: A = {A:b}")

    p(f"│  >> B: chamando recursivamente karatsuba({soma_x:b}, {soma_y:b})")
    B = karatsuba(soma_x, soma_y, nivel + 1)
    p(f"│  << voltou da recursão: B = {B:b}")

    p(f"│  >> C: chamando recursivamente karatsuba({x0:b}, {y0:b})")
    C = karatsuba(x0, y0, nivel + 1)
    p(f"│  << voltou da recursão: C = {C:b}")

    # ---------- 4) Montar o resultado ----------
    meio = B - A - C
    resultado = (A << (2 * m)) + (meio << m) + C

    p("│")
    p("│  Montando o resultado:")
    p(f"│     x·y = 2^{2*m}·A + 2^{m}·(B - A - C) + C")
    p(f"│     x·y = 2^{2*m}·({A:b}) + 2^{m}·({B:b} - {A:b} - {C:b}) + {C:b}")
    p(f"│     x·y = 2^{2*m}·({A:b}) + 2^{m}·({meio:b}) + {C:b}")
    p(f"│     x·y = {A << (2*m):b} + {meio << m:b} + {C:b}")
    p(f"│     x·y = {resultado:b} (={resultado})")
    p(f"└─ retorna {resultado:b}")
    return resultado


if __name__ == "__main__":
    x, y = 0b0001, 0b0011  # exemplo do quadro: 11 * 9 = 99

    r = karatsuba(x, y)

    print()
    print(f"Karatsuba: {r:b} ({r})")
    print(f"Normal:    {x * y:b} ({x * y})")
    print("Correto!" if r == x * y else "ERRO!")