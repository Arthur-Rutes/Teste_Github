def anagaramas(palavra1 ,palavra2):

    return sorted(palavra1) == sorted(palavra2)


print(anagaramas("amar", "rama"))
print(anagaramas("batty", "tabby"))
print(anagaramas("uber", "rube"))