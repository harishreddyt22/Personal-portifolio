# Adding your certificates

The site looks for certificate files in this folder and shows them in a
pop-up viewer when their card is clicked on the "certifications" section.

## How to add a certificate

1. Export/save your certificate as a **PDF** (preferred) or an image (**.png/.jpg**).
2. Drop it into this `certificates/` folder.
3. Open `data.js` in the project root and find the `CERTIFICATES` array.
4. Make sure the `file` path for that certificate matches your filename exactly, e.g.:

```js
{
  title: "Programming for Everybody (Getting Started with Python)",
  issuer: "University of Michigan · Coursera",
  file: "certificates/python-for-everybody.pdf",   // <-- must match the real filename
  link: "https://coursera.org/verify/XXXXXXXX",     // optional fallback / verify link
}
```

5. To add a brand-new certificate (e.g. your upcoming Andor Tech certificate),
   copy the block above, paste it into the `CERTIFICATES` array, and edit the
   `title`, `issuer`, `file`, and `link` fields.

If a file listed in `data.js` isn't found in this folder, the card will still
open — it just shows a small notice plus a link to the original certificate
URL instead of the in-page preview.
