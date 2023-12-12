import rclpy
import os
from rclpy.node import Node
from flask import Flask, send_from_directory, send_file, request, jsonify, render_template

ROS_DOMAIN_ID :int = int(os.environ.get('ROS_DOMAIN_ID',0))
rclpy.init(domain_id=ROS_DOMAIN_ID)
ros_web_node = Node("ros_web_node")

www_path = "../resource/web"
app = Flask(__name__, static_folder=www_path + '/static', template_folder=www_path)


def get_video_topics(node: Node):
    
    topics = []
    for topic in node.get_topic_names_and_types():
        if topic[1] == ['sensor_msgs/msg/Image']:
            # topics.append(topic[0].replace('/compressed',''))
            topics.append(topic[0])

    return topics        


@app.route("/")
def serve_index():
  ip_address = request.host.split(':')[0]
  return render_template('index.html', 
                        ros_host = ip_address,
                        video_topics = get_video_topics(ros_web_node))
#   return "Hello World1!"

def main():
  app.run(host="0.0.0.0", port=8080, threaded=True)

if __name__ == "__main__":
  main()