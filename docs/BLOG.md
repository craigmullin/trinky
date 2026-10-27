# Publishing to the TriNKY blog

The blog is published at `https://tri-nky.com/blog/` using Jekyll and GitHub Pages. Posts are Markdown files in `_posts/`.

## Add a post

1. In GitHub, open the `_posts` folder and choose **Add file → Create new file**.
2. Name the file using this pattern: `YYYY-MM-DD-short-title.md`, for example `2026-11-04-first-pool-session.md`.
3. Start with front matter:

   ```yaml
   ---
   layout: post
   title: "Your post title"
   date: 2026-11-04
   author: Your name
   excerpt: "A short summary for the blog listing."
   ---
   ```

4. Write the post below the closing `---` using Markdown.
5. Commit the file to `main` (or merge a pull request). GitHub Pages builds and publishes the site.

Use a date in the filename and the `date` field that agree. Future-dated posts may not appear until their date has arrived.

## Markdown quick reference

- `## Heading` creates a section heading.
- `**bold**` creates **bold** text.
- `*italic*` creates *italic* text.
- `[link text](https://example.com)` creates a link.
- `![description](/images/photo.jpg)` adds an image; put the image file in the repository first.

The blog uses the TriNKY colors and branding. The RSS/Atom feed is available at `/feed.xml`.
