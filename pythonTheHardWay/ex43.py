from sys import exit
from random import randint


class Scene(object):
	def enter_scene(self):
		print "not configured"
		exit(1)
		
	
class Death(Scene):
	
	def enter_scene(self):
		print "you die!"
		exit(0)

class Bridge(Scene):
	
	def enter_scene(self):
		print "bridge comander"
		
class Escape(Scene): 
	
	def enter_scene(self):
		print "escape woho"

class Map(object):
	
	scene_map = { 'bridge' : Bridge(), 'escape' : Escape(), 'death' : Death() }
	
	def __init__(self, start_scene):	
		self.start_scene = start_scene
			
	def get_next_scene(self, scene_name):
		return Map.scene_map[scene_name]
	
	def get_opening_scene(self):
		return self.get_next_scene(self.start_scene)
		

		
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
		self.scene_num_map = { 1 : 'bridge' , 2 : 'death' , 3 : 'escape' }
		
	def play(self):
		current_scene = self.scene_map.get_opening_scene()
		current_scene.enter_scene()
		num = int(raw_input())
		map_name = self.scene_num_map[num]
		current_scene = self.scene_map.get_next_scene(map_name)
		current_scene.enter_scene()
		
game_map = Map('bridge')
game = Engine(game_map)
game.play()