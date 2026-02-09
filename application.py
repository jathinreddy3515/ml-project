from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask app
application = Flask(__name__)
app = application

# -------------------------
# Route for Home Page
# -------------------------
@app.route('/')
def index():
    return render_template('index.html')  # Render main index page

# -------------------------
# Route to handle predictions
# -------------------------
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        # Show home page with input form
        return render_template('home.html')
    else:
        # Collect input data from form
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),  # ✅ fixed
            writing_score=float(request.form.get('writing_score'))   # ✅ fixed
        )

        # Convert input to DataFrame for prediction
        pred_df = data.get_data_as_data_frame()
        print("Input DataFrame:")
        print(pred_df)

        # Initialize prediction pipeline
        predict_pipeline = PredictPipeline()
        print("Making Prediction...")

        # Get prediction
        results = predict_pipeline.predict(pred_df)
        print("Prediction Result:", results[0])

        # Render results in template
        return render_template('home.html', results=results[0])

# -------------------------
# Run Flask App
# -------------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)