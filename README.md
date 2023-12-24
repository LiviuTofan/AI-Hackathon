<h1 align="center" id="title">AI Hackathon</h1>

<p id="description">Welcome to my first  AI Hackathon. This project focuses on utilizing AI to optimize the process of company description generation, industry field assignment, and the creation of promotional and reward emails. Below is a breakdown of the project components:</p>

# [Generate Description & Idustry Field](https://github.com/LiviuTofan/AI-Hackathon/tree/master/description)
Input: Company name and URL provided by the user.
Scraping: A scraper is used to find "about us" page and another scraper extracts data.
GPT Integration: Using the GPT API, the obtained data is used to prompt the model with examples for generating a company description and selecting an industry field.
Output: The generated description and industry field are stored in Firebase for later use.

# [Generate Promotional & Reward Email](https://github.com/LiviuTofan/AI-Hackathon/tree/master/emails)
Retrieval from Firebase: All data related to promotion requirements is retrieved from Firebase.
GPT Prompting: GPT is employed again, this time with a well-structured JSON prompt, to generate promotional and reward emails based on user-input requirements.
Firebase Storage: The generated promotional and reward emails are stored in Firebase for further use.

# Conclusion
Through the integration of AI technologies, this project facilitates the automated generation of company descriptions, industry field assignment, and the creation of promotional and reward emails.
