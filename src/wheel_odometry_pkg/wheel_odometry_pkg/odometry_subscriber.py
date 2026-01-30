#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class OdometrySubscriber(Node):
    def __init__(self):
        super().__init__('odometry_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'wheel_odometry',
            self.odom_callback,
            10
        )
        self.get_logger().info('Odometry Subscriber started.')

    def odom_callback(self, msg):
        self.get_logger().info(
            f'Received odometry → v = {msg.linear.x:.2f} m/s, ω = {msg.angular.z:.2f} rad/s'
        )

def main(args=None):
    rclpy.init(args=args)
    node = OdometrySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

