const fs = require('fs');

// Path to your posts
const jsonPath = './public/all_posts.json'; // Adjust path if necessary
const sitemapPath = './public/sitemap.xml';

try {
    const posts = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
    
    let xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://cheptiony.com/</loc><priority>1.0</priority></url>
  <url><loc>https://cheptiony.com/journey</loc><priority>0.8</priority></url>
  <url><loc>https://cheptiony.com/work</loc><priority>0.8</priority></url>
  <url><loc>https://cheptiony.com/pareto-profit</loc><priority>0.8</priority></url>
  <url><loc>https://cheptiony.com/book</loc><priority>0.8</priority></url>
  <url><loc>https://cheptiony.com/renewed-mind</loc><priority>0.8</priority></url>
  <url><loc>https://cheptiony.com/blog</loc><priority>0.9</priority></url>
  <url><loc>https://cheptiony.com/contact</loc><priority>0.7</priority></url>`;

    posts.forEach(post => {
        xml += `
  <url>
    <loc>https://cheptiony.com/${post.slug}</loc>
    <priority>0.7</priority>
  </url>`;
    });

    xml += `\n</urlset>`;

    fs.writeFileSync(sitemapPath, xml);
    console.log(`✅ Success! Sitemap updated with ${posts.length} articles.`);
} catch (err) {
    console.error("Error generating sitemap:", err);
}