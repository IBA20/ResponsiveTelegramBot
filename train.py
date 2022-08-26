import os
import os
import sys
import json
from google.cloud import dialogflow_v2 as df


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""

    intents_client = df.IntentsClient()

    parent = df.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = df.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = df.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = df.Intent.Message.Text(text=message_texts)
    message = df.Intent.Message(text=text)

    intent = df.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )
    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))

def main():
    with open(sys.argv[1]) as file:
        intents = json.load(file)
    for k, v in intents.items():
        intent_name = k
        questions = v['questions']
        answer = v['answer']
        try:
            create_intent(os.environ['GOOGLE_CLOUD_PROJECT'], intent_name, questions, [answer])
        except Exception as err:
            print('ERROR!!!')
            print(err)
        break


if __name__ == '__main__':
    main()