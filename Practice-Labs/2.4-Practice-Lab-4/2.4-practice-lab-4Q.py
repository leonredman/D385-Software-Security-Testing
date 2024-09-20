"""
With rate limiting, a unique IP address is restricted from making too many 
requests in a fixed period of time.

The code snippet below implements rate limiting using a "Token Bucket." 
Each time a message is received: the bucket is checked for tokens. 
If the bucket has 1 or more tokens, the algorithm removes one token 
and sends the message. If no tokens remain in the bucket, the algorithm 
drops the message.

Complete line #18 to finish the limit() function and ensure that the 
API only allows 5 messages per every 10 seconds.

See commented lines for detailed instructions.

When correct, this code should produce no output.

The output to the console will be the following:
(Your program produced no output)

"""

import time
    
class Limiter:

  def __init__(self, rate, per):
    self.rate = rate
    self.per = per
    self.bucket = rate
    self.last_check = time.time()

  def limit(self, callback_fn):
      current = time.time()
      time_passed = current - self.last_check
      self.last_check = current
      
      # Finish line 18 by writing an expression that determines the value 
      # of the bucket
      # Use the following variables in your expression: 
      # time_passed, self.bucket, self.rate, and self.per 
      
      bucket = # Insert your expression here
     
      
      if (bucket > self.rate):
          self.bucket = self.rate
      if (bucket < 1):
          pass
      else:
          callback_fn()
          self.bucket = bucket - 1