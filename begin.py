def beg1 (c, h, w, n):
    import random as r
    begining = r.randint(1,100)
    if begining == 1:
        print ("На полу тёмной пещеры лежал без сознания", c, ". \nОн был жив или мёртв?\nВидимо, мёртв...")
        hp = 0
    else:
        print ("На полу мрачной пещеры без сознания лежал", c,". \nЕго звали", n,". Из оружия у него был лишь", w,".\n\'Человек открыл глаза\'\n\"Где это я? Помню, что я праздновал день рождения своего друга...а потом...\"")
        input()
        print ("Внезапно, у человека заболела голова, и он схватился за неё.")
        print ("Руки почувствовали какую-то сырость,", c, "посмотрел на ладони и увидел кровь...")
        input()
        hp = h-10
        print ("\'Ваш персонаж ранен, здоровье уменьшено на 10 ед. Здоровье:", hp,"/",h)
        print ("Встав,", c, "огляделся вокруг себя. Он увидел над собой небо, видимо, он провалился в яму.")
        print ("\"Назад я без помощи не выберусь.\"")
        input()
        print ("Вглуби пещеры", n, "заметил проход.")
        choose = input("1-Идти вглубь пещеры, 2-Оставаться на месте. Выбор:", )
        while choose != "1" and choose != "2":
            choose = input("1-Идти вглубь пещеры, 2-Оставаться на месте. Выбор:", )
        if choose == "2":
            print (n, "сидел в яме, ожидая помощи, 3 дня и скончался от голода.")
            hp = 0
    return hp