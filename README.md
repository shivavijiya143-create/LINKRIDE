# LinkRide Frontend Prototype

A responsive, static website prototype for the LinkRide college project.

## Files
- `index.html` — page structure and content
- `styles.css` — responsive navy, white, and green visual design
- `app.js` — demo interactions for passenger requests, rider decisions, and booking status

## Run locally
Open `index.html` in a modern browser. No build step or package installation is required.

## Deploy online
You can publish this folder as a static website using:
- **GitHub Pages:** create a repository, upload all three website files, then enable Pages in repository settings.
- **Netlify:** drag and drop the folder (or its ZIP after extracting) into the Netlify deploy area.
- **Vercel:** import a Git repository and deploy as a static site.

Make sure `index.html`, `styles.css`, and `app.js` remain in the same directory.

## Important prototype limits
This is front-end only. Ride requests, rider accept/decline actions, and status transitions are simulated in the browser. There is no backend, account authentication, live rider matching, real-time database, live maps, payments, identity verification, or emergency support. Do not use this demo to arrange real rides.

Before any public production service, implement a secure backend and authorization rules; review local transport laws, licensing, insurance, permitted passenger capacity, privacy, emergency handling, and operational safety.
