import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_readme(desc, stack, audience, name, version, usage_steps, author, showcase_video):
    prompt = f"""
    Create a comprehensive and professional README.md file for the following project. 
    Use EXACTLY these project details and create documentation specifically for THIS project:
    
    Project Name: {name}
    Version: {version}
    Description: {desc}
    Technology Stack: {stack}
    Target Audience: {audience}
    Usage Steps: {usage_steps}
    Author: {author}
    Demo Video: {showcase_video}
    
    Requirements for the README:
    1. Use the EXACT project name "{name}" as the title
    2. Include the EXACT version "{version}" in badges
    3. Write about THIS specific project: "{desc}"
    4. Use the EXACT technology stack: "{stack}"
    5. Target the EXACT audience: "{audience}"
    6. Include the EXACT usage steps: "{usage_steps}"
    7. Credit the EXACT author: "{author}"
    8. Add proper markdown formatting with headers, code blocks, and sections
    9. Include badges, installation instructions, features, troubleshooting
    10. Make it comprehensive and professional for THIS specific project
    
    DO NOT create a generic template - use the EXACT project information provided above!
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert technical writer who creates comprehensive, professional README files. You MUST use the exact project information provided by the user and create documentation specifically for that project. Never create generic examples."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()