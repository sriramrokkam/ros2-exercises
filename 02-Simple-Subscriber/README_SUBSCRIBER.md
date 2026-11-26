# 📖 README - Simple Subscriber

Complete reference for the ROS2 Simple Subscriber example.

---

## 📋 Overview

The Simple Subscriber is a ROS2 node that **listens to messages** published on the `/chatter` topic and processes them through a callback function.

**Key Features**:
- ✅ Subscribes to `/chatter` topic
- ✅ Receives String messages
- ✅ Processes messages via callback
- ✅ Logs each received message
- ✅ Works with the Publisher from 01-Simple-Publisher

---

## 🎯 Learning Objectives

After working with this example, you will understand:

✅ How subscribers work in ROS2  
✅ Topic-based publish-subscribe pattern  
✅ Callback-based message processing  
✅ The difference between publishers and subscribers  
✅ How to test pub-sub communication  
✅ Message flow in ROS2  

---

## 📂 Project Structure

```
02-Simple-Subscriber/
├── START_HERE.txt           ← Quick navigation
├── QUICK_START.txt          ← 5-minute reference
├── DOCUMENTATION_SUMMARY.md ← Learning paths
├── TESTING_GUIDE.md         ← 7 test scenarios
├── MAIN_FUNCTION_GUIDE.md   ← Code explanation
├── README_SUBSCRIBER.md     ← This file
└── src/
    └── arduinobot_py_example/
        ├── setup.py                           ← Package config
        ├── package.xml                        ← ROS2 manifest
        └── arduinobot_py_example/
            └── simple_subscriber.py           ← Subscriber code (48 lines)
```

---

## ⚡ Quick Start

### Build

```bash
cd /sapmnt/home/I310202/Desktop/ros2-exercises/02-Simple-Subscriber
colcon build --packages-select arduinobot_py_example
source install/setup.bash
```

### Run

**Terminal 1 - Publisher** (from 01-Simple-Publisher):
```bash
cd /sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher
source install/setup.bash
ros2 run arduinobot_py_example simple_publisher
```

**Terminal 2 - Subscriber**:
```bash
cd /sapmnt/home/I310202/Desktop/ros2-exercises/02-Simple-Subscriber
source install/setup.bash
ros2 run arduinobot_py_example simple_subscriber
```

### Expected Output

**Terminal 1 (Publisher)**:
```
[INFO] [simple_publisher]: SimplePublisher node initialized
[INFO] [simple_publisher]: Published message #1
[INFO] [simple_publisher]: Published message #2
...
```

**Terminal 2 (Subscriber)**:
```
[INFO] [simple_subscriber]: SimpleSubscriber node initialized
[INFO] [simple_subscriber]: Received message #1: Hello, world! 0
[INFO] [simple_subscriber]: Received message #2: Hello, world! 1
...
```

---

## 📖 Code Explanation

### Subscriber Class

```python
class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__('simple_subscriber')
        
        # Create subscription to /chatter topic
        self.subscription = self.create_subscription(
            String,                    # Message type
            'chatter',                # Topic name
            self.listener_callback,   # Callback function
            10)                       # Queue size
        
        self.counter = 0
```

### Callback Function

```python
def listener_callback(self, msg):
    # Called automatically when message arrives
    self.counter += 1
    self.get_logger().info(
        f'Received message #{self.counter}: {msg.data}'
    )
```

### Main Function

```python
def main(args=None):
    rclpy.init(args=args)           # 1. Initialize ROS2
    node = SimpleSubscriber()        # 2. Create node
    rclpy.spin(node)                # 3. Listen (infinite loop)
    node.destroy_node()             # 4. Cleanup
    rclpy.shutdown()                # 5. Shutdown
```

---

## 🔄 How It Works

### 1. Initialization

When `SimpleSubscriber()` is created:
1. Node name is set to 'simple_subscriber'
2. Subscription to /chatter topic is created
3. Callback function is registered
4. Node is ready to receive messages

### 2. Message Flow

```
Publisher              ROS2 Middleware         Subscriber
   │                         │                      │
   ├─ Create message ─────→  │                      │
   ├─ Publish message ─────→ [/chatter topic]       │
   │                         │                      │
   │                         ├─ Has subscriber? YES │
   │                         │                      │
   │                         ├─ Call callback ─────→│
   │                         │                      │
   │                         │  listener_callback() │
   │                         │  ├─ counter++       │
   │                         │  ├─ log message     │
   │                         │  └─ done            │
   │                         │                      │
   │                         ├─ Ready for next msg  │
```

### 3. The Spin Loop

`rclpy.spin(node)` creates an infinite loop:

```
Loop:
  Wait for message on /chatter
  When message arrives:
    Call listener_callback(message)
  Continue loop
```

---

## 🧪 Testing

For comprehensive testing, see `TESTING_GUIDE.md`. Quick tests:

**Basic Test**:
```bash
# Terminal 1
ros2 run arduinobot_py_example simple_publisher

# Terminal 2
ros2 run arduinobot_py_example simple_subscriber
```

**Monitor Topic**:
```bash
ros2 topic echo /chatter
ros2 topic hz /chatter
```

**Node Information**:
```bash
ros2 node list
ros2 node info /simple_subscriber
ros2 topic info /chatter
```

---

## 🔧 Configuration

### Queue Size

The queue size (10) affects message buffering:

