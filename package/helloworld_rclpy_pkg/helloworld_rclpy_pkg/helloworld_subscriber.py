import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

class HelloworldSubscriber(Node):

    def __init__(self):
        super().__init__('helloworld_subscriber')
        qoSProfile = QoSProfile(depth=10)
        self.helloworld_subscriber = self.create_subscription(String, 'helloworld',self.subscriber_topic_msg, qoSProfile)
        
    
    def subscriber_topic_msg(self, msg):
        self.get_logger().info('Received message: {0}'.format(msg.data))
        

def main(args=None):
    rclpy.init(args=args)
    node = HelloworldSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()



if __name__ == '__main__':
    main()