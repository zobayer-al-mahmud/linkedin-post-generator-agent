"""
AI Agent for LinkedIn Post Generation
Module 13 - AI Agent Project
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()


class LinkedInPostAgent:
    """
    AI Agent that generates LinkedIn posts using GitHub Models.
    
    Features:
    - Generates professional LinkedIn-style posts
    - Supports multiple languages
    - Creates engaging 2-4 paragraph content
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize the LinkedIn Post Agent.
        
        Args:
            api_key: GitHub token (optional, can use env variable)
        """
        # Get API key from parameter or environment
        self.api_key = api_key or os.getenv("GITHUB_TOKEN")
        
        if not self.api_key:
            raise ValueError(
                "GitHub token not found. Please set GITHUB_TOKEN "
                "in your .env file or pass it to the constructor."
            )
        
        # Initialize the OpenAI client with GitHub Models endpoint
        self.client = OpenAI(
            base_url="https://models.github.ai/inference",
            api_key=self.api_key,
        )
        
        self.model = "openai/gpt-4o-mini"
    
    def generate_post(self, topic: str, language: str = "English") -> str:
        """
        Generate a LinkedIn post based on the given topic and language.
        
        Args:
            topic: The topic of the LinkedIn post
            language: The language for the post (default: English)
            
        Returns:
            Generated LinkedIn post as a string
        """
        try:
            # Create the prompt
            prompt = f"""You are a professional LinkedIn content creator. Create an engaging, 
professional LinkedIn post about the following topic.

Topic: {topic}
Language: {language}

Requirements:
- Write 2-4 well-structured paragraphs
- Use a professional yet conversational tone
- Include relevant insights or perspectives
- Make it engaging and thought-provoking
- Use appropriate formatting (line breaks between paragraphs)
- Write ENTIRELY in {language}
- Do not include hashtags or emojis unless they fit naturally

Generate the LinkedIn post:"""

            # Call GitHub Models API
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional LinkedIn content creator who writes engaging posts.",
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            return f"Error generating post: {str(e)}"
    
    def generate_post_with_details(self, topic: str, language: str = "English") -> dict:
        """
        Generate a LinkedIn post and return detailed information.
        
        Args:
            topic: The topic of the LinkedIn post
            language: The language for the post (default: English)
            
        Returns:
            Dictionary with post content and metadata
        """
        post_content = self.generate_post(topic, language)
        
        return {
            "topic": topic,
            "language": language,
            "post": post_content,
            "word_count": len(post_content.split()),
            "character_count": len(post_content)
        }


def main():
    """Main function to demonstrate the AI Agent."""
    print("=" * 60)
    print("LinkedIn Post Generator - AI Agent")
    print("=" * 60)
    print()
    
    try:
        # Initialize the agent
        agent = LinkedInPostAgent()
        
        # Get user input
        print("Enter the topic for your LinkedIn post:")
        topic = input("> ").strip()
        
        if not topic:
            print("Error: Topic cannot be empty.")
            return
        
        print("\nEnter the language for your post (e.g., English, Spanish, Bengali):")
        language = input("> ").strip()
        
        if not language:
            language = "English"
            print(f"Using default language: {language}")
        
        print("\n" + "=" * 60)
        print("Generating your LinkedIn post...")
        print("=" * 60)
        print()
        
        # Generate the post
        result = agent.generate_post_with_details(topic, language)
        
        # Display the result
        print(f"📝 Topic: {result['topic']}")
        print(f"🌐 Language: {result['language']}")
        print(f"📊 Word Count: {result['word_count']}")
        print(f"📏 Character Count: {result['character_count']}")
        print("\n" + "=" * 60)
        print("Generated LinkedIn Post:")
        print("=" * 60)
        print()
        print(result['post'])
        print()
        print("=" * 60)
        
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\nPlease ensure you have:")
        print("1. Created a .env file in the project directory")
        print("2. Added your GitHub token: GITHUB_TOKEN=your_token_here")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