```python
self.create_subscription(
    String,
    'chatter',
    self.listener_callback,
    10)  # Queue size - buffer for 10 messages
```

**Increase queue size** if:
- Messages are arriving faster than you can process
- You need to buffer more messages
- You want fewer dropped messages

**Decrease queue size** if:
- You have memory constraints
- You only care about recent messages
- Dropping old messages is acceptable

---

## 🐛 Troubleshooting

### "No messages received"

**Problem**: Subscriber runs but doesn't receive messages

**Solutions**:
1. Check publisher is running in another terminal
2. Verify both nodes are using same setup.bash
3. Check topic name: `ros2 topic list`

### "Module not found: rclpy"

**Problem**: Python can't find rclpy module

**Solutions**:
1. Source ROS2: `source /opt/ros/humble/setup.bash`
2. Source workspace: `source install/setup.bash`
3. Rebuild: `colcon build`

### "Package not found"

**Problem**: Package doesn't exist

**Solutions**:
1. Navigate to correct directory
2. Run: `colcon build --packages-select arduinobot_py_example`
3. Source: `source install/setup.bash`

### "Address already in use"

**Problem**: Another process using the port

**Solutions**:
1. Kill previous process: `pkill -f simple_subscriber`
2. Wait a few seconds and try again
3. Use different terminal

### "Subscriber won't stop"

**Problem**: Can't stop with Ctrl+C

**Solutions**:
1. Try Ctrl+C again
2. Send SIGTERM: `kill -TERM <PID>`
3. Use `killall simple_subscriber`

---

## 📚 Key Concepts

### Subscription

A subscription tells ROS2 that you want to listen to messages on a specific topic:

```python
self.create_subscription(
    String,                    # What type of messages?
    'chatter',                # Which topic?
    self.listener_callback,   # What to do with messages?
    10)                       # How many to buffer?
```

### Callback

A function automatically called by ROS2 framework when something happens:

```python
def listener_callback(self, msg):
    # This runs AUTOMATICALLY when message arrives
    # YOU DON'T CALL IT - ROS2 FRAMEWORK DOES
    # msg contains the received message
```

### Topic

A named channel for messages:

```
Topic: /chatter
  ├─ Publishers: 1 (simple_publisher)
  └─ Subscribers: 1 (simple_subscriber)
  
Messages flow from publishers to subscribers
```

### Node

A single process in ROS2:

```
Node: /simple_subscriber
  ├─ Subscriptions: /chatter (std_msgs/msg/String)
  ├─ Publishers: none
  └─ State: running (listening for messages)
```

---

## 🔀 Comparison with Publisher

| Feature | Publisher | Subscriber |
|---------|-----------|-----------|
| **Purpose** | Sends messages | Receives messages |
| **main() pattern** | Same | Same |
| **Key method** | create_publisher() | create_subscription() |
| **Timing** | Timer-based | Event-based (callback) |
| **Callback** | timer_callback() | listener_callback() |
| **Control** | Publisher decides when to send | Subscriber waits for publisher |

---

## 🎓 Learning Path

1. **5 min**: Read QUICK_START.txt
2. **10 min**: Read DOCUMENTATION_SUMMARY.md
3. **20 min**: Read MAIN_FUNCTION_GUIDE.md
4. **30 min**: Run TESTING_GUIDE.md tests
5. **30 min**: Modify code and experiment
6. **60 min**: Study and compare with Publisher code

---

## 💡 Tips

**Tip 1**: Always run publisher before subscriber
- Subscriber won't crash, just won't receive messages
- Once publisher starts, messages flow to subscriber

**Tip 2**: Use different terminals for publisher and subscriber
- Makes debugging easier
- Can see both outputs simultaneously

**Tip 3**: Source setup.bash in EVERY new terminal
- ROS2 environment must be active
- Common cause of "command not found" errors

**Tip 4**: Monitor with ROS2 tools
```bash
ros2 topic echo /chatter       # See messages
ros2 topic hz /chatter         # Measure rate
ros2 node list                 # See all nodes
```

**Tip 5**: Read logs carefully
- Error messages tell you what went wrong
- INFO messages show program flow
- Stack traces help debug crashes

---

## 📖 Related Files

- **01-Simple-Publisher**: Publish messages (compare/contrast)
- **03-Pub-Sub-Communication**: Combined pub-sub (next exercise)
- **MAIN_FUNCTION_GUIDE.md**: Deep code explanation
- **TESTING_GUIDE.md**: 7 comprehensive tests

---

## 🚀 Next Steps

After mastering this subscriber:

1. ✅ Modify the callback to do more with messages
2. ✅ Create multiple subscribers
3. ✅ Change queue size and observe behavior
4. ✅ Compare with 01-Simple-Publisher
5. ✅ Study 03-Pub-Sub-Communication

---

## 📞 Help

**Quick answers**: See DOCUMENTATION_SUMMARY.md  
**Testing help**: See TESTING_GUIDE.md  
**Code explanation**: See MAIN_FUNCTION_GUIDE.md  
**Quick reference**: See QUICK_START.txt  

---

## 📝 Notes

- Subscriber runs in an infinite loop (rclpy.spin)
- Callback is called automatically, not manually
- Multiple subscribers can receive same messages
- Messages are delivered in order (FIFO)
- Topic name must match between pub and sub

---

**Happy Learning! 🎉**

For updates and more exercises, visit the ros2-exercises repository.
