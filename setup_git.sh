#!/bin/bash

# Navigate to project directory
cd "/Users/joe/Library/CloudStorage/OneDrive-OurWiltonTrust/Jen and Jones/2023-08-11 Dithering Research/Windsurf Projects/realtime-dithering-001"

# Initialize Git repository
git init

# Configure remote
git remote add origin git@github.com:djDAOjones/realtime-dithering-001.git

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Project setup with comprehensive plan and documentation

- Added PROJECT_PLAN.md with 6-phase development roadmap
- Created README.md with project overview
- Added MIT LICENSE
- Set up documentation structure with transcripts directory
- Created .gitignore for macOS, Xcode, and Max/MSP
- Established src/ and examples/ directories
- Added BUILDING.md with build instructions
- Documented initial setup in cascade transcript"

# Push to GitHub
git push -u origin main

echo "Git repository initialized and pushed to GitHub!"
