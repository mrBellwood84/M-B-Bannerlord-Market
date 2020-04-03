class Item:

    def __init__(self, name, avg_price = 0, min_price = 0, max_price = 0, times_added = 0):

        """ Default constructor """

        self.name = name
        self.avg_price = avg_price
        self.min_price = min_price
        self.max_price = max_price
        self.times_added = times_added
        self.last_avg = None
        self.last_min = None
        self.last_max = None
    
    def __str__(self):
        content = """
          Prouct name: {}
        Average price: {}
            Min price: {}
            Max price: {}
            """.format(self.name, int(self.avg_price), self.min_price,self.max_price)
        return content

    def append(self, price):
        
        """
        Append price to set min,max and average
        If times_added is 0, min, max and average is set to price
        """
        self.last_avg = self.avg_price
        self.last_min = self.min_price
        self.last_max = self.max_price

        if self.times_added == 0:
            
            self.avg_price = price
            self.min_price = price
            self.max_price = price
            self.times_added += 1

        else:

            # Set new average price
            total = self.avg_price * self.times_added
            total += price

            self.times_added += 1
            self.avg_price = total / self.times_added

            # Set new min or max value if true
            if price > self.max_price:
                self.max_price = price
            elif price < self.min_price:
                self.min_price = price
    
    def undo_last(self):
        if (self.last_avg != None):

            self.min_price = self.last_min
            self.last_min = None

            self.max_price = self.last_max
            self.last_max = None

            self.avg_price = self.last_avg
            self.last_avg = None

            self.times_added -= 1
