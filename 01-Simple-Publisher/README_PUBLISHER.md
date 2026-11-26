# ROS2 Simple Publisher - Testing Guide

This document explains the Simple Publisher implementation in both Python and C++, what happens in the `main()` function, and how to test both implementations.

---

## 📋 Overview

The **Simple Publisher** is a ROS2 node that:
- **Creates a publisher** that sends String messages to a topic called `chatter`
- **Sets up a timer** that triggers message publishing at a fixed frequency (1 Hz / 1 message per second)
- **Logs information** about each message being published
- **Maintains a counter** to track the number of messages sent

---

## 🔄 What Happens in the `main()` Function

Both the Python and C++ implementations follow the same logical flow:

### **Step-by-Step Breakdown:**

```
1. INITIALIZE ROS2
   └─ Establishes connection to the ROS2 middleware
   └─ Sets up communication infrastructure
   └─ Prepares the system to create nodes

2. CREATE NODE INSTANCE
   └─ Instantiates the SimplePublisher node
   └─ Runs the node's __init__ constructor which:
      ├─ Calls parent class constructor with node name
      ├─ Creates a publisher for the 'chatter' topic
      ├─ Initializes internal variables (counter, frequency)
      ├─ Sets up a timer callback function
      └─ Logs initialization message

3. SPIN THE NODE
   └─ Enters an infinite loop that:
      ├─ Waits for events (timers, subscriptions, etc.)
      ├─ Executes timer callbacks at scheduled intervals
      ├─ Publishes messages automatically
      └─ Keeps the node running until interrupted

4. CLEANUP & SHUTDOWN
   └─ When interrupted (Ctrl+C):
      ├─ Destroys the node and releases resources
      ├─ Closes all publishers and subscriptions
      └─ Shuts down ROS2 communication
```

---

## 🐍 Python Implementation

### **File Location:**
```
/sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher/src/arduinobot_py_example/
  └── arduinobot_py_example/
      └── simple_publisher.py
```

### **Key Components:**

| Component | Purpose |
|-----------|---------|
| `import rclpy` | ROS2 Python client library |
| `from rcply.node import node` | Base Node class to inherit from |
| `from std_msgs.msg import String` | String message type |
| `SimplePublisher(node)` | Custom node class |
| `self.create_publisher()` | Creates a publisher for the topic |
| `self.create_timer()` | Sets up periodic callback execution |
| `main()` | Entry point that initializes and spins the node |

### **Testing Python Publisher:**

#### **Method 1: Using ros2 run command**

```bash
# Terminal 1 - Run the publisher
cd /sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher
source install/setup.bash
ros2 run arduinobot_py_example simple_publisher

# Expected Output:
# [INFO] [SimplePublisher]: SimplePublisher node initialized
# [INFO] [SimplePublisher]: Published message #1
# [INFO] [SimplePublisher]: Published message #2
# ... (continues every 1 second)
```

#### **Method 2: Listen to the topic in another terminal**

```bash
# Terminal 2 - Subscribe to messages
cd /sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher
source install/setup.bash
ros2 topic echo /chatter

# Expected Output:
# data: 'Hello, world! 0'
# ---
# data: 'Hello, world! 1'
# ---
# data: 'Hello, world! 2'
# ... (new message every 1 second)
```

#### **Method 3: Check topic information**

```bash
# Terminal 3 - View topic details
cd /sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher
source install/setup.bash
ros2 topic list              # List all active topics
ros2 topic info /chatter     # Get info about the 'chatter' topic
ros2 topic bw /chatter       # Monitor bandwidth/frequency
ros2 topic hz /chatter       # Measure publishing rate
```

#### **Method 4: Run test suite**

```bash
cd /sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher
colcon test --packages-select arduinobot_py_example
```

---

## ⚙️ C++ Implementation

### **File Location:**
```
/sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher/src/arduinobot_cpp_example/
  └── (C++ source files would be here)
```

### **Testing C++ Publisher:**

#### **Step 1: Build the C++ Package**

```bash
cd /sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher
colcon build --packages-select arduinobot_cpp_example
source install/setup.bash
```

#### **Step 2: Run the publisher**

```bash
# Terminal 1 - Run the C++ publisher
ros2 run arduinobot_cpp_example simple_publisher

# Expected Output (similar to Python):
# [INFO] [SimplePublisher]: SimplePublisher node initialized
# [INFO] [SimplePublisher]: Published message #1
# [INFO] [SimplePublisher]: Published message #2
# ... (continues every 1 second)
```

