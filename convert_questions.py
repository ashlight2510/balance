#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert QUESTIONS array from string format to object format with English translations
"""

import re
import json

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract QUESTIONS array
match = re.search(r'const QUESTIONS = \[(.*?)\];', content, re.DOTALL)
if not match:
    print("Could not find QUESTIONS array")
    exit(1)

questions_text = match.group(1)

# Parse questions
questions = []
for line in questions_text.split('\n'):
    line = line.strip()
    if not line or line.startswith('//'):
        continue
    # Remove quotes and comma
    line = line.strip(',').strip()
    if line.startswith('"') and line.endswith('"'):
        q_text = line[1:-1]
        questions.append(q_text)

print(f"Found {len(questions)} questions")

# For now, create structure with placeholder English translations
# In production, these should be properly translated
output = []
for i, q in enumerate(questions):
    # Simple translation placeholder - in production, use proper translation
    # For now, we'll use a pattern that can be easily replaced
    en_text = q  # Placeholder - should be replaced with actual English translation
    output.append(f'  {{ ko: "{q}", en: "{en_text}" }}')

# Write to a temporary file for review
with open('questions_converted.txt', 'w', encoding='utf-8') as f:
    f.write('const QUESTIONS = [\n')
    f.write(',\n'.join(output))
    f.write('\n];')

print(f"Converted {len(output)} questions to object format")
print("Review questions_converted.txt and replace English translations")
