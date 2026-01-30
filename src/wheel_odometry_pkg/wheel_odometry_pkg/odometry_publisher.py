#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class OdometryPublisher(Node):
    def __init__(self):
        super().__init__('odometry_publisher')
        self.publisher_ = self.create_publisher(Twist, 'wheel_odometry', 10)
        self.timer = self.create_timer(0.1, self.publish_odometry)
        self.t = 0.0
        self.get_logger().info('Odometry Publisher started.')

    def publish_odometry(self):
        msg = Twist()
        msg.linear.x = 0.6 + 0.1 * math.sin(self.t)
        msg.angular.z = 0.3 * math.cos(self.t)
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Linear vel: {msg.linear.x:.2f} m/s | Angular vel: {msg.angular.z:.2f} rad/s'
        )
        self.t += 0.1

def main(args=None):
    rclpy.init(args=args)
    node = OdometryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class OdometryPublisher(Node):
    def __init__(self):
        super().__init__('odometry_publisher')
        self.publisher_ = self.create_publisher(Twist, 'wheel_odometry', 10)
        self.timer = self.create_timer(0.1, self.publish_odometry)
        self.t = 0.0
        self.get_logger().info('Odometry Publisher started.')

    def publish_odometry(self):
        msg = Twist()
        msg.linear.x = 0.6 + 0.1 * math.sin(self.t)
        msg.angular.z = 0.3 * math.cos(self.t)
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Linear vel: {msg.linear.x:.2f} m/s | Angular vel: {msg.angular.z:.2f} rad/s'
        )
        self.t += 0.1

def main(args=None):
    rclpy.init(args=args)
    node = OdometryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