#### **Step 3: Listen to the topic**

```bash
# Terminal 2 - Subscribe to messages (same as Python)
ros2 topic echo /chatter
```

---

## 🧪 Complete Testing Workflow

### **Full End-to-End Test (Both Python and C++)**

```bash
# Step 1: Navigate to workspace
cd /sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher

# Step 2: Source the setup (do this in every new terminal)
source install/setup.bash

# Step 3: Build everything (if not already built)
colcon build

# Step 4: Terminal 1 - Run the Python publisher
ros2 run arduinobot_py_example simple_publisher

# Step 5: Terminal 2 - Listen to the topic
ros2 topic echo /chatter
# You should see messages appearing every 1 second

# Step 6: Terminal 3 - Monitor the publishing rate
ros2 topic hz /chatter
# You should see: average rate: 1.00 Hz (or close to 1 Hz)

# Step 7: Terminal 4 - View all topics
ros2 topic list
# You should see: /chatter and /rosout

# Step 8: Stop the publisher
# Go back to Terminal 1 and press Ctrl+C

# Step 9: Repeat with C++ version
# Repeat steps 4-8 but use: ros2 run arduinobot_cpp_example simple_publisher
```

---

## 📊 Expected Behavior

### **Publishing Frequency:**
- **Interval:** 1 message per second
- **Frequency:** 1 Hz
- **Topic:** `/chatter`
- **Message Type:** `std_msgs/msg/String`

### **Sample Output:**
```
[INFO] [SimplePublisher]: SimplePublisher node initialized
[INFO] [SimplePublisher]: Published message #1
[INFO] [SimplePublisher]: Published message #2
[INFO] [SimplePublisher]: Published message #3
[INFO] [SimplePublisher]: Published message #4
[INFO] [SimplePublisher]: Published message #5
...
```

### **Topic Echo Output:**
```
data: 'Hello, world! 0'
---
data: 'Hello, world! 1'
---
data: 'Hello, world! 2'
---
data: 'Hello, world! 3'
---
```

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| **Command not found:** `ros2 run` | Make sure to source: `source install/setup.bash` |
| **Package not found:** `arduinobot_py_example` | Build the packages: `colcon build` |
| **Topic `/chatter` not appearing** | Check if publisher is running in another terminal |
| **Messages not appearing in `ros2 topic echo`** | Verify the publisher is still running |
| **Port already in use** | Kill previous ROS2 processes and restart |
| **Build errors** | Clean build: `colcon build --packages-select <package> --no-warn-unused-cli` |

### **Kill all ROS2 nodes:**
```bash
pkill -f ros2
# or
pkill -f simple_publisher
```

---

## 📝 Summary of `main()` Workflow

| Step | Function | Action |
|------|----------|--------|
| 1 | `rclpy.init(args=args)` | Initializes ROS2 middleware |
| 2 | `node = SimplePublisher()` | Creates the node with all callbacks |
| 3 | `rclpy.spin(node)` | Keeps node running, processes timers/callbacks |
| 4 | `node.destroy_node()` | Cleans up node resources (on exit) |
| 5 | `rclpy.shutdown()` | Shuts down ROS2 communication |

---

## 🔗 Additional Commands

```bash
# View all running nodes
ros2 node list

# Get information about a node
ros2 node info /simple_publisher

# View the message structure
ros2 interface show std_msgs/msg/String

# Record messages to a bag file
ros2 bag record /chatter

# Play back recorded messages
ros2 bag play rosbag2_*

# Monitor system resources
ros2 topic stat /chatter
```

---

## 📚 References

- [ROS2 Official Documentation](https://docs.ros.org/en/humble/)
- [Creating your first ROS2 package](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html)
- [Writing a simple publisher](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)
- [Colcon build documentation](https://colcon.readthedocs.io/)

---

## ✅ Verification Checklist

After implementing and testing:

- [ ] Python publisher builds without errors
- [ ] C++ publisher builds without errors
- [ ] Python publisher runs and shows initialization message
- [ ] C++ publisher runs and shows initialization message
- [ ] Messages appear on `/chatter` topic at 1 Hz rate
- [ ] Counter increments correctly with each message
- [ ] Both implementations can be run simultaneously without interference
- [ ] Publisher gracefully shuts down with Ctrl+C
- [ ] Node cleanup executes without errors
- [ ] Both implementations follow the same main() workflow

