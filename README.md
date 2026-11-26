# ROS2 Exercises - Progressive Learning Series

A comprehensive, progressive learning series for ROS2 development with hands-on exercises and comprehensive documentation.

## 📚 Exercises

### Level 1: Fundamentals
1. **[01-Simple-Publisher](./01-Simple-Publisher/README.md)** - Create a basic publisher node
   - Learn how the main() function works
   - Understand node initialization
   - Publish messages on a topic
   - **Status**: ✅ Complete

2. **02-Simple-Subscriber** - Create a subscriber node (Coming soon)
   - Subscribe to messages
   - Callback mechanisms
   - Message handling

3. **03-Pub-Sub-Communication** - Publisher and subscriber together (Coming soon)
   - Multiple nodes communicating
   - Topic-based communication
   - Testing inter-node communication

### Level 2: Intermediate
4. **04-Custom-Messages** - Define and use custom message types (Coming soon)
5. **05-Services** - Request/response pattern (Coming soon)
6. **06-Parameters-and-Config** - Working with parameters (Coming soon)

### Level 3: Advanced
7. **07-Timers-and-Callbacks** - Advanced callback mechanisms (Coming soon)
8. **08-Node-Lifecycle** - Startup and shutdown patterns (Coming soon)
9. **09-Testing-and-Debugging** - Unit tests and debugging (Coming soon)

### Level 4: Real-World Applications
10. **10-Robotics-Simulation** - Gazebo integration (Coming soon)
11. **11-Real-Robot-Integration** - Physical robot control (Coming soon)
12. **12-Project-Integration** - Combine all concepts (Coming soon)

---

## 🚀 Quick Start

### Prerequisites
- Ubuntu 22.04 or later
- ROS2 Humble installed
- Python 3.10+
- Git

### Setup

```bash
# 1. Source ROS2 setup
source /opt/ros/humble/setup.bash

# 2. Navigate to an exercise
cd 01-Simple-Publisher

# 3. Build the packages
colcon build

# 4. Source the install space
source install/setup.bash

# 5. Run the exercise
ros2 run arduinobot_py_example simple_publisher
```

### Verify Installation

```bash
# Check ROS2 installation
ros2 --version

# List available topics
ros2 topic list

# Check a node's information
ros2 node info /simple_publisher
```

---

## 📖 How to Use This Repository

1. **Start with Exercise 01** - Begin with the Simple Publisher
2. **Follow Numerical Order** - Each exercise builds on previous knowledge
3. **Read the Documentation** - Each exercise has comprehensive guides:
   - `START_HERE.txt` - Quick navigation
   - `README.md` - Exercise overview
   - `TESTING_GUIDE.md` - How to test
   - `MAIN_FUNCTION_GUIDE.md` - Code explanation
4. **Complete Hands-On Work** - Build and test each exercise
5. **Move to Next Exercise** - Once you've mastered the current one

---

## 📂 Repository Structure

```
ros2-exercises/
├── .git/
├── .gitignore                        # Excludes build/, install/, etc.
├── README.md                         # This file
├── 01-Simple-Publisher/              # Exercise 1
│   ├── README.md                    # Exercise overview
│   ├── START_HERE.txt               # Quick entry point
│   ├── TESTING_GUIDE.md             # How to test
│   ├── MAIN_FUNCTION_GUIDE.md       # Code explanation
│   ├── src/
│   │   └── arduinobot_py_example/
│   │       └── simple_publisher.py
│   └── [other documentation files]
├── 02-Simple-Subscriber/             # Exercise 2 (Future)
├── 03-Pub-Sub-Communication/         # Exercise 3 (Future)
└── [Additional exercises...]
```

---

## 🎯 Learning Objectives

By the end of this course, you will understand:

- ✅ ROS2 node lifecycle and main() function
- ✅ Publishers and subscribers
- ✅ Topic-based communication
- ✅ Custom message types
- ✅ Services and service calls
- ✅ Parameters and configuration
- ✅ Timers and callbacks
- ✅ Testing and debugging ROS2 nodes
- ✅ Robotics simulation
- ✅ Real robot integration

---

## 🧪 Testing

Each exercise includes comprehensive testing guides. To test an exercise:

```bash
cd 01-Simple-Publisher

# Option 1: Use ROS2 tools
Terminal 1:
  ros2 run arduinobot_py_example simple_publisher

Terminal 2:
  ros2 topic echo /chatter

# Option 2: Run unit tests
colcon test --packages-select arduinobot_py_example

# Option 3: Monitor with ROS2 tools
ros2 topic hz /chatter
ros2 topic info /chatter
```

For detailed testing procedures, see the `TESTING_GUIDE.md` in each exercise folder.

---

## 🐛 Troubleshooting

### "Command not found: ros2"
```bash
source /opt/ros/humble/setup.bash
```

### "Package not found"
```bash
cd 01-Simple-Publisher
colcon build
source install/setup.bash
```

### "Failed to run command"
Make sure you sourced setup.bash in EVERY new terminal:
```bash
source /opt/ros/humble/setup.bash
source install/setup.bash
```

For more troubleshooting help, see [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)

---

## 📝 Documentation

Each exercise includes:
- **README.md** - Exercise overview and learning objectives
- **START_HERE.txt** - Quick navigation guide
- **TESTING_GUIDE.md** - Multiple testing scenarios
- **MAIN_FUNCTION_GUIDE.md** - Detailed code explanation
- **Source code** - Fully commented Python and C++ examples

---

## 🤝 Contributing

Found an issue or want to improve? Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

---

## 📄 License

This project is licensed under the Apache License 2.0 - see [LICENSE](./LICENSE) file for details.

(Note: ROS2 uses Apache License 2.0 as the standard)

---

## 🔗 Resources

- [ROS2 Official Documentation](https://docs.ros.org/)
- [ROS2 Tutorials](https://docs.ros.org/en/humble/Tutorials.html)
- [ROS2 GitHub](https://github.com/ros2)
- [Colcon Documentation](https://colcon.readthedocs.io/)

---

## 📧 Questions?

- Check the exercise's `START_HERE.txt` for quick answers
- Read the `TESTING_GUIDE.md` for testing issues
- Review `MAIN_FUNCTION_GUIDE.md` for code understanding
- See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) for common issues

---

## 🎓 Course Progression

```
Beginner                Intermediate           Advanced              Expert
   |                        |                      |                   |
00-Getting-Started ─► 01-Publisher ─► 04-Messages ─► 07-Callbacks ─► 10-Simulation
                         │                │               │               │
                     02-Subscriber    05-Services      08-Lifecycle   11-Real Robot
                         │                │               │               │
                     03-Pub/Sub       06-Parameters   09-Testing     12-Integration
```

---

## ✨ What's Next?

After completing all exercises, you can:
- Build real robotics applications
- Contribute to ROS2 community projects
- Develop commercial robotics solutions
- Teach ROS2 to others
- Create advanced simulations with Gazebo

---

## 📊 Statistics

- **Total Exercises**: 12 (3 levels + 1 advanced)
- **Estimated Time**: 40-60 hours
- **Languages**: Python and C++
- **Documentation Pages**: 50+
- **Code Examples**: 100+

---

**Happy Learning! 🚀**

For the latest updates, star this repository and watch for new exercises!
