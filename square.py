from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length,length)

    def set_length(self,new_length):
        if new_length>=0 :
            self.length=new_length
            if self.has_been_drawn :
                self.draw_shape()
                

    
