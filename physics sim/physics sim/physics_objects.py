import pygame
import math 
pygame.init()
clock = pygame.time.Clock()
class physics_box(pygame.sprite.Sprite):
    
    def __init__(
                 self,group,mass,position:tuple,image,gravity:bool,boundaries:bool,movement:bool,
                 air_resistance:bool,initial_velocity:tuple,constant_force:tuple,type_of_motion:str
                 ):
        super().__init__(group)
        self.dt = dt = clock.tick(60) / 1000
        self.image = image
        self.rect = self.image.get_frect(topleft = position)
        self.window_width,self.window_height = pygame.display.get_window_size() 
        self.position = position 
        self.boundaries = boundaries
        self.gravity = gravity
        self.movement = movement
        self.constant_force = pygame.math.Vector2(constant_force)
        self.normal_reaction = pygame.math.Vector2()
        self.movement_vector = pygame.math.Vector2(initial_velocity)
        self.air_resistance = pygame.math.Vector2()
        self.all_vectors = []
        self.air_density = 2*1.2278
        self.drag_coefficient = 1.22
        self.mass = mass
        self.apply_resistance = air_resistance
        
    def update(self):
        self.dt = dt = clock.tick(60) / 1000
        self.calc_resulting_vector(dt)
        if self.boundaries:
            self.independant_vector_normal_reaction()
        if self.movement :
            self.move(self.dt)
        if self.gravity:
            self.independant_vector_gravity()

    def independant_vector_normal_reaction(self):
     if self.rect.bottom > self.window_height:
        self.movement_vector.y *= -1
    
     elif self.rect.top < 0:
        self.movement_vector.y *= -1

     if self.rect.left < 0:
        self.movement_vector.x *= -1
        self.rect.left= 0
     elif self.rect.right > self.window_width:
        self.movement_vector.x *= -1

    def move(self,dt):
        self.rect.center += self.movement_vector*dt 
    
    def independant_vector_gravity(self):
        pass
    
    def calc_resulting_vector(self,dt):
        if self.movement_vector.length() > 0:
            self.air_resistance = self.movement_vector.normalize() * self.calc_air_resistance()
        else:
            self.air_resistance = pygame.math.Vector2(0, 0)
        self.movement_vector += ((self.constant_force)  - (self.air_resistance))/self.mass
           
        
        
        if self.movement_vector.length() < 5:
            self.movement_vector = pygame.math.Vector2(0, 0)
        
    def calc_totall_energy_in_system(self):
        displacement = (self.position-self.rect.center).length()
        potential_energy = self.constant_force * displacement
        
    
    def calc_air_resistance(self):
     if self.apply_resistance:
      """Calculate air resistance based on the drag force formula."""
      angle = math.atan2(self.movement_vector.y, self.movement_vector.x)
      cross_sec_length = self.image.get_width() * abs(math.cos(angle))
    
      velocity_squared = self.movement_vector.length_squared()
      drag = 0.5 * self.air_density * velocity_squared * self.drag_coefficient * cross_sec_length
    
      
      return drag
     return 0


    
