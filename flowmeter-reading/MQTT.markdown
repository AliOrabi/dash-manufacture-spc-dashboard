# Raspberry Pi MQTT Server – Install and test Mosquitto

sudo apt-get install -y mosquitto mosquitto-clients

# After installation, a Mosquitto server is started automatically. We open a subscriber in the channel “test_channel” waiting for messages:

mosquitto_sub -h localhost -v -t test_channel

# The channel is here like a frequency, on which one hears. For example, different data may be sent in different channels (e.g., temperature, humidity, brightness, etc.).

# In order to simply transfer data, we can either use the same Raspberry Pi (open new terminal / SSH connection) or send the data from another Pi. If we use the same Raspberry Pi, use is easily possible. For this we simply send a test message (as publisher) in the same channel:

mosquitto_pub -h localhost -t test_channel -m "Hello Raspberry Pi"

# Otherwise you have to specify the internal IP address (eg 192.168.1.5) of the recipient instead of “localhost”. On the receiver side, the message should appear soforn.

## Raspberry Pi MQTT data exchange with Python

# The communication is super easy, as we have seen. In order for us to be able to use the whole thing from scripts, we want to make it available to Python. For this purpose, we first install a library via the Python package manager (for Python3 also use pip3):

sudo pip install paho-mqtt

