class SequenceDataset(Dataset):
    def __init__(self, data, transform):
        self.data = data
        self.transform = transform
        chain_sizes = [data['in'].iloc[i].shape[0] for i in range(len(data))]
        self.longest_chain = max(chain_sizes)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        x = self.data['in'].iloc[index]
        y = self.data['out'].iloc[index]
        seq_len = self.data['seq_len'].iloc[index]

        x = np.pad(x, ((0, self.longest_chain-x.shape[0]), (0,0)), 'minimum')
        
        y = y.astype(np.float16) # convert from bool to float

        y_amplified = amplify_sharp(y, 41) 
        y_amplified = np.pad(y_amplified, (0, self.longest_chain-y_amplified.shape[0]), 'minimum')
        y = np.pad(y, (0, self.longest_chain-y.shape[0]), 'minimum')
        y_amplified = y_amplified.reshape((1,-1))
        y_amplified = np.array(y_amplified, dtype=np.float64)
        key = self.data['key'].iloc[index]

        return x, y, y_amplified, key, seq_len