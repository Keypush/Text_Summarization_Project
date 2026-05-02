from textSummarization.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text, pred_trained_model=False):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path) if not pred_trained_model else AutoTokenizer.from_pretrained(self.config.trained_tokenizer)
        model_path = self.config.model_path if not pred_trained_model else self.config.trained_model
        
        gen_kwargs = {
            "length_penalty": 0.8,
            "num_beams": 8,
            "max_length": 128,
        }

        summarization_pipeline = pipeline("summarization", model=model_path, tokenizer=tokenizer)
        summary = summarization_pipeline(text, **gen_kwargs)

        print ("Dialogue: ", text)
        print ("Summary: ", summary[0]['summary_text'])
    
        return summary[0]['summary_text']