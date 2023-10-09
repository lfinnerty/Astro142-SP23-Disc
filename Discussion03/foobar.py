import numpy as np


class foobar():
	def __init__(self, foo, bar=None):
		''' Constructor method, instantiates a foobar object.
		A numpy array foo is required. A second array, bar,
		is not required, but if given must have the same
		shape as foos. If bar is not given, its set to 0. '''
		### Instantiate the foo attribute
		self.foo = foo
		### Different behavior if bar is given or not
		if bar is not None:	
			### If given, check that the shape matches before
			### setting the bar attribute
			assert foo.shape == bar.shape, 'Shapes must match!'
			self.bar = bar
		### If bar is not given, set it to 0s
		else:
			self.bar = np.zeros(foo.shape)

	def set_foo(self, newfoo):
		''' Setter for foo attribute, raises an error if the
		shape is wrong
		'''
		if newfoo.shape==self.bar.shape:
			self.foo = newfoo
		else:
			raise ValueError('Shapes of foo and bar must match!')
	
	def set_bar(self, newbar):
		''' Setter for foo attribute, raises an error if the
		shape is wrong
		'''
		if newbar.shape==self.foo.shape:
			self.bar = newbar
		else:
			raise ValueError('Shapes of foo and bar must match!')

	def get_foo(self):
		''' Returns the value of the foo attribute'''
		return self.foo

	def get_bar(self):
		''' Returns the value of the bar attribute'''
		return self.bar

	def foo_greater(self):
		''' Returns an array of whether foo is > bar '''
		return self.foo > self.bar