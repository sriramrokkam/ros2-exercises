# 🧪 Quick Testing Guide - Simple Publisher

## ⚡ Quick Start (5 minutes)

### **Setup (Do Once)**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash
```

---

## 🚀 Test Scenario 1: Run Python Publisher Only

### **Terminal 1 - Start the Publisher**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash
ros2 run arduinobot_py_example simple_publisher
```

**Expected Output:**
```
[INFO] [SimplePublisher]: SimplePublisher node initialized
[INFO] [SimplePublisher]: Published message #1
[INFO] [SimplePublisher]: Published message #2
[INFO] [SimplePublisher]: Published message #3
...
```

**Stop:** Press `Ctrl+C`

---

## 👂 Test Scenario 2: Publisher + Listener (Two Terminals)

### **Terminal 1 - Run Publisher**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash
ros2 run arduinobot_py_example simple_publisher
```

### **Terminal 2 - Listen to Messages**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash
ros2 topic echo /chatter
```

**Expected Terminal 2 Output:**
```
data: 'Hello, world! 0'
---
data: 'Hello, world! 1'
---
data: 'Hello, world! 2'
---
```

**Note:** Messages appear every 1 second

---

## 📊 Test Scenario 3: Full Monitoring (Three Terminals)

### **Terminal 1 - Run Publisher**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash
ros2 run arduinobot_py_example simple_publisher
```

### **Terminal 2 - View Messages**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash
ros2 topic echo /chatter
```

### **Terminal 3 - Monitor Publish Rate**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash
ros2 topic hz /chatter
```

**Expected Terminal 3 Output:**
```
average rate: 1.000
	min: 0.999s max: 1.001s std dev: 0.00057s window: 10
average rate: 1.000
	min: 0.999s max: 1.002s std dev: 0.00051s window: 20
...
```

---

## 📋 Test Scenario 4: Topic Information

### **Terminal - Check Topic Details**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash

# List all topics
ros2 topic list

# Get detailed info about the chatter topic
ros2 topic info /chatter

# View message structure
ros2 interface show std_msgs/msg/String
```

**Expected Output:**
```
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

---

## 🔄 Test Scenario 5: Multiple Publishers (Two Instances)

### **Terminal 1 - Run First Python Publisher**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash
ros2 run arduinobot_py_example simple_publisher
```

### **Terminal 2 - Run Second Python Publisher** (Optional)
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash
ros2 run arduinobot_py_example simple_publisher
```

### **Terminal 3 - Listen to All Messages**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
source install/setup.bash
ros2 topic echo /chatter
```

**Expected Behavior:** You'll see messages from both publishers (rate will be ~2 Hz)

---

## ⚙️ Test Scenario 6: Run Unit Tests

```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
colcon test --packages-select arduinobot_py_example
```

**Expected Output:**
```
Starting >>> arduinobot_py_example
Finished <<< arduinobot_py_example [X.XXs]

Summary: 1 package finished [X.XXs]
```

---

## 🔧 Test Scenario 7: Build and Test C++ Version

### **Build C++ Package**
```bash
cd /sapmnt/home/I310202/Desktop/01-ROS2
colcon build --packages-select arduinobot_cpp_example
source install/setup.bash
```

### **Run C++ Publisher**
```bash
ros2 run arduinobot_cpp_example simple_publisher
```

### **In Another Terminal - Listen**
```bash
source /sapmnt/home/I310202/Desktop/01-ROS2/install/setup.bash
ros2 topic echo /chatter
```

---

## 🐛 Debugging Tips

### **Check if ROS2 is properly initialized**
```bash
ros2 node list
```

### **View all running nodes**
```bash
ros2 node info /simple_publisher
```

### **See real-time statistics**
```bash
ros2 topic stat /chatter
```

### **Record messages to a file**
```bash
ros2 bag record /chatter
```

### **Play back recorded messages**
```bash
ros2 bag play rosbag2_*
```

### **Kill all ROS2 processes**
```bash
pkill -f ros2
# or
pkill -f simple_publisher
```

---

## ✅ Verification Checklist

After running each test, verify:

- ✅ Messages are published at 1 Hz (1 message per second)
- ✅ Message counter increments correctly (#1, #2, #3, ...)
- ✅ Message content is "Hello, world! {counter}"
- ✅ Publisher logs show successful initialization
- ✅ Listener receives all messages without drops
- ✅ Node can be stopped gracefully with Ctrl+C
- ✅ No error messages in output
- ✅ Both Python and C++ versions work identically

---

## 🚨 Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| **"ros2: command not found"** | Run: `source install/setup.bash` |
| **"Package not found"** | Run: `colcon build` first |
| **No messages appearing** | Check publisher is running in another terminal |
| **Wrong publishing rate** | Verify timer frequency in code (should be 1.0 Hz) |
| **Port already in use** | Kill previous ROS2: `pkill -f ros2` |
| **Can't connect to ROS2** | Make sure ROS2 middleware is available |

---

## 📊 Expected Performance

| Metric | Expected Value |
|--------|-----------------|
| Publishing Frequency | 1.0 Hz (±0.001) |
| Message Interval | 1.000 ± 0.001 seconds |
| CPU Usage | < 1% (per node) |
| Memory Usage | ~20-50 MB per node |
| Latency | < 100 ms |

---

## 🎯 Test Completion

You have successfully tested the Simple Publisher when:

1. ✅ Python publisher runs and publishes messages
2. ✅ Messages appear on `/chatter` topic at 1 Hz
3. ✅ Message counter increments correctly
4. ✅ Listener receives all messages
5. ✅ Publishing rate is confirmed at 1 Hz
6. ✅ Node shuts down gracefully with Ctrl+C
7. ✅ C++ version (if built) performs identically
8. ✅ All tests pass without errors

---

## 📚 For More Information

See: **README_PUBLISHER.md** (Full documentation with detailed explanations)

