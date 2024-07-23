from langs import en, ru

class Setting:
    """ Class For Storing And Changing App Settings """

    def __init__(self, params: dict) -> None:
        self.params = params
        self.lang = params.get("lang", "en")

        self.lang_preset = self.set_language(self.lang)


    def set_language(self, lang):
        """ Changing language """

        lang_phrases = en.preset
        self.lang = "en"
        
        if lang == "ru":
            self.lang = "ru"
            lang_phrases = ru.preset
        return lang_phrases