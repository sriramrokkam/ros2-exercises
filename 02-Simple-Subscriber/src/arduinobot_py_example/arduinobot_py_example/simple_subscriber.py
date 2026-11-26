# Import ROS2 client library for Python
import rclpy
# Import the base Node class to inherit from
from rclpy.node import Node
# Import the standard String message type
from std_msgs.msg import String

class SimpleSubscriber(Node):
    # Initialize the subscriber node with necessary attributes
    def __init__(self):
        # Call parent Node class constructor with node name 'simple_subscriber'
        super().__init__('simple_subscriber')
        # Create a subscription to the 'chatter' topic with String message type
        # Set queue size to 10 (buffer size for incoming messages)
        # Set callback function to handle incoming messages
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10)
        # Suppress unused variable warning (subscription is used by the framework)
        self.subscription
        # Log that the node has been initialized successfully
        self.get_logger().info('SimpleSubscriber node initialized')
        # Initialize a counter to track the number of received messages
        self.counter = 0

    # Callback function that is called whenever a message is received on the subscribed topic
    def listener_callback(self, msg):
        # Increment the message counter
        self.counter += 1
        # Log the received message with its sequence number
        self.get_logger().info(f'Received message #{self.counter}: {msg.data}')

# Main entry point for the node
def main(args=None):
    # Initialize the ROS2 communication with the provided arguments
    rclpy.init(args=args)
    # Create an instance of the SimpleSubscriber node
    node = SimpleSubscriber()
    # Keep the node running and processing callbacks
    # This will continuously listen for messages on the subscribed topic
    rclpy.spin(node)
    # Clean up the node resources after the spin is complete
    node.destroy_node()
    # Shutdown ROS2 communication
    rclpy.shutdown()

# Check if this script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Call the main function to start the node
    main()
