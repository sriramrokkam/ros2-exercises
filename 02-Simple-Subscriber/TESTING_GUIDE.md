# 🧪 TESTING GUIDE - Simple Subscriber

Complete testing scenarios for the ROS2 Simple Subscriber.

---

## 📋 Test Overview

This guide includes 7 different test scenarios, from basic to advanced:

1. **Basic Subscriber Test** - Verify the subscriber works
2. **Multiple Subscribers Test** - Test multiple subscribers on same topic
3. **Message Rate Test** - Measure how many messages per second
4. **Topic Monitoring Test** - Monitor topic with ROS2 tools
5. **Node Information Test** - Inspect the node with ROS2 commands
6. **Error Handling Test** - Test behavior when publisher stops
7. **Integration Test** - Full pub-sub communication test

**Time Required**: 20-30 minutes total

---

## ⚙️ Prerequisites

Before running tests:

```bash
# 1. Navigate to subscriber directory
cd /sapmnt/home/I310202/Desktop/ros2-exercises/02-Simple-Subscriber

# 2. Build the package
colcon build --packages-select arduinobot_py_example

# 3. Source the setup file
source install/setup.bash

# 4. Source ROS2 (if not already done)
source /opt/ros/humble/setup.bash
```

---

## 🧪 TEST SCENARIO 1: Basic Subscriber Test

**Objective**: Verify the subscriber runs and receives messages

**Time**: 2 minutes

### Setup

**Terminal 1 - Publisher**:
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
[INFO] [simple_publisher]: Published message #3
...
```

**Terminal 2 (Subscriber)**:
```
[INFO] [simple_subscriber]: SimpleSubscriber node initialized
[INFO] [simple_subscriber]: Received message #1: Hello, world! 0
[INFO] [simple_subscriber]: Received message #2: Hello, world! 1
[INFO] [simple_subscriber]: Received message #3: Hello, world! 2
...
```

### Verification

✅ **PASS** if:
- Subscriber receives messages from publisher
- Counter increments correctly
- Messages display in correct format

❌ **FAIL** if:
- No "Received message" appears
- Counter doesn't increment
- Error messages appear

### Troubleshooting

| Issue | Solution |
|-------|----------|
| "No messages received" | Check publisher is running in Terminal 1 |
| "Module not found" | Run `source /opt/ros/humble/setup.bash` |
| "Port already in use" | Kill existing processes or use different terminal |

---

## 🧪 TEST SCENARIO 2: Multiple Subscribers Test

**Objective**: Verify multiple subscribers receive the same messages

**Time**: 3 minutes

### Setup

**Terminal 1 - Publisher**:
```bash
cd /sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher
source install/setup.bash
ros2 run arduinobot_py_example simple_publisher
```

**Terminal 2 - Subscriber 1**:
```bash
cd /sapmnt/home/I310202/Desktop/ros2-exercises/02-Simple-Subscriber
source install/setup.bash
ros2 run arduinobot_py_example simple_subscriber
```

**Terminal 3 - Subscriber 2**:
```bash
cd /sapmnt/home/I310202/Desktop/ros2-exercises/02-Simple-Subscriber
source install/setup.bash
ros2 run arduinobot_py_example simple_subscriber
```

### Expected Output

**Terminal 2 (Subscriber 1)**:
```
[INFO] [simple_subscriber]: SimpleSubscriber node initialized
[INFO] [simple_subscriber]: Received message #1: Hello, world! 0
[INFO] [simple_subscriber]: Received message #2: Hello, world! 1
...
```

**Terminal 3 (Subscriber 2)**:
```
[INFO] [simple_subscriber]: SimpleSubscriber node initialized
[INFO] [simple_subscriber]: Received message #1: Hello, world! 0
[INFO] [simple_subscriber]: Received message #2: Hello, world! 1
...
```

### Verification

✅ **PASS** if:
- Both subscribers receive the same messages
- Both have independent counters
- Messages arrive at approximately the same time

❌ **FAIL** if:
- One subscriber gets messages but not the other
- Messages are different between subscribers
- Counters are out of sync

---

## 🧪 TEST SCENARIO 3: Message Rate Test

**Objective**: Verify the message rate (1 message per second)

**Time**: 5 minutes

### Setup

**Terminal 1 - Publisher**:
```bash
cd /sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher
source install/setup.bash
ros2 run arduinobot_py_example simple_publisher
```

**Terminal 2 - Measure Message Rate**:
```bash
source /opt/ros/humble/setup.bash
ros2 topic hz /chatter
```

### Expected Output

```
average rate: 1.000
	min: 0.999s max: 1.001s std dev: 0.001s window: 10
```

### Verification

✅ **PASS** if:
- Average rate is approximately 1.0 Hz (1 message per second)
- Standard deviation is very low (< 0.01)
- Rates are consistent

❌ **FAIL** if:
- Rate is significantly different from 1.0 Hz
- High variability in message timing
- Messages are not arriving regularly

---

## 🧪 TEST SCENARIO 4: Topic Monitoring Test

**Objective**: Monitor the topic with ROS2 tools

**Time**: 3 minutes

### Setup

**Terminal 1 - Publisher**:
```bash
cd /sapmnt/home/I310202/Desktop/ros2-exercises/01-Simple-Publisher
source install/setup.bash
ros2 run arduinobot_py_example simple_publisher
```

**Terminal 2 - Echo Messages**:
```bash
source /opt/ros/humble/setup.bash
ros2 topic echo /chatter
```

### Expected Output

```
data: Hello, world! 0
---
data: Hello, world! 1
---
data: Hello, world! 2
---
```

### Additional Monitoring Commands

**Get topic info**:
```bash
ros2 topic info /chatter
```

Expected output:
```
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

