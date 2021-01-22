class T:
    def __init__(self, max_readings=60):
        self.t = []
        self.m = max_readings
        
    def avg(self):
        if self.t:
            return sum(self.t)/len(self.t)
        else:
            return None
        
    def add(self, _new_reading):
        if len(self.t) >= self.m:
            self.t.pop(0)
        self.t.append(_new_reading)
        
    def trend(self):
        if self.t:
            t_all = sum(self.t)/len(self.t)
            t_ten = sum(self.t[::-1][0:10])/len(self.t[::-1][0:10])
            if t_ten > t_all:
                return 'warming'
            elif t_ten < t_all:
                return 'cooling'
            else:
                return 'no change'
            
    def plot(self, y_range=20):
        if self.t:
            t_max = max(self.t)
            t_min = min(self.t)
            if t_max - t_min:
                m = y_range / (t_max - t_min)
                return [round((_t-t_min)*m) for _t in self.t]
        return []
    
    def mm(self):
        return min(self.t), max(self.t)
            
            
if __name__ == '__main__':
    from random import uniform
    test_t = T()
    for x in range(60):
        test_t.add(uniform(60, 80))
        
    print(test_t.avg())
    print(test_t.trend())
    print(test_t.plot())
        
        
        