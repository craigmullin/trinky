# Adding races to the TriNKY calendar

The live calendar is `calendar.html`. It reads `events.json` from the repository root. You can edit `events.json` directly in GitHub, or locally and push. GitHub Pages publishes the update automatically.

The file starts as `[]` (no events). Replace it with a JSON array of events, for example:

```json
[
  {
    "date": "2027-05-15",
    "name": "Example race — replace with a verified event",
    "type": "triathlon",
    "location": "Example city, OH",
    "description": "Optional details, such as distances or format.",
    "url": "https://example.com/"
  }
]
```

**The above is an example only, not a real event.** Verify dates and official registration URLs before publishing.

Required fields: `date` (YYYY-MM-DD), `name`, `type` (`triathlon`, `run`, `bike`, `swim`, or `other`), and `location`. Optional: `description` and `url` (HTTPS link). Separate objects with commas; JSON cannot contain comments or trailing commas.

Only upcoming events are displayed. The page automatically sorts by date and includes category and keyword filters. Past events stay in the JSON but are hidden. For a canceled event, remove it or update its description.

The calendar is deliberately a curated race **list**, not an account-based calendar or registration system. Events and links are maintained manually. No backend or external API is required.
