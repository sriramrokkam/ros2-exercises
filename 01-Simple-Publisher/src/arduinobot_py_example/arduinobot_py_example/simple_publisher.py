# Import ROS2 client library for Python
import rclpy
# Import the base Node class to inherit from
from rclpy.node import Node
# Import the standard String message type
from std_msgs.msg import String

class SimplePublisher(Node):
    # Initialize the publisher node with necessary attributes
    def __init__(self):
        # Call parent Node class constructor with node name 'simple_publisher'
        super().__init__('simple_publisher')
        # Create a publisher that sends String messages to the 'chatter' topic with queue size of 10
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        # Initialize a counter to track the number of published messages
        self.counter = 0
        # Set the publishing frequency in Hz (1 message per second)
        self.frequency = 1.0  # Frequency in Hz
        # Log that the node has been initialized successfully
        self.get_logger().info('SimplePublisher node initialized')
        # Create a timer that calls timer_callback at the specified frequency (1.0 / self.frequency = 1 second interval)
        self.timer_ = self.create_timer(1.0 / self.frequency, self.timer_callback)

    # Method to publish a message to the topic
    def publish_message(self, msg):
        # Send the message through the publisher
        self.publisher_.publish(msg)
        # Increment the message counter
        self.counter += 1
        # Log the published message with its sequence number
        self.get_logger().info(f'Published message #{self.counter}')

    # Timer callback to periodically publish messages
    def timer_callback(self):
        # Create a new String message object
        msg = String()
        # Set the message data with a greeting and the current counter value
        msg.data = f'Hello, world! {self.counter}'
        # Call the publish_message method to send the message
        self.publish_message(msg)
    
# Main entry point for the node
def main(args=None):
    # Initialize the ROS2 communication with the provided arguments
    rclpy.init(args=args)
    # Create an instance of the SimplePublisher node
    node = SimplePublisher()
    # Keep the node running and processing callbacks
    rclpy.spin(node)
    # Clean up the node resources after the spin is complete
    node.destroy_node()
    # Shutdown ROS2 communication
    rclpy.shutdown()

# Check if this script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Call the main function to start the node
    main()