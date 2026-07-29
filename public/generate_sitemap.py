import os
import json
from datetime import datetime

# Configuration
BASE_URL = "https://cheptiony.com"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(SCRIPT_DIR, "all_posts.json")  
SITEMAP_FILE = os.path.join(SCRIPT_DIR, "sitemap.xml") 

def generate_sitemap():
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            posts = json.load(f)

        today = datetime.now().strftime('%Y-%m-%d')
        
        xml_content = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
            f'  <url><loc>{BASE_URL}/</loc><lastmod>{today}</lastmod><priority>1.0</priority></url>',
            f'  <url><loc>{BASE_URL}/journey</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>',
            f'  <url><loc>{BASE_URL}/work</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>',
            f'  <url><loc>{BASE_URL}/pareto-profit</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>',
            f'  <url><loc>{BASE_URL}/book</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>',
            f'  <url><loc>{BASE_URL}/renewed-mind</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>',
            f'  <url><loc>{BASE_URL}/blog</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>',
            f'  <url><loc>{BASE_URL}/contact</loc><lastmod>{today}</lastmod><priority>0.7</priority></url>'
        ]

        for post in posts:
            slug = post.get('slug')
            if slug:
                # Updated for Clean URLs: domain.com/slug-name
                loc = f"{BASE_URL}/{slug.strip()}"
                xml_content.append(f'  <url><loc>{loc}</loc><priority>0.6</priority></url>')

        xml_content.append('</urlset>')

        with open(SITEMAP_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(xml_content))
            
        print(f"Success! Generated sitemap with {len(posts)} Clean URLs.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_sitemap()