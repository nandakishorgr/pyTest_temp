#dict={'Mango':[10,20],'Apple':20,'Orange':30}

event={}

event1={
    "Records": [
        {
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:EXAMPLE",
            "EventSource": "aws:sns",
            "Sns": {
                "Signature": "EXAMPLE",
                "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
                "Type": "Notification",
                "TopicArn": "arn:aws:sns:EXAMPLE",
                "MessageAttributes": {
                    "Test": {
                        "Type": "String",
                        "Value": "TestString"
                    },
                    "TestBinary": {
                        "Type": "Binary",
                        "Value": "TestBinary"
                    }
                },
                "SignatureVersion": "1",
                "Timestamp": "2015-06-03T17:43:27.123Z",
                "SigningCertUrl": "EXAMPLE",
                "Message": "Hello from SNS!",
                "UnsubscribeUrl": "EXAMPLE",
                "Subject": "TestInvoke"
            }
        }
    ]
}
metadata = event.get('Records', [{'Sns': 'cwr'}])[0]
print(metadata)
if metadata.get("Sns", None) is not None:
    print("Event found!!!")
else:
    print("event not found...")