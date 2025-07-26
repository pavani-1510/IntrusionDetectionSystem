def extract_features(data):
    data['protocol_type'] = data['protocol_type'].astype('category').cat.codes
    data['service'] = data['service'].astype('category').cat.codes
    data['flag'] = data['flag'].astype('category').cat.codes
    features = data[['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes']]
    return features

def select_important_features(features, importance_threshold=0.1):
    return features

def preprocess_features(data):
    extracted_features = extract_features(data)
    important_features = select_important_features(extracted_features)
    return important_features