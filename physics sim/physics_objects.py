import pygame
import math 
import data
pygame.init()
clock = pygame.time.Clock()
class physics_box(pygame.sprite.Sprite):
    
    def __init__(
                 self,group,mass,position:tuple,image,gravity:bool,boundaries:bool,movement:bool,
                 air_resistance:bool,initial_velocity:tuple,constant_force:tuple,type_of_motion:str
                 ):
        super().__init__(group)
        self.dt = dt = clock.tick() / 1000
        self.image = image
        self.rect = self.image.get_frect(topleft = position)
        self.window_width,self.window_height = pygame.display.get_window_size() 
        self.position = position 
        self.boundaries = boundaries
        self.gravity = gravity
        self.movement = movement
        self.constant_force = pygame.math.Vector2(constant_force)
        self.normal_reaction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2(initial_velocity)
        self.air_resistance = pygame.math.Vector2()
        self.all_vectors = []
        self.air_density = 1.2278
        self.drag_coefficient = 1.22
        self.mass = mass
        self.data = []
        self.apply_resistance = air_resistance
        self.pre_vel = initial_velocity
    
    def update(self):
        """the update function is called each frame 
        .this is where every function is called
        this can only help to arrange the order in which the functions
        are called.for more info about the function go to the respective 
        function."""
       
        self.dt = clock.tick() / 1000
        self.calc_resulting_vector(self.dt)
       
        if self.boundaries:
            self.independant_vector_normal_reaction()
        
        if self.movement :
            self.move(self.dt)
        
        if self.gravity:
            self.independant_vector_gravity()
        
        """any variable can be put as arguments to view changes with time with that variable
         space should be pressed to view the changes
         example: self.data_visualization_for_debigging(self.velocity.x) """
        self.data_visualization_for_debugging(self.rect.centerx)    
    
    def independant_vector_normal_reaction(self):
     """this function acts as a reaction force whenever a body
     collides with a boundary. this function does not change the 
     magnitude but only multiplies the velocity vector by -1 thus making
     the body go in the opposite direction"""
     
     if self.rect.bottom > self.window_height:
        self.velocity.y *= -1
        self.rect.bottom = self.window_height
     elif self.rect.top < 0:
        self.velocity.y *= -1
        self.rect.top = 0
     if self.rect.left < 0:
        self.velocity.x *= -1
        self.rect.left= 0
     elif self.rect.right > self.window_width:
        self.velocity.x *= -1
        self.rect.right = self.window_width 

    def move(self,dt):
        self.rect.center += self.velocity*dt 
   
    def independant_vector_gravity(self):
        pass
    
    def calc_resulting_vector(self,dt):
        self.velocity += ((self.constant_force)  + (self.calc_air_resistance()))/self.mass * dt
    
    def calc_totall_energy_in_system(self):
        displacement = (self.position-self.rect.center).length()
        potential_energy = self.constant_force * displacement
        
    def calc_air_resistance(self):
     
     if self.apply_resistance:
     
      """Calculate air resistance based on the drag force formula.
      [drag] = c*(v)*d*a
       where [] stands for magnitude"""
      
      angle = math.atan2(self.velocity.y, self.velocity.x)
      cross_sec_length = self.image.get_width() * abs(math.cos(angle))
    
      velocity_squared = self.velocity.length_squared()
      drag = -0.001 * self.air_density * velocity_squared * self.drag_coefficient * cross_sec_length
      
      #calc the resistance vector by multiplying 
      #velocity's unit vector to the drag
      resistance_vector = (self.velocity/self.velocity.length()) *drag
      return resistance_vector
     
     return pygame.math.Vector2(0,0)

    def data_visualization_for_debugging(self,iterator:float):
        self.data.append(iterator)
        if pygame.key.get_just_pressed()[pygame.K_SPACE]:

            data.transform_to_file(self.data)
