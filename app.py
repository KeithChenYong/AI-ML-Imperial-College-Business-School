# app.py
from flask import Flask, request, jsonify
import torch
import torch.nn as nn

app = Flask(__name__)

# Define LSTM model class
class LSTM(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim, num_layers, dropout):
        super(LSTM, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim)
        out, _ = self.lstm(x, (h0, c0))
        return self.fc(out[:, -1, :])
    

# Load the model
checkpoint = torch.load('best_model.pth')
model_state_dict = checkpoint['model_state_dict']
hyperparameters = checkpoint['hyperparameters']

model = LSTM(input_dim=1, output_dim=1, 
             hidden_dim=hyperparameters['hidden_dim'], 
             num_layers=hyperparameters['num_layers'], 
             dropout=hyperparameters['dropout'])

model.load_state_dict(model_state_dict)

model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_tensor = torch.tensor(data['input'], dtype=torch.float32)
    with torch.no_grad():
        predictions = model(input_tensor).numpy()
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
