# Import stuff for random etc.

# Setup database / redis
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Import own stuff
import advice as adv;  
import stream as strm;   # can be used without instantiating 
import estimate as es;

# try usage of stream
print(strm.mean(10,2,5))

nvisitors = 100

adv = adv.Advice();
x = 0;
for i in range(1, nvisitors):
	print(adv.getAdvice());
	x = strm.mean(x, i, i)
	print(x)
	
print(x)
	