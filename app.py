from flask import Flask, request, current_app
from flask_cors import *

app = Flask(__name__)
CORS(app)


@app.route("/test", methods=["GET"])
def test():
  return "gaming hoge generator is running"

@app.route("/segmentation", methods=["POST"])
def inference():
    pass
#   image_file = request.files.get('image')

#   image = np.array(Image.open(image_file))
#   image = np.asarray(image, dtype=np.float32)
#   if image.shape[2] == 4:
#     image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
  
#   result = predict(image)

#   return json.dumps(result)

def predict(image):
    pass

if __name__ == '__main__':
  app.run(host="0.0.0.0")