import rclpy
from rclpy.node import Node
import requests
from example_interfaces.msg import String
from queue import Queue

class NovelPunNode(Node):
    def __init_(self,node_name):
        super().__init__(node_name)
        self.novels_queue_=Queue()   #   创建队列，存放小说
        self.novel_publisher_=self.create_publisher(String,'novel',10)
        self.timer_ = self.create_timer(5,self.timer_callback)

    def download_novel(self,url):
        response=requests.get(url)
        response.encoding = 'utf-8'
        self.get_logger().info(f'下载完成：{url}')
        for line in response.text.splitlines():
            self.novels_queue_.put(line)

    def timer_callback(self):
        if self.novels_queue_.qsize()>0:
            msg = String()
            msg.data = self.novels_queue_.get()
            self.novel_publisher_.publish(msg)
            self.get_logger().info(f'发布了一行小说：{msg.data}')


def main():
    rclpy.init()
    node = NovelPunNode('novel_pub')
    node.download_novel('http://localhost:8000/novel1.txt')
    rclpy.spin(node)
    rclpy.shutdown()