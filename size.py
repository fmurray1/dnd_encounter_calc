class Size:
    def __init__(self, size='medium'):
        self.size = size

        if size == 'tiny':    
            self.area ='2.5ft x 2.5ft'
            self.hit_dice = 'd4'
        elif size == 'small':
            self.area ='5ft x 5ft'
            self.hit_dice = 'd6'
        elif size == 'medium':
            self.area ='5ft x 5ft'
            self.hit_dice = 'd8'
        elif size == 'large':
            self.area ='10ft x 10ft'
            self.hit_dice = 'd10'
        elif size == 'huge':
            self.area ='15ft x 15ft'
            self.hit_dice = 'd12'
        else:
            self.area ='20ft x 20ft'
            self.hit_dice = 'd20'
        # TO-DO finish these