
class Shahtask:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    

class piyada(Shahtask):
    def hrkt(self):
        print("Piyadanın hərəkət istiqamətləri:")
        print("Bir addım irəli")
        print("İlk hərəkətdə iki addım irəli (yalnız əsas mövqe)")
        print("Qərb tərəfə hücum")
        print("Şərq tərəfə hücum")

class At(Shahtask):
    def hrkt(self):
        print("Atın hərəkət istiqamətləri:")
        print("Bir addım irəli, iki addım sağa/sola")
        print("Bir addım sağa/sola, iki addım irəli")

class Fil(Shahtask):
    def hrkt(self):
        print("Filin hərəkət istiqamətləri:")
        print("Diaqonal irəli")

class top(Shahtask):
    def hrkt(self):
        print("Topun hərəkət istiqamətləri:")
        print("İrəli, arxa, sağ və sola hərəkət")
        print("Top  irəli hərəkət edir")

class Vezir(Shahtask):
    def hrkt(self):
        print("Vezirin hərəkət istiqamətləri:")
        print("İrəli, arxa, sağ və sola hərəkət ")
        print("Diagonal hərəkət ")

class Şah(Shahtask):
    def hrkt(self):
        print("Şahın hərəkət istiqamətləri:")
        print("Bir addım irəli, arxa, sağ və sola hərəkət")
        print("Diaqonal hərəkət")
        print("Qala")

piyada = piyada(4, 3)
piyada.hrkt()

at = At(5, 5)
at.hrkt()

fil = Fil(4, 4)
fil.hrkt()

top = top(2, 2)
top.hrkt()

vezir = Vezir(8, 8)
vezir.hrkt()

şah = Şah(6, 6)
şah.hrkt()
