from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length,length)

    def set_length(self,new_length):
        if new_length>=0 :
            self.length=new_length
            if self.has_been_drawn :
                self.draw_shape()

    
    def draw_shape(self,x,y):
        """
        Draw the shape, starting at 0,0.

        If any old drawings exist, remove them.
        """
        x = 
        
        self.turtle.clear() #Remove old drawings (if they exist)
        self.turtle.penup()
        self.turtle.goto(x,y)
        self.turtle.pendown()
        self.turtle.goto(self.length,y)
        self.turtle.goto(self.length,self.length)
        self.turtle.goto(x,self.length)
        self.turtle.goto(x,y)
        self.turtle.penup()
        self.has_been_drawn=True


