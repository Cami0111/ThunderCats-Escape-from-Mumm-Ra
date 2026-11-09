from sys import stdin


def main():
    entrada = stdin.readline()
    t = int(entrada)

    for _ in range(t):
        n, m, k, v = map(int, stdin.readline().split())
        grafo = [[] for _ in range(n)]

        for _ in range(m):
            a, b, d = map(int, stdin.readline().split())
            a -= 1
            b -= 1
            grafo[a].append((b, d))
            grafo[b].append((a, d))

        lion, mumm_ra = map(int, stdin.readline().split())
        salidas = list(map(int, stdin.readline().split()))

        print(f"m:{m},n:{n},k:{k},v:{v}")
        print(*grafo)
        print(f"lion:{lion}  mumm_ra:{mumm_ra}")
        print(*salidas)


if __name__ == "__main__":
    main()
