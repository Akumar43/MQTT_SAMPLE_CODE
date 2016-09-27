# Import Adafruit IO REST client.
from Adafruit_IO import Client

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = '1595a6b30efb45acba3bd599cd842f70'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)

# Send a value to the feed 'Test'.  This will create the feed if it doesn't
# exist already.
aio.send('photocell', 42)

# Send a string value 'bar' to the feed 'Foo', again creating it if it doesn't 
# exist already.
aio.send('photocell', 'bar')

# Now read the most recent value from the feed 'Test'.  Notice that it comes
# back as a string and should be converted to an int if performing calculations
# on it.
data = aio.receive('photocell')
print('Retrieved value from Test has attributes: {0}'.format(data))
print('Latest value from Test: {0}'.format(data.value))

# Finally read the most revent value from feed 'Foo'.
data = aio.receive('photocell')
print('Retrieved value from Test has attributes: {0}'.format(data))
print('Latest value from Test: {0}'.format(data.value))
