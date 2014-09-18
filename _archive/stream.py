### Methods for streaming updates of parameters


class Stream(object):
	'Common class for streaming update'
			
	def increment(self, x0=0, x1=1):
		'Updates x0 to include x1 as a counter'
		return(x0 + x1);
	
	def sum(self, x0=0., x1=1.):
		'Updates x0 to include x1 as a sum'
		return(x0 + x1);
	
	def mean(self, m0=0., n0=.1, x1=0.):
		'computes a streaming mean with old mean m0, old n n0, '
		return(m0 + (x1 - m0)/(++n0))
		
	# Implement variance
	# Implement lin.reg
	# Implement log.reg using SGD
	# Implement online bootstrap
	# Implement "bucket versions"
	

## make available a.la. random.py
__stream = Stream();
increment = __stream.increment
sum = __stream.sum
mean = __stream.mean
