class Physics:
    def __init__(self,clock):
        self.solid_objects = []
        self.clock = clock
        #Constants
        self.g = 9.8
        self.dt = 0
    def set_solid_obj_list(self, obj_list):
        self.solid_objects = obj_list
    def add_solid_obj(self,obj_rect):
        self.solid_objects.append(obj_rect)
    def handle_collisions(self,obj_rect):
        pass

    def gravity(self,obj_velocity):
        self.dt = self.clock.get_time() / 1000
        obj_velocity.y += self.g * self.dt
