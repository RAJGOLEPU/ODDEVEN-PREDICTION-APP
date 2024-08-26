# flask_ml_app/model/dummy_model.py

class DummyModel:
    def predict(self, data):
            # This dummy model just checks if the number is odd or even
                    num = int(data[0])
                    return ["Odd" if num % 2 else "Even"]

                            # Save this model as a serialized object if needed, but for simplicity, we'll just use this class directly.