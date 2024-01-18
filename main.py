meme_dict = {
            "gaje": "GAk JElas",
            "gabut": "gak ada kerjaan",
            "ygy": "Ya Guys Ya",
            "cmiiw": "Correct Me If I'm Wrong (koreksi saya jika saya salah)",
            "gercep": "GERak CEPat",
            "mager": "MAles GERak",
            "mantul": "MANtap beTUL",
            "jadul": "JAman DULu",
            "anw": "anyway (ngomong-ngomong)",
            "btw": "By The Way (ngomong-ngomong)",
            "aka": "As Known As (Alias)",
            "otw": "On The Way (dalam perjalanan)",
            "lol": "Laugh Of Loud (tertawa keras)",
            "gws": "Get Well Soon (semoga lekas sembuh)"
            }
            
            
for i in range(len(meme_dict):
    word = input("Ketik kata yang tidak Kamu mengerti: ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Kata tersebut tidak ada dalam kamus")
