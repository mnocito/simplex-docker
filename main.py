from simplex import Simplex
import os
from dotenv import load_dotenv

def main():
   # Load environment variables from .env file
   load_dotenv()
   
   api_key = os.getenv("SIMPLEX_API_KEY")
   print(f"API Key loaded: {api_key is not None}")  # Don't print actual key
   
   simplex = Simplex(api_key=api_key)
   simplex.create_session()
   simplex.goto("google.com")
   pw_browser = simplex.pw.chromium.connect_over_cdp(simplex.connect_url)
   print("Expecting 'hello' in page console:")
   print(pw_browser.contexts[0].pages[0].evaluate("'hello'"))
   
if __name__ == "__main__":
    main() 