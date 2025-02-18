#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

class JointPublisher(Node):
    def __init__(self):
        super().__init__('joint_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        timer_period = 0.1  # segundos
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.joint_state = JointState()

        self.joint_state.name = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6', 'gripper_joint_left']  # Nombres de las articulaciones
        self.joint_state.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # Posiciones iniciales de las articulaciones

    def timer_callback(self):
        self.joint_state.header.stamp = self.get_clock().now().to_msg()
        
        # Aquí puedes actualizar los ángulos de las articulaciones
        self.joint_state.position[0] = math.sin(self.get_clock().now().seconds_nanoseconds()[0])  # Ejemplo de movimiento sinusal
        self.joint_state.position[1] = math.cos(self.get_clock().now().seconds_nanoseconds()[0])
        self.joint_state.position[2] = math.sin(self.get_clock().now().seconds_nanoseconds()[0] / 2)

        self.publisher_.publish(self.joint_state)
        self.get_logger().info('Publishing joint states: "%s"' % str(self.joint_state.position))

def main(args=None):
    rclpy.init(args=args)
    joint_publisher = JointPublisher()
    rclpy.spin(joint_publisher)

    # Destruimos el nodo explícitamente
    joint_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

