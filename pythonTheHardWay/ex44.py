class Parent(object):
	def implicit(self):
		print "parent implicit"
	
	def override(self):
		print "parent override"
		
	def alter(self):
		print "parent alter"

class Child(Parent):
	def override(self):
		print "child override"
	
	def alter(self):
		print "child before alter"
		super(Child, self).alter()
		print "child after alter"
	
dad = Parent()
son = Child()

print "IMPLICIT"
dad.implicit()
son.implicit()

print "OVERRIDE"
dad.override()
son.override()

print "ALTER"
dad.alter()
son.alter()


#composition
class Other(object):
	def implicit(self):
		print "Implicit"
	
	def override(self):
		print "Override"
	
	def alter(self):
		print "Alter"

class CompChild(object):
	def __init__(self):
		self.other = Other()
	
	def implicit(self):
		self.other.implicit()

	def override(self):
		print "Comp Child override"
	
	def alter(self):
		print "CC before alter"
		self.other.alter()
		print "CC after alter"

other = Other()
cc = CompChild()

other.implicit()
cc.implicit()

other.override()
cc.override()

other.alter()
cc.alter()


