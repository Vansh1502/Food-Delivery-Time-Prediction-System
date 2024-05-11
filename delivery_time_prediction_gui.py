import tkinter as tk
from flask import Flask, request, render_template # type: ignore
import numpy as np
from tensorflow.keras.models import load_model # type: ignore

from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=False) 

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
model = load_model('my_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form['data']
        # Preprocess the input data if needed
        prediction = model.predict(np.array([[data]]))
        return str(prediction[0][0])

# Tkinter GUI
class DeliveryTimePredictionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Delivery Time Prediction")

        # Labels and Entry fields
        self.age_label = tk.Label(master, text="Age of Delivery Partner:")
        self.age_label.pack()
        self.age_entry = tk.Entry(master)
        self.age_entry.pack()

        self.rating_label = tk.Label(master, text="Ratings of Previous Deliveries:")
        self.rating_label.pack()
        self.rating_entry = tk.Entry(master)
        self.rating_entry.pack()

        self.distance_label = tk.Label(master, text="Total Distance:")
        self.distance_label.pack()
        self.distance_entry = tk.Entry(master)
        self.distance_entry.pack()

        # Button and result label
        self.predict_button = tk.Button(master, text="Predict Delivery Time", command=self.predict_delivery_time)
        self.predict_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def predict_delivery_time(self):
        age = self.age_entry.get()
        rating = self.rating_entry.get()
        distance = self.distance_entry.get()

        # Concatenate input data
        input_data = f"{age},{rating},{distance}"

        # Make a request to the Flask app
        with app.test_request_context():
            prediction = app.dispatch_request(request.form.encode({'data': input_data}))

        # Display the prediction result
        self.result_label.configure(text=f"Predicted Delivery Time: {prediction}")

# Run the Flask app and the Tkinter GUI
if __name__ == '__main__':
    root = tk.Tk()
    gui = DeliveryTimePredictionGUI(root)
    app.run()
    root.mainloop()