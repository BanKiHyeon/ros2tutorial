from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(
        self, topic_name, qos_profile, event_callbacks,
        publish_count=0, assert_topic_period=None
    ):
        super().__init__('talker')
        self.get_logger().info('Talker starting up')
        self.publisher = self.create_publisher(
            String, topic_name, qos_profile,
            event_callbacks=event_callbacks)
        self.publish_timer = self.create_timer(0.5, self.publish)
        if assert_topic_period:
            self.assert_topic_timer = self.create_timer(
                assert_topic_period, self.publisher.assert_liveliness)
        else:
            self.assert_topic_timer = None
        self.pause_timer = None
        self.publish_count = 0
        self.stop_at_count = publish_count

    def pause_for(self, seconds):
        if self.pause_timer:
            return
        self.publish_timer.cancel()
        self.pause_timer = self.create_timer(seconds, self._pause_expired)

    def _pause_expired(self):
        self.publish()
        self.publish_timer.reset()
        self.destroy_timer(self.pause_timer)
        self.pause_timer = None

    def publish(self):
        message = String()
        message.data = f'Talker says {self.publish_count}'
        self.get_logger().info(f"Publishing: '{message.data}'")
        self.publish_count += 1
        if self.stop_at_count > 0 and self.publish_count >= self.stop_at_count:
            self.publish_timer.cancel()
        self.publisher.publish(message)

    def stop(self):
        if self.assert_topic_timer:
            self.assert_topic_timer.cancel()
        self.publish_timer.cancel()
        self.assert_topic_timer = None


class Listener(Node):
    def __init__(self, topic_name, qos_profile, event_callbacks, defer_subscribe=False):
        super().__init__('listener')
        self.subscription = None
        self.topic_name = topic_name
        self.qos_profile = qos_profile
        self.event_callbacks = event_callbacks
        if not defer_subscribe:
            self.start_listening()

    def start_listening(self):
        if not self.subscription:
            self.subscription = self.create_subscription(
                String, self.topic_name, self._message_callback,
                self.qos_profile,
                event_callbacks=self.event_callbacks)
            self.get_logger().info('Listener starting up')

    def _message_callback(self, message):
        self.get_logger().info(f'Listener heard: [{message.data}]')
