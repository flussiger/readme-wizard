#!/usr/bin/env python3
"""
README Wizard CLI - Command Line Interface for generating README files
"""

import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.generator import generate_readme

def main():
    parser = argparse.ArgumentParser(description="Generate professional README files")
    parser.add_argument("--description", "-d", required=True, help="Project description")
    parser.add_argument("--stack", "-s", required=True, help="Technology stack used")
    parser.add_argument("--audience", "-a", required=True, help="Target audience")
    parser.add_argument("--output", "-o", default="README.md", help="Output file name (default: README.md)")
    
    args = parser.parse_args()
    
    try:
        print("🚀 Generating README file...")
        readme_content = generate_readme(args.description, args.stack, args.audience)
        
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"✅ README file successfully generated: {args.output}")
        
    except Exception as e:
        print(f"❌ Error generating README: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()