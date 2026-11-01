# Mario's Collision Center — website (RGWebD)

Live: https://rgwebd.github.io/marios-collision-center/

Static one-page site (index.html, css/, js/). Photos are real Google Business Profile photos (assets/gallery/), compressed to 1600px.

## Notes for Reese
- **The Google Business Profile is UNCLAIMED and has no website listed.** Suggest Mario claim it (business.google.com) and add this site's URL. A reviewer also mentioned a wrong phone number on some website.
- **Phone conflict:** GBP lists (706) 738-1093 (used on the site). CarCultureHQ lists +1-706-855-9869. Confirm with Mario.
- **ZIP conflict:** GBP 30904 (used) vs CarCultureHQ 30909.
- Services were built from CarCultureHQ (Body, Paint, Aero), the GBP category (Auto body shop) and what the shop photos show. Confirm the list with Mario.
- No real before/after pairs and no team photos, so the site uses a "Work in progress" strip instead.

## Placeholders to fill
- `index.html` estimate form: `action="#FORM-ENDPOINT-PLACEHOLDER"` → Formspree/Netlify endpoint + shop email (no email found). Until then submitting shows "please call".
- `js/reviews.js`: `GOOGLE_API_KEY` and `PLACE_ID` for live Google reviews (Places API New). Falls back to the 9 static real 5-star reviews.
- No social media links found.

Rebuild after editing template.html: `python3 build.py`.
