# TriNKY — Website Implementation Handoff
Date: 2026-10-13

## Purpose
A polished portfolio-quality landing page that can become a real invitation to join a welcoming Northern Kentucky triathlon community. Invite adults of any experience level to connect for casual run/walks, rides, coffee or beers, race conversations, encouragement, and eventually informal meetups. Rooted in Northern Kentucky, open to everyone.

## Current implementation
- Static responsive `index.html` in repository root, suitable for GitHub Pages.
- Hero, introduction, possible community activities, newsletter section.
- Brand palette: Midnight Plum #21112F, Signal Orange #F35A28, Volt Lime #C5F04A, Chalk #F3F2EE.
- Newsletter form is intentionally **inactive** until connected to a provider; do not claim emails are collected yet.
- No server, database, build step, or dependencies.

## Brand assets
Use the exact approved TriNKY master SVG and symbol SVG from the final identity package. **Do not redraw or regenerate the logo.** Upload to `assets/trinky-master.svg` and `assets/trinky-symbol.svg`. Replace the temporary text-based header mark with the genuine asset. Preserve the original orange i, N/K geometry, Kentucky ribbons, spacing and tagline.

## Newsletter
Select a mailing list provider with consent records, double opt-in (preferred), unsubscribe support, and an embeddable hosted form. Buttondown or Mailchimp are possible options, subject to current pricing/features. Follow the provider's documented integration, including hidden fields if required. Do not use a fake local-only success message, a hardcoded API token, or public Google Sheet as the subscriber store.

Required: proper email validation, provider-confirmed success/error states, privacy explanation, unsubscribe mechanism, and sender identification. Test signup, confirmation and unsubscribe with a real address before launch.

## Acceptance criteria
1. Works on mobile and desktop; keyboard accessible.
2. Uses approved SVG with no visual reinterpretation.
3. GitHub Pages serves the static site over HTTPS.
4. Email opt-in works end-to-end, or is clearly labeled coming soon.
5. No invented dates, existing events, partnerships, or formal membership claims.
6. No exposed credentials or tracking without disclosure.

## Deployment
GitHub Settings → Pages → Deploy from a branch → main → / (root). Optional custom domain later.

## Open questions for owner
- Which mailing list provider should collect signups?
- What sender email and contact details should appear in newsletters/privacy notice?
- Publish now as portfolio preview or wait until signup works?
- Custom domain or github.io URL?

## Optional later
Race calendar, social links, meetup details, photo gallery with permissions, group interest survey. Keep initial scope intentionally small.
