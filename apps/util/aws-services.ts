import { SQS } from "aws-sdk";

export const sendSQSMessage = async (url, message) => {
  console.debug("Sending message to SQS: ", message, " to url: ", url);
  const sqs = new SQS();
  const params = {
    MessageBody: JSON.stringify(message),
    QueueUrl: url,
  };
  console.debug("SQS_DELAY_SECONDS: ", process.env.SQS_DELAY_SECONDS);
//   if (process.env.SQS_DELAY_SECONDS) {
//     params.DelaySeconds = process.env.SQS_DELAY_SECONDS;
//   }
  await sqs.sendMessage(params).promise();
  console.debug("Message sent to SQS: ", message, " to url: ", url);
};
