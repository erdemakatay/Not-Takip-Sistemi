class NotAraligiHatasi(Exception):
    def __init__(self, mesaj="Not 0 ile 100 arasında olmalıdır."):
        super().__init__(mesaj)
