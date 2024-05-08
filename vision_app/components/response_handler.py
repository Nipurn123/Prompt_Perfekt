from .message_history import MessageHistory

class ResponseHandler:
    @staticmethod
    def generate_prompt_with_history(prompt, messages, max_messages):
        prompt_with_history = prompt + " If you don't get any other data other than user input, simply answer the user input. If you get some data apart from user input, then give the answer by taking reference of that data. If no reference is available, still answer the question.\n"
        prompt_with_history += MessageHistory.get_chat_history(messages, max_messages)
        return prompt_with_history
