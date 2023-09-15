meme_dict = {
            "gaje": "gak jelas",
            "gabut": "gak ada kerjaan",
            "ygy": "ya guys ya"
            
            }
            
            
for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti: ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Kata tersebut tidak ada dalam kamus")
