
import tensorflow as tf

LABEL_KEY = "label"
FEATURE_KEY = "text"

def transformed_name(key):
    return key + "_xf"

def preprocessing_fn(inputs):
    outputs = {}

    # Cast the label to int64
    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)

    # Convert text to lowercase
    text = tf.strings.lower(inputs[FEATURE_KEY])

    # Remove URLs
    url_pattern = r'http\S+|www\S+|https\S+'
    text = tf.strings.regex_replace(text, url_pattern, '')

    outputs[transformed_name(FEATURE_KEY)] = text

    return outputs
