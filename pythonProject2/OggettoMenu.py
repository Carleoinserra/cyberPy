class Menu:

    def init(self, first, second, third, price, mail):
        self.first = first

        self.second = second

        self.third = third

        self.price = price

        self.mail = mail

    def str(self):
        return f'''

      Menù scelto:

         Primo: {self.first}

         Secondo: {self.second}

         Contorno: {self.third}



      Il prezzo è stato mandato alla seguente mail: {self.mail}

      '''
