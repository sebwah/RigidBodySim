import matplotlib

class Plot:
    """class for drawing 2D scenes with matplotlib"""
    def __init__(self, dt, bodies, arrows=False):
        
        self.dt = dt
        self.bodies = bodies

    def insert_body(self):
        for body in self.bodies:
            if body.type = 'ground':
                #TODO: draw a line at the specified height
                pass
            elif body.type = 'circle':
                #TODO: insert circle at starting position
                pass
            elif body.type = 'rectangle':
                #TODO: insert rectangle at starting position
                pass

    def draw(self):
        """draws each trajectory over specified time frame"""
        pass
