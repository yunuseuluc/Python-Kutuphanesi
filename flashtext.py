from flashtext import KeywordProcessor

keyword_processor=KeywordProcessor()

keyword_processor.add_keyword("python")
keyword_processor.add_keyword("Flashtext")
keyword_processor.add_keyword("kütüphane")

metin="Flashtext kütüphanesinde python ile hızlı arama işlemleri için kullanılır"
bulunan_kelime=keyword_processor.extract_keywords(metin)

print("Bulunan anahtar kelimeler: ",bulunan_kelime)
