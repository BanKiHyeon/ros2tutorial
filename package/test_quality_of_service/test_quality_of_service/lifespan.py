import argparse
import sys

from test_quality_of_service.common_nodes import Listener
from test_quality_of_service.common_nodes import Talker

import rclpy
from rclpy.duration import Duration
from rclpy.executors import ExternalShutdownException
from rclpy.executors import SingleThreadedExecutor
from rclpy.qos import QoSDurabilityPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSReliabilityPolicy


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'lifespan', type=int,
        help='Duration in positive integer milliseconds of the Lifespan QoS setting.')
    parser.add_argument(
        '--history', type=int, default=10,
        help="The depth of the Publisher's history queue - "
             'the maximum number of messages it will store for late-joining subscriptions.')
    parser.add_argument(
        '--publish-count', type=int, default=10,
        help='How many messages to publish before stopping.')
    parser.add_argument(
        '--subscribe-after', type=int, default=2500,
        help='The Subscriber will be created this long (in positive integer milliseconds) '
             'after application startup.')
    return parser.parse_args()


def main(args=None):
    parsed_args = parse_args()
    rclpy.init(args=args)

    topic = 'qos_lifespan_chatter'
    lifespan = Duration(seconds=parsed_args.lifespan / 1000.0)

    qos_profile = QoSProfile(
        depth=parsed_args.history,
        reliability=QoSReliabilityPolicy.RELIABLE,
        durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
        lifespan=lifespan)

    listener = Listener(
        topic, qos_profile, event_callbacks=None, defer_subscribe=True)
    talker = Talker(
        topic, qos_profile, event_callbacks=None, publish_count=parsed_args.publish_count)
    subscribe_timer = listener.create_timer(  
        parsed_args.subscribe_after / 1000.0,
        lambda: listener.start_listening())

    executor = SingleThreadedExecutor()
    executor.add_node(listener)
    executor.add_node(talker)
    try:
        executor.spin()
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        rclpy.try_shutdown()

    return 0


if __name__ == '__main__':
    sys.exit(main())