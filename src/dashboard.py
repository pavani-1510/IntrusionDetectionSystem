from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import joblib
import numpy as np
import pandas as pd
import datetime

# === Load the trained model ===
model_path = "/home/pavani/Documents/VSCODE/IntrusionDetectionSystem/models/trained_model.pkl"
model = joblib.load(model_path)

# === Extract the exact feature names the model was trained on ===
feature_names = model.feature_names_in_

# === Initialize the Dash app ===
app = Dash(__name__)

# === Define the layout ===
app.layout = html.Div([
    html.H1("Real-time Anomaly Detection Dashboard"),
    
    dcc.Graph(id='live-update-graph'),
    
    dcc.Interval(
        id='interval-component',
        interval=5 * 1000,  # 5 seconds interval
        n_intervals=0
    ),
    
    html.Div(id='live-update-text', style={'marginTop': 20, 'fontSize': 18})
])

# === Define callback to update graph and text ===
@app.callback(
    [Output('live-update-graph', 'figure'),
     Output('live-update-text', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    try:
        # Simulate real-time data (10 samples with the same number of features)
        simulated_data = pd.DataFrame(
            np.random.rand(10, len(feature_names)),
            columns=feature_names
        )

        # Get anomaly scores from the model
        scores = model.decision_function(simulated_data)

        # Create Plotly figure
        figure = go.Figure(data=[
            go.Scatter(x=list(range(len(scores))), y=scores, mode='lines+markers', marker=dict(color='black'))
        ])
        figure.update_layout(
            title='Anomaly Scores (Isolation Forest)',
            xaxis_title='Sample Index',
            yaxis_title='Anomaly Score',
            template='plotly_white'
        )

        # Update time
        update_time = f"Last updated at {datetime.datetime.now().strftime('%H:%M:%S')}"
        return figure, update_time

    except Exception as e:
        return go.Figure(), f"Error during update: {e}"

# === Run the app ===
if __name__ == '__main__':
    app.run(debug=True)
