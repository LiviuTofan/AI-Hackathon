# Generate Promotional/Reward mails using AI, based on user input.

from openai import OpenAI

# Function to generate Promotional & Reward email based on user input which is from firebase saved as user_message
def generate_emails(user_message):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": '''You are a good email writer, based on given information from the client you have to create two emails, in JSON format. One email will focus on promotion and rewards, while the other will specifically address a reward. Please provide me with the details you'd like to include in these emails in JSON format. Next, I provide you two examples of emails.
                    example of good JSON:
                    {
                      "Promotional email": {
                        "emailSubjectText": "Provide your feedback to companyName - Get a $20 gift card",
                        "emailPreviewText": "Email Preview Text",
                        "headingText": "Your feedback is important to us!",
                        "subheadingText": "Provide your feedback to companyName, get a $20 gift card!",
                        "emailMessage": "Your active engagement means a lot to us! Share your thoughts on our performance dashboards, and be a key player in shaping our future initiatives. Your feedback is pivotal in enhancing your platform experience, let's co-create the platform of your dream!"
                        "buttonText": "GIVE FEEDBACK"
                        "mailingAddress": "548 Market St., Suite 39231 San Francisco, CA 94104"
                        "companyName": "Extole"
                        "companyURL": "Company URL"
                    },
                    {
                      "Reward email": {
                        "participantReward": "participantReward",
                        "emailSubjectText": "High Five, participant.firstName",
                        "emailPreviewText": "Click to redeem your reward",
                        "headingText": "You've earned a participantReward virtual high five participant.firstName",
                        "subheadingText": "Subheading Text",
                        "emailMessage": "Your feedback is pivotal in sculpting the future of our product at [companyName]. In appreciation, here's a virtual high five as a participantReward, along with a motivational reminder to continue making a positive impact on our journey together. Thank you for being an integral part of our success!"
                        "defaultCouponCode": "COUPON_CODE",
                        "reminderMessage": "Thank you for your participation. Earn more with every action!",
                        "shareAgainButtonText - en": "SHARE AGAIN",
                        "rewardRedemptionButtonURL": "companyUrl",
                        "companyName": "Extole",
                        "mailingAddress": "Mailing Address",
                        "participantRewardAmount": "1",
                        "company URL": "https://ana-maria-railean-test.extole.io/",
                      }
                    }
                    Perfect Email Message should contain around 250 characters.
                    '''
            },
            {"role": "user", "content": f"Generate text in JSON format for promo email and reward email.\n{user_message}"}
        ]
    )

    return completion.choices[0].message.content