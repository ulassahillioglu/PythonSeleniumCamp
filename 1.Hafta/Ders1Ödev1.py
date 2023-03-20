#String = Metinsel ifadelerin tutulduğu veri tipidir. "" ve '' şeklinde tırnak içerisinde yazılarak ifade edilir

#Integer = Negatif veya pozitif tam sayıların tutulduğu numerik veri tipidir. Sayının uzunluğuyla ilgili bir sınır
## bulunmamaktadır.

#Float = Negatif veya pozitif ondalıklı sayıların tutulduğu numerik veri tipidir. Integer ifadede 10 olarak görünen sayı, float
## ifadede 10.0 olarak gösterilir. 

#Complex = Karmaşık sayıların tutulduğu veri tipidir. " x + yj " şeklinde ifade edilir. cmath

#List = Sequence veri tipidir. Sıralı, elemanları değiştirilebilir, ekleme yapılabilir ve  aynı ögeyi birden fazla bulundurabilir. [] ile ifade edilir.

#Tuple = Sequence veri tipidir . Sıralı, elemanları değiştirilemeyen veri tipidir. Aynı ögeyi birden fazla bulundurabilir. (,) şeklinde
## ifade edilir. Elemanlar üzerinde değişiklik yapılamaz

#Set = Sequence veri tipidir. Setleri bir veri yığını olarak düşünebiliriz. Sırasızdır, elemanların yeri tamamen belirsizdir.
## Elemanlar kendini tekrar edemez. Ekleme, çıkarma yapılabilir. Elemanlar üzerinde değişiklik yapılamaz

#Boolean = Mantıksal veri tipleridir. True veya False olarak ifade edilir. Mantıksal kıyaslamada kullanılır.


##Oturum Açma bölümünde şart blokları kullanılır. Ödevler bölümünde de şart blokları kullanılıyor olabilir. Ödevi bitir butonuna
## tıklanması ödeve tik atılmasını sağlar.

user1 = ["engindemirog@kodlamaio.com",'0601']
user2 = ["ulassahillioglu@kodlamaio.com",'1234']


def log_in():
    e_mail = input("E-mail adresinizi girin: ")
    password = input("Parolanızı girin: ")
    
    if e_mail== user1[0] and password==user1[1]:
        print("Giriş başarılı")
    elif e_mail== user2[0] and password==user2[1]:
        print("Giriş Başarılı")
            
    else:
            print("Hatalı giriş")

log_in()


homework_done = False

if homework_done is True:
    print("Tik atıldı")
else:
    print("Tik atılmadı")
