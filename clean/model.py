import torch
from torch import nn

class BiLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(BiLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=True, dropout=0.0)
        # x -> batch_size, sequence_length, input_size
        self.fc0 = nn.Linear(hidden_size*2,80)
        self.fc1 = nn.Linear(80,60)
        self.fc2 = nn.Linear(60,50)
        self.fc3 = nn.Linear(50,20)
        self.fc4 = nn.Linear(20,10)
        self.fc5 = nn.Linear(10, 1)

        self.a = nn.ReLU()
        self.sig = nn.Sigmoid()
        self.loss_history = []
        self.mcc_history = []
        self.validation_loss_history = []

    def forward(self, x):
        h0 = torch.zeros(self.num_layers*2, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers*2, x.size(0), self.hidden_size).to(device) 
        # out: batch_size, seq_length, hidden_size

        out, _ = self.lstm(x, (h0, c0))
        out = self.a(out)

        out = self.fc0(out)
        out = self.a(out)

        out = self.fc1(out)
        out = self.a(out)

        out = self.fc2(out)
        out = self.a(out)

        out = self.fc3(out)
        out = self.a(out)

        out = self.fc4(out)
        out = self.a(out)

        out = self.fc5(out)
        out = self.sig(out)
        return out