**List all topics**:
```bash
ros2 topic list
```

Should include `/chatter` in the output.

### Verification

✅ **PASS** if:
- Messages display correctly with `ros2 topic echo`
- Topic info shows correct message type
- Topic appears in topic list

❌ **FAIL** if:
- Messages don't appear
- Topic info is missing
- Topic not in list

---

## 🧪 TEST SCENARIO 5: Node Information Test

**Objective**: Inspect the node with ROS2 commands

**Time**: 3 minutes

### Setup

**Terminal 1 - Publisher**:
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

**Terminal 3 - Inspect Node**:
```bash
source /opt/ros/humble/setup.bash

# List all nodes
ros2 node list

# Get subscriber node info
ros2 node info /simple_subscriber
```

### Expected Output

**Node list**:
```
/simple_publisher
/simple_subscriber
```

**Node info**:
```
/simple_subscriber
  Subscribers:
    /chatter: std_msgs/msg/String
  Publishers:
  Services:
  Actions:
```

### Verification

✅ **PASS** if:
- Both nodes appear in node list
- Subscriber shows subscription to `/chatter`
- Subscription type is correct (std_msgs/msg/String)

❌ **FAIL** if:
- Subscriber node doesn't appear
- Subscription not shown
- Wrong message type

---

## 🧪 TEST SCENARIO 6: Error Handling Test

**Objective**: Test behavior when publisher stops

**Time**: 5 minutes

### Setup and Procedure

**Terminal 1 - Publisher**:
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

### Procedure

1. Let both run for 5 seconds (see messages in Terminal 2)
2. Stop the publisher (Ctrl+C in Terminal 1)
3. Observe that subscriber continues running
4. Restart publisher (run same command again in Terminal 1)

### Expected Behavior

**Before stopping publisher** (Terminal 2):
```
[INFO] [simple_subscriber]: Received message #1: Hello, world! 0
[INFO] [simple_subscriber]: Received message #2: Hello, world! 1
[INFO] [simple_subscriber]: Received message #3: Hello, world! 2
```

**After stopping publisher** (Terminal 2):
```
(No new messages appear, but subscriber keeps running)
(No error messages appear)
```

**After restarting publisher** (Terminal 2):
```
[INFO] [simple_subscriber]: Received message #4: Hello, world! 3
(Counter continues from where it left off)
```

### Verification

✅ **PASS** if:
- Subscriber continues running when publisher stops
- No error messages appear
- Subscriber resumes receiving when publisher restarts
- Counter continues from where it left off

❌ **FAIL** if:
- Subscriber crashes when publisher stops
- Error messages appear
- Counter resets

---

## 🧪 TEST SCENARIO 7: Integration Test

**Objective**: Full pub-sub communication test with verification

**Time**: 5 minutes

### Setup

**Terminal 1 - Publisher**:
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

**Terminal 3 - Monitor**:
```bash
source /opt/ros/humble/setup.bash
ros2 topic echo /chatter --no-arr
```

**Terminal 4 - Inspect**:
```bash
source /opt/ros/humble/setup.bash
ros2 topic info /chatter
ros2 node list
```

### Expected Behavior

All terminals should work together:
- Publisher publishes messages
- Subscriber receives and logs messages
- Monitor shows messages in real-time
- Node and topic info displays correctly

### Verification Checklist

✅ **PASS** if ALL of the following are true:
- [ ] Publisher publishes message #1, #2, #3, ...
- [ ] Subscriber receives message #1, #2, #3, ...
- [ ] Monitor shows all messages
- [ ] Topic info shows 1 publisher and 1 subscriber
- [ ] Both nodes appear in node list
- [ ] Message format is correct
- [ ] All processes run without errors

---

## 🎯 Test Results Summary

| Test | Pass | Fail | Notes |
|------|------|------|-------|
| 1. Basic Subscriber | ⬜ | ⬜ | |
| 2. Multiple Subscribers | ⬜ | ⬜ | |
| 3. Message Rate | ⬜ | ⬜ | |
| 4. Topic Monitoring | ⬜ | ⬜ | |
| 5. Node Information | ⬜ | ⬜ | |
| 6. Error Handling | ⬜ | ⬜ | |
| 7. Integration | ⬜ | ⬜ | |

---

## 🔧 Useful Commands Reference

```bash
# Build
cd /sapmnt/home/I310202/Desktop/ros2-exercises/02-Simple-Subscriber
colcon build --packages-select arduinobot_py_example

# Source
source install/setup.bash
source /opt/ros/humble/setup.bash

# Run subscriber
ros2 run arduinobot_py_example simple_subscriber

# Monitor topics
ros2 topic list
ros2 topic info /chatter
ros2 topic hz /chatter
ros2 topic echo /chatter

# Node information
ros2 node list
ros2 node info /simple_subscriber

# Debug/Logging
ros2 run arduinobot_py_example simple_subscriber --ros-args --log-level DEBUG
```

---

## 📝 Notes

- Always run the publisher before the subscriber (or start publisher first)
- Use different terminals for publisher and subscriber
- Remember to source setup.bash in each new terminal
- Tests can be run independently or in sequence
- For detailed code explanation, see MAIN_FUNCTION_GUIDE.md

---

## ✅ You've Completed All Tests!

If all tests passed:
1. ✅ Subscriber works correctly
2. ✅ Messages flow properly
3. ✅ ROS2 tools work as expected
4. ✅ Integration with publisher successful

**Next Steps**:
- Read MAIN_FUNCTION_GUIDE.md for deep understanding
- Try modifying the code
- Read README_SUBSCRIBER.md for complete reference
- Compare with Publisher code

---

**Happy Testing! 🧪**
