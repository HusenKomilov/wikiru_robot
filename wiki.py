import wikipedia


def search_result(search_text):
    try:
        asd = wikipedia.search(search_text)
        wikipedia.set_lang('ru')
        print(asd)
        sad = wikipedia.summary(asd[0])
    except:
        sad = "Bu so'zning manosini topolmadim"
    return sad
